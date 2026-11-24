# Design e experiência de uso: MedTeca

**Situação**: aprovado. Etapa 5 encerrada.

**Aprovado**: 2026-11-24 - usuário: "Aprovar Etapa 5"

Identidade visual, sistema de design, tom de voz, navegação, fluxos e tamanhos de tela do MedTeca, definidos na Etapa 5. As decisões estão no índice: D-028 (identidade visual), D-029 (sistema de design e tom de voz), D-030 (arquitetura de informação e navegação) e D-031 (riscar alternativas). Os critérios testáveis que saíram da etapa estão em `docs/requisitos-mvp.md`: CONT-25 a CONT-29 e RISC-01 a RISC-07.

Este documento registra o que foi aprovado. Não é código: estilos e componentes são construídos com React e React Aria Components (D-006), depois da especificação de cada funcionalidade (D-017).

## Referência visual

As páginas usadas para aprovar a etapa ficam em `docs/design/`. Abra num navegador; elas trocam entre claro e escuro e têm demonstrações que funcionam.

| Página | Conteúdo |
|---|---|
| `docs/design/identidade.html` | Nome, ícone, cores e fontes, com telas de exemplo da identidade |
| `docs/design/sistema-de-design.html` | Cores com contraste medido, tipografia, espaço, componentes em todos os estados, movimento e tom de voz |
| `docs/design/navegacao.html` | Mapa do app, tamanhos de tela, fluxos, telas-chave e a questão que divide ao responder |

As fontes vêm do Google Fonts; sem internet, aparecem as fontes de reserva. Textos e números marcados [FICTÍCIO] são exemplos, sem conteúdo clínico. A página de identidade ainda mostra a opção de papel casca de ovo, que ficou só como teste: o papel aprovado é o verde-claro. Onde uma tela de exemplo divergir deste documento, vale este documento.

## 1. Identidade visual (D-028)

**A ideia.** A esmeralda é a pedra da Medicina no Brasil; o roxo é o livro. "Teca" é o mesmo final de biblioteca, então o nome junta a Medicina e a biblioteca na mesma palavra. O tom é editorial e acolhedor, com leitura confortável por horas.

**Nome escrito.** "MedTeca" em Literata 600, com "Med" em esmeralda e "Teca" em roxo. No modo escuro e sobre a capa roxa, "Teca" fica em casca de ovo. No fundo claro, a casca de ovo não é usada como texto: o contraste seria de 1,15:1.

**Ícone.** Fundo branco, aro esmeralda em volta de um M em Literata e uma fita roxa de marcador de livro. Geometria numa grade de 120 por 120:

- canto arredondado de raio 27, com um fio de borda claro;
- aro com centro no meio, raio 34 e traço 5;
- M com 40 de corpo;
- fita de x = 80 a x = 93, saindo da borda de cima e terminando em y = 23,5, na altura do topo do aro, com recorte em V até y = 18. Ela fica por cima do fio de borda e não encosta no aro.

O ícone não muda entre claro e escuro. Um designer pode refinar nome e ícone depois, sem mudar a ideia.

**Por que esta direção.** Foram comparadas três direções: Cartão-resposta, Esmeralda e Marca-texto. As alternativas e os motivos estão no ADR de D-028.

## 2. Cores

Todas as cores são tokens em oklch, com valor para o claro e para o escuro. O app segue o ajuste do aparelho, e a pessoa pode fixar claro ou escuro na Conta.

