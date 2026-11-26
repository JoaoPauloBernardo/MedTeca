"""Rota de saúde da API (FUND-07 a FUND-09), sobre o PostgreSQL real (D-026)."""

import pytest
from django.db import OperationalError, connection
from django.test import Client

pytestmark = pytest.mark.django_db

# Texto de erro que o banco poderia devolver; a resposta nunca pode trazê-lo.
ERRO_DO_BANCO = "connection refused: db:5432 (usuario medteca)"


@pytest.fixture
def banco_fora(monkeypatch: pytest.MonkeyPatch) -> None:
    """Simula o banco fora do ar: abrir um cursor falha como numa conexão recusada."""

    def falhar(*args: object, **kwargs: object) -> None:
        raise OperationalError(ERRO_DO_BANCO)

    monkeypatch.setattr(connection, "cursor", falhar)


def test_fund_07_saude_responde_ok(client: Client) -> None:
    resposta = client.get("/api/saude")

    assert resposta.status_code == 200
    assert resposta.json() == {"situacao": "ok"}


def test_fund_08_banco_fora_responde_503(client: Client, banco_fora: None) -> None:
    resposta = client.get("/api/saude")

    assert resposta.status_code == 503
    assert resposta.json() == {"situacao": "indisponivel"}
    assert "connection refused" not in resposta.content.decode()


@pytest.mark.parametrize("banco", ["banco-no-ar", "banco-fora"])
def test_fund_09_saude_sem_cache(
    client: Client, request: pytest.FixtureRequest, banco: str
) -> None:
    if banco == "banco-fora":
        request.getfixturevalue("banco_fora")

    resposta = client.get("/api/saude")

    assert resposta["Cache-Control"] == "no-store"
