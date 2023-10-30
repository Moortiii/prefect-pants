from example_service.tasks.task_1 import task_1
from example_service.tasks.task_2 import task_2
from example_service.tasks.task_3 import task_3
from prefect import flow


@flow
def example_flow():
    print("Hello from the start of the flow!")
    task_1()
    task_2()
    task_3()
    print("Goodbye from the end of the flow!")