| Token | Papel | Claro | Escuro |
|---|---|---|---|
| Papel | Fundo de todas as telas | oklch(98.6% 0.006 160) | oklch(17% 0.015 165) |
| Superfície | Etiquetas, hover, áreas de apoio | oklch(96.5% 0.01 160) | oklch(21% 0.018 165) |
| Fio | Divisórias e bordas | oklch(89% 0.014 160) | oklch(31% 0.02 165) |
| Tinta | Texto principal e opção escolhida | oklch(23% 0.02 165) | oklch(94% 0.008 160) |
| Tinta secundária | Metadados, legendas, bordas de campo | oklch(49% 0.02 165) | oklch(72% 0.015 160) |
| Esmeralda | Marca, ação principal, progresso, "Med" | oklch(40% 0.11 163) | oklch(68% 0.14 160) |
| Esmeralda, toque | Botão principal pressionado ou sob o mouse | oklch(35% 0.1 163) | oklch(74% 0.13 160) |
| Texto sobre a esmeralda | Rótulo do botão principal | oklch(99% 0.005 160) | oklch(18% 0.02 165) |
| Foco | Anel do teclado | oklch(55% 0.14 163) | oklch(82% 0.11 163) |
| Acerto | Só a resposta certa | oklch(46% 0.12 150) | oklch(78% 0.12 150) |
| Erro | Resposta errada e falhas | oklch(48% 0.16 18) | oklch(74% 0.13 20) |
| Atenção | Gabarito preliminar e resultado provisório | oklch(52% 0.12 70) | oklch(80% 0.12 80) |
| Texto sobre status | Letra dentro da bolinha certa ou errada | oklch(99% 0.005 160) | oklch(17% 0.015 165) |
| Destaque | Trecho-chave do comentário | oklch(91% 0.05 163) | oklch(34% 0.06 163) |
| Texto do destaque | Texto sobre o destaque | oklch(23% 0.02 165) | oklch(94% 0.008 160) |
| Teca | "Teca" no nome escrito | oklch(44% 0.16 305) | oklch(94% 0.025 85), casca de ovo |
| Fita | Fita das questões marcadas | oklch(44% 0.16 305) | oklch(76% 0.11 305) |
| Capa | Capa roxa da tela de início | oklch(28% 0.12 305) | oklch(28% 0.12 305) |
| Verde da capa | "Med" sobre a capa | oklch(63% 0.15 160) | oklch(63% 0.15 160) |
| Casca de ovo | "Teca" e textos sobre a capa | oklch(94% 0.025 85) | oklch(94% 0.025 85) |

Cores do ícone, iguais nos dois modos: fundo oklch(99.5% 0.002 160), fio de borda oklch(88% 0.01 160), aro e M oklch(40% 0.11 163), fita oklch(44% 0.16 305).

**Contraste (WCAG 2.2 AA, RNF-01).** Todo texto tem pelo menos 4,5:1 e toda borda ou ícone que identifica um controle tem pelo menos 3:1, nos dois modos. Os pares mais justos: "Med" sobre a capa, 4,7:1; foco no claro, 4,2:1, acima do mínimo de 3:1 para indicador; atenção sobre o papel no claro, 5,4:1.

**Regras de uso.**

- O roxo tem só três usos: o nome escrito, a fita das marcadas e a capa da tela de início.
- O verde de acerto fica perto da esmeralda. Por isso a opção escolhida, antes da correção, usa tinta escura, e o acerto vem sempre com ícone e texto.
- Cor nunca sozinha: todo estado também tem ícone ou texto.
- Sem sombras. A separação vem de fios e superfícies.

## 3. Tipografia

Literata para ler, Figtree para usar. Tudo em rem, para acompanhar o tamanho de letra escolhido no aparelho.

| Papel | Fonte | Tamanho | Uso |
|---|---|---|---|
| Número de destaque | Literata 600 | 52 px | Taxa de acerto, com números tabulares |
| Título de tela | Literata 600 | 28 px | Títulos de tela de conteúdo |
| Título de seção | Literata 600 | 19 px | Seções dentro das telas |
| Leitura | Literata 400 | 17 px, entrelinha 1,6 | Enunciado e comentário, até cerca de 68 caracteres por linha |
| Interface | Figtree 400 e 600 | 16 px | Botões, alternativas, menus |
| Apoio | Figtree 400 | 14 px | Origem, metadados, legendas |
| Nota | Figtree 500 | 13 px | Observações; nunca conteúdo principal |

## 4. Espaço, forma e movimento

- **Espaço:** múltiplos de 4 (4, 8, 12, 16, 24, 40, 64).
- **Cantos:** controles 8, painéis 14, etiquetas 6, barras redondas.
- **Toque:** área mínima de 44 por 44 px em todo controle.
- **Movimento:** 120 ms para cores e preenchimentos; 220 ms para aparecer e sumir. O botão encolhe para 98% enquanto pressionado. A curva começa rápida e assenta devagar. Nada se move sozinho, e nunca há confete, tremor ou animação ao errar. Com "reduzir movimento" ligado no aparelho, as transições somem.

## 5. Componentes e estados (D-029)

Cada componente tem equivalente direto no React Aria Components (D-006); o encaixe exato é conferido na implementação.

