import polars as pl
from prefect import task


@task
def load_shipments(filepath: str) -> pl.DataFrame:
    ...
