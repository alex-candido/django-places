#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "--- Setting up environment variables ---"
# Vercel builds the project in /var/task, so $PWD will be /var/task
export LD_LIBRARY_PATH=$PWD/libs
# Note: Ensure libgdal.so is present in the libs/ directory for GeoDjango to work
export GDAL_LIBRARY_PATH=$PWD/libs/libgdal.so.30.0.1
export GEOS_LIBRARY_PATH=$PWD/libs/libgeos_c.so.1.16.0
echo "LD_LIBRARY_PATH set to: $LD_LIBRARY_PATH"
echo "GDAL_LIBRARY_PATH set to: $GDAL_LIBRARY_PATH"
echo "GEOS_LIBRARY_PATH set to: $GEOS_LIBRARY_PATH"

echo "--- Installing Python dependencies ---"
pip install -r requirements.txt

echo "--- Running Django migrations ---"
python3 ./src/manage.py makemigrations --noinput
python3 ./src/manage.py migrate --noinput

echo "--- Collecting static files ---"
python3 src/manage.py collectstatic --noinput

echo "--- Build script finished successfully ---"
