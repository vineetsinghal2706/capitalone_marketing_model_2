import argparse
import os
import tempfile
from pathlib import Path

import boto3
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, trim, lower, when, log1p, month, quarter, dayofweek, sin, cos, lit,
)

BUCKET = os.getenv("S3_BUCKET", "bank-marketing-ml-poc-vineet")
TARGET = "campaign_response"
NUMERIC_FEATURES = [
    "age", "annual_income", "tenure_months", "credit_score", "existing_products",
    "monthly_spend", "avg_monthly_balance", "digital_txn_ratio", "mobile_logins_30d",
    "branch_visits_6m", "web_visits_30d", "credit_utilization", "delinquency_12m",
    "marketing_contacts_90d", "days_since_last_txn",
]
CATEGORICAL_FEATURES = ["customer_segment", "acquisition_channel", "employment_type"]


def parse_s3_uri(uri):
    if not uri.startswith("s3://"):
        raise ValueError(f"Expected an s3:// URI, got: {uri}")
    bucket, _, key = uri[5:].partition("/")
    return bucket, key


def download_parquet_prefix(s3, uri, local_dir):
    bucket, prefix = parse_s3_uri(uri)
    if prefix and not prefix.endswith("/"):
        prefix += "/"
    paginator = s3.get_paginator("list_objects_v2")
    downloaded = []
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        for obj in page.get("Contents", []):
            key = obj["Key"]
            if key.lower().endswith(".parquet"):
                local_path = os.path.join(local_dir, os.path.basename(key))
                s3.download_file(bucket, key, local_path)
                downloaded.append(local_path)
    if not downloaded:
        raise FileNotFoundError(f"No Parquet files found under {uri}")
    return downloaded


def clear_s3_prefix(s3, bucket, prefix):
    paginator = s3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        objects = [{"Key": obj["Key"]} for obj in page.get("Contents", [])]
        for start in range(0, len(objects), 1000):
            s3.delete_objects(
                Bucket=bucket,
                Delete={"Objects": objects[start:start + 1000], "Quiet": True},
            )


def upload_parquet_directory(s3, local_dir, bucket, prefix):
    files = sorted(Path(local_dir).glob("*.parquet"))
    if not files:
        raise RuntimeError(f"Spark produced no Parquet files in {local_dir}")
    for file_path in files:
        key = f"{prefix.rstrip('/')}/{file_path.name}"
        s3.upload_file(str(file_path), bucket, key)
        print(f"Uploaded s3://{bucket}/{key}")
    return len(files)


