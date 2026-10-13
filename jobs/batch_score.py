import argparse
import io
import json
import os
import sys
import tempfile
from datetime import datetime, timezone

# Work around duplicate SageMaker MLflow plugin metadata in this EC2 venv.
# The venv exposes both lib/ and lib64/ site-packages; loading both registers
# the request-header provider twice and duplicates x-mlflow-sm-tracking-server-arn.
# Remove the lib/ path before importing MLflow so only lib64/ is used.
_duplicate_site_packages = os.path.abspath(
    os.path.join(
        sys.prefix,
        "lib",
        f"python{sys.version_info.major}.{sys.version_info.minor}",
        "site-packages",
    )
)
sys.path[:] = [
    entry
    for entry in sys.path
    if os.path.abspath(entry or os.getcwd()) != _duplicate_site_packages
]

import boto3
import mlflow
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    log_loss,
    precision_score,
    recall_score,
    roc_auc_score,
)

from scoring.score_if_else import score_dataframe


# ============================================================
# CONFIGURATION
# ============================================================

DEFAULT_EXPERIMENT_NAME = "bank-marketing-scoring"

MODEL_NAME = "MarketingResponseGBM"
MODEL_VERSION = "1.0"
MODEL_TYPE = "XGBoost"
NUMBER_OF_TREES = 100
SCORING_METHOD = "IF_ELSE"


# ============================================================
# S3 HELPERS
# ============================================================

s3 = boto3.client("s3")


def parse_s3_uri(s3_uri):
    """
    Convert:
        s3://bucket/path/file.parquet

    into:
        bucket
        key
    """

    if not s3_uri.startswith("s3://"):
        raise ValueError(f"Invalid S3 URI: {s3_uri}")

    path = s3_uri.replace("s3://", "", 1)

    parts = path.split("/", 1)

    bucket = parts[0]

    if len(parts) == 1:
        key = ""
    else:
        key = parts[1]

    return bucket, key


def list_parquet_files(s3_uri):
    """
    List all parquet files below an S3 prefix.
    """

    bucket, prefix = parse_s3_uri(s3_uri)

    if prefix and not prefix.endswith("/"):
        prefix += "/"

    parquet_files = []

    paginator = s3.get_paginator("list_objects_v2")

    for page in paginator.paginate(
        Bucket=bucket,
        Prefix=prefix
    ):

        for obj in page.get("Contents", []):

            key = obj["Key"]

            if key.lower().endswith(".parquet"):

                parquet_files.append(
                    f"s3://{bucket}/{key}"
                )

    return parquet_files


def read_parquet_from_s3(s3_uri):
    """
    Read one Parquet file from S3 into pandas.
    """

    bucket, key = parse_s3_uri(s3_uri)

    response = s3.get_object(
        Bucket=bucket,
        Key=key
    )

    data = response["Body"].read()

    return pd.read_parquet(
        io.BytesIO(data)
    )


def write_parquet_to_s3(df, s3_uri):
    """
    Write pandas DataFrame as Parquet to S3.
    """

    bucket, key = parse_s3_uri(s3_uri)

    buffer = io.BytesIO()

    df.to_parquet(
        buffer,
        index=False
    )

    buffer.seek(0)

    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=buffer.getvalue()
    )


def write_json_to_s3(data, s3_uri):
    """
    Write JSON object to S3.
    """

    bucket, key = parse_s3_uri(s3_uri)

    body = json.dumps(
        data,
        indent=2,
        default=str
    )

    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=body.encode("utf-8"),
        ContentType="application/json"
    )


# ============================================================
# METRICS
# ============================================================

