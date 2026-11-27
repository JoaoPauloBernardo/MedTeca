"""Política de dependências (FUND-04 a FUND-06; seção 6.E).

Os testes de lockfile rodam o uv e o pnpm de verdade, sobre cópias numa pasta
temporária, para nunca tocar nos arquivos do repositório.
"""

import json
import os
import re
import shutil
import subprocess
import tomllib
from pathlib import Path
from typing import Any

from ruamel.yaml import YAML

RAIZ = Path(__file__).resolve().parents[3]
BACKEND = RAIZ / "backend"
FRONTEND = RAIZ / "frontend"


def rodar(comando: list[str], pasta: Path, **ambiente: str) -> subprocess.CompletedProcess[str]:
    # Ferramentas do próprio ambiente (uv e pnpm), com argumentos fixos.
    return subprocess.run(  # noqa: S603
        comando,
        cwd=pasta,
        env={**os.environ, **ambiente},
        capture_output=True,
        text=True,
        timeout=300,
        check=False,
    )


def pnpm_workspace() -> dict[str, Any]:
    dados: dict[str, Any] = YAML(typ="safe").load(
        (FRONTEND / "pnpm-workspace.yaml").read_text(encoding="utf-8")
    )
    return dados


def test_fund_04_uv_lockfile_divergente_falha(tmp_path: Path) -> None:
    for nome in ("pyproject.toml", "uv.lock"):
        shutil.copy(BACKEND / nome, tmp_path / nome)
    lock_antes = (tmp_path / "uv.lock").read_bytes()
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text(
        pyproject.read_text(encoding="utf-8").replace(
            '"django-ninja>=1.8",', '"django-ninja>=1.8",\n    "six>=1.17",'
        ),
        encoding="utf-8",
    )

    resultado = rodar(
        ["uv", "sync", "--locked"], tmp_path, UV_PROJECT_ENVIRONMENT=str(tmp_path / "venv")
    )

    assert resultado.returncode != 0
    assert "--locked" in resultado.stderr
    assert (tmp_path / "uv.lock").read_bytes() == lock_antes


def test_fund_04_pnpm_lockfile_divergente_falha(tmp_path: Path) -> None:
    for nome in ("package.json", "pnpm-workspace.yaml", "pnpm-lock.yaml"):
        shutil.copy(FRONTEND / nome, tmp_path / nome)
    lock_antes = (tmp_path / "pnpm-lock.yaml").read_bytes()
    manifesto = json.loads((tmp_path / "package.json").read_text(encoding="utf-8"))
    manifesto["dependencies"]["left-pad"] = "^1.3.0"
    (tmp_path / "package.json").write_text(json.dumps(manifesto, indent=2), encoding="utf-8")

    resultado = rodar(["pnpm", "install", "--frozen-lockfile"], tmp_path)

    assert resultado.returncode != 0
    assert "ERR_PNPM_OUTDATED_LOCKFILE" in resultado.stdout + resultado.stderr
    assert (tmp_path / "pnpm-lock.yaml").read_bytes() == lock_antes


def test_fund_04_comandos_usam_o_lockfile() -> None:
    # Todo comando de instalação do repositório usa o lockfile, sem
    # recalcular: o uv com --locked e o pnpm com --frozen-lockfile. O uv run
    # do script de contrato também, porque ele instala o que falta.
    arquivos = [*sorted((RAIZ / "scripts").glob("*")), RAIZ / "compose.yaml"]
    trechos = [(arquivo, arquivo.read_text(encoding="utf-8")) for arquivo in arquivos]

    uv_sync = [
        (a.name, linha) for a, t in trechos for linha in t.splitlines() if "uv sync" in linha
    ]
    pnpm_install = [
        (a.name, linha) for a, t in trechos for linha in t.splitlines() if "pnpm install" in linha
    ]
    contrato = (RAIZ / "scripts" / "conferir_contrato.py").read_text(encoding="utf-8")

    assert uv_sync and pnpm_install
    assert all("--locked" in linha for _, linha in uv_sync), uv_sync
    assert all("--frozen-lockfile" in linha for _, linha in pnpm_install), pnpm_install
    assert '"uv", "run", "--locked"' in contrato


def test_fund_04_dependencias_diretas_do_registro() -> None:
    # O blockExoticSubdeps do pnpm só cobre as dependências indiretas: as
    # diretas precisam ser faixas de versão do registro, sem git:, file:,
    # link:, github: ou endereço.
    manifesto = json.loads((FRONTEND / "package.json").read_text(encoding="utf-8"))
    faixa_do_registro = re.compile(r"^[\^~]?\d+\.\d+\.\d+$")
    diretas = {**manifesto["dependencies"], **manifesto["devDependencies"]}
    fora_do_registro = {
        nome: versao for nome, versao in diretas.items() if not faixa_do_registro.match(versao)
    }
    assert fora_do_registro == {}

    # No Python, uma dependência com " @ " aponta direto para um endereço.
    pyproject = tomllib.loads((BACKEND / "pyproject.toml").read_text(encoding="utf-8"))
    requisitos = [
        *pyproject["project"]["dependencies"],
        *pyproject["dependency-groups"]["dev"],
    ]
    assert [r for r in requisitos if " @ " in r] == []


def test_fund_05_uv_espera_7_dias() -> None:
    pyproject = tomllib.loads((BACKEND / "pyproject.toml").read_text(encoding="utf-8"))
    lock = tomllib.loads((BACKEND / "uv.lock").read_text(encoding="utf-8"))

    assert pyproject["tool"]["uv"]["exclude-newer"] == "7 days"
    # O lock guarda a espera como período, para não envelhecer de um dia para
    # o outro (V37).
    assert lock["options"]["exclude-newer-span"] == "P7D"


def test_fund_05_pnpm_espera_7_dias() -> None:
    # 10.080 minutos são 7 dias.
    assert pnpm_workspace()["minimumReleaseAge"] == 10080


def test_fund_06_pnpm_bloqueia_scripts() -> None:
    workspace = pnpm_workspace()

    assert workspace["strictDepBuilds"] is True
    # Nenhum script de instalação liberado até hoje; cada liberação futura é
    # aprovada pelo usuário e acrescentada aqui (seção 6.E.3).
    assert workspace["allowBuilds"] == {}
