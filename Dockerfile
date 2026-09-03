# Stage 1: Build Environment
FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim AS builder

ENV UV_COMPILE_BYTECODE=1 
ENV UV_LINK_MODE=copy

WORKDIR /app

# Install dependencies using the lockfile and pyproject.toml
# Mount cache volumes to make subsequent builds blisteringly fast
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# Copy the actual application source code and install it
ADD src /app/src
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Stage 2: Production Runtime Environment
FROM python:3.14-slim-bookworm

# Copy the built virtual environment from the builder stage
COPY --from=builder --chown=app:app /app /app

# Ensure the virtual environment executables are at the front of the PATH
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Default command for FastAPI service
CMD ["fastapi", "run", "--host", "0.0.0.0", "src/credit_classification_pipeline/serve/app.py"]