def calculate_metrics(
    scored_df,
    target_column
):
    """
    Calculate supervised metrics if target exists.
    """

    metrics = {}

    metrics["row_count"] = int(len(scored_df))

    # --------------------------------------------------------
    # Score distribution
    # --------------------------------------------------------

    if "score" in scored_df.columns:

        metrics["score_min"] = float(
            scored_df["score"].min()
        )

        metrics["score_max"] = float(
            scored_df["score"].max()
        )

        metrics["score_mean"] = float(
            scored_df["score"].mean()
        )

        metrics["score_median"] = float(
            scored_df["score"].median()
        )

    # --------------------------------------------------------
    # Probability distribution
    # --------------------------------------------------------

    if "probability" in scored_df.columns:

        metrics["probability_min"] = float(
            scored_df["probability"].min()
        )

        metrics["probability_max"] = float(
            scored_df["probability"].max()
        )

        metrics["probability_mean"] = float(
            scored_df["probability"].mean()
        )

    # --------------------------------------------------------
    # Prediction distribution
    # --------------------------------------------------------

    if "prediction" in scored_df.columns:

        metrics["prediction_rate"] = float(
            scored_df["prediction"].mean()
        )

    # --------------------------------------------------------
    # Target not available
    # --------------------------------------------------------

    if target_column not in scored_df.columns:

        metrics["evaluation_status"] = (
            "Target column not available. "
            "Only operational scoring metrics calculated."
        )

        return metrics

    # --------------------------------------------------------
    # Remove missing target rows
    # --------------------------------------------------------

    evaluation_df = scored_df[
        scored_df[target_column].notna()
    ].copy()

    if len(evaluation_df) == 0:

        metrics["evaluation_status"] = (
            "Target column exists but contains no "
            "non-null values."
        )

        return metrics

    y_true = evaluation_df[
        target_column
    ].astype(int)

    y_pred = evaluation_df[
        "prediction"
    ].astype(int)

    y_prob = evaluation_df[
        "probability"
    ].astype(float)

    # --------------------------------------------------------
    # Classification metrics
    # --------------------------------------------------------

    metrics["evaluation_rows"] = int(
        len(evaluation_df)
    )

    metrics["accuracy"] = float(
        accuracy_score(
            y_true,
            y_pred
        )
    )

    metrics["precision"] = float(
        precision_score(
            y_true,
            y_pred,
            zero_division=0
        )
    )

    metrics["recall"] = float(
        recall_score(
            y_true,
            y_pred,
            zero_division=0
        )
    )

    metrics["f1"] = float(
        f1_score(
            y_true,
            y_pred,
            zero_division=0
        )
    )

    # --------------------------------------------------------
    # ROC-AUC
    # --------------------------------------------------------

    if y_true.nunique() == 2:

        metrics["roc_auc"] = float(
            roc_auc_score(
                y_true,
                y_prob
            )
        )

        metrics["log_loss"] = float(
            log_loss(
                y_true,
                y_prob
            )
        )

    else:

        metrics["roc_auc"] = None
        metrics["log_loss"] = None

    # --------------------------------------------------------
    # Confusion matrix
    # --------------------------------------------------------

    cm = confusion_matrix(
        y_true,
        y_pred,
        labels=[0, 1]
    )

    metrics["confusion_matrix"] = {
        "true_negative": int(cm[0][0]),
        "false_positive": int(cm[0][1]),
        "false_negative": int(cm[1][0]),
        "true_positive": int(cm[1][1])
    }

    metrics["actual_response_rate"] = float(
        y_true.mean()
    )

    metrics["evaluation_status"] = "Completed"

    return metrics


# ============================================================
# MLFLOW
# ============================================================

def configure_mlflow():
    """
    Configure SageMaker managed MLflow.

    The environment variable should contain the
    SageMaker MLflow Tracking Server ARN.

    Example:

    MLFLOW_TRACKING_URI=
    arn:aws:sagemaker:us-east-1:783495713343:
    mlflow-tracking-server/marketing-mlflow-server
    """

    tracking_uri = os.getenv(
        "MLFLOW_TRACKING_URI"
    )

    if not tracking_uri:

        print(
            "MLFLOW_TRACKING_URI is not configured."
        )

        print(
            "MLflow logging will be disabled."
        )

        return False

    print(
        f"MLflow Tracking URI: {tracking_uri}"
    )

    mlflow.set_tracking_uri(
        tracking_uri
    )

    experiment_name = os.getenv(
        "MLFLOW_EXPERIMENT_NAME",
        DEFAULT_EXPERIMENT_NAME
    )

    print(
        f"MLflow Experiment: {experiment_name}"
    )

    mlflow.set_experiment(
        experiment_name
    )

    return True


