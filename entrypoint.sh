#!/bin/bash

set -e

# Manually set the environment for PDM/PEP 582
export PYTHONPATH="/app/__pypackages__/3.10/lib"
export PATH="/app/__pypackages__/3.10/bin:$PATH"

# Run database migrations
pdm run manage migrate --noinput

# Collect static files
pdm run manage collectstatic --noinput

# Start Gunicorn
exec pdm run gunicorn
