## Prefect Pants

Example repository for using Prefect in combination with Pants for seamless task orchestration in a monorepo setting.

### Running deployments

To run the preconfigured deployment represented in `prefect.yaml`:

```
prefect deployment run 'example-flow/example-deployment'
```

### Serving flows directly

Serving an polling for runs of a flow can be done using:

```
prefect flow serve --name example-flow example_flow.py:example_flow
```

Multiple instances of this command (e.g. in separate containers) will all poll for runs of the same flow. This can be used to easily scale to X number of workers.