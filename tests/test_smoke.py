"""Fast smoke tests that do not contact AWS or mutate cloud resources."""
import subprocess
import sys
from pathlib import Path


def test_scorer_import_smoke():
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "from scoring.score_if_else import FEATURE_NAMES, score_dataframe; assert len(FEATURE_NAMES) == 38",
        ],
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    assert result.returncode == 0, result.stderr


def test_job_cli_help_smoke():
    """All pipeline job entrypoints should parse CLI help without AWS calls."""
    checks = [
        ("jobs/snowflake_to_s3.py", ["--run-date"]),
        ("jobs/preprocessing.py", ["--run-date"]),
        ("jobs/batch_score.py", ["--run-date", "--input-s3", "--output-s3", "--metrics-s3"]),
    ]
    for script, expected_options in checks:
        result = subprocess.run(
            [sys.executable, script, "--help"],
            capture_output=True,
            text=True,
            timeout=45,
            check=False,
        )
        assert result.returncode == 0, f"{script}: {result.stderr}"
        for option in expected_options:
            assert option in result.stdout, f"{script} missing {option}"


def test_required_pipeline_files_exist():
    for path in (
        "jobs/snowflake_to_s3.py",
        "jobs/preprocessing.py",
        "jobs/batch_score.py",
        "airflow/dags/01_snowflake_to_s3.py",
        "airflow/dags/02_preprocessing.py",
        "airflow/dags/03_batch_scoring.py",
        "scoring/score_if_else.py",
    ):
        assert Path(path).is_file(), path
