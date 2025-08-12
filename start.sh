#!/bin/bash

# Apply database migrations
python manage.py migrate

# Collect static files (optional, if you're serving static files)
python manage.py collectstatic --noinput

# Start Gunicorn server
gunicorn learning_log.wsgi:application --bind 0.0.0.0:$PORT
