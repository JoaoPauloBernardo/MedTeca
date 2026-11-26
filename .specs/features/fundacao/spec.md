# Fundação do projeto Specification

**Approved**: 2026-11-26 - user: "Aprovo, pode seguir"

## Problem Statement

O MedTeca tem o planejamento aprovado (Etapas 1 a 6), mas ainda não tem nenhuma linha de código. Antes da primeira funcionalidade, o projeto precisa de um esqueleto que rode de ponta a ponta: página React, API Django Ninja e PostgreSQL 18, em contêineres no computador do usuário, com os portões de qualidade do CI rodando em todo pull request. Sem isso, cada funcionalidade teria de montar o ambiente, e os portões aprovados na D-034 não teriam onde rodar.

## Goals

- [ ] Com um comando (`docker compose up`), o usuário abre `http://localhost:5173` e vê "Servidor no ar", com a página consultando a API e a API consultando o banco.
- [ ] Todo pull request roda os portões do CI desta funcionalidade, em contêineres, e fica verde.
- [ ] O usuário abre o projeto no VS Code dentro do contêiner, com autocompletar, depuração e testes (V49).

## Out of Scope

| Item | Motivo |
| --- | --- |
| Imagem de produção, Caddy, inventário (Syft), varredura da imagem (Grype), OWASP ZAP, envio ao ECR por OIDC, registro de versão e atestado | Pertencem à funcionalidade "Publicação e infraestrutura", que depende da AWS e de autorização a cada operação (seção 5.4). O ZAP precisa do app montado como na produção. |
| Testes de mutação (mutmut e Stryker) | Rodam antes de cada versão, sobre as regras críticas (P6-21); ainda não existe nenhuma. |
| Squawk sobre o SQL das migrações | Ainda não há migração própria; entra com a primeira, em Contas. O `makemigrations --check` entra já. |
| Matriz do ASVS (P6-17) | Documento próprio, num pull request de documentação antes de Contas. |
| Sistema de design: tokens, fontes Literata e Figtree servidas pelo app (RNF-95), componentes e casca de navegação | Próxima funcionalidade. A página desta fundação usa os estilos padrão do navegador. |
| Contas, sessão, CSRF, Argon2id e permissões | Funcionalidade Contas (D-007, blocos 1 e 2). |
| Fila de tarefas do Django (D-024) e envio de e-mail | Entram com o primeiro uso, em Contas. |
| Registros e eventos da D-032 | Entram com Contas (eventos de acesso) e com a publicação (CloudWatch). |
| Configurações do repositório no GitHub: checagens obrigatórias na regra da `main` (RNF-71, V50), relato privado de vulnerabilidades, varredura de segredos e bloqueio no envio (V35), política de SHA obrigatório (V36), aprovação de workflows de fora (V46) | São atos do usuário nas configurações do GitHub. O Claude lista o passo a passo no pull request da fase 5. |
| Gitleaks antes de cada commit, no computador do usuário | Exige mudar a configuração do Git do usuário (hook); fica para quando ele autorizar. O gitleaks roda no CI desde já. |
| Mover a pasta do projeto para o WSL 2 | Decisão do usuário, se a medição da V43 pedir (seção 6.J.1). |

---

## Assumptions & Open Questions

