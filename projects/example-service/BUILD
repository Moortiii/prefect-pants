pex_binary(
    name="prefect-example-service",
    execution_mode="venv",
    layout="loose",
    script="prefect",
    output_path="prefect.pex",
    inherit_path="prefer",
    dependencies=[
        "3rdparty/python#prefect",
        "projects/example-service/example_service/flows",
        "projects/example-service/example_service/tasks"
    ]
)

docker_image(
    name="prefect-pants",
)
