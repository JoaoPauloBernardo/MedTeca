# Fundação do projeto Tasks

## Execution Protocol (MANDATORY -- do not skip)

Implement these tasks with the `tlc-spec-driven` skill: **activate it by name and follow its Execute flow and Critical Rules.** Do not search for skill files by filesystem path. The skill is the source of truth for the full flow (per-task cycle, sub-agent delegation, the walk, check_proofs, the Verifier and the screens sub-agent).

**If the skill cannot be activated, STOP and tell the user - do not proceed without it.**

Regras do projeto que valem junto (D-034, seção 6.C):

- Cada fase vira um pull request, numa branch própria a partir da `main` atualizada. Ao abrir o pull request, o Claude para e espera a revisão e o merge do usuário antes de começar a fase seguinte.
- Lockfiles e arquivos gerados entram em commits separados e marcados (6.C.7).
- Antes de apresentar cada pull request: revisão por outra sessão do Claude, sem o contexto de quem escreveu (6.C.5), e explicação técnica com os 7 itens (6.C.6).
- Qualquer dependência fora das listadas no design, liberação de script de instalação (6.E.3) ou exceção à espera de 7 dias é perguntada ao usuário antes.

---

**Design**: `.specs/features/fundacao/design.md`
**Status**: Approved
**Approved**: 2026-11-26 - user: "Aprovo, pode seguir"
**Build**: none - o repositório ainda não tem código; os portões nascem nas fases 2 e 3 (`scripts/portoes-backend.sh` e `scripts/portoes-frontend.sh`) e rodam no CI a partir da fase 5
**Run backend**: `docker compose run --rm dev sh -c "cd backend && uv run pytest -v -p no:cacheprovider"`
**Run frontend**: `docker compose run --rm dev sh -c "cd frontend && pnpm exec vitest run --reporter=verbose"`
**Run e2e**: `docker compose up -d --wait db api web && docker compose --profile e2e run --rm e2e`
**Run isolamento**: `docker compose run --rm dev scripts/conferir-isolamento.sh`

---

## Test Coverage Matrix

> Generated from project guidelines and spec - confirm before Execute. Guidelines found: D-026 (`docs/decisions.md`), seção 6.D (`docs/seguranca-e-privacidade.md`). O repositório ainda não tem testes.

| Code Layer | Required Test Type | Coverage Expectation | Location Pattern | Run Command |
| --- | --- | --- | --- | --- |
| Rotas da API (Django Ninja) | integration (pytest-django em PostgreSQL 18) | Cada rota: caminho feliz e cada falha listada; um teste por critério | `backend/tests/test_*.py` | Run backend |
| Configurações de produção | integration (subprocesso com `medteca.settings.prod`) | FUND-19 a FUND-21 | `backend/tests/test_producao.py` | Run backend |
| Configuração do repositório (compose, workflows, Dependabot, pnpm, uv, `SECURITY.md`, modelo de PR) | unit (leitura dos arquivos) | Um teste por critério | `backend/tests/repositorio/test_*.py` | Run backend |
| Checagem de contrato | unit | Caso em dia e caso divergente | `backend/tests/repositorio/test_contrato.py` | Run backend |
| Componentes React | unit (Vitest e Testing Library) | Cada estado dos critérios | `frontend/src/**/*.test.tsx` | Run frontend |
| Página no navegador | e2e (Playwright e axe-core) | FUND-01 e FUND-14 a FUND-16, nos três perfis | `frontend/e2e/*.spec.ts` | Run e2e |
| Ambiente (imagem e Compose) | script | FUND-03 | `scripts/conferir-isolamento.sh` | Run isolamento |
| Editor (Dev Containers) | walk do usuário | FUND-32 a FUND-34 | - | walk |
| Arquivos de configuração sem critério próprio | none | Só o portão | - | Gate |

## Gate Check Commands

> Generated from the design - confirm before Execute.

| Gate Level | When to Use | Command |
| --- | --- | --- |
| ambiente | Tarefas de imagem, Compose e configuração sem teste próprio | `docker compose build dev` |
| isolamento | Depois de mexer na imagem ou nas montagens | `docker compose run --rm dev scripts/conferir-isolamento.sh` |
| instalar | Depois de gerar um lockfile | `docker compose run --rm dev sh -c "cd backend && uv sync --locked"` ou `docker compose run --rm dev sh -c "cd frontend && pnpm install --frozen-lockfile"` |
| django | Projeto Django antes do primeiro teste | `docker compose run --rm dev sh -c "cd backend && uv run python manage.py check"` |
| backend | Tarefas com testes do backend ou do repositório | `docker compose run --rm dev scripts/portoes-backend.sh` |
| frontend | Tarefas do frontend | `docker compose run --rm dev scripts/portoes-frontend.sh` |
| e2e | Tarefas de ponta a ponta | `docker compose up -d --wait db api web && docker compose --profile e2e run --rm e2e` |

---

## Execution Plan

Phases are ordered and run sequentially - each phase completes before the next begins, and tasks within a phase execute in order. Cada fase termina num pull request e numa parada para a revisão do usuário.

### Phase 1: Ambiente de desenvolvimento (pull request 1)

```
T2 -> T3 -> T4 -> T5
T4 -> T6
```

T1 não depende de nenhuma tarefa.

### Phase 2: Backend (pull request 2)

```
T7 -> T8 -> T9 -> T10 -> T11
T10 -> T12
```

### Phase 3: Frontend base e contrato (pull request 3)

```
T13 -> T14 -> T15 -> T16
T14 -> T17 -> T18
T17 -> T19
```

### Phase 4: Página, ponta a ponta e política de dependências (pull request 4)

```
T20 -> T21 -> T22 -> T24 -> T25
```

T23 não depende de nenhuma tarefa desta fase.

### Phase 5: CI e repositório (pull request 5)

```
T26 -> T27
T26 -> T28
```

T29, T30 e T31 não dependem de nenhuma tarefa desta fase.

---

## Task Breakdown

### Phase 1 tasks

### T1: Fins de linha LF no repositório

