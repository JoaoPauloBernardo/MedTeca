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

echo "== tipos (tsc estrito: navegador e Node)"
pnpm exec tsc --noEmit -p tsconfig.json
pnpm exec tsc --noEmit -p tsconfig.node.json

echo "== contrato da API (OpenAPI e tipos gerados)"
python3 ../scripts/conferir_contrato.py

echo "== componentes (Vitest e Testing Library)"
pnpm exec vitest run

echo "== build do Vite"
pnpm exec vite build