| Assumption / decision | Chosen default | Rationale | Confirmed? |
| --- | --- | --- | --- |
| Editor do usuário | VS Code, com a extensão Dev Containers e um `devcontainer.json` no repositório | Resposta do usuário: "VS Code" (2026-11-26) | y |
| Idioma dos nomes no código | Nomes do domínio em português, sem acento, seguindo o catálogo e o modelo conceitual (`Questao`, `/api/questoes`, `/api/saude`); o que vem das bibliotecas e dos frameworks continua em inglês (`settings`, `urls`, `tests`). Registrado como D-035 | Resposta do usuário: "Domínio em português (Recomendado)" (2026-11-26) | y |
| Comentários, mensagens de commit e scripts próprios | Em português, como os documentos e os commits feitos até aqui; mensagens de commit no formato `tipo(escopo): descrição` | Mantém o idioma do projeto; o formato é o que a TLC confere a cada commit | n |
| Organização do repositório | Um repositório só, com `backend/` (Django) e `frontend/` (React) na raiz, `compose.yaml` na raiz e `.devcontainer/` para o VS Code | Um só pull request pode mudar a API e o cliente juntos, e a checagem de contrato compara os dois no mesmo commit | n |
| Contêiner de desenvolvimento | Uma imagem de desenvolvimento com Python e uv e com Node e pnpm, montada a partir das imagens oficiais. Ela serve ao VS Code, aos servidores da API e do frontend e aos comandos de teste. O Playwright roda na imagem oficial dele | Uma janela do VS Code só se liga a um contêiner; com as duas linguagens no mesmo, o autocompletar funciona para o backend e para o frontend sem trocar de janela | n |
| Cliente TypeScript da API | `openapi-typescript` gera os tipos a partir do OpenAPI, e `openapi-fetch` faz as chamadas com esses tipos (os dois com licença MIT, conferida na instalação) | Gera só tipos e um cliente pequeno, sem código de execução gerado. Alternativas: `orval` e `@hey-api/openapi-ts`, que geram mais código para revisar | n |
| Versões | Django 6.1.x; Python na versão mais nova que o Django 6.1 suporta; Node na versão LTS ativa; pnpm 11; PostgreSQL 18.x. Todas fixadas na implementação, respeitando a espera de 7 dias, e as imagens fixadas por digest | D-004 e D-005 deixam a versão exata para a implementação; P6-07 e P6-08 | n |
| Banco no desenvolvimento | PostgreSQL 18 só na rede interna do Compose, com senha fictícia, sem porta publicada. O socket local com autenticação peer (D-005, D-033) é da produção e entra com a publicação | Cada contêiner tem os próprios usuários, então a autenticação peer entre contêineres exigiria casar os IDs de usuário; isso não muda nada do que esta fundação prova | n |
| Pasta do projeto | Fica em `C:\MedTeca`. A fase 1 mede o tempo de subida e dos testes (V43) e leva o número ao usuário | Seção 6.J.1: mover para o WSL 2 é decisão do usuário, se a medição pedir | n |
| Nomes dos testes | O nome de cada teste cita o ID do critério (por exemplo, `test_fund_07_...`) | D-026 | n |
| "Imagens oficiais" da seção 6.E.1 | As Docker Official Images (`postgres`, `python`, `node`) e as imagens publicadas pelo próprio projeto da ferramenta (Playwright, pela Microsoft; gitleaks, pelo projeto gitleaks), todas fixadas por digest. O uv vem do PyPI e o pnpm, do registro do npm | Os navegadores do Playwright e o gitleaks não estão no PyPI nem no npm; a imagem do próprio projeto é a distribuição oficial deles | n |
| Caminho da rota de saúde | `/api/saude`, porque toda a API do Django Ninja fica sob `/api/`. A seção 5.I.2 cita `/saude` para a troca de versão no deploy; a publicação aponta o proxy para `/api/saude` | Um prefixo só para a API simplifica o repasse do Vite e, depois, o do Caddy | n |
| Cabeçalhos HSTS e redirecionamento para HTTPS | Ficam no Caddy (seção 5.H.3 e 5.H.4, V26). No `check --deploy`, os avisos do Django sobre isso são silenciados com esse motivo escrito nas configurações de produção | Dois lugares mandando HSTS geram cabeçalho duplicado; a seção 5.H já dá essa tarefa ao Caddy | n |

**Open questions:** none - all resolved or logged above.

### Implicit-requirement dimensions

| Dimension | Resolução |
| --- | --- |
| Input validation & bounds | N/A porque `GET /api/saude` não recebe parâmetro nem corpo. |
| Failure / partial-failure states | FUND-08 (banco fora), FUND-12 (API fora ou lenta), FUND-21 (segredo ausente na produção), FUND-04 (lockfile divergente). |
| Idempotency / retry / duplicate handling | N/A porque a única rota é uma leitura sem efeito colateral; a página não repete a consulta sozinha. |
| Auth boundaries & rate limits | N/A porque ainda não há contas. `/api/saude` é pública por desenho, para o monitor e a checagem depois do deploy (RNF-79). Limites de requisição entram com Contas e com o Caddy. |
| Concurrency / ordering | N/A porque não há escrita nem estado compartilhado. |
| Data lifecycle / expiry | FUND-28 (artefatos do CI por no máximo 14 dias). Nenhum dado é gravado no banco. |
| Observability | N/A nesta funcionalidade: os registros da D-032 entram com Contas e com a publicação. O Django escreve no console do contêiner. |
| External-dependency failure | FUND-08 e FUND-12. |
| State-transition integrity | FUND-10 a FUND-12: a página vai de "Verificando o servidor…" para "Servidor no ar" ou "Servidor fora do ar", e não volta sozinha. |

