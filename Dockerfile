# The builder image, used to build the virtual environment
FROM python:3.11-buster as builder

RUN apt-get update && apt-get install -y git

RUN pip install poetry==1.4.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

ENV HOST=0.0.0.0
ENV LISTEN_PORT 8080
EXPOSE 8080

WORKDIR /app

#COPY pyproject.toml ./app/pyproject.toml
#COPY poetry.lock ./app/poetry.lock
COPY pyproject.toml ./

COPY requirements.txt ./

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

RUN pip install -r requirements.txt

# The runtime image, used to just run the code provided its virtual environment
FROM python:3.11-slim-buster as runtime

ENV VIRTUAL_ENV=/app/.venv
ENV PATH = "${VIRTUAL_ENV}/bin:$PATH"
ENV PATH="/app/.venv/bin:$PATH"

ENV PATH="/root/.local/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY ./demo_app ./demo_app
COPY ./.streamlit ./.streamlit

EXPOSE 8080

#ENTRYPOINT [ ".venv/bin/python", "-m", "streamlit", "run", "demo_app/main.py", "--server.port", "8501", "--server.address=0.0.0.0"]

CMD ["streamlit", "run", "--client.showSidebarNavigation=False", "demo_app/main.py", "--server.port", "8080"]