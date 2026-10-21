# Pre-deployment validation

The GitHub Actions workflow runs these checks in a validation job before the EC2 deploy job. Because deployment uses `needs: validate`, validation failure prevents deployment.

## Checks
- Python syntax compilation across `jobs/`, `scoring/`, `airflow/`, and `tests/`.
- Unit/regression tests for the IF/ELSE scorer, including required-feature and output-contract checks.
- Smoke tests import the scorer and run `jobs/batch_score.py --help` without calling AWS or changing S3.
- Synthetic sample-score regression compares score, prediction, and probability to checked-in expected values when approved reference scores have been supplied.

## Score parity is intentionally not misrepresented
The repository does not currently include an independent original-model/reference scorer output file. Expected scores must come from the modeling-team-approved reference implementation or trusted score output, not from the same implementation under test. Until those expected values are supplied, the score-parity test fails deliberately and blocks deployment. Once expected values are added to `tests/fixtures/score_parity.json`, any score mismatch fails validation and blocks EC2 deployment.

Run locally:

```bash
python -m pip install pytest pandas numpy
python -m compileall -q jobs scoring airflow tests
pytest -q
```
