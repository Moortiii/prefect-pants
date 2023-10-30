from prefect import task


@task
def task_1():
    print("Hello from Task 1")