**What**: `.gitattributes` com `* text=auto eol=lf` e os tipos binários marcados, para que scripts e arquivos montados no contêiner tenham LF mesmo com `core.autocrlf=true` no Windows.
**Where**: `.gitattributes`
**Depends on**: None
**Reuses**: nada
**Requirement**: FUND-01

**Done when**:

- [x] `git ls-files --eol` mostra `w/lf` nos arquivos de texto depois de um novo checkout (conferido num clone novo, com `core.autocrlf=true`: 29 de 29 com LF; na cópia de trabalho do usuário, os 17 arquivos antigos, o README e os documentos, ficam com CRLF até serem tocados, sem efeito, porque nenhum roda no contêiner)
- [x] Nenhum documento existente muda de conteúdo no diff

**Tests**: none - configuração, sem camada de teste na matriz
**Gate**: ambiente
**Commit**: `build(repo): fixa fins de linha LF`

---

### T2: Contexto de build enxuto

**What**: `.dockerignore` que deixa fora do build `.git`, `node_modules`, `.venv`, caches e documentação.
**Where**: `.dockerignore`
**Depends on**: None
**Reuses**: nada
**Requirement**: FUND-03

**Done when**:

- [x] `docker compose build dev` não envia `.git` no contexto (provado por um build descartável que copia o contexto inteiro: `.git`, `.claude`, `docs` e `.specs` ficam de fora; os 345 bytes do build da imagem não provavam nada, porque o BuildKit só envia o que o Dockerfile copia)

**Tests**: none - configuração
**Gate**: ambiente
**Commit**: `build(docker): ignora arquivos fora do build`

---

### T3: Imagem de desenvolvimento

**What**: Imagem com Python, uv, Node e pnpm nas versões fixadas, a partir das imagens oficiais fixadas por digest, rodando como usuário `dev` (UID 1000), com as pastas de `.venv`, `node_modules` e caches criadas com esse dono.
**Where**: `docker/dev.Dockerfile`
**Depends on**: T2
**Reuses**: nada
**Requirement**: FUND-01, FUND-03, FUND-04

**Done when**:

- [x] `docker compose build dev` passa (conferido com `docker build`; o Compose chega no T4)
- [x] `python --version`, `uv --version`, `node --version` e `pnpm --version` dentro da imagem mostram as versões fixadas
- [x] Cada `FROM` traz o digest e a versão num comentário

**Tests**: none - imagem, provada pelo portão e pelo T5
**Gate**: ambiente
**Commit**: `build(docker): cria a imagem de desenvolvimento`

---

### T4: Compose com banco e contêiner do editor

**What**: `compose.yaml` com `db` (PostgreSQL 18 por digest, sem porta publicada, checagem por `pg_isready`, senha fictícia) e `dev` (`sleep infinity`, repositório em `/workspace`, volumes nomeados para `.venv`, `node_modules` e caches, nenhuma pasta do usuário).
**Where**: `compose.yaml`
**Depends on**: T3
**Reuses**: nada
**Requirement**: FUND-01, FUND-02, FUND-03, FUND-35

**Done when**:

- [x] `docker compose up -d --wait db dev` sobe os dois serviços
- [x] O `db` fica `healthy` pela checagem com `pg_isready` dentro do próprio contêiner do banco
- [x] Nenhum serviço publica porta

**Tests**: none - configuração; a porta é provada no T22 (FUND-02)
**Gate**: ambiente
**Commit**: `build(compose): sobe banco e contêiner de desenvolvimento`

---

### T5: Script de isolamento do contêiner

**What**: Script que, dentro do contêiner, confere a ausência de `~/.ssh`, `~/.aws`, `~/.config/gh`, `~/.gitconfig`, `SSH_AUTH_SOCK`, variáveis `GH_*`, `GITHUB_*` e `AWS_*` e de auxiliar de credenciais do Git; imprime `ok - FUND-03: ...` e sai com 0, ou lista o que achou e sai com 1.
**Where**: `scripts/conferir-isolamento.sh`
**Depends on**: T4
**Reuses**: nada
**Requirement**: FUND-03, FUND-35

**Done when**:

- [x] Run isolamento imprime `ok - FUND-03`
- [x] Com `-e GH_TOKEN=ficticio` no `docker compose run`, o script sai com 1 e cita a variável
- [x] A V43 começa a ser medida: tempo do `docker compose build dev` e do `docker compose up -d --wait db dev`, anotados no pull request. Medido em 2026-11-26, com a pasta em `C:\MedTeca`: build do zero 55 s, com cache 5 s; primeira subida (baixar o PostgreSQL e criar o banco) 50 s, depois 6,4 s; `docker compose run --rm dev true` 2,5 s

**Tests**: integration (o próprio script, nos dois casos acima)
**Gate**: isolamento
**Commit**: `test(ambiente): confere o isolamento do contêiner`

---

### T6: Configuração do VS Code no contêiner

**What**: `devcontainer.json` que liga o VS Code ao serviço `dev` do `compose.yaml`, com as extensões de Python, Ruff, ESLint, Prettier e Vitest, o Python do `.venv` e a pasta `/workspace`.
**Where**: `.devcontainer/devcontainer.json`
**Depends on**: T4
**Reuses**: `compose.yaml`
**Requirement**: FUND-32, FUND-33, FUND-34

**Done when**:

- [ ] O pull request traz o passo a passo das configurações do VS Code do usuário que impedem copiar o `.gitconfig` e repassar credenciais (`dev.containers.copyGitConfig` e `dev.containers.gitCredentialHelperConfigLocation`, conferidas na documentação na hora). Pendente: a documentação oficial não traz essas opções, e a extensão Dev Containers ainda não está instalada no computador do usuário para conferir o manifesto dela. Até lá, o pull request da fase 1 diz para não usar "Reopen in Container". `git.terminalAuthentication` e `git.useIntegratedAskPass` foram conferidas no manifesto do VS Code do usuário e desligadas no `devcontainer.json`; o `postAttachCommand` roda o script de isolamento a cada conexão
- [x] O walk completo fica para o fim da fase 4, quando houver dependências e testes

**Tests**: none - configuração do editor; prova por walk (FUND-32 a FUND-34)
**Gate**: ambiente
**Commit**: `build(editor): configura o VS Code no contêiner`

