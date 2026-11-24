# D-030: Arquitetura de informação e navegação

- **Status**: Aprovada
- **Data**: 2026-11-24
- **Aprovação**: respostas "4 abas, Praticar junto", "Divide ao responder", "Estante" e "Some durante a sessão" (2026-11-24); navegação aprovada com "Pra mim, parece lindo, polido e sóbrio. Está perfeito." (2026-11-24); registro autorizado com "Aprovar Etapa 5" (2026-11-24)
- **Relacionadas**: D-001, D-014, D-020, D-028, D-029, D-031; RNF-04, RNF-14, RNF-15, SIM-09 e EDIT-03 em `docs/requisitos-mvp.md`; M-10, M-11 e M-32 em `docs/modelo-conceitual.md`; `docs/design-e-ux.md`; referência visual em `docs/design/navegacao.html`

## Contexto

- O estudante usa principalmente celular e tablet (D-014). Todas as funcionalidades dele precisam funcionar em celular, tablet em pé e deitado e computador (RNF-04), por toque (RNF-15), preservando o estado ao girar o aparelho (RNF-14).
- O catálogo deixou para a Etapa 5 os breakpoints e o layout por tamanho de tela, com o exemplo da questão e da correção lado a lado no tablet deitado.
- O treino e o simulado usam os mesmos filtros de área, tema, banca e ano (SIM-09). O treino também aceita "não resolvidas" e "erradas" (CAT-02).
- O painel do editor é só para computador (EDIT-03).

## Opções consideradas

### Organização das abas

- **Quatro abas, com Praticar (escolhida):** Início, Praticar, Estante e Desempenho. Treino e simulado partem da mesma tela de filtros, e o modo é escolhido no fim. A conta fica num botão no canto do Início.
- **Cinco abas:** Início, Treinar, Simulados, Estante e Desempenho. Cada funcionalidade a um toque, mas a barra fica apertada e as duas telas repetem os mesmos filtros.
- **Três abas:** Início, Estante e Desempenho, com treinar e fazer simulado como botões no Início. Mais limpo, mas praticar fica a dois toques quando a pessoa está em outra aba.

### Questão e correção na tela larga

- **Divide ao responder (escolhida):** antes da resposta, a questão fica centralizada para leitura; ao responder, ela vai para a esquerda e a correção abre à direita, cada lado rolando sozinho.
- **Sempre dividido:** enunciado à esquerda e alternativas à direita desde o começo; a correção fica espremida embaixo das alternativas.
- **Uma coluna só:** igual ao celular, com mais margem; desperdiça a tela larga e obriga a rolar até a correção.

### Nome da aba das listas pessoais

- **Estante (escolhida):** combina com a ideia de biblioteca e com a fita roxa das marcadas (D-028).
- **Caderno:** lembra o caderno de erros, mais familiar e menos ligado à marca.
- **Revisão:** direto, mas genérico.

### Abas durante a sessão

- **Somem, em modo foco (escolhida):** a tela fica só com a questão, como numa prova.
- **Sempre visíveis:** dá para pular de aba no meio do treino, com menos espaço e mais distração.

Custo e complexidade não foram critérios nestas escolhas.

## Decisão

- Quatro abas: Início, Praticar, Estante e Desempenho; a conta no canto do Início.
- Modo foco em treino e simulado, saindo pelo botão do topo. No simulado, esse botão é Pausar, porque a pausa é sempre explícita (M-11).
- Três faixas de largura, propostas pelo consultor e aprovadas com a página de navegação:
  - até 599 px: abas embaixo, uma coluna;
  - de 600 a 1023 px: trilho lateral com ícones e nomes, inclusive no celular deitado, para não gastar altura;
  - 1024 px ou mais: barra lateral com nomes.
- A partir de 1024 px, no modo foco, a questão divide ao responder.
- O mapa do app, os fluxos e a lista de requisitos atendidos por tela estão em `docs/design-e-ux.md`.

## Consequências

- Ganhamos: praticar a um toque de qualquer aba, com uma só tela de filtros; foco total na questão; uso pleno da tela larga sem atrapalhar a leitura.
- Abrimos mão de: trocar de aba no meio de uma sessão; uma aba própria para simulados.
- Exige: ao trocar de tela, levar o foco ao título da nova tela; desligar "não resolvidas" e "erradas" no modo simulado (SIM-09); avisar no início do simulado que fechar o app não para o tempo (M-11, M-32); preservar resposta, riscos, posição e cronômetro ao mudar de faixa girando o aparelho (RNF-14).
- Revisitar se: o uso no tablet em pé pedir a divisão também abaixo de 1024 px; ou o painel do editor precisar funcionar no tablet, o que hoje está fora do MVP (EDIT-03).
