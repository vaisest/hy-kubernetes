FROM ghcr.io/astral-sh/uv:alpine

ENV PORT=8080

WORKDIR /app
COPY main.py .
COPY pyproject.toml .
COPY uv.lock .

RUN uv sync

CMD ["uv", "run", "fastapi", "dev"]