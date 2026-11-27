#!/usr/bin/env python3
"""Contrato entre a API e o frontend (FUND-17 e FUND-18).

Exporta o OpenAPI do Django Ninja e gera os tipos TypeScript com o
openapi-typescript numa pasta temporária, e compara os dois com os arquivos
versionados em frontend/src/api/.

    docker compose run --rm dev python3 scripts/conferir_contrato.py
    docker compose run --rm dev python3 scripts/conferir_contrato.py --gerar

Sem opções, confere: sai com 1 e mostra a diferença quando a API e o cliente
divergem. Com --gerar, regera os arquivos versionados. Não usa o Git, que
roda fora dos contêineres (seção 6.J.1).
"""

import argparse
import difflib
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BACKEND = RAIZ / "backend"
FRONTEND = RAIZ / "frontend"
VERSIONADO = FRONTEND / "src" / "api"
ARQUIVOS = ("openapi.json", "esquema.d.ts")


def gerar(destino: Path) -> None:
    """Exporta o OpenAPI e gera os tipos TypeScript dentro de `destino`."""
    openapi = destino / "openapi.json"
    # Comandos fixos, com ferramentas do próprio ambiente (uv e pnpm). O
    # --locked impede o uv de reescrever o uv.lock se o pyproject.toml mudou
    # sem um lock novo: a checagem falha, como pede o FUND-04.
    subprocess.run(  # noqa: S603
        ["uv", "run", "--locked", "python", "manage.py", "export_openapi_schema",  # noqa: S607
         "--api", "medteca.api.api", "--output", str(openapi), "--indent", "2", "--sorted"],
        cwd=BACKEND,
        check=True,
    )  # fmt: skip
    subprocess.run(  # noqa: S603
        ["pnpm", "exec", "openapi-typescript", str(openapi),  # noqa: S607
         "--output", str(destino / "esquema.d.ts")],
        cwd=FRONTEND,
        check=True,
    )  # fmt: skip


def diferencas(versionado: Path, gerado: Path) -> list[str]:
    """Diferença unificada de cada arquivo do contrato; vazia quando batem."""
    saida: list[str] = []
    for nome in ARQUIVOS:
        arquivo = versionado / nome
        antes = arquivo.read_text(encoding="utf-8").splitlines(True) if arquivo.exists() else []
        depois = (gerado / nome).read_text(encoding="utf-8").splitlines(True)
        saida.extend(difflib.unified_diff(antes, depois, f"versionado/{nome}", f"gerado/{nome}"))
    return saida


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0] if __doc__ else None)
    parser.add_argument("--gerar", action="store_true", help="regera os arquivos versionados")
    parser.add_argument("--versionado", type=Path, default=VERSIONADO, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    if args.gerar:
        args.versionado.mkdir(parents=True, exist_ok=True)
        gerar(args.versionado)
        print(f"contrato gerado em {args.versionado}")
        return 0

    with tempfile.TemporaryDirectory() as temporaria:
        gerado = Path(temporaria)
        gerar(gerado)
        diferenca = diferencas(args.versionado, gerado)

    if diferenca:
        sys.stdout.writelines(diferenca)
        print(
            "falha - FUND-18: a API e o cliente TypeScript divergem. Rode "
            "scripts/conferir_contrato.py --gerar e revise a diferença."
        )
        return 1

    print("ok - FUND-18: contrato em dia")
    return 0


if __name__ == "__main__":
    sys.exit(main())