---

## User Stories

### P1: Ambiente de desenvolvimento em contêineres ⭐ MVP

**User Story**: Como responsável pelo projeto, quero subir o MedTeca inteiro com um comando, em contêineres, para rodar, testar e escrever código sem instalar dependências de terceiros no Windows (P6-04, P6-24).

**Why P1**: Todo o resto roda dentro deste ambiente.

**Acceptance Criteria**:

1. WHEN o usuário roda `docker compose up` na raiz do repositório THEN the system SHALL servir a página inicial em `http://localhost:5173`, com a API e o PostgreSQL 18 em contêineres. (FUND-01)
2. The system SHALL publicar no computador do usuário somente a porta 5173, ligada a `127.0.0.1`. (FUND-02)
3. The system SHALL rodar os contêineres de desenvolvimento sem as credenciais do GitHub e da AWS, sem as chaves SSH e sem a configuração do Git do usuário. (FUND-03; RNF-85)
4. IF o `uv.lock` ou o `pnpm-lock.yaml` não corresponde ao manifesto THEN the system SHALL falhar a instalação das dependências sem alterar o lockfile. (FUND-04; RNF-72)
5. The system SHALL recusar, no uv e no pnpm, versões de dependência publicadas há menos de 7 dias. (FUND-05; RNF-73)
6. The system SHALL bloquear os scripts de instalação das dependências do frontend, salvo os liberados pelo usuário e registrados. (FUND-06; P6-09)

**Independent Test**: Num clone limpo, `docker compose up` e abrir `http://localhost:5173`; dentro do contêiner, rodar o script de isolamento e ver que nenhuma credencial aparece.

---

### P1: API com rota de saúde ⭐ MVP

**User Story**: Como responsável pelo projeto, quero uma rota que diga se a API e o banco estão de pé, para provar o caminho até o banco e, mais tarde, servir ao monitor e à checagem depois do deploy (RNF-79).

**Why P1**: É a menor fatia que atravessa API e banco.

**Acceptance Criteria**:

1. WHEN alguém faz `GET /api/saude` e o banco responde THEN the system SHALL responder 200 com o corpo `{"situacao": "ok"}`. (FUND-07)
2. IF a consulta ao banco falha em `GET /api/saude` THEN the system SHALL responder 503 com o corpo `{"situacao": "indisponivel"}`, sem detalhes do erro. (FUND-08)
3. The system SHALL responder `GET /api/saude` com o cabeçalho `Cache-Control: no-store`. (FUND-09)

**Independent Test**: `curl -i http://localhost:5173/api/saude` com o banco de pé e com o banco parado.

---

### P1: Página inicial que consulta a API ⭐ MVP

**User Story**: Como responsável pelo projeto, quero uma página que mostre a situação do servidor, para provar o caminho do navegador até o banco, na mesma origem.

**Why P1**: É a fatia vertical completa; as telas de verdade chegam com o sistema de design.

**Acceptance Criteria**:

1. WHEN a página inicial abre THEN the system SHALL mostrar "Verificando o servidor…" até a resposta de `/api/saude`. (FUND-10)
2. WHEN `/api/saude` responde 200 com `situacao` igual a `ok` THEN the system SHALL mostrar "Servidor no ar". (FUND-11)
3. IF `/api/saude` responde com status diferente de 200 ou não responde em 5 segundos THEN the system SHALL mostrar "Servidor fora do ar". (FUND-12)
4. The system SHALL exibir a situação do servidor numa região `role="status"`, para que leitores de tela a anunciem. (FUND-13; RNF-01)
5. The system SHALL declarar o idioma da página como `pt-BR`. (FUND-14; RNF-02)
6. The system SHALL buscar `/api/saude` na mesma origem da página, sem carregar recurso de outra origem. (FUND-15; D-020, RNF-96)
7. WHEN a página inicial abre no Chromium e no WebKit, com os perfis de iPhone e iPad THEN the system SHALL passar no axe-core sem violação séria ou crítica. (FUND-16; D-026, RNF-01)

