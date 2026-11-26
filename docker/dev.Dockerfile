# Imagem de desenvolvimento do MedTeca: Python, uv, Node e pnpm num só
# contêiner, usado pelo VS Code, pelos servidores da API e do frontend e
# pelos testes (design da fundação; P6-04 e P6-24).
#
# Versões escolhidas em 2026-11-26, todas publicadas há mais de 7 dias
# (P6-08), e imagens fixadas por digest (seção 6.D). Quem atualiza é o
# Dependabot, com a mesma espera.

# Node 26.13.0 (LTS ativa), Debian 13 (trixie); publicado em 2026-11-05.
FROM node:26.13.0-trixie-slim@sha256:5adad64f9a1fca2d51972caa65983634c8a774eb300d72b20f7f2a0f60368072 AS node
# O Node depende da libatomic, que a imagem do Python não traz; ela sai
# daqui para não abrir outra fonte de pacotes (seção 6.E.1).
RUN mkdir /bibliotecas && cp -L /usr/lib/*-linux-gnu/libatomic.so.1 /bibliotecas/

# Python 3.15.1, Debian 13 (trixie); publicado em 2026-10-24.
FROM python:3.15.1-slim-trixie@sha256:533b0b2f9b5d46fd097091cf826f27902f1d6c3bca714b6dc74551356aa97a51

# Node e npm vêm da imagem oficial do Node, no mesmo Debian.
COPY --from=node /usr/local/bin/node /usr/local/bin/node
COPY --from=node /usr/local/lib/node_modules /usr/local/lib/node_modules
COPY --from=node /bibliotecas/libatomic.so.1 /usr/local/lib/libatomic.so.1
RUN ldconfig \
 && ln -s ../lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm \
 && ln -s ../lib/node_modules/npm/bin/npx-cli.js /usr/local/bin/npx

# uv do PyPI, com o hash de cada arquivo conferido (RNF-72).
ARG UV_VERSION=0.13.9
RUN printf '%s\n' \
      "uv==${UV_VERSION} \\" \
      "  --hash=sha256:d7f459fe4fd247d830351c75686d3996ace3c6f3f728eb0e85a30b7ada0cef19 \\" \
      "  --hash=sha256:ecb6028d79dc96fbeafffe5c8af62a7099487ebc05a701e76714eebcffd06375" \
      > /tmp/ferramentas.txt \
 && pip install --no-cache-dir --disable-pip-version-check --require-hashes -r /tmp/ferramentas.txt \
 && rm /tmp/ferramentas.txt

# pnpm do registro do npm: o pacote é baixado, o SHA-512 é conferido e só
# então ele é instalado, sem rodar scripts de instalação (P6-09). Depois, o
# npm e o npx saem da imagem: eles instalariam a versão mais nova de
# qualquer pacote, rodando os scripts dele, fora da política do projeto.
ARG PNPM_VERSION=11.28.13
ARG PNPM_SHA512=d5caa9cdcd6067ac2902f9f44daa00b1288a73babf1e98f4f375b3a7583b1894b4d49f7527da8f5e1530198bb10e03adba321a1f015429dc2946ce8a7a9a8c65
RUN cd /tmp \
 && npm pack --silent "pnpm@${PNPM_VERSION}" \
 && echo "${PNPM_SHA512}  pnpm-${PNPM_VERSION}.tgz" | sha512sum -c - \
 && npm install --global --ignore-scripts "./pnpm-${PNPM_VERSION}.tgz" \
 && rm "pnpm-${PNPM_VERSION}.tgz" \
 && npm cache clean --force \
 && rm -rf /usr/local/lib/node_modules/npm /usr/local/bin/npm /usr/local/bin/npx

# A política de dependências vale também para comandos avulsos, fora dos
# arquivos do projeto (seção 6.E): o pip exige hash, o uv e o pnpm esperam
# 7 dias por versões novas e o pnpm barra scripts de instalação. O uv nunca
# baixa Python por conta própria: usa o da imagem.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_REQUIRE_HASHES=1 \
    UV_EXCLUDE_NEWER="7 days" \
    UV_PYTHON_DOWNLOADS=never \
    UV_LINK_MODE=copy \
    UV_CACHE_DIR=/home/dev/.cache/uv \
    pnpm_config_minimum_release_age=10080 \
    pnpm_config_strict_dep_builds=true

# Usuário sem privilégio. As pastas que viram volumes nascem com esse dono,
# para que o Docker copie a permissão certa ao criar cada volume.
RUN useradd --create-home --uid 1000 --shell /bin/bash dev \
 && mkdir -p /workspace/backend/.venv /workspace/frontend/node_modules \
             /home/dev/.cache/uv /home/dev/.local/share/pnpm \
 && chown -R dev:dev /workspace /home/dev

USER dev
WORKDIR /workspace
