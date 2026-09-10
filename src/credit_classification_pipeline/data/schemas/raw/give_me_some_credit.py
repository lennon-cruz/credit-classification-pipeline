"""Raw contract v0 for Give Me Some Credit training extract."""

import pandera.pandas as pa
from pandera.typing.pandas import Series


class GiveMeSomeCreditRawTrain(pa.DataFrameModel):
    """Accepted Schema from training data before cleaning."""

    SeriousDlqin2yrs: Series[int] = pa.Field(isin=[0, 1])
    RevolvingUtilizationOfUnsecuredLines: Series[float] = pa.Field(ge=0)
    age: Series[int] = pa.Field(ge=0)
    NumberOfTime30_59DaysPastDueNotWorse: Series[int] = pa.Field(
        alias="NumberOfTime30-59DaysPastDueNotWorse",
        ge=0,
    )
    DebtRatio: Series[float] = pa.Field(ge=0)
    MonthlyIncome: Series[float] = pa.Field(nullable=True, ge=0)
    NumberOfOpenCreditLinesAndLoans: Series[int] = pa.Field(ge=0)
    NumberOfTimes90DaysLate: Series[int] = pa.Field(ge=0)
    NumberRealEstateLoansOrLines: Series[int] = pa.Field(ge=0)
    NumberOfTime60_89DaysPastDueNotWorse: Series[int] = pa.Field(
        alias="NumberOfTime60-89DaysPastDueNotWorse",
        ge=0,
    )
    NumberOfDependents: Series[float] = pa.Field(nullable=True, ge=0)

    class Config:
        strict = True   # unknown columns → fail
        coerce = True   # CSV ints/floats often need light coercion

def validate_raw_train(df):
    """Validate and return the DataFrame (or raise SchemaError)."""
    
    return GiveMeSomeCreditRawTrain.validate(df, lazy=True)