**Independent Test**: Abrir `http://localhost:5173` com o banco de pé ("Servidor no ar") e com a API parada ("Servidor fora do ar").

---

### P1: Contrato entre a API e o cliente ⭐ MVP

**User Story**: Como responsável pelo projeto, quero que o cliente TypeScript saia do OpenAPI do Django Ninja, para que uma mudança na API sem o cliente atualizado quebre o CI, e não a tela (D-004, D-026).

**Why P1**: É o portão de contrato da D-026, e toda funcionalidade com API depende dele.

**Acceptance Criteria**:

1. The system SHALL gerar os tipos do cliente TypeScript a partir do OpenAPI exportado pelo Django Ninja. (FUND-17)
2. IF o OpenAPI exportado difere do arquivo versionado, ou os tipos gerados diferem dos versionados THEN the system SHALL falhar a checagem de contrato. (FUND-18)

**Independent Test**: Mudar o corpo de `/api/saude` sem regenerar o cliente e ver a checagem de contrato falhar.

---

### P1: Configurações de produção seguras desde o início ⭐ MVP

**User Story**: Como responsável pelo projeto, quero que as configurações de produção passem pelas checagens do Django desde o primeiro commit, para que nenhuma funcionalidade nasça sobre uma configuração insegura (P6-06).

**Why P1**: É um portão de todo pull request (seção 6.D).

**Acceptance Criteria**:

1. WHILE as configurações de produção estão ativas the system SHALL responder 404 em `/api/docs` e em `/api/openapi.json`. (FUND-19; ASVS 13.4.5)
2. WHILE as configurações de produção estão ativas the system SHALL passar no `manage.py check --deploy` sem erros nem avisos, salvo os silenciados com o motivo escrito no arquivo de configurações. (FUND-20)
3. IF as configurações de produção são carregadas sem `DJANGO_SECRET_KEY` THEN the system SHALL recusar a inicialização com erro. (FUND-21)

**Independent Test**: Rodar `check --deploy` e os testes com as configurações de produção; tirar a variável do segredo e ver o Django recusar a subida.

---

### P1: Portões do CI ⭐ MVP

**User Story**: Como responsável pelo projeto, quero que cada pull request rode os portões aprovados, em contêineres, para revisar o código sabendo que lint, tipos, testes, contrato e segurança já passaram (P6-06, P6-10).

**Why P1**: Sem CI, os portões da D-034 não existem.

**Acceptance Criteria**:

1. WHEN um pull request é aberto ou atualizado THEN the system SHALL rodar em contêineres os portões da tabela "Portões desta funcionalidade". (FUND-22; P6-06)
2. The system SHALL fixar cada ação do GitHub pelo SHA completo do commit, com a versão num comentário. (FUND-23; RNF-74)
3. The system SHALL declarar `permissions: {}` no topo de cada workflow e, em cada job, só as permissões que ele usa. (FUND-24; P6-10)
4. The system SHALL fazer o checkout com `persist-credentials: false` e nunca usar o gatilho `pull_request_target`. (FUND-25; P6-10)
5. WHEN um pull request é aberto ou atualizado THEN the system SHALL rodar a revisão de dependências do GitHub, que falha com vulnerabilidade alta ou crítica ou com licença fora da lista da seção 6.E.7. (FUND-26; RNF-78)
6. WHEN um pull request é aberto ou atualizado, e uma vez por semana THEN the system SHALL rodar o CodeQL para Python, JavaScript/TypeScript e os workflows do Actions. (FUND-27; P6-15)
7. The system SHALL guardar os artefatos do CI por no máximo 14 dias. (FUND-28; RNF-84)

**Independent Test**: Abrir o pull request da fase 5 e ver cada portão listado e verde na página de checagens.

