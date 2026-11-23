# Registro de decisões: MedTeca

Índice das decisões do projeto. Só o que está como **Aprovada** é vinculante. O raciocínio das decisões aprovadas importantes fica em `docs/adr/`.

Status: Pendente → Proposta → Aprovada → Substituída · Descartada

## Decisões

| ID | Decisão | Status | Resumo (opções, escolha ou bloqueio) | ADR | Atualizado |
|---|---|---|---|---|---|
| D-001 | Escopo do MVP e público inicial | Aprovada | Beta fechado (primeira usuária e colegas convidados) ao fim das férias → abertura ao público só depois de resolver D-002 e D-003 → cobrança depois. MVP: login com e-mail e senha; classificação grande área → tema; filtros (área, tema, banca, ano, não resolvidas, erradas); treino por tema com correção imediata; simulado cronometrado com correção no fim; revisão dos erros + "marcar"; desempenho por área e tema; reportar erro na questão; painel do editor (origem, licença, referências, status, versões, imagens); termos de uso, política de privacidade, exportar e excluir conta. Aprovação: "Aprovo beta fechado primeiro" e "Aprovo como está" (2026-11-23). | [ADR](adr/D-001-escopo-mvp-e-publico-inicial.md) | 2026-11-23 |
| D-002 | Origem das questões e licenciamento | Pendente | Considerado até agora: provas anteriores de residência; demais origens em aberto. Bloqueia a abertura ao público (D-001). Recomendação feita: consultar advogado antes de publicar conteúdo de terceiros em produto aberto ou pago. Depende também de D-011. | — | 2026-11-23 |
| D-003 | Revisão do conteúdo clínico (quem revisa, como, critérios) | Pendente | Situação atual: revisão por estudantes conferindo referências; sem médico revisor. Bloqueia a abertura ao público (D-001). Caminhos levantados: nível de revisão visível por questão; médicos revisores antes de cobrar; MVP sem comentário próprio. | — | 2026-11-23 |
| D-004 | Backend: linguagem e framework | Pendente | Preferência inicial: Python. Experiência informada: backend em Python. | — | 2026-11-23 |
| D-005 | Banco de dados | Pendente | Preferência inicial: PostgreSQL. Experiência informada: SQL/PostgreSQL. | — | 2026-11-23 |
| D-006 | Frontend | Pendente | Sem experiência prévia informada em frontend; design é prioridade do projeto → maior risco técnico do MVP. Uso principal em celular e tablet (D-014). | — | 2026-11-23 |
| D-007 | Autenticação e contas de usuário | Pendente | O MVP prevê login com e-mail e senha (D-001); mecanismo e demais detalhes a decidir. | — | 2026-11-23 |
| D-008 | Modelo de dados das questões (versões, rastreabilidade) | Pendente | Requisitos já aprovados: classificação grande área → tema, aceitando outras classificações depois (D-013); origem, licença, referências, status, versões e imagens (D-001); três situações de gabarito distintas (D-014). | — | 2026-11-23 |
| D-009 | Tratamento de dados pessoais (LGPD) | Pendente | O MVP inclui termos de uso, política de privacidade, exportar e excluir conta (D-001). | — | 2026-11-23 |
| D-010 | Hospedagem, infraestrutura e orçamento | Pendente | Orçamento informado enquanto não há receita: R$ 50–150/mês. Experiência informada em deploy e infraestrutura. | — | 2026-11-23 |
| D-011 | Modelo de negócio e monetização | Pendente | Diretriz aprovada em D-014: preço justo, sem funcionalidades bloqueadas por plano. Intenção informada: preço baixo, cobrindo custos com lucro mínimo; cobrança só depois da abertura (D-001). Em aberto: modelo de cobrança e quem financia a revisão (D-003). Afeta o licenciamento (D-002). | — | 2026-11-23 |
| D-012 | Uso de IA para gerar ou revisar conteúdo | Pendente | Interesse futuro em chatbot com RAG sobre o acervo, fora do MVP. Pontos levantados: risco de gerar texto clínico; custo por uso frente ao preço baixo. | — | 2026-11-23 |
| D-013 | Foco do conteúdo no lançamento | Aprovada | Questões de residência organizadas por grande área → tema, para estudantes do ciclo clínico em diante. O modelo de dados deve aceitar outras classificações (graduação, exames nacionais) depois. Aprovação: "Aprovo residência por tema" (2026-11-23). | [ADR](adr/D-013-foco-do-conteudo-no-lancamento.md) | 2026-11-23 |
| D-014 | Proposta de valor e diferenciais | Aprovada | Proposta aprovada: questões de residência por tema com origem, gabarito oficial e nível de revisão visíveis em cada questão; interface pensada para tablet e celular; preço justo sem funcionalidades bloqueadas; não competir em volume de questões nem em IA. Aprovação: "Aprovo" (2026-11-23). Observação do usuário no registro (2026-11-23): a situação do gabarito deve distinguir, sem tratá-las como equivalentes, (a) gabarito oficialmente publicado pela banca, (b) gabarito revisado por uma pessoa e (c) gabarito ainda não confirmado oficialmente. Insumo obrigatório dos requisitos da Etapa 2. | — | 2026-11-23 |
| D-015 | Meta de acervo e operação de conteúdo do beta | Pendente | Em aberto: quantas questões, quem cadastra e como entram no acervo. | — | 2026-11-23 |
| D-016 | Idioma da interface | Pendente | Presumido português do Brasil; não confirmado. | — | 2026-11-23 |

## Histórico

- 2026-11-23: índice criado ao fim da Etapa 1 (descoberta do produto).
- 2026-11-23: D-001, D-013 e D-014 aprovadas; D-015 e D-016 abertas como pendências.
