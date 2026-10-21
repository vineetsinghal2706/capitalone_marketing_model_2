"""Golden regression tests for the deterministic IF/ELSE scorer."""
import json
from pathlib import Path

import pandas as pd
import pytest

from scoring.score_if_else import FEATURE_NAMES, score_dataframe

FIXTURE_PATH = Path(__file__).parent / "fixtures" / "score_parity.json"


def _fixture():
    data = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    assert data.get("cases"), "At least one sample case is required"
    return data


def _row(overrides):
    result = {feature: None for feature in FEATURE_NAMES}
    result.update(overrides)
    return result


def test_synthetic_sample_score_regression():
    """Compare output to trusted golden scores when those have been supplied."""
    fixture = _fixture()
    expected_cases = [case for case in fixture["cases"] if isinstance(case.get("expected"), dict)]
    if not expected_cases:
        pytest.fail(
            "No approved reference scores checked in yet. Populate each case's "
            "'expected' object in tests/fixtures/score_parity.json using the "
            "trusted reference scorer. Deployment is blocked until sample-score "
            "validation can actually be performed."
        )
    if len(expected_cases) != len(fixture["cases"]):
        pytest.fail("Each sample case must have approved expected outputs before deployment.")

    actual = score_dataframe(
        pd.DataFrame([_row(item["features"]) for item in fixture["cases"]])
    )
    assert len(actual) == len(fixture["cases"])
    assert {"prediction_margin", "probability", "prediction", "score"}.issubset(actual.columns)
    assert actual["score"].between(100, 999).all()
    assert actual["probability"].between(0, 1).all()
    assert set(actual["prediction"].unique()).issubset({0, 1})

    for index, case in enumerate(fixture["cases"]):
        got = actual.iloc[index]
        expected = case["expected"]
        assert int(got["score"]) == expected["score"], case["name"]
        assert int(got["prediction"]) == expected["prediction"], case["name"]
        assert float(got["probability"]) == pytest.approx(
            expected["probability"],
            abs=fixture["probability_tolerance"],
            rel=0,
        ), case["name"]


def test_scorer_rejects_missing_required_feature():
    row = {feature: None for feature in FEATURE_NAMES}
    row.pop(FEATURE_NAMES[0])
    with pytest.raises(ValueError, match="Missing required model features"):
        score_dataframe(pd.DataFrame([row]))
