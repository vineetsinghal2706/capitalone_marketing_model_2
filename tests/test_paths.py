from pathlib import Path


def test_required_project_files_exist():
    required = [
        "jobs/snowflake_to_s3.py",
        "jobs/preprocessing.py",
        "jobs/batch_score.py",
        "airflow/dags/01_snowflake_to_s3.py",
        "airflow/dags/02_preprocessing.py",
        "airflow/dags/03_batch_scoring.py",
        "scoring/score_if_else.py",
    ]

    for path in required:
        assert Path(path).exists(), path


def test_dag1_runs_extraction_remotely_and_loads_ec2_environment_file():
    dag1 = Path("airflow/dags/01_snowflake_to_s3.py").read_text()
    assert "SsmRunCommandOperator" in dag1
    assert "/etc/capitalone-marketing.env" in dag1
    assert "jobs/snowflake_to_s3.py" in dag1
    assert "trigger_preprocessing" in dag1


def test_dag2_runs_preprocessing_remotely():
    dag2 = Path("airflow/dags/02_preprocessing.py").read_text()
    assert "SsmRunCommandOperator" in dag2
    assert "jobs/preprocessing.py" in dag2
    assert "trigger_scoring" in dag2


def test_no_docker_deployment_files():
    assert not Path("Dockerfile").exists()
    assert not Path(".github/workflows/scoring.yml").exists()