**Portões desta funcionalidade** (subconjunto da seção 6.D; os demais estão em Out of Scope):

| Portão | Ferramenta |
| --- | --- |
| Lint e regras de segurança do Python | Ruff, com as regras do Bandit |
| Formatação do Python | Ruff |
| Tipos do Python | mypy com django-stubs |
| Testes do backend | pytest e pytest-django em PostgreSQL 18 |
| Migrações pendentes | `makemigrations --check` |
| Configuração de produção | `check --deploy` e documentação da API fora do ar (FUND-19 a FUND-21) |
| Lint, formatação e tipos do TypeScript | ESLint (typescript-eslint, react-hooks e jsx-a11y, com `eval` e HTML injetado barrados), Prettier e `tsc` estrito |
| Componentes | Vitest e Testing Library |
| Contrato da API | FUND-18 |
| Ponta a ponta e acessibilidade | Playwright no Chromium e no WebKit (perfis de iPhone e iPad), com axe-core |
| Workflows | zizmor |
| Segredos | gitleaks |
| Dependências novas | Revisão de dependências do GitHub (FUND-26) |
| Código | CodeQL (FUND-27) |

---

### P1: Manutenção, relato de falhas e modelo de pull request ⭐ MVP

**User Story**: Como responsável pelo projeto, quero as atualizações semanais, o canal de relato de falhas e o modelo da explicação técnica no repositório, para que a manutenção e a revisão sigam o que foi aprovado desde o primeiro pull request (P6-11, P6-26, P6-27).

**Why P1**: São decisões aprovadas que só nascem na implementação (seções 6.C.6 e 6.J.3).

**Acceptance Criteria**:

1. The system SHALL configurar o Dependabot com atualizações semanais de uv, pnpm, imagens Docker e ações do GitHub, agrupadas por ecossistema e com espera de 7 dias. (FUND-29; P6-11)
2. The system SHALL publicar um `SECURITY.md` que aponta o relato privado de vulnerabilidades do GitHub como canal. (FUND-30; RNF-86)
3. WHEN um pull request é aberto THEN the system SHALL preencher a descrição com o modelo dos 7 itens da explicação técnica. (FUND-31; P6-27)

**Independent Test**: Abrir um pull request e ver o modelo na descrição; abrir a aba de segurança e ver o `SECURITY.md`.

---

### P1: Editor dentro do contêiner ⭐ MVP

**User Story**: Como responsável pelo projeto, quero ler, escrever, depurar e testar o código no VS Code dentro do contêiner, para aprender com o projeto sem rodar código de terceiros no Windows (V49, RNF-85).

**Why P1**: O usuário lê e revisa todo o código (D-034); sem autocompletar e depuração, isso fica muito mais difícil.

**Acceptance Criteria**:

1. WHEN o usuário abre o repositório no VS Code e escolhe "Reopen in Container" THEN the system SHALL abrir o editor dentro do contêiner de desenvolvimento, com autocompletar de Python e de TypeScript. (FUND-32; V49)
2. WHILE o editor está dentro do contêiner the system SHALL rodar e depurar os testes do backend e do frontend pelo VS Code. (FUND-33; V49)
3. WHILE o editor está dentro do contêiner the system SHALL manter fora dele as credenciais do Git, as chaves SSH e a configuração do Git do usuário. (FUND-34; RNF-85)

**Independent Test**: O usuário abre o projeto no VS Code, roda um teste do backend e um do frontend pelo painel de testes e, no terminal do contêiner, roda o script de isolamento.

---

## Edge Cases

- IF o banco está fora THEN `/api/saude` responde 503 (FUND-08) e a página mostra "Servidor fora do ar" (FUND-12).
- IF a API demora mais de 5 segundos THEN a página mostra "Servidor fora do ar" (FUND-12).
- IF a API responde 200 com um corpo diferente de `{"situacao": "ok"}` THEN a página mostra "Servidor fora do ar" (FUND-12: só `situacao` igual a `ok` conta como no ar).
- IF o segredo da produção falta THEN o Django não sobe (FUND-21).
- IF um lockfile está desatualizado THEN a instalação falha sem reescrevê-lo (FUND-04).

---

## Requirement Traceability

