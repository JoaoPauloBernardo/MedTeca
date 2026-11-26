"""Configurações de produção (FUND-19 a FUND-21).

Cada teste roda o Django num processo separado, com DJANGO_SETTINGS_MODULE
apontando para medteca.settings.prod. A API é montada quando o módulo é
importado; trocar configurações dentro do processo dos testes não provaria o
que a produção carrega.
"""

import os
import secrets
import subprocess
import sys
from pathlib import Path

import pytest

BACKEND = Path(__file__).resolve().parent.parent
HOST = "medteca.test"


def rodar_em_producao(
    *argumentos: str,
    sem: tuple[str, ...] = (),
    com: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    """Roda o Python do projeto com as variáveis de ambiente da produção."""
    ambiente = {
        **os.environ,
        "DJANGO_SETTINGS_MODULE": "medteca.settings.prod",
        "DJANGO_SECRET_KEY": secrets.token_urlsafe(64),
        "DJANGO_ALLOWED_HOSTS": HOST,
        **(com or {}),
    }
    for nome in sem:
        ambiente.pop(nome, None)
    # Os argumentos são fixos, escritos nos próprios testes.
    return subprocess.run(  # noqa: S603
        [sys.executable, *argumentos],
        cwd=BACKEND,
        env=ambiente,
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )


PEDIDOS_EM_PRODUCAO = f"""
import django
django.setup()
from django.test import Client
cliente = Client(HTTP_HOST="{HOST}")
for caminho in ("/api/docs", "/api/openapi.json", "/api/saude"):
    print(caminho, cliente.get(caminho, secure=True).status_code)
"""


def test_fund_19_docs_fora_em_producao() -> None:
    resultado = rodar_em_producao("-c", PEDIDOS_EM_PRODUCAO)

    assert resultado.returncode == 0, resultado.stderr
    # A rota de saúde responde 200: a API está de pé, só a documentação some.
    assert resultado.stdout.split() == [
        "/api/docs", "404",
        "/api/openapi.json", "404",
        "/api/saude", "200",
    ]  # fmt: skip


AVISOS_SILENCIADOS = """
import django
django.setup()
from django.conf import settings
print(" ".join(settings.SILENCED_SYSTEM_CHECKS))
"""


def test_fund_20_check_deploy_sem_avisos() -> None:
    resultado = rodar_em_producao("manage.py", "check", "--deploy", "--fail-level", "WARNING")

    assert resultado.returncode == 0, resultado.stdout + resultado.stderr
    assert "System check identified no issues" in resultado.stdout

    # Só os dois avisos que ficam a cargo do Caddy (seção 5.H) podem estar
    # silenciados; qualquer outro precisa passar por aqui com motivo.
    silenciados = rodar_em_producao("-c", AVISOS_SILENCIADOS)
    assert silenciados.stdout.split() == ["security.W004", "security.W008"]


@pytest.mark.parametrize("segredo", ["ausente", "vazio"])
def test_fund_21_producao_exige_segredo(segredo: str) -> None:
    if segredo == "ausente":
        resultado = rodar_em_producao("manage.py", "check", sem=("DJANGO_SECRET_KEY",))
    else:
        resultado = rodar_em_producao("manage.py", "check", com={"DJANGO_SECRET_KEY": ""})

    assert resultado.returncode != 0
    assert "ImproperlyConfigured" in resultado.stderr
    assert "DJANGO_SECRET_KEY" in resultado.stderr
