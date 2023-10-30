from prefect import flow, task


@task
def task_1():
    print("Hello from Task 1")


@task
def task_2():
    print("Hello from Task 2")


@flow
def example_flow():
    print("Hello from the start of the flow!")
    task_1()
    task_2()