| Componente | Estados | Requisitos |
|---|---|---|
| Botão principal | Padrão, mouse por cima, foco, pressionado, desabilitado, carregando. Um só por tela | RNF-01, RNF-15 |
| Botão secundário e Marcar | Padrão, mouse por cima, foco, desabilitado; Marcar ligado mostra a fita roxa | REV-03 |
| Alternativa | Padrão, mouse por cima, foco, escolhida (tinta escura), riscada; depois de responder: a sua errada, a certa, as outras esmaecidas. A linha inteira escolhe; a bolinha traz a letra em Literata | TREINO-02, RISC-01 a RISC-05 |
| Tesoura (riscar) | Desligada, ligada (vermelha), some depois da resposta. Rótulo para leitor de tela: "Riscar opção X" | RISC-01 a RISC-04 |
| Procedência | Origem; situação do gabarito; "Revisão editorial, mês e ano", que abre a explicação ao tocar. Antes e depois de responder | CONT-02, CONT-04, CONT-25 a CONT-29, D-014 |
| Resultado | Acertou, errou, errou com "Resultado provisório" | TREINO-02, CONT-12 |
| Gabarito que muda | Gabarito mudou e o resultado foi recalculado; gabarito confirmado depois da resposta; resposta não reavaliada | CONT-10, CONT-17, CONT-19, CONT-24 |
| Histórico e retiradas | Resposta normal; gabarito mudou; não reavaliada; retirada com a questão visível; retirada por licenciamento, só com o registro e o motivo | DES-05, CONT-07, FLUXO-15, FLUXO-16, REV-04 |
| Imagem na questão | Carregando com o espaço reservado; carregada, com texto alternativo e opção de ampliar; descrição dos achados na correção | RNF-19, EDIT-07 a EDIT-10 |
| Campo de texto | Padrão, mouse por cima, foco, erro com mensagem, desabilitado. Rótulo sempre visível | RNF-01 |
| Filtro | Desligado, mouse por cima, foco, ligado com marca, desabilitado | CAT-02 a CAT-04 |
| Controle segmentado | Uma escolha entre poucas, como Geral, Treino e Simulados | DES-06 |
| Avisos | Informação, sucesso, erro com "Tentar de novo", sem conexão, sem conexão no simulado | RNF-05 a RNF-07 |
| Estados de tela | Carregando, vazia, com erro e cheia, em toda tela que carrega dados | RNF-01 |
| Barra de abas | Aba atual com cor, peso e fundo, e anunciada ao leitor de tela | RNF-01, D-030 |
| Mapa do simulado | Respondida, em branco, marcada (fita), atual | SIM-07, SIM-08 |
| Simulado pausado | Questão escondida, "Retomar" e "Sair; o simulado fica pausado" | SIM-03, M-11 |

## 6. Textos

### Tom de voz (D-029)

Direto e acolhedor.

1. Trate por você, em frases curtas.
2. Diga o que aconteceu e o que fazer a seguir.
3. Sem exclamação, gíria ou emoji.
4. Em erro, explique sem culpar quem estuda.
5. Números com contexto: "3 de 6 respostas", não só "50%".
6. Não exagere certeza: "provisório", "ainda não dá para concluir".

| Assim | Não assim |
|---|---|
| Você errou. A resposta certa é D. | Ops! Resposta errada!! |
| Não foi possível salvar sua resposta. Tente de novo. | Erro 500: falha na requisição. |
| Poucas respostas: 3 de 6. Ainda não dá para concluir. | Você vai mal neste tema. |
| Gabarito definido pelo MedTeca. A banca não publicou gabarito oficial. | Gabarito correto. |

### Textos aprovados

| Onde | Texto | Requisito |
|---|---|---|
| Gabarito oficial | "Gabarito oficial da banca" | CONT-25 |
| Gabarito definido por uma pessoa | "Gabarito definido pelo MedTeca", com "A banca não publicou gabarito oficial." nas questões de prova e "Questão própria: não existe gabarito de banca." nas de autoria própria | CONT-25, CONT-26 |
| Gabarito preliminar | "Gabarito preliminar da banca", com "Ainda não confirmado. Seu resultado nesta questão será provisório." antes da resposta e "... é provisório." na correção | CONT-25, CONT-27 |
| Nível de revisão | "Revisão editorial", com mês e ano; ao tocar: "Uma pessoa diferente do autor revisou esta versão antes de publicar. Não é revisão médica." | CONT-28, CONT-29 |
| Certa que tinha sido riscada | "Resposta certa. Você tinha riscado esta." | RISC-05 |
| Resposta não reavaliada | "Resultado pelo gabarito da versão respondida; não reavaliado pelo gabarito atual" | CONT-24 |

