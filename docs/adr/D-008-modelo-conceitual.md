# D-008: Modelo conceitual dos dados

- **Status**: Aprovada
- **Data**: 2026-11-23
- **Aprovação**: "Aprovar Etapa 4" (2026-11-23); registro autorizado com "Autorizo" (2026-11-23)
- **Relacionadas**: D-001, D-005, D-009, D-013, D-014, D-019, D-022, D-024, D-032; documento `docs/modelo-conceitual.md`

## Contexto

- O catálogo de requisitos aprovado na Etapa 2 exige, entre outros:
  - integridade do gabarito, com três situações e três camadas: na resposta, atual e histórico (CONT);
  - versões e revisão antes de publicar (FLUXO);
  - tentativas, simulados e desempenho (TREINO, SIM, DES);
  - autorização de uso com evidência (EDIT);
  - exclusão de conta com anonimização (CONTA).
- A skill do projeto traz uma lista do que cada questão precisa ter rastreável: origem, licença, versões, revisão e situação na banca.
- O banco aprovado é o PostgreSQL (D-005), e as regras de integridade devem ser garantidas também no banco.
- O modelo passou por duas revisões de consenso, a partir de revisões externas trazidas pelo usuário.

## Opções consideradas

As alternativas de cada decisão estão no documento do modelo. Este quadro resume as decisões mais difíceis de reverter.

| Tema | Escolhido | Alternativas consideradas |
|---|---|---|
| Alternativas entre versões | Identificador estável, com seleção e ordem por versão (M-03, M-30). Questões de prova oficial mantêm as alternativas e a ordem da banca, e uma tentativa que não dá para recalcular mantém o resultado original (M-37) | Estrutura rígida, sem acrescentar, remover nem reordenar; recalcular sempre comparando identificadores; comparar pela letra |
| Classificação | Sistemas de classificação (M-04), que valem para a questão; a reclassificação muda o desempenho retroativamente (M-05) | Grande área e tema fixos; tema da época em cada tentativa |
| "Não resolvidas" e "erradas" | Olham para a questão, em qualquer versão (M-08) | Só a versão vigente |
| Desempenho | Calculado na consulta (M-09) | Resultados guardados e recalculados em tarefas |
| Treino e simulado | No servidor, com o servidor como autoridade do tempo (M-10, M-11, M-32) | Guardados no aparelho; pausa automática ao fechar o app |
| Autorização de uso | Por fonte, com exceção por item (M-15), e bloqueio imediato da exibição quando revogada (M-33) | Por questão e por imagem; retirada só manual |
| Referências | Estruturadas por tipo (M-16) | Texto livre |
| Texto alternativo das imagens | É conteúdo e gera versão nova (M-17) | Metadado, sem revisão |
| Pessoas editoriais | Um só cadastro de pessoa editorial para autor, ator e autor do comentário (M-18, M-31, M-38) | Autor sempre como conta; autor e ator separados |
| Exclusão de conta | Desvínculo total, com as datas reduzidas ao mês (M-21, M-36) | Pseudônimo; datas exatas; remover as datas |
| Trilha de auditoria | Trilha única, só de inclusão, apontando para a pessoa editorial, protegida no MVP por permissão do banco (M-23, M-31, M-34) | Histórico por entidade; hash encadeado e armazenamento externo já no MVP |

## Decisão

Adotar o modelo conceitual de `docs/modelo-conceitual.md`: 38 decisões de modelagem (M-01 a M-38), das quais M-03 e M-18 foram substituídas em parte por M-30 e M-38, e 17 regras de integridade (RM-01 a RM-17), com diagrama, rastreabilidade e comparação com a lista de integridade de conteúdo do projeto.

## Atualizações da Etapa 6

- **Bloco 4 (D-032, 2026-11-24):** entrou a M-39 (auditoria de ações sensíveis), com a regra RM-18. Nenhuma decisão da Etapa 4 mudou.
- **Bloco 3 (D-009, aprovado em 2026-11-24 e registrado no modelo em 2026-11-26):** a linha "Exclusão de conta" do quadro acima foi substituída. Na exclusão, a primeira resposta da pessoa em cada versão vira contagem e as tentativas são apagadas (M-40); o reporte concluído perde o texto livre (M-41); cada registro tem destino definido (M-42); a RM-19 substitui a RM-13. M-21 e M-36 ficam como substituídas, e M-07 e M-22, como substituídas em parte, com o texto original mantido. O motivo é a LGPD (art. 16, IV, e art. 12): num beta pequeno, as tentativas desvinculadas podiam não ser anônimas de verdade. O raciocínio e as alternativas estão no ADR da D-009.

## Consequências

- **Ganhamos**:
  - as regras de integridade do conteúdo garantidas também por restrições do banco;
  - recálculos de desempenho automáticos, sem tarefa em segundo plano;
  - histórico fiel ao que o estudante viu quando respondeu;
  - privacidade na exclusão de conta sem perder a rastreabilidade editorial.
- **Abrimos mão de**:
  - desempenho pré-calculado (pode vir depois como visão, sem mudar o modelo);
  - uma auditoria inviolável já no MVP.
- **Exige**:
  - catálogo atualizado com CONT-23, CONT-24, DES-11 a DES-13, REV-07, EDIT-12, EDIT-13 e CONTA-25;
  - D-024 sem os recálculos entre os usos;
  - as pendências listadas no documento do modelo para as specs da TLC e para a Etapa 6.
- **Revisitar se**:
  - as consultas de desempenho ficarem lentas;
  - D-012 aprovar uso de IA no conteúdo, o que pede uma origem "gerado por IA";
  - D-003 definir a revisão clínica, o que pede a data da última revisão clínica.
