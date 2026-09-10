import pandas as pd

from credit_classification_pipeline.data.schemas.raw.give_me_some_credit import (
    validate_raw_train,
)


def validate_raw(df: pd.DataFrame, *, split: str = "train") -> pd.DataFrame:
    """Validate the raw data."""

    if split != "train":
        raise NotImplementedError("v0 only covers train; test target is often null")
    return validate_raw_train(df)