"MedTeca", e não "equipe", porque hoje a pessoa editorial é uma só (M-38). A revisão editorial não equivale a revisão médica (M-26); quando a D-003 definir a revisão médica, ela entra como um segundo nível ao lado da editorial.

## 7. Navegação (D-030)

**Quatro abas**, embaixo no celular:

| Aba | Conteúdo |
|---|---|
| Início | Continuar de onde parou; avisos, como o resultado de um reporte; resumo da estante; botão Conta no canto, sobre a capa roxa |
| Praticar | Uma tela em dois passos: o que estudar (área, tema, banca, ano, não resolvidas, erradas, com a contagem de questões) e como praticar (Treino ou Simulado, com quantidade e duração). No simulado, "não resolvidas" e "erradas" ficam desligadas, porque o sorteio usa só área, tema, banca e ano (SIM-09) |
| Estante | Questões marcadas, erros para revisar (com "Treinar meus erros", que usa o filtro "erradas"), simulados feitos e histórico de respostas |
| Desempenho | Geral, Treino e Simulados; por área e por tema, com a quantidade e o aviso de poucas respostas; temas mais fracos só na visão geral e só com 5 respostas ou mais; tentativas fora do cálculo |

**Conta**, pelo botão do Início: apelido, aparência, reportes enviados com o resultado, termos e privacidade, exportar meus dados (preparado em segundo plano, D-024), excluir conta e sair.

**Modo foco.** Treino e simulado escondem as abas. Sai pelo botão do topo. No simulado esse botão é Pausar: a pausa é sempre explícita, e a tela pausada oferece Retomar ou Sair. Fechar o app sem pausar não para o tempo, e o início do simulado avisa isso (M-11, M-32).

**Fora da conta:** criar conta pelo convite, entrar, recuperar senha.

**Painel do editor**, só no computador (EDIT-03), com barra lateral própria: Questões por status, Revisão, Reportes e Administração (fontes e autorizações, convites e papéis).

## 8. Tamanhos de tela

| Faixa de largura | Aparelhos típicos | Navegação | Conteúdo |
|---|---|---|---|
| Até 599 px | Celular em pé | Abas embaixo | Uma coluna |
| 600 a 1023 px | Tablet em pé e celular deitado | Trilho lateral com ícones e nomes | Uma coluna |
| 1024 px ou mais | Tablet deitado e computador | Barra lateral com nomes | Listas e desempenho em duas colunas |

- **Divide ao responder.** A partir de 1024 px, no modo foco, a questão fica centralizada antes da resposta. Ao responder, ela vai para a esquerda e a correção abre à direita, cada lado rolando sozinho. Abaixo disso, a correção aparece embaixo da questão.
- **Leitura:** o texto de leitura não passa de cerca de 68 caracteres por linha em nenhuma faixa.
- **Girar o aparelho** muda só a faixa. Resposta marcada, riscos, posição na sequência e cronômetro continuam iguais (RNF-14).

## 9. Fluxos

| Fluxo | Passos |
|---|---|
| Primeiro acesso | Convite por e-mail; senha, apelido opcional e aceite dos termos; Início vazio com "Começar a praticar" (CONTA-01 a CONTA-05, CONTA-09) |
| Treinar | Praticar; filtros; Treino; responde e vê a correção na hora; próxima questão; sai pelo topo. Quando o treino termina fica para a especificação de TREINO; a retomada já está resolvida em M-10 |
| Simulado | Praticar; filtros; Simulado, quantidade e duração; responde com o cronômetro do servidor; pausa antes de sair; confere o mapa; entrega, ou o tempo acaba e entrega sozinho; nota, acertos, erros e em branco; correção de cada questão |
| Revisar erros | Estante; erros para revisar; "Treinar meus erros"; acertou, a questão sai da lista (REV-01, REV-02) |
| Reportar erro | Na correção, "Reportar erro"; descreve o problema, e a tela pede para não escrever dados pessoais (M-22); o resultado aparece nos avisos do Início e em Conta (REP-01 a REP-03) |
| Publicar uma questão | Rascunho; origem, gabarito e situação, comentário, referências e imagens com texto alternativo; revisão por outra pessoa, que não é autora nem cadastrou; publicada se a autorização tiver evidência, o comentário tiver referência e o gabarito oficial tiver o documento da banca; mudar o conteúdo cria versão nova; retirar exige motivo e vale na hora (FLUXO, EDIT, CONT-22) |

