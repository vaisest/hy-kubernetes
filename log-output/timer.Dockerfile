FROM ghcr.io/astral-sh/uv:alpine

ENV PORT=8080

WORKDIR /app
COPY pyproject.toml .
COPY uv.lock .

RUN uv sync

COPY timer.py .
CMD ["uv", "run", "timer.py"]