import polars as pl
from prefect import task


@task
def format_shipments(df: pl.DataFrame) -> pl.DataFrame:
    ...
