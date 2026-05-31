#!/usr/bin/env bash
set -e

if [ -n "$DATABASE_URL" ]; then
  python manage.py migrate --noinput
  python manage.py setup_admin
fi
