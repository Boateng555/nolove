#!/usr/bin/env bash
set -e

DB_URL="${DATABASE_URL:-${POSTGRES_URL:-${POSTGRES_PRISMA_URL:-}}}"

if [ -n "$VERCEL" ] && [ -z "$DB_URL" ]; then
  echo ""
  echo "ERROR: No database configured for Vercel."
  echo "Add DATABASE_URL in Vercel → Project → Settings → Environment Variables."
  echo "Get a free Postgres URL from https://neon.tech"
  echo ""
  exit 1
fi

if [ -n "$DB_URL" ]; then
  export DATABASE_URL="$DB_URL"
  python manage.py migrate --noinput
  python manage.py setup_admin
fi
