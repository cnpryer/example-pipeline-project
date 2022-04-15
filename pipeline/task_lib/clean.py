import polars as pl
from prefect import task


@task
def clean_shipments(df: pl.DataFrame) -> pl.DataFrame:
    ...