def build_features(df):
    df = df.dropDuplicates(["customer_id"])
    df = df.withColumn("campaign_date", col("campaign_date").cast("date"))
    for c in CATEGORICAL_FEATURES:
        df = df.withColumn(c, lower(trim(col(c))))
    df = (
        df.withColumn("campaign_month", month("campaign_date"))
        .withColumn("campaign_quarter", quarter("campaign_date"))
        .withColumn("campaign_dayofweek", dayofweek("campaign_date"))
        .withColumn("campaign_is_weekend", when(col("campaign_dayofweek").isin(1, 7), 1).otherwise(0))
        .withColumn("campaign_month_sin", sin(2 * lit(3.141592653589793) * col("campaign_month") / lit(12)))
        .withColumn("campaign_month_cos", cos(2 * lit(3.141592653589793) * col("campaign_month") / lit(12)))
    )
    df = (
        df.withColumn("annual_income", when(col("annual_income") > 250000, 250000).otherwise(col("annual_income")))
        .withColumn("annual_income", when(col("annual_income") < 18000, 18000).otherwise(col("annual_income")))
        .withColumn("monthly_spend", when(col("monthly_spend") > 20000, 20000).otherwise(col("monthly_spend")))
        .withColumn("monthly_spend", when(col("monthly_spend") < 100, 100).otherwise(col("monthly_spend")))
        .withColumn("avg_monthly_balance", when(col("avg_monthly_balance") > 100000, 100000).otherwise(col("avg_monthly_balance")))
    )
    df = (
        df.withColumn("log_income", log1p(col("annual_income")))
        .withColumn("log_monthly_spend", log1p(col("monthly_spend")))
        .withColumn("log_avg_balance", log1p(col("avg_monthly_balance")))
        .withColumn("log_web_visits", log1p(col("web_visits_30d")))
    )
    df = (
        df.withColumn("spend_to_income", col("monthly_spend") / (col("annual_income") / 12 + 1))
        .withColumn("balance_to_income", col("avg_monthly_balance") / (col("annual_income") / 12 + 1))
        .withColumn("digital_engagement", 0.6 * col("digital_txn_ratio") + 0.4 * (col("mobile_logins_30d") / 101))
        .withColumn("channel_engagement", col("mobile_logins_30d") + col("web_visits_30d"))
        .withColumn("product_penetration", col("existing_products") / (col("tenure_months") / 12 + 1))
        .withColumn("delinquency_rate", col("delinquency_12m") / 12)
        .withColumn("contact_pressure", col("marketing_contacts_90d") / 3)
    )
    df = (
        df.withColumn("high_value_customer", when((col("annual_income") >= 120000) & (col("avg_monthly_balance") >= 10000), 1).otherwise(0))
        .withColumn("digital_customer", when((col("digital_txn_ratio") >= 0.70) & (col("mobile_logins_30d") >= 15), 1).otherwise(0))
        .withColumn("credit_risk_flag", when((col("credit_score") < 600) | (col("credit_utilization") > 0.80) | (col("delinquency_12m") >= 2), 1).otherwise(0))
    )
    return (
        df.withColumn("income_x_credit_score", (col("annual_income") / 100000) * col("credit_score"))
        .withColumn("digital_x_spend", col("digital_txn_ratio") * col("monthly_spend"))
        .withColumn("tenure_x_products", col("tenure_months") * col("existing_products"))
        .withColumn(TARGET, col(TARGET).cast("double"))
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-date", required=True)
    args = parser.parse_args()
    run_date = args.run_date
    input_uri = f"s3://{BUCKET}/raw/{run_date}/"
    output_prefix = f"processed/marketing_features/{run_date}/"
    s3 = boto3.client("s3")

    # Download with boto3 so local Spark does not require Hadoop S3A jars.
    with tempfile.TemporaryDirectory(prefix="marketing_preprocess_") as temp_dir:
        local_input = os.path.join(temp_dir, "input")
        local_output = os.path.join(temp_dir, "output")
        os.makedirs(local_input)
        os.makedirs(local_output)
        downloaded = download_parquet_prefix(s3, input_uri, local_input)
        spark = (
            SparkSession.builder.appName("bank-marketing-preprocessing")
            .master(os.getenv("SPARK_MASTER", "local[*]"))
            .config("spark.driver.memory", os.getenv("SPARK_DRIVER_MEMORY", "4g"))
            .getOrCreate()
        )
        spark.sparkContext.setLogLevel(os.getenv("SPARK_LOG_LEVEL", "WARN"))
        try:
            print(f"Reading {len(downloaded)} Parquet file(s) from {input_uri}")
            df = spark.read.parquet(local_input)
            df = df.toDF(*[c.strip().lower() for c in df.columns])
            required = ["customer_id", "campaign_date", TARGET] + NUMERIC_FEATURES + CATEGORICAL_FEATURES
            missing = [c for c in required if c not in df.columns]
            if missing:
                raise ValueError(f"Missing required columns: {missing}")
            input_count = df.count()
            processed = build_features(df)
            processed_count = processed.count()
            if processed_count == 0:
                raise RuntimeError("Preprocessing produced zero rows; refusing to publish empty output")
            print(f"Input records: {input_count:,}")
            print(f"Processed records: {processed_count:,}")
            processed.repartition(5).write.mode("overwrite").parquet(local_output)
            clear_s3_prefix(s3, BUCKET, output_prefix)
            file_count = upload_parquet_directory(s3, local_output, BUCKET, output_prefix)
            print(f"Processed data written to s3://{BUCKET}/{output_prefix} ({file_count} files)")
        finally:
            spark.stop()


if __name__ == "__main__":
    main()
