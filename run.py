from prefect import Flow

from pipeline.task_lib import job

if __name__ == "__main__":
    with Flow("Example Job") as flow:
        job.run_example_job()

    flow.run()
