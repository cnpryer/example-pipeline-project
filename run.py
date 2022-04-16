from prefect import Flow

from task.src import job

if __name__ == "__main__":
    with Flow("Example Job") as flow:
        job.run_example_job()

    flow.run()
