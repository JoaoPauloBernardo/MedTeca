#!/bin/sh
# Portões do backend (seção 6.D), os mesmos no computador e no CI.
#
#   docker compose run --rm dev scripts/portoes-backend.sh
#
# Para no primeiro que falhar.
set -eu

cd "$(dirname "$0")/../backend"

echo "== dependências pelo lockfile"
uv sync --locked

echo "== Ruff: lint e regras de segurança do Bandit"
uv run ruff check .

echo "== Ruff: formatação"
uv run ruff format --check .

echo "== mypy estrito"
uv run mypy .

echo "== migrações pendentes"
uv run python manage.py makemigrations --check --dry-run

echo "== configuração de produção (check --deploy)"
DJANGO_SETTINGS_MODULE=medteca.settings.prod \
DJANGO_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(64))')" \
DJANGO_ALLOWED_HOSTS=medteca.test \
  uv run python manage.py check --deploy --fail-level WARNING

echo "== testes (pytest no PostgreSQL 18)"
uv run pytest