## 10. Riscar alternativas (D-031)

- A linha inteira escolhe a alternativa; a tesoura no fim da linha risca. Riscar não escolhe.
- Riscar a escolhida desfaz a escolha; escolher uma riscada tira o risco; tocar de novo na tesoura desfaz o risco.
- Na correção, os riscos ficam à vista. Se a certa estava riscada, ela aparece em verde com "Resposta certa. Você tinha riscado esta."
- Os riscos ficam só no aparelho, até a correção da questão, e sobrevivem a navegar entre questões e a pausar e retomar. Não entram na tentativa, no desempenho, nas listas, no histórico nem na exportação. Por isso não mudam o modelo de dados (D-008).
- Critérios: RISC-01 a RISC-07.

## 11. Acessibilidade

Meta WCAG 2.2 AA (RNF-01), com testes automáticos e manuais (D-026). O que o design garante:

- regiões nomeadas: navegação principal, conteúdo e avisos;
- ao trocar de tela, o foco vai para o título da nova tela; na correção, vai para o resultado;
- a aba atual é anunciada, não só colorida;
- tudo funciona por toque (RNF-15) e por teclado, sem depender de passar o mouse;
- o cronômetro não fala a cada segundo: avisa com 5 minutos e com 1 minuto restantes;
- com a letra do aparelho em 200%, nada é cortado e os nomes das abas quebram linha em vez de sumir;
- a explicação da revisão abre por botão com estado anunciado;
- imagens seguem as três categorias de EDIT-07 a EDIT-09.

## 12. Rastreabilidade

| Tela | Requisitos |
|---|---|
| Início | TREINO-04, TREINO-05, SIM-03, REP-03 |
| Praticar | CAT-01 a CAT-04, TREINO-01, SIM-01, SIM-09 |
| Questão e correção no treino | TREINO-02, TREINO-03, CONT-02, CONT-04, CONT-11, CONT-12, CONT-25 a CONT-29, REV-03, REP-01, RISC-01 a RISC-07, EDIT-10, RNF-13, RNF-19 |
| Simulado em andamento, mapa e pausa | SIM-02 a SIM-08, RISC-01 a RISC-07, RNF-06, RNF-07, M-11, M-32 |
| Estante | REV-01 a REV-07, SIM-05, SIM-08, DES-05, CONT-07, CONT-10, CONT-19, CONT-24, FLUXO-15, FLUXO-16 |
| Desempenho | DES-01 a DES-13, CONT-05 |
| Conta | CONTA-05, CONTA-07, CONTA-09 a CONTA-12, CONTA-18, CONTA-24, CONTA-25, REP-03 |
| Fora da conta | CONTA-01 a CONTA-06, CONTA-08, CONTA-09, CONTA-14 |
| Painel do editor | EDIT-01 a EDIT-13, FLUXO-01 a FLUXO-17, REP-01, REP-02, CONTA-02, CONTA-16, CONTA-17 |
| Todas as telas do estudante | RNF-01 a RNF-04, RNF-14, RNF-15 |

## 13. Em aberto

| Questão | Para onde vai |
|---|---|
| Quando um treino termina | Spec de TREINO |
| Limite de pausas, se pausar exige conexão, quantidade máxima de questões, respostas que chegam depois do prazo (M-32) e questão bloqueada no meio de um simulado (M-33) | Spec de SIM |
| Recorte de tempo do desempenho, regra da visão só de treino e aviso quando uma reclassificação muda o desempenho (M-05) | Spec de DES |
| Mostrar o nome do autor nas questões de autoria própria | Autorização escrita dos autores (D-019) e Etapa 6 |
| Como mostrar a revisão médica, quando existir | D-003 |
| Que dados aparecem no histórico de uma questão retirada por licenciamento | Etapa 6, com a consulta jurídica (D-002) |
| Refinamento do nome escrito e do ícone por um designer | Quando houver designer; não muda a ideia de D-028 |

## Histórico

- 2026-11-24: documento criado no fechamento da Etapa 5, com autorização do usuário ("Aprovar Etapa 5").
