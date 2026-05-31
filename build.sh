#!/usr/bin/env bash
set -e

python manage.py collectstatic --noinput

if [ -n "$DATABASE_URL" ]; then
  python manage.py migrate --noinput
  python manage.py setup_admin
fi
