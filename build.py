"""Vercel build step: run migrations and seed admin when DATABASE_URL is set."""
import os
import subprocess
import sys


def run(*args: str) -> None:
    print('>>>', ' '.join(args), flush=True)
    subprocess.check_call(args)


def main() -> None:
    db_url = (
        os.environ.get('DATABASE_URL')
        or os.environ.get('POSTGRES_URL')
        or os.environ.get('POSTGRES_PRISMA_URL')
    )
    is_vercel = bool(os.environ.get('VERCEL') or os.environ.get('VERCEL_ENV'))

    if is_vercel and not db_url:
        print(
            '\n'
            'BUILD FAILED: DATABASE_URL is not set.\n'
            '\n'
            '1. Go to https://neon.tech and create a free Postgres database\n'
            '2. Copy the connection string\n'
            '3. Vercel -> nolove -> Settings -> Environment Variables\n'
            '4. Add DATABASE_URL = your connection string\n'
            '5. Check Production, Preview, and Development, then Redeploy\n'
            '\n',
            flush=True,
        )
        sys.exit(1)

    if not db_url:
        print('No DATABASE_URL — skipping migrate (local dev).', flush=True)
        return

    os.environ['DATABASE_URL'] = db_url
    run(sys.executable, 'manage.py', 'migrate', '--noinput')
    run(sys.executable, 'manage.py', 'setup_admin')


if __name__ == '__main__':
    main()
