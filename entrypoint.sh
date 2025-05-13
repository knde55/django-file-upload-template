#!/bin/sh
set -e

# Wait for PostgreSQL to be ready
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -c '\q'; do
  echo "PostgreSQL is unavailable - sleeping"
  sleep 2
done

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start server
echo "Starting Gunicorn..."
exec gunicorn core.wsgi:application --bind 0.0.0.0:8000
