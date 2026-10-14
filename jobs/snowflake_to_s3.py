"""Extract Snowflake data with the Spark Snowflake connector and publish Parquet to S3.

Runs on EC2 in Spark local mode; it does not require AWS Glue or S3A Hadoop jars.
The EC2 instance role supplies S3 permissions. Snowflake credentials are read from
environment variables and must not be committed to the repository.
"""
import argparse
import os
import tempfile
from pathlib import Path

import boto3
from pyspark.sql import SparkSession

BUCKET = os.getenv("S3_BUCKET", "bank-marketing-ml-poc-vineet")
SNOWFLAKE_QUERY = """
    SELECT *
    FROM INGEST_DATA.PUBLIC.CUSTOMERS
    WHERE CUSTOMER_ID IS NOT NULL
"""
DEFAULT_SPARK_PACKAGE = "net.snowflake:spark-snowflake_2.12:3.2.2-spark_3.5"


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-date", required=True)
    return parser.parse_args()


def required_env(name):
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Required environment variable is not set: {name}")
    return value


def snowflake_options():
    account = required_env("SNOWFLAKE_ACCOUNT")
    url = os.getenv("SNOWFLAKE_URL")
    if not url:
        url = account
        if not url.startswith(("http://", "https://")) and "snowflakecomputing.com" not in url:
            url = f"{url}.snowflakecomputing.com"
    url = url.removeprefix("https://").removeprefix("http://").rstrip("/")
    options = {
        "sfURL": url,
        "sfUser": required_env("SNOWFLAKE_USER"),
        "sfPassword": required_env("SNOWFLAKE_PASSWORD"),
        "sfDatabase": os.getenv("SNOWFLAKE_DATABASE", "INGEST_DATA"),
        "sfSchema": os.getenv("SNOWFLAKE_SCHEMA", "PUBLIC"),
        "sfWarehouse": required_env("SNOWFLAKE_WAREHOUSE"),
        "query": os.getenv("SNOWFLAKE_QUERY", SNOWFLAKE_QUERY).strip(),
    }
    role = os.getenv("SNOWFLAKE_ROLE")
    if role:
        options["sfRole"] = role
    return options


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


def main():
    args = get_args()
    bucket = BUCKET
    prefix = f"raw/{args.run_date}/"
    spark_package = os.getenv("SNOWFLAKE_SPARK_CONNECTOR_PACKAGE", DEFAULT_SPARK_PACKAGE)
    spark = (
        SparkSession.builder
        .appName("bank-marketing-snowflake-extraction")
        .master(os.getenv("SPARK_MASTER", "local[*]"))
        .config("spark.jars.packages", spark_package)
        .config("spark.sql.session.timeZone", "UTC")
        .config("spark.driver.memory", os.getenv("SPARK_DRIVER_MEMORY", "4g"))
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel(os.getenv("SPARK_LOG_LEVEL", "WARN"))
    s3 = boto3.client("s3")
    try:
        print(f"Reading Snowflake query into Spark; target s3://{bucket}/{prefix}")
        df = (
            spark.read.format("net.snowflake.spark.snowflake")
            .options(**snowflake_options())
            .load()
        )
        count = df.count()
        if count == 0:
            raise RuntimeError("Snowflake query returned zero rows; refusing to publish empty output")
        print(f"Extracted {count:,} records from Snowflake")
        with tempfile.TemporaryDirectory(prefix="snowflake_extract_") as temp_dir:
            local_output = os.path.join(temp_dir, "parquet")
            df.write.mode("overwrite").parquet(local_output)
            clear_s3_prefix(s3, bucket, prefix)
            file_count = upload_parquet_directory(s3, local_output, bucket, prefix)
        print(f"Extraction complete: {count:,} rows, {file_count} Parquet file(s) at s3://{bucket}/{prefix}")
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
