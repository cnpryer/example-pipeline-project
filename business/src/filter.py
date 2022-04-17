import polars as pl

from core.src.filter import FilterConfig


def exclude(df: pl.DataFrame, config: FilterConfig) -> None:
    ...
