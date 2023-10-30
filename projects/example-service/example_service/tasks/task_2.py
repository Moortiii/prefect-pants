from prefect import task


@task
def task_2():
    print("Hello from Task 2")
