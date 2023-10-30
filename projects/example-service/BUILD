file(name="deployments", source="prefect.yaml")

pex_binary(
    name="prefect-deps",
    layout="packed",
    output_path="prefect-deps.pex",
    dependencies=[
        "3rdparty/python#prefect",
        "projects/example-service/example_service/flows",
        "projects/example-service/example_service/tasks",
    ],
    include_sources=False,
    include_requirements=True,
    include_tools=True
)

pex_binary(
    name="prefect-srcs",
    layout="packed",
    output_path="prefect-srcs.pex",
    dependencies=[
        "projects/example-service/example_service/flows",
        "projects/example-service/example_service/tasks",
    ],
    include_sources=True,
    include_requirements=False,
    include_tools=True
)

docker_image(
    name="prefect-pants",
    dependencies=[
        ":deployments"
    ]
)
