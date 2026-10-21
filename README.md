# Capital One Marketing Model — Local Airflow, EC2 PySpark, No Glue


Local Airflow orchestrates the pipeline. Extraction, preprocessing, and batch scoring run on the EC2 instance via AWS Systems Manager (SSM). Snowflake credentials are stored in a root-protected environment file on EC2; the local Airflow DAG sends a command, not the credentials.

## Architecture

```text
Airflow UI / scheduler on your local computer
  |
  | DAG 1 uses SsmRunCommandOperator
  v
EC2: retrieve Snowflake credentials from Secrets Manager using instance role
  -> jobs/snowflake_to_s3.py (PySpark Snowflake connector)
  -> S3 raw/{run_date}/
  |
  | only after DAG 1 succeeds, trigger DAG 2
  v
EC2: jobs/preprocessing.py (local PySpark feature engineering)
  -> S3 processed/marketing_features/{run_date}/
  |
  | only after DAG 2 succeeds, trigger DAG 3
  v
EC2: jobs/batch_score.py
  -> S3 output/model_v1/{run_date}/
```

No AWS Glue jobs are called. Each SSM task waits for its remote script to finish. Failed extraction prevents DAG 1 from triggering preprocessing; failed preprocessing prevents DAG 2 from triggering scoring.

## 1. Snowflake credentials in AWS Secrets Manager

The extraction job retrieves credentials from your existing AWS Secrets Manager secret at runtime. It no longer reads a Snowflake password from `/etc/capitalone-marketing.env`, and the password is never passed in the SSM command or stored in this repository.

### Secret format

The secret's **SecretString** must be a JSON object. Common lowercase keys or the uppercase `SNOWFLAKE_*` names are supported. Example structure only—keep your real values in Secrets Manager:

```json
{
  "account": "your_snowflake_account_identifier",
  "username": "your_snowflake_username",
  "password": "your_snowflake_password",
  "warehouse": "your_warehouse",
  "database": "INGEST_DATA",
  "schema": "PUBLIC",
  "role": "your_read_role"
}
```

The `account` value may be an account identifier or a Snowflake hostname. An optional `url` key can supply the full host. Do not put actual credentials in README files, GitHub Actions variables, or DAG configuration.

### Tell local Airflow which existing secret to use

In the **local Airflow UI**, open **Admin → Variables** and create:

- **Key:** `snowflake_secret_id`
- **Value:** the name or ARN of your existing Secrets Manager secret

This is only the secret identifier, not the password. DAG 1 passes the identifier to EC2; credentials are retrieved by the EC2 instance role.

### EC2 IAM permissions

Attach a least-privilege policy to the EC2 instance role allowing `secretsmanager:GetSecretValue` on that specific secret ARN. If the secret uses a customer-managed KMS key, the role may also need `kms:Decrypt` for that key. Keep the existing S3 permissions for the pipeline. The AWS identity used by local Airflow still needs its existing SSM permissions; it does not need permission to read the Snowflake secret.

Remove the old Snowflake username/password from `/etc/capitalone-marketing.env` once you've confirmed the new path works. If that file is still needed for unrelated settings, do not keep the Snowflake password in it. Rotate the password if it was ever committed to GitHub or otherwise exposed.


## 2. Local Airflow configuration

Install provider packages in the Python environment/container where local Airflow runs. Choose versions compatible with your Airflow version:

```bash
pip install apache-airflow-providers-amazon apache-airflow-providers-standard
```

If your Airflow version includes the standard provider already, keep the compatible installed version rather than blindly upgrading Airflow itself. For Docker-based Airflow, the providers must be installed in the Airflow container/image.

Create or verify the Airflow AWS connection:

- **Connection Id:** `aws_default`
- **Connection Type:** Amazon Web Services
- Configure credentials using an approved local AWS profile/role or the connection's supported authentication fields.
- **Region:** `us-east-1`

The AWS identity used by local Airflow needs permission to send commands to this EC2 managed instance and poll command status (including the required SSM `SendCommand`, `GetCommandInvocation`, and `ListCommandInvocations` access). Scope permissions to the instance and the `AWS-RunShellScript` document where feasible. Never put AWS access keys in DAG code.

