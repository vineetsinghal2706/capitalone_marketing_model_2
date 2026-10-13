import pendulum

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator


local_tz = pendulum.timezone("Asia/Kolkata")
APP_DIR = "/opt/capitalone_marketing_model"


with DAG(
    dag_id="02_preprocessing",
    start_date=pendulum.datetime(2026, 10, 1, tz=local_tz),
    schedule=None,
    catchup=False,
    tags=["marketing", "pyspark", "preprocessing"],
) as dag:

    preprocess = BashOperator(
        task_id="run_preprocessing",
        bash_command=(
            f"set -euo pipefail; cd {APP_DIR}; "
            "test -x .venv/bin/python; "
            "RUN_DATE='{{ dag_run.conf.get(\"run_date\", ds) }}'; "
            "echo \"Starting local PySpark preprocessing for $RUN_DATE\"; "
            ".venv/bin/python jobs/preprocessing.py --run-date \"$RUN_DATE\""
        ),
    )

    trigger_scoring = TriggerDagRunOperator(
        task_id="trigger_scoring",
        trigger_dag_id="03_batch_scoring",
        conf={"run_date": "{{ dag_run.conf.get('run_date', ds) }}"},
        wait_for_completion=False,
    )

    preprocess >> trigger_scoring
