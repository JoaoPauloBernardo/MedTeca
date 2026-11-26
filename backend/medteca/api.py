"""API do MedTeca (Django Ninja), servida sob /api/."""

from typing import Literal

from django.conf import settings
from django.db import DatabaseError, connection
from django.http import HttpRequest, HttpResponse
from ninja import NinjaAPI, Schema, Status

api = NinjaAPI(
    title="MedTeca",
    version="0.1.0",
    # Documentação e OpenAPI só fora da produção (FUND-19, ASVS 13.4.5).
    docs_url="/docs" if settings.MEDTECA_DOCS_DA_API else None,
    openapi_url="/openapi.json" if settings.MEDTECA_DOCS_DA_API else None,
)


class Saude(Schema):
    situacao: Literal["ok", "indisponivel"]


@api.get(
    "/saude",
    response={200: Saude, 503: Saude},
    summary="Situação da API e do banco",
    tags=["saúde"],
)
def saude(request: HttpRequest, response: HttpResponse) -> Status[Saude]:
    """Responde 200 quando o banco atende a uma consulta e 503 quando não.

    Nunca devolve detalhes do erro (FUND-08), e a resposta não vai para
    cache (FUND-09). O `response` é a resposta temporária do Django Ninja,
    onde se põem cabeçalhos.
    """
    response["Cache-Control"] = "no-store"
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
    except DatabaseError:
        return Status(503, Saude(situacao="indisponivel"))
    return Status(200, Saude(situacao="ok"))
