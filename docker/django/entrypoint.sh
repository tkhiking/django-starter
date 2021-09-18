#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

main() {
  if [ -z "${POSTGRES_USER}" ]; then
    base_postgres_image_default_user='postgres'
    export POSTGRES_USER="${base_postgres_image_default_user}"
  fi
  export DATABASE_URL="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"
  wait_postgres
  python ./manage.py collectstatic --noinput
  exec gunicorn config.wsgi --bind 0.0.0.0:$PORT --chdir=.
}

wait_postgres() {
  until postgres_ready; do
    echo 'Waiting for PostgreSQL to become available...' >&2
    sleep 1
  done
  echo 'PostgreSQL is available!' >&2
}

postgres_ready() {
  python << EOS
import sys
import psycopg2
try:
    psycopg2.connect(
        dbname="${POSTGRES_DB}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASSWORD}",
        host="${POSTGRES_HOST}",
        port="${POSTGRES_PORT}",
    )
except psycopg2.OperationalError:
    sys.exit(1)
sys.exit(0)
EOS
}

main "$@"
