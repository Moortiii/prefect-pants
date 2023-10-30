## Prefect Pants

An example repository for using Prefect in combination with Pants for seamless task orchestration in a monorepo setting.

I don't personally recommend using docker volumes in  a production setting, but it has been included here to show that it is possible for development purposes.

## Prerequisites

* Docker and the docker-compose plugin must be installed and available on PATH.

* The Python executable is built using Python 3.11.6. This version of Python must be installed and available as an interpreter on your local system

* The Taskfile.yml requires [go-task](https://taskfile.dev/), a modern Makefile alternative, but is completely optional. I only use it to maintain the `.env` file with the PYTHONPATH and to have quick aliases for generating lockfiles and packaging / building images. 

## Getting started

1. Create our custom Docker image:

    `pants package ::`

2. Start the server:

    `docker compose up server`

3. Start the worker:

    `docker-compose up worker`
    
4. Run the CLI:

    `docker compose run cli`

5. Run the command:

    `prefect deploy`

    Press Enter to use existing deployment to use values in preconfigured `prefect.yaml` file. Alternatively create a new deployment and set your schedule as you please.

## What's included in this project

The instructions above create a flow that will run every 15 seconds by the worker.

Both your flow code, task code and included libraries are being volumed in. This means that you can update your flows and library without restarting your services.

We use a multi-stage build, as outlined in this [excellent article](https://blog.pantsbuild.org/optimizing-python-docker-deploys-using-pants/) by Joshua Cannon, to ensure we can make use of caching for both Pants and Docker. This significantly speeds up build times as most of the time we're only making changes to our first-party code and not adding new third-party requirements.

## Trigger a flow manually

If you don't want your flow to run on a schedule you can turn it off in the Web UI and trigger it manually using:

`prefect deployment run 'example-flow/example-deployment'`


