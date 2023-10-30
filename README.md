## Prefect Pants

Example repository for using Prefect in combination with Pants for seamless task orchestration in a monorepo setting.

## Starting the services

To start the server:

```
docker compose --profile server up
```

This starts the database as well. You can now run:

```
docker compose run cli
```

To enter a container where you can run the prefect commands.

### Running deployments

To run the preconfigured deployment represented in `prefect.yaml`:

```
python /app/prefect deployment run 'example-flow/example-deployment'
```

### Serving flows directly

Serving an polling for runs of a flow can be done using:

```
python /app/prefect flow serve --name example-flow example_flow.py:example_flow
```

Multiple instances of this command (e.g. in separate containers) will all poll for runs of the same flow. This can be used to easily scale to X number of workers.