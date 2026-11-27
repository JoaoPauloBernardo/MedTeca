"""Contrato entre a API e o cliente TypeScript (FUND-17 e FUND-18).

Roda o próprio scripts/conferir_contrato.py, como o portão faz.
"""

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parents[3]
SCRIPT = RAIZ / "scripts" / "conferir_contrato.py"
VERSIONADO = RAIZ / "frontend" / "src" / "api"


def conferir(*argumentos: str) -> subprocess.CompletedProcess[str]:
    # Script do próprio repositório, com argumentos escritos nos testes.
    return subprocess.run(  # noqa: S603
        [sys.executable, str(SCRIPT), *argumentos],
        capture_output=True,
        text=True,
        timeout=300,
        check=False,
    )


def test_fund_17_tipos_gerados_do_openapi() -> None:
    # Os arquivos versionados são exatamente o que sai da API atual: o
    # OpenAPI exportado pelo Django Ninja e os tipos gerados a partir dele.
    resultado = conferir()

    assert resultado.returncode == 0, resultado.stdout + resultado.stderr
    assert "ok - FUND-18" in resultado.stdout
    assert '"/api/saude"' in (VERSIONADO / "esquema.d.ts").read_text(encoding="utf-8")


@pytest.mark.parametrize(
    ("arquivo", "trecho", "troca"),
    [
        ("openapi.json", '"indisponivel"', '"fora_do_ar"'),
        ("esquema.d.ts", '"indisponivel"', '"fora_do_ar"'),
    ],
    ids=["openapi-divergente", "tipos-divergentes"],
)
def test_fund_18_contrato_divergente_falha(
    tmp_path: Path, arquivo: str, trecho: str, troca: str
) -> None:
    # Uma cópia dos arquivos versionados com um deles alterado faz a
    # checagem falhar e apontar o arquivo.
    for nome in ("openapi.json", "esquema.d.ts"):
        shutil.copy(VERSIONADO / nome, tmp_path / nome)
    alterado = tmp_path / arquivo
    conteudo = alterado.read_text(encoding="utf-8")
    assert trecho in conteudo
    alterado.write_text(conteudo.replace(trecho, troca), encoding="utf-8")

    resultado = conferir("--versionado", str(tmp_path))

    assert resultado.returncode == 1
    assert "falha - FUND-18" in resultado.stdout
    assert f"versionado/{arquivo}" in resultado.stdout