---

### Phase 2 tasks

### T7: Projeto Python

**What**: `pyproject.toml` com Django 6.1, Django Ninja e psycopg 3; grupo de desenvolvimento com pytest, pytest-django, Ruff, mypy, django-stubs, PyYAML e zizmor; `[tool.uv] exclude-newer = "7 days"`; Ruff com as regras do Bandit (`S`); mypy estrito com o plugin do django-stubs; pytest com `DJANGO_SETTINGS_MODULE = medteca.settings.test`.
**Where**: `backend/pyproject.toml`
**Depends on**: T4
**Reuses**: nada
**Requirement**: FUND-04, FUND-05, FUND-22

**Done when**:

- [x] Licenças de cada dependência direta conferidas contra a lista da seção 6.E.7 e citadas no pull request (todas as 29 do lock conferidas; psycopg e psycopg-binary, LGPL-3.0, e pathspec, MPL-2.0, aceitas com o motivo escrito no `pyproject.toml`). Desvio: o PyYAML fica para o T22, que é quem o usa; a versão de 7 dias atrás é de 2025 e provavelmente não tem pacote pronto para o Python 3.15. Entram `no-build = true` (nada compilado do código-fonte, para nenhum script de instalação rodar) e um `.gitignore` na raiz, para os caches das ferramentas

**Tests**: none - configuração; a política é provada no T23
**Gate**: ambiente
**Commit**: `build(backend): declara o projeto Python`

---

### T8: Lockfile do Python

**What**: `uv.lock` gerado dentro do contêiner, respeitando a espera de 7 dias.
**Where**: `backend/uv.lock`
**Depends on**: T7
**Reuses**: `backend/pyproject.toml`
**Requirement**: FUND-04, FUND-05

**Done when**:

- [x] `uv sync --locked` passa num volume vazio (29 pacotes instalados)
- [x] Se o `exclude-newer` relativo falhar com `--locked` (V37), parar e levar ao usuário a alternativa de data fixa. Não falhou: o uv 0.13.9 grava a espera no lock como período (`exclude-newer-span = "P7D"`), não como data, então o lock não envelhece de um dia para o outro

**Tests**: none - arquivo gerado
**Gate**: instalar
**Commit**: `chore(deps): gera o uv.lock`

---

### T9: Projeto Django

**What**: `manage.py`, `medteca/settings/base.py`, `dev.py` e `test.py`, `urls.py` (só `/api/`), `wsgi.py` e `asgi.py`, com pt-BR, `America/Sao_Paulo`, `USE_TZ`, middlewares de segurança e banco pelas variáveis `PG*` com tempo de conexão de 2 s.
**Where**: `backend/medteca/`
**Depends on**: T8
**Reuses**: nada
**Requirement**: FUND-07, FUND-14

**Done when**:

- [x] `manage.py check` passa
- [x] `makemigrations --check --dry-run` não acusa nada (Ruff e mypy estrito também passam)

**Tests**: none - configuração do projeto; a primeira rota e os testes vêm no T10
**Gate**: django
**Commit**: `feat(backend): cria o projeto Django`

---

### T10: Rota de saúde e portões do backend

**What**: `medteca/api.py` com a `NinjaAPI` e `GET /api/saude`, mais os testes de FUND-07 a FUND-09 e o script `scripts/portoes-backend.sh` (Ruff, formatação, mypy, pytest, `makemigrations --check` e `check --deploy` com as configurações de produção a partir do T11).
**Where**: `backend/medteca/api.py`, `backend/tests/test_saude.py`, `scripts/portoes-backend.sh`
**Depends on**: T9
**Reuses**: `backend/medteca/settings/`
**Requirement**: FUND-07, FUND-08, FUND-09

**Done when**:

- [x] `test_fund_07_saude_responde_ok`, `test_fund_08_banco_fora_responde_503` (falha simulada do cursor, corpo exato e sem detalhe) e `test_fund_09_saude_sem_cache` passam
- [x] Gate check passes: `docker compose run --rm dev scripts/portoes-backend.sh`
- [x] Test count: 3 tests pass (no silent deletions). São 4 execuções: o FUND-09 roda com o banco no ar e fora, porque o cabeçalho vale para as duas respostas

**Tests**: integration
**Gate**: backend
**Commit**: `feat(api): cria a rota de saúde`

---

### T11: Configurações de produção

**What**: `settings/prod.py` sem depuração, com `DJANGO_SECRET_KEY` obrigatória, hosts por `DJANGO_ALLOWED_HOSTS`, cookies seguros, documentação da API desligada e os avisos de HSTS e redirecionamento silenciados com o motivo (seção 5.H); testes por subprocesso; o `check --deploy` entra no `portoes-backend.sh`.
**Where**: `backend/medteca/settings/prod.py`, `backend/tests/test_producao.py`
**Depends on**: T10
**Reuses**: `backend/medteca/settings/base.py`
**Requirement**: FUND-19, FUND-20, FUND-21

**Done when**:

- [x] `test_fund_19_docs_fora_em_producao`, `test_fund_20_check_deploy_sem_avisos` e `test_fund_21_producao_exige_segredo` passam
- [x] Gate check passes: `docker compose run --rm dev scripts/portoes-backend.sh`
- [x] Test count: 6 tests pass (no silent deletions). São 8 execuções: o FUND-21 roda com o segredo ausente e vazio

**Tests**: integration
**Gate**: backend
**Commit**: `feat(backend): define as configurações de produção`

---

### T12: Serviço da API no Compose

**What**: Serviço `api` no `compose.yaml`, com a imagem de desenvolvimento, `runserver 0.0.0.0:8000`, dependência do `db` saudável e nenhuma porta publicada.
**Where**: `compose.yaml` (modify)
**Depends on**: T10
**Reuses**: serviço `dev`
**Requirement**: FUND-01

**Done when**:

- [x] Com `docker compose up -d --wait db api`, uma requisição a `http://api:8000/api/saude` feita de dentro do `dev`, com o `urllib` do Python, responde 200; o resultado vai no pull request (200, `no-store`, `{"situacao": "ok"}`; a API fica saudável em 14 s; com o banco parado, 503 e `{"situacao": "indisponivel"}` em 4 s)
- [x] A V43 continua: tempo do `portoes-backend.sh`, anotado no pull request (32 s, com a pasta no Windows)

