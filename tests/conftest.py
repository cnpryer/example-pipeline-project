import polars as pl
from pytest import fixture


@fixture
def test_df() -> pl.DataFrame:
    return pl.DataFrame()