| Requirement ID | Story | Phase | Status |
| --- | --- | --- | --- |
| FUND-01 | P1: Ambiente de desenvolvimento | Tasks | Pending |
| FUND-02 | P1: Ambiente de desenvolvimento | Tasks | Pending |
| FUND-03 | P1: Ambiente de desenvolvimento | Tasks | Pending |
| FUND-04 | P1: Ambiente de desenvolvimento | Tasks | Pending |
| FUND-05 | P1: Ambiente de desenvolvimento | Tasks | Pending |
| FUND-06 | P1: Ambiente de desenvolvimento | Tasks | Pending |
| FUND-07 | P1: API com rota de saúde | Tasks | Pending |
| FUND-08 | P1: API com rota de saúde | Tasks | Pending |
| FUND-09 | P1: API com rota de saúde | Tasks | Pending |
| FUND-10 | P1: Página inicial | Tasks | Pending |
| FUND-11 | P1: Página inicial | Tasks | Pending |
| FUND-12 | P1: Página inicial | Tasks | Pending |
| FUND-13 | P1: Página inicial | Tasks | Pending |
| FUND-14 | P1: Página inicial | Tasks | Pending |
| FUND-15 | P1: Página inicial | Tasks | Pending |
| FUND-16 | P1: Página inicial | Tasks | Pending |
| FUND-17 | P1: Contrato da API | Tasks | Pending |
| FUND-18 | P1: Contrato da API | Tasks | Pending |
| FUND-19 | P1: Configurações de produção | Tasks | Pending |
| FUND-20 | P1: Configurações de produção | Tasks | Pending |
| FUND-21 | P1: Configurações de produção | Tasks | Pending |
| FUND-22 | P1: Portões do CI | Tasks | Pending |
| FUND-23 | P1: Portões do CI | Tasks | Pending |
| FUND-24 | P1: Portões do CI | Tasks | Pending |
| FUND-25 | P1: Portões do CI | Tasks | Pending |
| FUND-26 | P1: Portões do CI | Tasks | Pending |
| FUND-27 | P1: Portões do CI | Tasks | Pending |
| FUND-28 | P1: Portões do CI | Tasks | Pending |
| FUND-29 | P1: Manutenção e relato | Tasks | Pending |
| FUND-30 | P1: Manutenção e relato | Tasks | Pending |
| FUND-31 | P1: Manutenção e relato | Tasks | Pending |
| FUND-32 | P1: Editor dentro do contêiner | Tasks | Pending |
| FUND-33 | P1: Editor dentro do contêiner | Tasks | Pending |
| FUND-34 | P1: Editor dentro do contêiner | Tasks | Pending |

**Coverage:** 34 total, 34 mapped to tasks, 0 unmapped.

---

## Sources

- `docs/decisions.md`: D-004 (Django e Django Ninja), D-005 (PostgreSQL 18), D-006 (React, TypeScript, Vite e React Aria), D-017 (specs da TLC e escopo da autorização), D-020 (app e API na mesma origem), D-026 (camadas de teste e nome do teste com o ID), D-027 (GitHub Actions), D-034 (portões, dependências e revisão).
- `docs/seguranca-e-privacidade.md`, seção 6: portões do CI (6.D), dependências (6.E), código e segredos (6.G), desenvolvimento em contêineres (6.J.1), repositório público (6.J.2), relato de falhas (6.J.3), explicação técnica (6.C.6), tamanho dos pull requests (6.C.7) e verificações V37, V38, V43 e V49.
- `docs/requisitos-mvp.md`: RNF-01, RNF-02, RNF-72 a RNF-74, RNF-78, RNF-84 a RNF-86 e RNF-96.
- Respostas do usuário em 2026-11-26: "VS Code" e "Domínio em português (Recomendado)".

---

## Success Criteria

- [ ] `docker compose up` num clone limpo e "Servidor no ar" em `http://localhost:5173`.
- [ ] Os cinco pull requests da fundação revisados e com merge feito pelo usuário; o último, com o CI verde.
- [ ] O usuário roda e depura um teste do backend e um do frontend no VS Code, dentro do contêiner.
- [ ] Medição da V43 (tempo de subida e dos testes com a pasta no Windows) entregue ao usuário.
