import pendulum

from airflow import DAG
from airflow.providers.amazon.aws.operators.ssm import SsmRunCommandOperator
from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator


local_tz = pendulum.timezone("Asia/Kolkata")
AWS_REGION = "us-east-1"
EC2_INSTANCE_ID = "i-06ea3e388448b991c"
APP_DIR = "/opt/capitalone_marketing_model"


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
test -r /etc/capitalone-marketing.env || {{ echo "Snowflake environment file is missing or unreadable" >&2; exit 1; }}
. /etc/capitalone-marketing.env

cd {APP_DIR}
test -x .venv/bin/python
test -f jobs/snowflake_to_s3.py

export AWS_DEFAULT_REGION={AWS_REGION}
RUN_DATE="{{{{ dag_run.conf.get('run_date', ds) }}}}"

echo "Starting Snowflake-to-S3 extraction for $RUN_DATE on EC2"
.venv/bin/python jobs/snowflake_to_s3.py --run-date "$RUN_DATE"
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