**Tests**: none - configuração; a rota é provada no T10 e o caminho completo no T25
**Gate**: backend
**Commit**: `build(compose): sobe a API`

---

### Phase 3 tasks

### T13: Projeto do frontend

**What**: `package.json` com React, React DOM e `openapi-fetch`, e no desenvolvimento Vite, TypeScript, ESLint (typescript-eslint, react-hooks e jsx-a11y), Prettier, Vitest, Testing Library, jsdom, `openapi-typescript`, Playwright e `@axe-core/playwright`; `pnpm-workspace.yaml` com `minimumReleaseAge: 10080`, `strictDepBuilds: true`, `allowBuilds` vazio e `trustPolicy: no-downgrade`.
**Where**: `frontend/package.json`, `frontend/pnpm-workspace.yaml`
**Depends on**: T4
**Reuses**: nada
**Requirement**: FUND-04, FUND-05, FUND-06

**Done when**:

- [x] Licenças de cada dependência direta conferidas contra a seção 6.E.7 e citadas no pull request (todas MIT ou Apache-2.0, menos `@axe-core/playwright`, MPL-2.0, aceita com o motivo escrito no `pnpm-workspace.yaml`). Desvios de versão, por compatibilidade: TypeScript 5.9 (o typescript-eslint aceita até a 6.0 e o openapi-typescript só a 5.x). ESLint 10, embora o eslint-plugin-jsx-a11y declare suporte só até o 9: o 9 está sem suporte ("This version is no longer supported"), e um teste com uma imagem sem `alt` e um hook dentro de `if` mostrou as duas regras funcionando no 10; a liberação desse par fica no `pnpm-workspace.yaml`. `@testing-library/jest-dom` e `user-event` ficam de fora até algum teste precisar
- [ ] A versão do `@playwright/test` é a mesma da imagem do Playwright usada no T24. Pendente até o T24: o pacote está fixado em 1.65.1 exato, e a tag `mcr.microsoft.com/playwright:v1.65.1` existe (conferida pela revisão independente da fase 3); o T24 fixa o digest e confere `playwright --version`

**Tests**: none - configuração; a política é provada no T23
**Gate**: ambiente
**Commit**: `build(frontend): declara o projeto do frontend`

---

### T14: Lockfile do frontend

**What**: `pnpm-lock.yaml` gerado dentro do contêiner, respeitando a espera de 7 dias e sem rodar scripts de instalação.
**Where**: `frontend/pnpm-lock.yaml`
**Depends on**: T13
**Reuses**: `frontend/package.json`
**Requirement**: FUND-04, FUND-05, FUND-06

**Done when**:

- [x] `pnpm install --frozen-lockfile` passa num volume vazio (numa pasta vazia em `/tmp`, com os três arquivos do pnpm; `pnpm peers check` sem nenhum problema)
- [x] Se alguma dependência pedir script de instalação, parar e perguntar ao usuário (6.E.3). Nenhuma pediu: a instalação passou com `strictDepBuilds` ligado e `allowBuilds` vazio

**Tests**: none - arquivo gerado
**Gate**: instalar
**Commit**: `chore(deps): gera o pnpm-lock.yaml`

---

### T15: Lint, formatação e tipos do TypeScript

**What**: `tsconfig.json` estrito, `eslint.config.js` (typescript-eslint, react-hooks, jsx-a11y, `no-eval`, `no-implied-eval` e `dangerouslySetInnerHTML` barrado), `.prettierrc.json` e `scripts/portoes-frontend.sh` (ESLint, Prettier, `tsc --noEmit` e build do Vite).
**Where**: `frontend/tsconfig.json`, `frontend/eslint.config.js`, `frontend/.prettierrc.json`, `scripts/portoes-frontend.sh`
**Depends on**: T14
**Reuses**: nada
**Requirement**: FUND-22

**Done when**:

- [x] Gate check passes: `docker compose run --rm dev scripts/portoes-frontend.sh` (ESLint, Prettier e `tsc`; o build do Vite entra no T21, quando houver o `main.tsx` que o `index.html` carrega, e o Vitest no T20, com o primeiro teste)
- [x] Um `eval("1")` de teste, apagado em seguida, faz o ESLint falhar (`no-eval`, saída 1)

**Tests**: none - configuração de ferramentas
**Gate**: frontend
**Commit**: `build(frontend): configura lint, formatação e tipos`

---

### T16: Vite e página HTML

**What**: `vite.config.ts` com o repasse de `/api` para `http://api:8000`, `allowedHosts` com `web` e `usePolling`; `index.html` com `lang="pt-BR"`.
**Where**: `frontend/vite.config.ts`, `frontend/index.html`
**Depends on**: T15
**Reuses**: nada
**Requirement**: FUND-14, FUND-15

**Done when**:

- [x] Gate check passes: `docker compose run --rm dev scripts/portoes-frontend.sh`

**Tests**: none - configuração; FUND-14 e FUND-15 são provados no T25
**Gate**: frontend
**Commit**: `build(frontend): configura o Vite`

---

### T17: Contrato gerado

**What**: `openapi.json` exportado pelo `manage.py export_openapi_schema` e `esquema.d.ts` gerado pelo `openapi-typescript`, fora do ESLint e do Prettier.
**Where**: `frontend/src/api/openapi.json`, `frontend/src/api/esquema.d.ts`
**Depends on**: T14
**Reuses**: `backend/medteca/api.py`
**Requirement**: FUND-17

**Done when**:

- [x] `esquema.d.ts` tem o caminho `/api/saude` com as respostas 200 e 503 (gerado por `scripts/conferir_contrato.py --gerar`, com o OpenAPI exportado com as chaves ordenadas, para a saída ser estável)

**Tests**: none - arquivos gerados; provados no T18
**Gate**: frontend
**Commit**: `chore(api): gera o contrato da API`

---

### T18: Checagem de contrato

