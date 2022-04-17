from typing import TypedDict

import click
from prefect import Flow

from tasks.src import job

DEFAULT_PROJECT_NAME = "Example Pipeline"


class Options(TypedDict):
    project: str
    offline: bool


@click.group()
def main() -> None:
    """Job running script"""
    ...


@main.command()
@click.option(
    "--project",
    default=DEFAULT_PROJECT_NAME,
    help="Project name registered with prefect dashboard.",
)
@click.option(
    "--offline",
    is_flag=True,
    help="Run job without prefect dashboard visibility.",
)
def jobs(**kwargs: Options) -> None:
    """Run all jobs."""
    with Flow("Example") as flow:
        job.run_example_job()

    if not kwargs["offline"]:
        flow.register(project_name=kwargs["project"])

    flow.run()


if __name__ == "__main__":
    main()
