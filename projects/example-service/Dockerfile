FROM python:3.11.6 as deps

COPY prefect-deps.pex /app/prefect-deps.pex
RUN PEX_TOOLS=1 python /app/prefect-deps.pex venv --scope=deps --compile /bin/app

FROM python:3.11.6 as srcs

COPY prefect-srcs.pex /app/prefect-srcs.pex
RUN PEX_TOOLS=1 python /app/prefect-srcs.pex venv --scope=srcs --compile /bin/app

FROM python:3.11.6

WORKDIR /bin/app

COPY --from=deps /bin/app /bin/app
COPY --from=srcs /bin/app /bin/app

COPY projects/example-service/prefect.yaml prefect.yaml

RUN ln -s /bin/app/bin/prefect /bin/prefect