**What**: `scripts/conferir_contrato.py` (gera numa pasta temporária, compara e sai com 1 mostrando a diferença) e os testes de FUND-17 e FUND-18; o script entra no `portoes-frontend.sh`.
**Where**: `scripts/conferir_contrato.py`, `backend/tests/repositorio/test_contrato.py`
**Depends on**: T17
**Reuses**: `frontend/src/api/`
**Requirement**: FUND-17, FUND-18

**Done when**:

- [x] `test_fund_17_tipos_gerados_do_openapi` e `test_fund_18_contrato_divergente_falha` passam (o FUND-18 com o OpenAPI e com os tipos alterados, uma prova por variante). Prova manual: um valor novo em `situacao` na API, sem regenerar, fez a checagem sair com 1 e mostrar a diferença nos dois arquivos
- [x] Gate check passes: `docker compose run --rm dev scripts/portoes-backend.sh` (o Ruff e o mypy passam a olhar também `scripts/`, e as dependências do frontend são instaladas antes do pytest, porque o teste do contrato gera os tipos com o pnpm); `scripts/portoes-frontend.sh` termina na checagem de contrato
- [x] Test count: 8 tests pass (no silent deletions). Na prática, 9 funções de teste e 14 execuções no backend: o FUND-21 ganhou um teste na revisão da fase 2 e as variantes contam à parte; nenhum teste foi apagado

**Tests**: unit
**Gate**: backend
**Commit**: `test(contrato): compara a API com o cliente`

---

### T19: Cliente da API

**What**: `cliente.ts` com `createClient<paths>({ baseUrl: "" })` do `openapi-fetch`.
**Where**: `frontend/src/api/cliente.ts`
**Depends on**: T17
**Reuses**: `frontend/src/api/esquema.d.ts`
**Requirement**: FUND-15, FUND-17

**Done when**:

- [x] Gate check passes: `docker compose run --rm dev scripts/portoes-frontend.sh`

**Tests**: none - uma linha de configuração; usado e provado pelos testes do T20
**Gate**: frontend
**Commit**: `feat(frontend): cria o cliente da API`

---

### Phase 4 tasks

### T20: Situação do servidor

**What**: Componente `SituacaoDoServidor` com os estados `verificando`, `no-ar` e `fora-do-ar`, limite de 5 s e mensagem em `role="status"`; testes de FUND-10 a FUND-13 com o `fetch` simulado; o Vitest entra no `portoes-frontend.sh`.
**Where**: `frontend/src/SituacaoDoServidor.tsx`, `frontend/src/SituacaoDoServidor.test.tsx`
**Depends on**: T19
**Reuses**: `frontend/src/api/cliente.ts`
**Requirement**: FUND-10, FUND-11, FUND-12, FUND-13

**Done when**:

- [ ] Testes `FUND-10`, `FUND-11`, `FUND-12` (status 503, corpo inesperado e 5 s sem resposta) e `FUND-13` passam
- [ ] Gate check passes: `docker compose run --rm dev scripts/portoes-frontend.sh`
- [ ] Test count: 6 tests pass (no silent deletions)

**Tests**: unit
**Gate**: frontend
**Commit**: `feat(frontend): mostra a situação do servidor`

---

### T21: Página inicial

**What**: `PaginaInicial` (título "MedTeca" e a situação do servidor) e `main.tsx`, com teste do título.
**Where**: `frontend/src/PaginaInicial.tsx`, `frontend/src/main.tsx`
**Depends on**: T20
**Reuses**: `frontend/src/SituacaoDoServidor.tsx`
**Requirement**: FUND-01

**Done when**:

- [ ] Teste `FUND-01: a página mostra o título MedTeca` passa
- [ ] Gate check passes: `docker compose run --rm dev scripts/portoes-frontend.sh`
- [ ] Test count: 7 tests pass (no silent deletions)

**Tests**: unit
**Gate**: frontend
**Commit**: `feat(frontend): monta a página inicial`

---

### T22: Serviço do frontend no Compose

**What**: Serviço `web` no `compose.yaml` (`vite --host 0.0.0.0`, porta `127.0.0.1:5173:5173`, depende da `api`) e o teste de FUND-02 lendo o `compose.yaml`.
**Where**: `compose.yaml` (modify), `backend/tests/repositorio/test_compose.py`
**Depends on**: T21
**Reuses**: serviço `dev`
**Requirement**: FUND-01, FUND-02

**Done when**:

- [ ] `test_fund_02_so_porta_5173_em_localhost` passa
- [ ] `docker compose up` e "Servidor no ar" em `http://localhost:5173`, aberto no navegador do app
- [ ] Gate check passes: `docker compose run --rm dev scripts/portoes-backend.sh`
- [ ] Test count: 9 tests pass (no silent deletions)

**Tests**: unit
**Gate**: backend
**Commit**: `build(compose): sobe o frontend`

---

### T23: Testes da política de dependências

**What**: Testes de FUND-04 (lockfile divergente faz `uv sync --locked` e `pnpm install --frozen-lockfile` falharem sem alterar o lockfile, numa cópia temporária; os comandos de instalação e o `uv run` do repositório usam essas opções; e toda dependência direta do `package.json` é uma faixa de versão do registro, sem `git:`, `file:`, `link:` ou endereço, porque o `blockExoticSubdeps` só cobre as indiretas; acrescentado pela revisão independente da fase 3), FUND-05 (`exclude-newer` e `minimumReleaseAge`) e FUND-06 (`strictDepBuilds` e `allowBuilds`).
**Where**: `backend/tests/repositorio/test_dependencias.py`
**Depends on**: None
**Reuses**: `backend/pyproject.toml`, `frontend/pnpm-workspace.yaml`
**Requirement**: FUND-04, FUND-05, FUND-06

**Done when**:

- [ ] `test_fund_04_uv_lockfile_divergente_falha`, `test_fund_04_pnpm_lockfile_divergente_falha`, `test_fund_05_uv_espera_7_dias`, `test_fund_05_pnpm_espera_7_dias` e `test_fund_06_pnpm_bloqueia_scripts` passam
- [ ] Gate check passes: `docker compose run --rm dev scripts/portoes-backend.sh`
- [ ] Test count: 14 tests pass (no silent deletions)

**Tests**: unit
**Gate**: backend
**Commit**: `test(deps): prova a política de dependências`

