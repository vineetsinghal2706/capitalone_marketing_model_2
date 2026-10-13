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


def test_no_docker_deployment_files():
    assert not Path("Dockerfile").exists()
    assert not Path(".github/workflows/scoring.yml").exists()
