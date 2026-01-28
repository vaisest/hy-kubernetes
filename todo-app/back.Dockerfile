FROM ghcr.io/astral-sh/uv:alpine

ENV PORT=8080

WORKDIR /app
COPY pyproject.toml .
COPY uv.lock .

RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    uv sync && \
    apk --purge del .build-deps

COPY backend.py .
CMD ["uv", "run", "fastapi", "run", "backend.py"]