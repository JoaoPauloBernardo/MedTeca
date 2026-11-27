"""Portas que o Compose publica no computador do usuário (FUND-02)."""

from pathlib import Path
from typing import Any

from ruamel.yaml import YAML

RAIZ = Path(__file__).resolve().parents[3]


def carregar_compose() -> dict[str, Any]:
    compose: dict[str, Any] = YAML(typ="safe").load(
        (RAIZ / "compose.yaml").read_text(encoding="utf-8")
    )
    return compose


def test_fund_02_so_porta_5173_em_localhost() -> None:
    servicos: dict[str, dict[str, Any]] = carregar_compose()["services"]

    publicadas = {
        nome: servico["ports"] for nome, servico in servicos.items() if "ports" in servico
    }

    # Só o servidor do frontend, e só para o próprio computador (127.0.0.1):
    # nem a API nem o banco ficam alcançáveis de fora.
    assert publicadas == {"web": ["127.0.0.1:5173:5173"]}