def log_mlflow_run(
    run_date,
    input_s3,
    output_s3,
    metrics_s3,
    metrics,
    scored_df,
    metrics_file_local
):
    """
    Create one MLflow run for this scoring execution.
    """

    experiment_name = os.getenv(
        "MLFLOW_EXPERIMENT_NAME",
        DEFAULT_EXPERIMENT_NAME
    )

    run_name = (
        f"scoring-{run_date}-"
        f"{datetime.now(timezone.utc).strftime('%H%M%S')}"
    )

    print(
        f"Starting MLflow run: {run_name}"
    )

    with mlflow.start_run(
        run_name=run_name
    ) as run:

        # ----------------------------------------------------
        # Parameters
        # ----------------------------------------------------

        mlflow.log_params({

            "model_name": MODEL_NAME,

            "model_version": MODEL_VERSION,

            "model_type": MODEL_TYPE,

            "number_of_trees": NUMBER_OF_TREES,

            "scoring_method": SCORING_METHOD,

            "run_date": run_date,

            "input_s3": input_s3,

            "output_s3": output_s3,

            "metrics_s3": metrics_s3,

            "experiment_name": experiment_name

        })

        # ----------------------------------------------------
        # Operational metrics
        # ----------------------------------------------------

        numeric_metrics = {}

        operational_metric_names = [
            "row_count",
            "evaluation_rows",
            "score_min",
            "score_max",
            "score_mean",
            "score_median",
            "probability_min",
            "probability_max",
            "probability_mean",
            "prediction_rate",
            "actual_response_rate"
        ]

        for metric_name in operational_metric_names:

            value = metrics.get(
                metric_name
            )

            if value is not None:

                numeric_metrics[
                    metric_name
                ] = float(value)

        # ----------------------------------------------------
        # Model performance metrics
        # ----------------------------------------------------

        performance_metric_names = [
            "accuracy",
            "precision",
            "recall",
            "f1",
            "roc_auc",
            "log_loss"
        ]

        for metric_name in performance_metric_names:

            value = metrics.get(
                metric_name
            )

            if value is not None:

                numeric_metrics[
                    metric_name
                ] = float(value)

        # ----------------------------------------------------
        # Log metrics
        # ----------------------------------------------------

        if numeric_metrics:

            mlflow.log_metrics(
                numeric_metrics
            )

        # ----------------------------------------------------
        # Log metrics JSON
        # ----------------------------------------------------

        if os.path.exists(
            metrics_file_local
        ):

            mlflow.log_artifact(
                metrics_file_local,
                artifact_path="metrics"
            )

        # ----------------------------------------------------
        # Create scoring summary artifact
        # ----------------------------------------------------

        summary = {

            "run_name": run_name,

            "run_id": run.info.run_id,

            "run_date": run_date,

            "model_name": MODEL_NAME,

            "model_version": MODEL_VERSION,

            "number_of_trees": NUMBER_OF_TREES,

            "scoring_method": SCORING_METHOD,

            "input_s3": input_s3,

            "output_s3": output_s3,

            "metrics_s3": metrics_s3,

            "metrics": metrics

        }

        summary_file = os.path.join(
            tempfile.gettempdir(),
            "mlflow_scoring_summary.json"
        )

        with open(
            summary_file,
            "w"
        ) as f:

            json.dump(
                summary,
                f,
                indent=2,
                default=str
            )

        mlflow.log_artifact(
            summary_file,
            artifact_path="scoring"
        )

        print(
            "MLflow run completed."
        )

        print(
            f"MLflow Run ID: {run.info.run_id}"
        )


# ============================================================
# MAIN
# ============================================================