## 3. EC2 and network prerequisites

- EC2 instance ID used by the DAGs: `i-06ea3e388448b991c` in `us-east-1`. Update the constants in all three DAGs if your instance changes.
- SSM Agent is running and the instance appears as an online managed node in Systems Manager.
- The EC2 instance role includes SSM managed-instance permissions (commonly `AmazonSSMManagedInstanceCore`) and access to required S3 prefixes.
- EC2 has Python and the project environment at `/opt/capitalone_marketing_model/.venv`.
- Java compatible with PySpark 3.5 (Java 11 or 17 are typical choices).
- EC2 has network access to Snowflake on HTTPS/443 and to Maven repositories on first connector resolution, unless connector/JDBC jars are installed in advance.
- EC2 has adequate temporary disk space and RAM for local Spark.
- Snowflake role has warehouse usage, database/schema usage, and SELECT privileges on the source table.

Install/update the EC2 project dependencies when the code changes:

```bash
cd /opt/capitalone_marketing_model
.venv/bin/python -m pip install --no-cache-dir -r requirements.txt
.venv/bin/python -m compileall -q jobs scoring airflow
.venv/bin/python -m pytest -q
```

The GitHub Actions deployment workflow is manual-dispatch only. It requires the repository variable `AWS_DEPLOY_ROLE_ARN` and a correctly configured GitHub OIDC trust/policy before it can deploy. Alternatively, update the checked-out code on EC2 using your approved deployment method.

## 4. DAGs and local Airflow folder

- `airflow/dags/01_snowflake_to_s3.py`: invokes extraction on EC2 via SSM and triggers DAG 2 only after success.
- `airflow/dags/02_preprocessing.py`: invokes preprocessing on EC2 via SSM and triggers DAG 3 only after success.
- `airflow/dags/03_batch_scoring.py`: invokes batch scoring on EC2 via SSM.

Because Airflow runs locally, copy these DAG files into the **local Airflow instance's configured DAGs folder** and restart/reload the local scheduler if needed. The GitHub deployment workflow's EC2 copy of DAG files does not update the DAGs folder on your local computer.

All DAGs have `schedule=None`; trigger DAG 1 manually in the local Airflow UI. The date defaults to the DAG logical date, but you can provide `run_date` in the DAG-run configuration.

## 5. S3 output locations

- Raw extraction: `s3://bank-marketing-ml-poc-vineet/raw/{run_date}/`
- Feature data: `s3://bank-marketing-ml-poc-vineet/processed/marketing_features/{run_date}/`
- Scoring output: `s3://bank-marketing-ml-poc-vineet/output/model_v1/{run_date}/`

The scripts clear objects under the matching run-date prefix before publishing new files. Avoid overlapping runs for the same date.

## 6. Source query and connector

The default query in `jobs/snowflake_to_s3.py` is:

```sql
SELECT *
FROM INGEST_DATA.PUBLIC.CUSTOMERS
WHERE CUSTOMER_ID IS NOT NULL
```

Verify the database/schema/table and the columns exist in your Snowflake environment. Override the query using `SNOWFLAKE_QUERY` if required. The default connector Maven coordinate is `net.snowflake:spark-snowflake_2.12:3.1.4-spark_3.5`; confirm compatibility with the installed Spark and Scala versions.

## Troubleshooting

- **DAG fails to import:** check local Airflow provider packages and scheduler logs.
- **SSM command cannot start:** check the local `aws_default` connection's IAM permissions, EC2 managed-node online status, and region/instance ID.
- **Secrets Manager access denied:** verify the Airflow Variable `snowflake_secret_id`, secret region, EC2 instance-role `secretsmanager:GetSecretValue` permission, and KMS decrypt permission if applicable.
- **Snowflake login/network failure:** verify account host, credentials, network policy/private routing/IP allowlisting, warehouse, role and grants.
- **S3 AccessDenied:** check the EC2 instance role and bucket policy.
- **Connector download failure:** check outbound Maven access or preinstall connector/JDBC jars.
- **Disk or memory pressure:** inspect `df -h`, available RAM, and `SPARK_DRIVER_MEMORY`.
