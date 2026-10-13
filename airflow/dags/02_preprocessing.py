import pendulum

from airflow import DAG
from airflow.providers.amazon.aws.operators.ssm import SsmRunCommandOperator
from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator


local_tz = pendulum.timezone("Asia/Kolkata")
AWS_REGION = "us-east-1"
EC2_INSTANCE_ID = "i-06ea3e388448b991c"
APP_DIR = "/opt/capitalone_marketing_model"
BUCKET = "bank-marketing-ml-poc-vineet"


with DAG(
    dag_id="02_preprocessing",
    start_date=pendulum.datetime(2026, 10, 1, tz=local_tz),
    schedule=None,
    catchup=False,
    tags=["marketing", "ec2", "ssm", "pyspark", "preprocessing"],
) as dag:

    preprocess = SsmRunCommandOperator(
        task_id="run_preprocessing",
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
test -f jobs/preprocessing.py

export AWS_DEFAULT_REGION={AWS_REGION}
export S3_BUCKET={BUCKET}
RUN_DATE="{{{{ dag_run.conf.get('run_date', ds) }}}}"

echo "Starting PySpark preprocessing for $RUN_DATE on EC2"
.venv/bin/python jobs/preprocessing.py --run-date "$RUN_DATE"
echo "PySpark preprocessing completed for $RUN_DATE"
"""
                ]
            },
        },
    )

    trigger_scoring = TriggerDagRunOperator(
        task_id="trigger_scoring",
        trigger_dag_id="03_batch_scoring",
        conf={"run_date": "{{ dag_run.conf.get('run_date', ds) }}"},
        wait_for_completion=False,
    )

    preprocess >> trigger_scoring