---

### T24: Playwright no Compose

**What**: `playwright.config.ts` com os projetos `chromium`, `webkit-iphone` e `webkit-ipad`, `baseURL` `http://web:5173`, relatório em lista; serviço `e2e` no `compose.yaml` com a imagem oficial do Playwright por digest, no perfil `e2e`.
**Where**: `frontend/playwright.config.ts`, `compose.yaml` (modify)
**Depends on**: T22
**Reuses**: `node_modules` do volume
**Requirement**: FUND-16

**Done when**:

- [ ] `docker compose --profile e2e run --rm e2e npx --no-install playwright --version` mostra a mesma versão do `@playwright/test`

**Tests**: none - configuração; provada no T25
**Gate**: ambiente
**Commit**: `build(e2e): configura o Playwright`

---

### T25: Testes de ponta a ponta

**What**: `pagina-inicial.spec.ts` com FUND-01 ("Servidor no ar" vindo da API real), FUND-14 (`html[lang="pt-BR"]`), FUND-15 (todas as requisições na mesma origem da página) e FUND-16 (axe-core sem violação séria ou crítica), nos três projetos.
**Where**: `frontend/e2e/pagina-inicial.spec.ts`
**Depends on**: T24
**Reuses**: `frontend/playwright.config.ts`
**Requirement**: FUND-01, FUND-14, FUND-15, FUND-16

**Done when**:

- [ ] Run e2e passa nos três projetos (12 testes)
- [ ] Walk do usuário no VS Code (FUND-32 a FUND-34), anotado no Handoff
- [ ] A V43 fecha: os tempos medidos nas fases 1 a 4, levados ao usuário no pull request

**Tests**: e2e
**Gate**: e2e
**Commit**: `test(e2e): prova a página de ponta a ponta`

---

### Phase 5 tasks

### T26: Workflow de CI

**What**: `ci.yml` (pull request e push na `main`) com os jobs `backend`, `frontend`, `e2e`, `workflows` (zizmor) e `segredos` (gitleaks pela imagem do projeto, histórico completo), ações fixadas por SHA, `permissions: {}` no topo, `contents: read` nos jobs, checkout com `persist-credentials: false` e relatório do Playwright só na falha, por 14 dias; `zizmor.yml` exigindo SHA em toda ação; testes que leem todos os workflows.
**Where**: `.github/workflows/ci.yml`, `.github/zizmor.yml`, `backend/tests/repositorio/test_workflows.py`
**Depends on**: T25
**Reuses**: `scripts/portoes-backend.sh`, `scripts/portoes-frontend.sh`
**Requirement**: FUND-22, FUND-23, FUND-24, FUND-25, FUND-28

**Done when**:

- [ ] `test_fund_23_acoes_fixadas_por_sha`, `test_fund_24_permissoes_minimas`, `test_fund_25_checkout_sem_credenciais`, `test_fund_25_sem_pull_request_target` e `test_fund_28_artefatos_ate_14_dias` passam
- [ ] O zizmor passa sem achados
- [ ] Gate check passes: `docker compose run --rm dev scripts/portoes-backend.sh`
- [ ] Test count: 19 tests pass (no silent deletions)

**Tests**: unit
**Gate**: backend
**Commit**: `ci: roda os portões em todo pull request`

---

### T27: Revisão de dependências

**What**: `dependencias.yml` (pull request) com a revisão de dependências do GitHub, `fail-on-severity: high` e a lista de licenças da seção 6.E.7; teste da configuração.
**Where**: `.github/workflows/dependencias.yml`
**Depends on**: T26
**Reuses**: `backend/tests/repositorio/test_workflows.py`
**Requirement**: FUND-26

**Done when**:

- [ ] `test_fund_26_revisao_de_dependencias_configurada` passa
- [ ] Gate check passes: `docker compose run --rm dev scripts/portoes-backend.sh`
- [ ] Test count: 20 tests pass (no silent deletions)

**Tests**: unit
**Gate**: backend
**Commit**: `ci: revisa dependências novas`

---

### T28: CodeQL

**What**: `codeql.yml` (pull request, push na `main` e semanal) para Python, JavaScript/TypeScript e Actions, sem compilação, com `security-events: write` só nesse job; teste da configuração.
**Where**: `.github/workflows/codeql.yml`
**Depends on**: T26
**Reuses**: `backend/tests/repositorio/test_workflows.py`
**Requirement**: FUND-27

**Done when**:

- [ ] `test_fund_27_codeql_linguagens_e_agenda` passa
- [ ] Gate check passes: `docker compose run --rm dev scripts/portoes-backend.sh`
- [ ] Test count: 21 tests pass (no silent deletions)

**Tests**: unit
**Gate**: backend
**Commit**: `ci: analisa o código com o CodeQL`

---

### T29: Dependabot

**What**: `dependabot.yml` semanal para uv, pnpm (ecossistema npm), Docker, Docker Compose e ações, agrupado por ecossistema, com `cooldown` de 7 dias; teste da configuração.
**Where**: `.github/dependabot.yml`
**Depends on**: None
**Reuses**: `backend/tests/repositorio/`
**Requirement**: FUND-29

**Done when**:

- [ ] `test_fund_29_dependabot_semanal_agrupado` passa
- [ ] Os ecossistemas `uv` e `docker-compose` conferidos na documentação do Dependabot na hora
- [ ] Gate check passes: `docker compose run --rm dev scripts/portoes-backend.sh`
- [ ] Test count: 22 tests pass (no silent deletions)

**Tests**: unit
**Gate**: backend
**Commit**: `ci: configura o Dependabot`

---

### T30: Política de segurança

**What**: `SECURITY.md` em português: como relatar uma falha pelo relato privado do GitHub (link `security/advisories/new`), o que não fazer (abrir issue pública) e o encaminhamento de relato com dado pessoal ao fluxo de incidentes; teste do link.
**Where**: `SECURITY.md`
**Depends on**: None
**Reuses**: `backend/tests/repositorio/`
**Requirement**: FUND-30

**Done when**:

