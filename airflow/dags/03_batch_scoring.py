import pendulum

from airflow import DAG
from airflow.providers.amazon.aws.operators.ssm import SsmRunCommandOperator


local_tz = pendulum.timezone("Asia/Kolkata")
AWS_REGION = "us-east-1"
EC2_INSTANCE_ID = "i-06ea3e388448b991c"
APP_DIR = "/opt/capitalone_marketing_model"
BUCKET = "bank-marketing-ml-poc-vineet"
MLFLOW_TRACKING_URI = (
    "arn:aws:sagemaker:us-east-1:783495713343:"
    "mlflow-tracking-server/marketing-mlflow-server"
)
MLFLOW_EXPERIMENT_NAME = "bank-marketing-scoring"


with DAG(
    dag_id="03_batch_scoring",
    start_date=pendulum.datetime(2026, 10, 1, tz=local_tz),
    schedule=None,
    catchup=False,
    tags=["marketing", "ec2", "ssm", "scoring", "mlflow"],
) as dag:

    score = SsmRunCommandOperator(
        task_id="run_batch_scoring",
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
test -f jobs/batch_score.py
test -f scoring/score_if_else.py

export AWS_DEFAULT_REGION={AWS_REGION}
export PYTHONPATH="{APP_DIR}"
export MLFLOW_TRACKING_URI="{MLFLOW_TRACKING_URI}"
export MLFLOW_EXPERIMENT_NAME={MLFLOW_EXPERIMENT_NAME}
export MLFLOW_REQUIRED=true

RUN_DATE="{{{{ dag_run.conf.get('run_date', ds) }}}}"
echo "Running batch scoring for $RUN_DATE"
echo "PYTHONPATH=$PYTHONPATH"
echo "MLflow tracking ARN=$MLFLOW_TRACKING_URI"

.venv/bin/python jobs/batch_score.py \\
  --run-date "$RUN_DATE" \\
  --input-s3 "s3://{BUCKET}/processed/marketing_features/$RUN_DATE/" \\
  --output-s3 "s3://{BUCKET}/output/model_v1/$RUN_DATE/" \\
  --metrics-s3 "s3://{BUCKET}/output/model_v1/$RUN_DATE/metrics.json"
"""
                ]
            },
        },
    )
