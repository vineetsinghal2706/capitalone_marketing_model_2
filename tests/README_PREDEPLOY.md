# Pre-deployment validation

The GitHub Actions workflow validates the code before copying it to EC2. The deployment job has `needs: validate`, so failed validation blocks the copy/deploy steps.

## Checks

- **Python syntax:** `python -m compileall -q jobs scoring airflow tests`
- **Unit tests:** model scorer rejects missing required model features.
- **Sample score regression:** three deterministic synthetic rows compare predicted score, prediction, and probability to the checked-in golden baseline in `tests/fixtures/score_parity.json`.
- **Smoke tests:** import the IF/ELSE scorer and run `--help` for extraction, preprocessing, and batch-scoring entry points without connecting to AWS or modifying S3.

## Score baseline provenance

The expected values in the fixture are a snapshot of the current checked-in IF/ELSE scorer. They are a useful regression gate: any code change that alters these sample outputs fails validation and blocks deployment. They are **not independent proof** that this scorer matches a separately executed original XGBoost artifact, because that model artifact/reference output is not currently in the repository. For independent model parity certification, confirm or replace the fixture outputs with score results from the modeling-team-approved reference implementation. Do not regenerate expected values from the implementation under test during routine CI.

## Run locally

```bash
python -m pip install -r requirements.txt pytest
python -m compileall -q jobs scoring airflow tests
pytest -q
```
