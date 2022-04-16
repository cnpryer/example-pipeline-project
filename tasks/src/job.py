from prefect import task


@task
def run_example_job() -> None:
    ...
