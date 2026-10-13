# Capital One Marketing Model — EC2 PySpark Pipeline

This branch removes AWS Glue from extraction and preprocessing. Airflow launches local PySpark scripts on EC2; the scripts connect to Snowflake and move Parquet files to/from S3 using boto3.

## Architecture

```text
Airflow DAG 1
  -> jobs/snowflake_to_s3.py (PySpark Snowflake connector)
  -> S3 raw/{run_date}/
Airflow DAG 2
  -> jobs/preprocessing.py (local PySpark feature engineering)
  -> S3 processed/marketing_features/{run_date}/
Airflow DAG 3
  -> existing batch scoring flow
  -> S3 output/model_v1/{run_date}/
```

DAG 1 triggers DAG 2 only after extraction succeeds; DAG 2 triggers DAG 3 only after preprocessing succeeds. No Glue jobs are called.

## EC2 prerequisites

- Python virtual environment at `/opt/capitalone_marketing_model/.venv`.
- Java compatible with PySpark 3.5 (Java 11 or 17 are typical choices).
- Outbound network access from EC2 to Snowflake on HTTPS/443 and to Maven repositories on the first run, unless compatible connector/JDBC jars are preinstalled.
- Enough EC2 disk space for temporary Parquet files and RAM for Spark local mode.
- EC2 instance role with `s3:ListBucket`, `s3:GetObject`, `s3:PutObject`, and `s3:DeleteObject` for the relevant bucket/prefixes. The scripts clear a run-date output prefix before publishing replacements.
- Airflow task runtime can read the Snowflake environment variables below.

Install dependencies:

```bash
cd /opt/capitalone_marketing_model
.venv/bin/python -m pip install --no-cache-dir -r requirements.txt
.venv/bin/python -m compileall -q jobs scoring airflow
.venv/bin/python -m pytest -q
```

## Snowflake configuration

Set these variables securely in the Airflow worker/scheduler runtime (or load them from your approved secrets manager before running tasks):

- `SNOWFLAKE_ACCOUNT`: account identifier or full account host.
- `SNOWFLAKE_USER`
- `SNOWFLAKE_PASSWORD`
- `SNOWFLAKE_WAREHOUSE`
- `SNOWFLAKE_DATABASE` (default: `INGEST_DATA`)
- `SNOWFLAKE_SCHEMA` (default: `PUBLIC`)
- `SNOWFLAKE_ROLE` (optional)
- `SNOWFLAKE_URL` (optional explicit hostname)
- `SNOWFLAKE_QUERY` (optional SQL override)
- `SNOWFLAKE_SPARK_CONNECTOR_PACKAGE` (optional Maven coordinate override)
- `S3_BUCKET` (default: `bank-marketing-ml-poc-vineet`)
- `SPARK_DRIVER_MEMORY` (default: `4g`)

Never commit credentials. Prefer approved key-pair/OAuth authentication or a managed secret store if required by your security policy. The Snowflake role needs warehouse usage and select privileges on the configured source table.

Default query in `jobs/snowflake_to_s3.py`:

```sql
SELECT *
FROM INGEST_DATA.PUBLIC.CUSTOMERS
WHERE CUSTOMER_ID IS NOT NULL
```

Confirm that this is the intended source table in the target environment. The default connector Maven coordinate is `net.snowflake:spark-snowflake_2.12:3.1.4-spark_3.5`; confirm connector, Scala, and Spark versions are compatible with the installed PySpark runtime.

## S3 paths

- Raw: `s3://bank-marketing-ml-poc-vineet/raw/{run_date}/`
- Preprocessed: `s3://bank-marketing-ml-poc-vineet/processed/marketing_features/{run_date}/`
- Scoring output: `s3://bank-marketing-ml-poc-vineet/output/model_v1/{run_date}/`

A rerun replaces objects under the matching run-date prefix. Do not run overlapping jobs for the same run date.

## Airflow and deployment

- `airflow/dags/01_snowflake_to_s3.py`: runs direct Snowflake extraction.
- `airflow/dags/02_preprocessing.py`: runs preprocessing locally.
- `airflow/dags/03_batch_scoring.py`: existing scoring task.

The DAGs use `schedule=None`; manually trigger DAG 1 unless you intentionally configure a schedule. Ensure the deployed Airflow process has the Snowflake environment variables. Updating GitHub alone does not change running Airflow processes until deployment completes and the DAGs reload.

## Troubleshooting

- Connector download fails: check Maven outbound access or install compatible connector/JDBC jars in advance.
- Snowflake connectivity/login fails: verify hostname, credentials/authentication, network policy, private routing/IP allowlisting, warehouse, role and grants.
- S3 AccessDenied: verify EC2 role and bucket policy.
- Out-of-disk or memory errors: inspect `df -h`, available RAM, Spark partitions and `SPARK_DRIVER_MEMORY`.
