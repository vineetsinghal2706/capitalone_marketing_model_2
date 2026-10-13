import pendulum

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator


local_tz = pendulum.timezone("Asia/Kolkata")
APP_DIR = "/opt/capitalone_marketing_model"


with DAG(
    dag_id="01_snowflake_to_s3",
    start_date=pendulum.datetime(2026, 10, 1, tz=local_tz),
    schedule=None,
    catchup=False,
    tags=["marketing", "pyspark", "snowflake", "s3"],
) as dag:

    extract = BashOperator(
        task_id="extract_snowflake_to_s3",
        bash_command=(
            f"set -euo pipefail; cd {APP_DIR}; "
            "test -x .venv/bin/python; "
            "RUN_DATE='{{ ds }}'; "
            "echo \"Starting direct PySpark Snowflake extraction for $RUN_DATE\"; "
            ".venv/bin/python jobs/snowflake_to_s3.py --run-date \"$RUN_DATE\""
        ),
    )

    trigger_preprocessing = TriggerDagRunOperator(
        task_id="trigger_preprocessing",
        trigger_dag_id="02_preprocessing",
        conf={"run_date": "{{ ds }}"},
        wait_for_completion=False,
    )

    extract >> trigger_preprocessing
