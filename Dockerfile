# syntax=docker/dockerfile:1

# --- Base Stage ---
FROM python:3.10.3-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PDM_USE_VENV=0

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl gcc bash libgeos-dev libgdal-dev libproj-dev gdal-bin && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://pdm-project.org/install-pdm.py | python3 - 

ENV PATH="/root/.local/bin:${PATH}"

# --- Builder Stage ---
FROM base AS builder

COPY pyproject.toml pdm.lock README.md ./

RUN pdm sync --prod --no-editable

# --- Final Stage ---
FROM base AS final

COPY --from=builder /app/__pypackages__ /app/__pypackages__
COPY . .

# Configure bashrc for interactive PDM sessions
RUN echo 'export PYTHONPATH="/app/__pypackages__/3.10/lib"' >> /root/.bashrc
RUN echo 'export PATH="/app/__pypackages__/3.10/bin:$PATH"' >> /root/.bashrc

# Make entrypoint script executable
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

# Run entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]