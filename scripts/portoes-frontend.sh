#!/bin/sh
# Portões do frontend (seção 6.D), os mesmos no computador e no CI.
#
#   docker compose run --rm dev scripts/portoes-frontend.sh
#
# Para no primeiro que falhar.
set -eu

cd "$(dirname "$0")/../frontend"

echo "== dependências pelo lockfile"
pnpm install --frozen-lockfile

echo "== ESLint: tipos, hooks do React, acessibilidade e padrões perigosos"
pnpm exec eslint .

echo "== Prettier: formatação"
pnpm exec prettier --check .

echo "== tipos (tsc estrito)"
pnpm exec tsc --noEmit
