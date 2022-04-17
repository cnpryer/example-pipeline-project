from business.src import filter


def test_lib(test_df, test_filter_config) -> None:
    filter.exclude(df=test_df, config=test_filter_config)
