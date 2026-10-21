import pendulum

from airflow import DAG
from airflow.providers.amazon.aws.operators.ssm import SsmRunCommandOperator
from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator


local_tz = pendulum.timezone("Asia/Kolkata")
AWS_REGION = "us-east-1"
EC2_INSTANCE_ID = "i-06ea3e388448b991c"
APP_DIR = "/opt/capitalone_marketing_model"
SPARK_TMP_DIR = "/var/tmp/spark-tmp"


with DAG(
    dag_id="01_snowflake_to_s3",
    start_date=pendulum.datetime(2026, 10, 1, tz=local_tz),
    schedule=None,
    catchup=False,
    tags=["marketing", "ec2", "ssm", "pyspark", "snowflake", "s3"],
) as dag:

    extract = SsmRunCommandOperator(
        task_id="extract_snowflake_to_s3",
        aws_conn_id="aws_default",
        region_name=AWS_REGION,
        document_name="AWS-RunShellScript",
        wait_for_completion=True,
        run_command_kwargs={
            "InstanceIds": [EC2_INSTANCE_ID],
            "Parameters": {
                "commands": [
                    f"""set -eu

cd {APP_DIR}
test -x .venv/bin/python
test -f jobs/snowflake_to_s3.py

# /tmp is a small RAM-backed tmpfs on this EC2 instance.
# Put Spark, JVM, and Python temporary files on the disk-backed root volume.
mkdir -p {SPARK_TMP_DIR}
chmod 700 {SPARK_TMP_DIR}
export TMPDIR={SPARK_TMP_DIR}
export SPARK_LOCAL_DIRS={SPARK_TMP_DIR}
export SPARK_TMP_DIR={SPARK_TMP_DIR}
export SPARK_SUBMIT_OPTS="${{SPARK_SUBMIT_OPTS:-}} -Djava.io.tmpdir={SPARK_TMP_DIR}"

export AWS_DEFAULT_REGION={AWS_REGION}
export AWS_REGION={AWS_REGION}
export SNOWFLAKE_SECRET_ID="{{{{ var.value.snowflake_secret_id }}}}"
RUN_DATE="{{{{ dag_run.conf.get('run_date', ds) }}}}"

echo "Starting Snowflake-to-S3 extraction for $RUN_DATE on EC2"
echo "Spark temporary directory: $SPARK_TMP_DIR"
df -hT / /tmp {SPARK_TMP_DIR}

.venv/bin/python -u jobs/snowflake_to_s3.py --run-date "$RUN_DATE"
echo "Snowflake-to-S3 extraction completed for $RUN_DATE"
"""
                ]
            },
        },
    )

    trigger_preprocessing = TriggerDagRunOperator(
        task_id="trigger_preprocessing",
        trigger_dag_id="02_preprocessing",
        conf={"run_date": "{{ dag_run.conf.get('run_date', ds) }}"},
        wait_for_completion=False,
    )

    extract >> trigger_preprocessing
