# D-028: Identidade visual

- **Status**: Aprovada
- **Data**: 2026-11-24
- **Aprovação**: direção escolhida com "O melhor foi o esmeralda" (2026-11-23); versão final aprovada com "[...] está PERFEITO!" e "passa ar de credibilidade" (2026-11-24); registro autorizado com "Aprovar Etapa 5" (2026-11-24)
- **Relacionadas**: D-006, D-014, D-029, D-030; RNF-01 em `docs/requisitos-mvp.md`; `docs/design-e-ux.md`; referência visual em `docs/design/identidade.html`

## Contexto

- Prioridade máxima do usuário: experiência de uso e design, com o iOS como referência de qualidade (D-020). O design é responsabilidade do Claude, com revisão e aprovação do usuário (D-006).
- Respostas do primeiro bloco da Etapa 5 (2026-11-23): tom "editorial acolhedor"; referências de sensação em apps editoriais e bancos digitais; modo claro e escuro desde o MVP, seguindo o aparelho; marca com o nome escrito numa tipografia própria e um ícone simples derivado dele, para a tela inicial do app instalado.
- A proposta de valor pede confiança no conteúdo e interface pensada para celular e tablet (D-014). O contraste precisa cumprir a WCAG 2.2 AA nos dois modos (RNF-01).

## Opções consideradas

Três direções completas, com cores, fontes, ícone e telas de exemplo, comparadas pelo usuário no celular e no tablet.

### Cartão-resposta

- Prós: vem da folha de respostas da prova, com a alternativa como uma bolha que se preenche; azul de caneta; é a mais próxima de um banco digital.
- Contras: azul é a cor mais comum em apps de banco e de saúde; o que a diferenciava era a bolha, não a cor.
- Custo e complexidade: não foi um critério nesta escolha.

### Esmeralda (escolhida)

- Prós: a esmeralda é a pedra da Medicina no Brasil; tom editorial, com referências como notas de rodapé de livro; fontes confortáveis para leitura longa, nas palavras do usuário "fácil de ler por várias horas".
- Contras: o verde da marca fica perto do verde de acerto. Por isso a opção escolhida, antes da correção, usa tinta escura, e o acerto vem sempre com ícone e texto.
- Custo e complexidade: não foi um critério nesta escolha.

### Marca-texto

- Prós: grafite no papel branco e o amarelo do marca-texto só no que importa; o maior contraste das três.
- Contras: o amarelo só pode ser fundo, nunca texto; na avaliação do usuário, "a ideia do marca-texto é boa mas a execução não ficou tão legal".
- Custo e complexidade: não foi um critério nesta escolha.

## Ajustes pedidos sobre a Esmeralda

Retorno trazido pelo usuário (2026-11-23 e 2026-11-24), aplicado antes da aprovação:

- alternativas em bolinha, no lugar do contorno lapidado, que ficava "muito bruto";
- ícone que mistura as três direções: fundo branco da Marca-texto, aro em volta do M do Cartão-resposta e o verde da Esmeralda;
- a identidade deve lembrar uma biblioteca ou um livro: entrou o roxo do livro, com "Med" em verde e "Teca" em roxo;
- "Teca" em tom de casca de ovo: usado sobre a capa roxa e no modo escuro, porque no fundo claro o contraste seria de 1,15:1;
- verde do "Med" mais escuro, para combinar com o roxo;
- fita do ícone reposicionada: sai da borda de cima e termina na altura do topo do aro.

## Decisão

Identidade Esmeralda, como descrita em `docs/design-e-ux.md`:

- esmeralda como cor da marca; roxo do livro só no nome escrito, na fita das questões marcadas e na capa da tela de início;
- papel verde-claro no modo claro; modo escuro seguindo o aparelho;
- Literata para ler e Figtree para usar;
- nome escrito "MedTeca", com "Med" em esmeralda e "Teca" em roxo, ou em casca de ovo sobre o roxo e no escuro;
- ícone com fundo branco, aro esmeralda em volta do M e fita roxa de marcador.

## Consequências

- Ganhamos: uma identidade ligada à Medicina e à biblioteca, que no retorno trazido pelo usuário "passa ar de credibilidade".
- Abrimos mão de: casca de ovo como cor de texto no fundo claro; mais de um uso decorativo do roxo.
- Exige: o roxo restrito a três usos; a escolha antes da correção em tinta escura; contraste conferido nos dois modos a cada cor nova.
- Revisitar se: um designer refinar o nome escrito e o ícone, o que já está previsto e não muda a ideia; ou testes com estudantes mostrarem confusão entre a esmeralda e o verde de acerto.

## Atualização da Etapa 6, bloco 6 (2026-11-24)

Conforme D-034: a revisão do usuário sobre o design inclui ler e revisar o código que o implementa, em todos os pull requests, além de conferir as telas.
