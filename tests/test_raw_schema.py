import pandas as pd
import pandera.errors
import pytest

from credit_classification_pipeline.data.validate import validate_raw


def _valid_row(**overrides):
    row = {
        "SeriousDlqin2yrs": 0,
        "RevolvingUtilizationOfUnsecuredLines": 0.1,
        "age": 45,
        "NumberOfTime30-59DaysPastDueNotWorse": 0,
        "DebtRatio": 0.3,
        "MonthlyIncome": 5000.0,
        "NumberOfOpenCreditLinesAndLoans": 5,
        "NumberOfTimes90DaysLate": 0,
        "NumberRealEstateLoansOrLines": 1,
        "NumberOfTime60-89DaysPastDueNotWorse": 0,
        "NumberOfDependents": 0.0,
    }

    row.update(overrides)
    return row


def test_raw_train_happy_path():
    df = pd.DataFrame([_valid_row(), _valid_row(SeriousDlqin2yrs=1, MonthlyIncome=None)])
    out = validate_raw(df, split="train")
    assert len(out) == 2


def test_raw_train_rejects_bad_target():
    df = pd.DataFrame([_valid_row(SeriousDlqin2yrs=2)])
    with pytest.raises(pandera.errors.SchemaErrors):
        validate_raw(df, split="train")


def test_raw_train_rejects_missing_column():
    df = pd.DataFrame([_valid_row()])
    df = df.drop(columns=["age"])
    with pytest.raises(pandera.errors.SchemaErrors):
        validate_raw(df, split="train")