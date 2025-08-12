#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Apply migrations
python manage.py migrate

# Collect static files (optional)
python manage.py collectstatic --noinput

# Start Gunicorn with correct module
gunicorn learning_log.wsgi:application --bind 0.0.0.0:$PORT
