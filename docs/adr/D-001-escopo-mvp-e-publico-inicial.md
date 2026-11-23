# D-001: Escopo do MVP e público inicial

- **Status**: Aprovada
- **Data**: 2026-11-23
- **Aprovação**: "Aprovo beta fechado primeiro" (sequência de lançamento) e "Aprovo como está" (escopo do MVP) (2026-11-23)
- **Relacionadas**: D-002, D-003, D-011, D-013, D-014

## Contexto

- Ambição informada para os próximos 12 meses: plataforma aberta ao público, com cobrança no futuro.
- Origem do conteúdo ainda em aberto; provas anteriores de residência são a origem considerada até agora (D-002). Revisão atual feita por estudantes conferindo referências (D-003). A combinação produto aberto e pago + questões de terceiros + revisão só por estudantes concentra o risco jurídico e de reputação justamente no diferencial do produto: a confiabilidade do conteúdo.
- Primeira usuária: estudante do ciclo clínico, que usa celular e tablet e estuda com treino por tema, simulado cronometrado e revisão dos erros.
- Restrições informadas: 5–10h/semana até 11/12/2026 e dedicação integral até fevereiro/2027; sem experiência prévia em frontend; orçamento de R$ 50–150/mês sem receita. O MVP precisa ser enxuto para caber nessa janela.

## Opções consideradas

### Beta fechado primeiro, depois abertura, depois cobrança

- Prós: valida o produto com usuários reais sem expor conteúdo cuja situação jurídica ainda não foi resolvida; compatível com a ambição "aberto, pago no futuro".
- Contras: menos alcance no início.
- Custo e complexidade: a completar.

### Aberto ao público desde o lançamento

- Prós: mais alcance logo no início.
- Contras: exige resolver as pendências de conteúdo (D-002) e de revisão (D-003) antes de lançar, além de termos de uso, política de privacidade e conteúdo com licença clara desde o início.
- Custo e complexidade: a completar.

### Escopo do MVP: itens avaliados e deixados de fora

| Item | Situação | Motivo apresentado |
|---|---|---|
| Importação em lote | Depois | — |
| Busca por texto livre | Depois | Filtros bastam com acervo pequeno |
| Comparação com outros alunos | Depois | Precisa de volume de usuários |
| Pagamentos | Depois | Cobrança só depois da abertura |
| Comentários dos alunos nas questões | Depois | — |
| Organização de estudos / cronograma | Fora por ora | Custo alto e valor incerto |
| Revisão espaçada | Fora por ora | A primeira usuária não pediu |
| Ranking e gamificação | Fora por ora | — |
| Chatbot com RAG | Fora por ora | Interesse futuro, ver D-012 |
| App nativo | Fora por ora | A web responsiva atende o tablet |

Favoritos e "questões para revisar" foram unificados em um único recurso ("marcar").

## Decisão

Lançar como beta fechado (primeira usuária e colegas convidados) ao fim das férias; abrir ao público só depois de resolver D-002 e D-003; cobrar depois. O MVP inclui: login com e-mail e senha; classificação grande área → tema; filtros (área, tema, banca, ano, não resolvidas, erradas); treino por tema com correção imediata; simulado cronometrado com correção no fim; revisão dos erros + "marcar"; desempenho por área e tema, destacando os temas mais fracos; reportar erro na questão; painel do editor (origem, licença, referências, status, versões, imagens); termos de uso, política de privacidade, exportar e excluir conta.

## Consequências

- Ganhamos: validação com uso real antes de expor o conteúdo ao público; escopo dimensionado para a janela de tempo informada.
- Abrimos mão de: alcance público no lançamento; os itens da tabela acima.
- Revisitar se: D-002 e D-003 forem resolvidas (gatilho para a abertura ao público). Demais gatilhos: a completar.