- [ ] `test_fund_30_security_md_aponta_relato_privado` passa
- [ ] Gate check passes: `docker compose run --rm dev scripts/portoes-backend.sh`
- [ ] Test count: 23 tests pass (no silent deletions)

**Tests**: unit
**Gate**: backend
**Commit**: `docs: explica como relatar falhas de segurança`

---

### T31: Modelo de pull request

**What**: `pull_request_template.md` com os 7 itens da explicação técnica (seção 6.C.6); teste que confere os 7 títulos.
**Where**: `.github/pull_request_template.md`
**Depends on**: None
**Reuses**: `backend/tests/repositorio/`
**Requirement**: FUND-31

**Done when**:

- [ ] `test_fund_31_modelo_com_7_itens` passa
- [ ] Gate check passes: `docker compose run --rm dev scripts/portoes-backend.sh`
- [ ] Test count: 24 tests pass (no silent deletions)

**Tests**: unit
**Gate**: backend
**Commit**: `docs: cria o modelo de pull request`

---

## Checks

**C1** - Com `docker compose up`, a página em `http://localhost:5173` mostra "Servidor no ar", vindo da API e do banco reais (FUND-01, P1 Ambiente AC 1)
Proof: run e2e | ✓ [chromium] FUND-01

**C2** - Só o serviço `web` publica porta, e só `127.0.0.1:5173` (FUND-02, P1 Ambiente AC 2)
Proof: run backend | test_fund_02_so_porta_5173_em_localhost PASSED

**C3** - Dentro do contêiner não há chaves SSH, credenciais do GitHub ou da AWS, configuração do Git nem auxiliar de credenciais (FUND-03, P1 Ambiente AC 3)
Proof: run isolamento | ok - FUND-03

**C35** - O repositório entra só para leitura, com escrita apenas em `backend/`, `frontend/` e `scripts/`, e nenhuma outra montagem (FUND-35, P1 Ambiente AC 7)
Proof: run isolamento | ok FUND-35

**C4** - Lockfile divergente faz a instalação falhar sem reescrever o lockfile, no uv e no pnpm (FUND-04, P1 Ambiente AC 4)
Proof: run backend | test_fund_04_uv_lockfile_divergente_falha PASSED
Proof: run backend | test_fund_04_pnpm_lockfile_divergente_falha PASSED

**C5** - uv com `exclude-newer = "7 days"` e pnpm com `minimumReleaseAge: 10080` (FUND-05, P1 Ambiente AC 5)
Proof: run backend | test_fund_05_uv_espera_7_dias PASSED
Proof: run backend | test_fund_05_pnpm_espera_7_dias PASSED

**C6** - pnpm com `strictDepBuilds: true` e só as liberações registradas em `allowBuilds` (FUND-06, P1 Ambiente AC 6)
Proof: run backend | test_fund_06_pnpm_bloqueia_scripts PASSED

**C7** - `GET /api/saude` com o banco de pé responde 200 e `{"situacao": "ok"}` (FUND-07, P1 API AC 1)
Proof: run backend | test_fund_07_saude_responde_ok PASSED

**C8** - Com falha no banco, `GET /api/saude` responde 503 e exatamente `{"situacao": "indisponivel"}` (FUND-08, P1 API AC 2)
Proof: run backend | test_fund_08_banco_fora_responde_503 PASSED

**C9** - `GET /api/saude` traz `Cache-Control: no-store` na resposta 200 e na 503 (FUND-09, P1 API AC 3)
Proof: run backend | test_fund_09_saude_sem_cache[banco-no-ar] PASSED
Proof: run backend | test_fund_09_saude_sem_cache[banco-fora] PASSED

**C10** - Antes da resposta, a página mostra "Verificando o servidor…" (FUND-10, P1 Página AC 1)
Proof: run frontend | ✓ FUND-10

**C11** - Com 200 e `situacao` igual a `ok`, a página mostra "Servidor no ar" (FUND-11, P1 Página AC 2)
Proof: run frontend | ✓ FUND-11

**C12** - Com status 503, com corpo inesperado ou sem resposta em 5 s, a página mostra "Servidor fora do ar" (FUND-12, P1 Página AC 3)
Proof: run frontend | ✓ FUND-12 status 503
Proof: run frontend | ✓ FUND-12 corpo inesperado
Proof: run frontend | ✓ FUND-12 sem resposta em 5 segundos

**C13** - A mensagem fica numa região `role="status"` (FUND-13, P1 Página AC 4)
Proof: run frontend | ✓ FUND-13

**C14** - O elemento `html` tem `lang="pt-BR"` (FUND-14, P1 Página AC 5)
Proof: run e2e | ✓ [chromium] FUND-14

**C15** - Toda requisição da página vai à origem da própria página, inclusive `/api/saude` (FUND-15, P1 Página AC 6)
Proof: run e2e | ✓ [chromium] FUND-15

**C16** - axe-core sem violação séria ou crítica no Chromium, no iPhone e no iPad (FUND-16, P1 Página AC 7)
Proof: run e2e | ✓ [chromium] FUND-16
Proof: run e2e | ✓ [webkit-iphone] FUND-16
Proof: run e2e | ✓ [webkit-ipad] FUND-16

**C17** - Os tipos versionados são os que o `openapi-typescript` gera do OpenAPI atual (FUND-17, P1 Contrato AC 1)
Proof: run backend | test_fund_17_tipos_gerados_do_openapi PASSED

**C18** - Um OpenAPI ou tipos divergentes fazem a checagem de contrato sair com 1 (FUND-18, P1 Contrato AC 2)
Proof: run backend | test_fund_18_contrato_divergente_falha[openapi-divergente] PASSED
Proof: run backend | test_fund_18_contrato_divergente_falha[tipos-divergentes] PASSED

**C19** - Com as configurações de produção, `/api/docs` e `/api/openapi.json` respondem 404 (FUND-19, P1 Produção AC 1)
Proof: run backend | test_fund_19_docs_fora_em_producao PASSED

**C20** - Com as configurações de produção, `check --deploy` sai com 0 e sem avisos além dos silenciados com motivo (FUND-20, P1 Produção AC 2)
Proof: run backend | test_fund_20_check_deploy_sem_avisos PASSED

