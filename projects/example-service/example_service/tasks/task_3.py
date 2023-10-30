from prefect import task
from example_lib.shared import SOME_SHARED_VARIABLE


@task
def task_3():
    print(f"Hello from Task 3. The shared variable value is: {SOME_SHARED_VARIABLE}")