def main():

    parser = argparse.ArgumentParser(
        description=(
            "Batch score Glue Job 2 processed "
            "data using the 100-tree IF/ELSE model."
        )
    )

    parser.add_argument(
        "--run-date",
        required=True,
        help="Data/scoring run date, e.g. 2026-10-06"
    )

    parser.add_argument(
        "--input-s3",
        required=True,
        help="S3 prefix containing processed Parquet files"
    )

    parser.add_argument(
        "--output-s3",
        required=True,
        help="S3 prefix for scored output"
    )

    parser.add_argument(
        "--metrics-s3",
        required=True,
        help="Full S3 path for metrics.json"
    )

    parser.add_argument(
        "--target-column",
        default="campaign_response",
        help="Target column used for evaluation"
    )

    args = parser.parse_args()

    run_date = args.run_date

    input_s3 = args.input_s3

    output_s3 = args.output_s3

    metrics_s3 = args.metrics_s3

    target_column = args.target_column

    print("=" * 70)

    print(
        "BANK MARKETING BATCH SCORING"
    )

    print("=" * 70)

    print(
        f"Run date       : {run_date}"
    )

    print(
        f"Input S3       : {input_s3}"
    )

    print(
        f"Output S3      : {output_s3}"
    )

    print(
        f"Metrics S3     : {metrics_s3}"
    )

    print(
        f"Target column  : {target_column}"
    )

    print(
        f"Model          : {MODEL_NAME}"
    )

    print(
        f"Model version  : {MODEL_VERSION}"
    )

    print(
        f"Trees          : {NUMBER_OF_TREES}"
    )

    # ========================================================
    # Configure MLflow
    # ========================================================

    mlflow_enabled = False
    mlflow_required = os.getenv("MLFLOW_REQUIRED", "false").strip().lower() in {
        "1", "true", "yes", "y"
    }

    try:

        mlflow_enabled = configure_mlflow()

    except Exception as e:

        if mlflow_required:
            raise RuntimeError(
                "MLflow configuration failed while MLFLOW_REQUIRED is enabled."
            ) from e

        print(
            "WARNING: MLflow configuration failed."
        )

        print(
            f"MLflow error: {e}"
        )

        print(
            "Scoring will continue without MLflow."
        )

    if mlflow_required and not mlflow_enabled:
        raise RuntimeError(
            "MLFLOW_REQUIRED is enabled, but MLflow tracking was not configured."
        )

    # ========================================================
    # Find input files
    # ========================================================

    print("\nFinding Parquet files...")

    parquet_files = list_parquet_files(
        input_s3
    )

    if not parquet_files:

        raise RuntimeError(
            f"No Parquet files found under {input_s3}"
        )

    print(
        f"Found {len(parquet_files)} parquet files"
    )

    # ========================================================
    # Read input data
    # ========================================================

    dataframes = []

    for file_uri in parquet_files:

        print(
            f"Reading {file_uri}"
        )

        df_part = read_parquet_from_s3(
            file_uri
        )

        print(
            f"Rows: {len(df_part)}"
        )

        dataframes.append(
            df_part
        )

    df = pd.concat(
        dataframes,
        ignore_index=True
    )

    print(
        f"\nInput rows: {len(df)}"
    )

    # ========================================================
    # Score
    # ========================================================

    print(
        "\nRunning 100-tree IF/ELSE scoring..."
    )

    scored_df = score_dataframe(
        df
    )

    print(
        f"Scored rows: {len(scored_df)}"
    )

    # ========================================================
    # Validate scoring columns
    # ========================================================

    required_output_columns = [
        "prediction_margin",
        "probability",
        "prediction",
        "score"
    ]

    missing_output_columns = [
        column
        for column in required_output_columns
        if column not in scored_df.columns
    ]

    if missing_output_columns:

        raise RuntimeError(
            "Scoring did not produce required "
            f"columns: {missing_output_columns}"
        )

    # ========================================================
    # Calculate metrics
    # ========================================================

    print(
        "\nCalculating metrics..."
    )

    metrics = calculate_metrics(
        scored_df,
        target_column
    )

    print(
        json.dumps(
            metrics,
            indent=2,
            default=str
        )
    )

    # ========================================================
    # Output paths
    # ========================================================

    output_s3 = output_s3.rstrip("/")

    scored_output_s3 = (
        f"{output_s3}/scored_data.parquet"
    )

    metrics_s3 = metrics_s3

    # ========================================================
    # Write scored data to S3
    # ========================================================

    print(
        f"\nWriting scored data to:"
    )

    print(
        scored_output_s3
    )

    write_parquet_to_s3(
        scored_df,
        scored_output_s3
    )

    print(
        "Scored data successfully written."
    )

    # ========================================================
    # Write metrics JSON to S3
    # ========================================================

    print(
        f"\nWriting metrics to:"
    )

    print(
        metrics_s3
    )

    write_json_to_s3(
        metrics,
        metrics_s3
    )

    print(
        "Metrics successfully written."
    )

    # ========================================================
    # MLflow
    # ========================================================

    if mlflow_enabled:

        try:

            with tempfile.NamedTemporaryFile(
                mode="w",
                suffix=".json",
                delete=False
            ) as tmp:

                json.dump(
                    metrics,
                    tmp,
                    indent=2,
                    default=str
                )

                metrics_file_local = tmp.name

            log_mlflow_run(
                run_date=run_date,
                input_s3=input_s3,
                output_s3=output_s3,
                metrics_s3=metrics_s3,
                metrics=metrics,
                scored_df=scored_df,
                metrics_file_local=metrics_file_local
            )

            try:

                os.remove(
                    metrics_file_local
                )

            except OSError:

                pass

        except Exception as e:

            if mlflow_required:
                raise RuntimeError(
                    "MLflow metric/artifact logging failed while MLFLOW_REQUIRED is enabled."
                ) from e

            print(
                "\nWARNING: MLflow logging failed."
            )

            print(
                f"MLflow error: {e}"
            )

            print(
                "Scoring and S3 output were successful."
            )

    # ========================================================
    # Final summary
    # ========================================================

    print("\n" + "=" * 70)

    print(
        "BATCH SCORING COMPLETED"
    )

    print("=" * 70)

    print(
        f"Input rows       : {len(df)}"
    )

    print(
        f"Output rows      : {len(scored_df)}"
    )

    print(
        f"Scored output    : {scored_output_s3}"
    )

    print(
        f"Metrics          : {metrics_s3}"
    )

    print(
        f"MLflow enabled   : {mlflow_enabled}"
    )

    print("=" * 70)


if __name__ == "__main__":

    main()