**C21** - Sem `DJANGO_SECRET_KEY`, com ela vazia, só com espaços ou com menos de 50 caracteres, as configurações de produção não carregam; com 50, carregam (FUND-21, P1 Produção AC 3)
Proof: run backend | test_fund_21_producao_exige_segredo[ausente] PASSED
Proof: run backend | test_fund_21_producao_exige_segredo[vazio] PASSED
Proof: run backend | test_fund_21_producao_exige_segredo[so-espacos] PASSED
Proof: run backend | test_fund_21_producao_exige_segredo[curto] PASSED
Proof: run backend | test_fund_21_producao_aceita_segredo_de_50_caracteres PASSED

**C22** - O pull request da fase 5 roda e passa os portões da tabela (FUND-22, P1 CI AC 1)
Proof: walk - a página de checagens do pull request da fase 5 lista `backend`, `frontend`, `e2e`, `workflows`, `segredos`, `dependencias` e o CodeQL, todos verdes

**C23** - Toda ação dos workflows está fixada por SHA de 40 caracteres, com a versão em comentário (FUND-23, P1 CI AC 2)
Proof: run backend | test_fund_23_acoes_fixadas_por_sha PASSED

**C24** - Todo workflow tem `permissions: {}` no topo, e cada job só as permissões que usa (FUND-24, P1 CI AC 3)
Proof: run backend | test_fund_24_permissoes_minimas PASSED

**C25** - Todo checkout tem `persist-credentials: false`, e nenhum workflow usa `pull_request_target` (FUND-25, P1 CI AC 4)
Proof: run backend | test_fund_25_checkout_sem_credenciais PASSED
Proof: run backend | test_fund_25_sem_pull_request_target PASSED

**C26** - A revisão de dependências roda em pull request, com `fail-on-severity: high` e a lista de licenças da seção 6.E.7 (FUND-26, P1 CI AC 5)
Proof: run backend | test_fund_26_revisao_de_dependencias_configurada PASSED

**C27** - O CodeQL roda em pull request e toda semana, para Python, JavaScript/TypeScript e Actions (FUND-27, P1 CI AC 6)
Proof: run backend | test_fund_27_codeql_linguagens_e_agenda PASSED

**C28** - Todo envio de artefato guarda por no máximo 14 dias (FUND-28, P1 CI AC 7)
Proof: run backend | test_fund_28_artefatos_ate_14_dias PASSED

**C29** - Dependabot semanal para uv, pnpm, Docker, Docker Compose e ações, agrupado e com espera de 7 dias (FUND-29, P1 Manutenção AC 1)
Proof: run backend | test_fund_29_dependabot_semanal_agrupado PASSED

**C30** - O `SECURITY.md` aponta o relato privado de vulnerabilidades do GitHub (FUND-30, P1 Manutenção AC 2)
Proof: run backend | test_fund_30_security_md_aponta_relato_privado PASSED

**C31** - O modelo de pull request traz os 7 itens da explicação técnica (FUND-31, P1 Manutenção AC 3)
Proof: run backend | test_fund_31_modelo_com_7_itens PASSED

**C32** - "Reopen in Container" abre o VS Code no contêiner, com autocompletar de Python e TypeScript (FUND-32, P1 Editor AC 1)
Proof: walk - o usuário abre o projeto no VS Code com "Reopen in Container", e o autocompletar sugere `django.db.connection` num arquivo Python e `useState` num arquivo TypeScript

**C33** - O usuário roda e depura um teste do backend e um do frontend pelo VS Code (FUND-33, P1 Editor AC 2)
Proof: walk - pelo painel de testes do VS Code, o usuário roda `test_fund_07_saude_responde_ok` e o teste `FUND-11`, e para num ponto de parada em cada um

**C34** - No terminal do VS Code dentro do contêiner, nenhuma credencial do usuário aparece (FUND-34, P1 Editor AC 3)
Proof: walk - no terminal do VS Code dentro do contêiner, `scripts/conferir-isolamento.sh` imprime `ok - FUND-03`

---

## Handoff

The feature's live state, written as it happens - a compaction gives no warning.

**Settled mid-build:** "Pode apagar" (2026-11-26): apagar os sockets velhos do Docker Desktop. Eles não se apagaram (erro 1920); as pastas `run` e `docker-secrets-engine` foram renomeadas, e o Docker passou a ser aberto só pelo usuário.
**Dispatched:** revisão independente da fase 1 (sessão sem o contexto do autor, com revisão de segurança), sobre `06b1347` - returned: 3 achados importantes e 7 menores; tratados de `8ebc56c` a este commit, e o das extensões do VS Code (fonte fora da seção 6.E.1) levado ao usuário. Revisão independente da fase 2, sobre `9258924` - returned: nada importante, 7 achados menores; 1, 2 e 5 corrigidos (`4f0650a`, `0135f03`, `79f89a0`), 3, 4, 6 e 7 registrados como cuidados para Contas e Publicação no `design.md`. Revisão independente da fase 3, sobre `0b635ec` - returned: 3 achados importantes e 5 menores; o 2 a 8 corrigidos de `f22f651` a `67dea2f` e nas caixas do T13 e do T18; o 1 (licenças BlueOak-1.0.0, CC-BY-4.0 e Python-2.0 em ferramentas de desenvolvimento) levado ao usuário, e o lightningcss (MPL-2.0) registrado com motivo; o CSRF_TRUSTED_ORIGINS do desenvolvimento entra nos cuidados para Contas.
**Walked:** none

---

## Phase Execution Map

```
Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5

Phase 1:  T2 → T3 → T4 → T5
          T4 → T6
          (T1 sozinha)
Phase 2:  T7 → T8 → T9 → T10 → T11
          T10 → T12
Phase 3:  T13 → T14 → T15 → T16
          T14 → T17 → T18
          T17 → T19
Phase 4:  T20 → T21 → T22 → T24 → T25
          (T23 sozinha)
Phase 5:  T26 → T27
          T26 → T28
          (T29, T30 e T31 sozinhas)
```

Execution is strictly sequential - there is no intra-phase parallelism. Cada fase termina num pull request e numa parada para a revisão do usuário; por isso, não há trabalhadores em lote entre fases.
