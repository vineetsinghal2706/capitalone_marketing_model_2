"""Extract Snowflake data with the Spark Snowflake connector and publish Parquet to S3.

Runs on EC2 in Spark local mode; it does not require AWS Glue or S3A Hadoop jars.
The EC2 instance role supplies S3 permissions and reads Snowflake credentials from
AWS Secrets Manager at runtime. Credentials must not be committed to the repository.

Spark's temporary files and local Parquet output are placed on disk-backed
/var/tmp/spark-tmp rather than a small RAM-backed /tmp (tmpfs).
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
SPARK_TMP_DIR = os.getenv("SPARK_TMP_DIR", "/var/tmp/spark-tmp")


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-date", required=True)
    return parser.parse_args()


def required_env(name):
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Required environment variable is not set: {name}")
    return value


def _secret_value(secret, *names, required=True, default=None):
    """Read a secret field accepting common uppercase/lowercase key conventions."""
    for name in names:
        value = secret.get(name)
        if value is not None and str(value).strip():
            return str(value).strip()
    if required:
        # Deliberately don't include secret contents or credential values in errors.
        raise RuntimeError(
            "Snowflake Secrets Manager secret is missing a required field. "
            f"Expected one of: {', '.join(names)}"
        )
    return default


def load_snowflake_secret():
    """Fetch and parse the existing Snowflake secret without logging its contents."""
    secret_id = required_env("SNOWFLAKE_SECRET_ID")
    region = os.getenv("AWS_REGION") or os.getenv("AWS_DEFAULT_REGION")
    client_kwargs = {"region_name": region} if region else {}
    client = boto3.client("secretsmanager", **client_kwargs)

    try:
        response = client.get_secret_value(SecretId=secret_id)
    except Exception as exc:
        # Do not print the SDK response or secret data; keep the failure actionable.
        error_code = getattr(exc, "response", {}).get("Error", {}).get("Code", "unknown")
        raise RuntimeError(
            "Unable to retrieve Snowflake secret from AWS Secrets Manager "
            f"(error code: {error_code}). Check the secret ID, region, IAM policy, "
            "and any customer-managed KMS key permissions."
        ) from exc

    secret_string = response.get("SecretString")
    if not secret_string:
        raise RuntimeError(
            "Snowflake secret must use SecretString containing a JSON object."
        )

    import json

    try:
        secret = json.loads(secret_string)
    except (TypeError, json.JSONDecodeError) as exc:
        raise RuntimeError(
            "Snowflake secret must contain valid JSON in SecretString."
        ) from exc
    if not isinstance(secret, dict):
        raise RuntimeError("Snowflake secret JSON must be an object.")

    return secret


def snowflake_options():
    secret = load_snowflake_secret()
    account = _secret_value(
        secret, "account", "SNOWFLAKE_ACCOUNT", "snowflake_account", "url", "SNOWFLAKE_URL"
    )
    url = _secret_value(
        secret, "url", "SNOWFLAKE_URL", required=False, default=account
    )
    if not url.startswith(("http://", "https://")) and "snowflakecomputing.com" not in url:
        url = f"{url}.snowflakecomputing.com"
    url = url.removeprefix("https://").removeprefix("http://").rstrip("/")

    options = {
        "sfURL": url,
        "sfUser": _secret_value(secret, "username", "user", "SNOWFLAKE_USER", "SNOWFLAKE_USERNAME"),
        "sfPassword": _secret_value(secret, "password", "SNOWFLAKE_PASSWORD"),
        "sfDatabase": _secret_value(
            secret, "database", "SNOWFLAKE_DATABASE", required=False,
            default=os.getenv("SNOWFLAKE_DATABASE", "INGEST_DATA")
        ),
        "sfSchema": _secret_value(
            secret, "schema", "SNOWFLAKE_SCHEMA", required=False,
            default=os.getenv("SNOWFLAKE_SCHEMA", "PUBLIC")
        ),
        "sfWarehouse": _secret_value(
            secret, "warehouse", "SNOWFLAKE_WAREHOUSE"
        ),
        "query": os.getenv("SNOWFLAKE_QUERY", SNOWFLAKE_QUERY).strip(),
    }
    role = _secret_value(
        secret, "role", "SNOWFLAKE_ROLE", required=False,
        default=os.getenv("SNOWFLAKE_ROLE")
    )
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
        print(f"Uploaded s3://{bucket}/{key}", flush=True)
    return len(files)


def main():
    args = get_args()
    bucket = BUCKET
    prefix = f"raw/{args.run_date}/"
    spark_package = os.getenv("SNOWFLAKE_SPARK_CONNECTOR_PACKAGE", DEFAULT_SPARK_PACKAGE)

    configure_spark_temp_dir()
    print(f"Spark temporary directory: {SPARK_TMP_DIR}", flush=True)

    spark = (
        SparkSession.builder
        .appName("bank-marketing-snowflake-extraction")
        .master(os.getenv("SPARK_MASTER", "local[*]"))
        .config("spark.jars.packages", spark_package)
        .config("spark.local.dir", SPARK_TMP_DIR)
        .config("spark.driver.extraJavaOptions", f"-Djava.io.tmpdir={SPARK_TMP_DIR}")
        .config("spark.sql.session.timeZone", "UTC")
        .config("spark.driver.memory", os.getenv("SPARK_DRIVER_MEMORY", "4g"))
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel(os.getenv("SPARK_LOG_LEVEL", "WARN"))
    s3 = boto3.client("s3")
    try:
        print(f"Reading Snowflake query into Spark; target s3://{bucket}/{prefix}", flush=True)
        df = (
            spark.read.format("net.snowflake.spark.snowflake")
            .options(**snowflake_options())
            .load()
        )
        count = df.count()
        if count == 0:
            raise RuntimeError("Snowflake query returned zero rows; refusing to publish empty output")
        print(f"Extracted {count:,} records from Snowflake", flush=True)

        # Keep local Parquet output off the small RAM-backed /tmp filesystem.
        with tempfile.TemporaryDirectory(
            prefix="snowflake_extract_",
            dir=SPARK_TMP_DIR,
        ) as temp_dir:
            local_output = os.path.join(temp_dir, "parquet")
            df.write.mode("overwrite").parquet(local_output)
            clear_s3_prefix(s3, bucket, prefix)
            file_count = upload_parquet_directory(s3, local_output, bucket, prefix)

        print(
            f"Extraction complete: {count:,} rows, {file_count} Parquet file(s) "
            f"at s3://{bucket}/{prefix}",
            flush=True,
        )
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
