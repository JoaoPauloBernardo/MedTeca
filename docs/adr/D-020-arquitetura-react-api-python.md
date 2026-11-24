# D-020: Estilo de arquitetura

- **Status**: Aprovada
- **Data**: 2026-11-23
- **Aprovação**: "React + API Python" (2026-11-23); registro autorizado com "Autorizo como está" (2026-11-23)
- **Relacionadas**: D-001, D-004, D-006, D-010, D-014, D-021; requisitos RNF-01, RNF-07, RNF-13 e RNF-14 em `docs/requisitos-mvp.md`

## Contexto

- Prioridade máxima do usuário: experiência de uso e design. Nas palavras dele: "Se a aplicação não for BONITA esteticamente e tiver funcionalidade intuitiva ninguém vai usar." A referência de qualidade citada é o iOS.
- O projeto não tem prazo (D-021). Frontend e design são responsabilidade do Claude, com revisão do usuário. O servidor fica no Brasil.
- Requisitos que pesam na arquitetura:
  - a próxima questão aparece em até 1 s no p75, num perfil de rede em que cada requisição custa cerca de 0,56 s (RNF-13). Por isso ela precisa já estar no aparelho antes do toque;
  - as respostas do simulado ficam guardadas se a conexão cair (RNF-07);
  - o estado da tela se mantém ao girar o aparelho (RNF-14);
  - acessibilidade WCAG 2.2 AA (RNF-01).
- A hipótese inicial do consultor, páginas montadas no servidor com pouco JavaScript, supunha prazo curto e ausência de quem fizesse o frontend. As duas condições deixaram de valer.

## Opções consideradas

### Frontend React que conversa com uma API em Python, servidos juntos (escolhida)

- Prós: fluidez de app; a próxima questão é carregada antes do toque; o aparelho guarda o estado e as respostas quando a conexão cai; um só deploy, no mesmo endereço, sem complicações entre domínios.
- Contras: dois projetos no código (Python e TypeScript); primeira carga maior, o que se mitiga dividindo o código; mais testes.
- Custo e complexidade: hospedagem igual à da opção seguinte, por ser um único serviço; mais código, com o frontend feito pelo Claude e revisado pelo usuário.

### Páginas montadas no servidor, com htmx

- Prós: um projeto só, pouco JavaScript, rápido de construir.
- Contras: fluidez de app e componentes acessíveis complexos viram trabalho artesanal; o estado guardado no aparelho (RNF-07) fica improvisado.
- Custo e complexidade: a completar.

### Tudo em TypeScript, com Next.js

- Prós: um só ecossistema.
- Contras: abandona a preferência por Python e o ponto forte do usuário; a renderização no servidor traz complexidade que um app atrás de login quase não aproveita.
- Custo e complexidade: a completar.

## Decisão

Frontend React que conversa com uma API em Python. No deploy, um único serviço entrega o app e a API no mesmo endereço.

## Consequências

- Ganhamos: fluidez de app, pré-carregamento da próxima questão e estado guardado no aparelho, com um só deploy.
- Abrimos mão de: ter um só projeto e uma só linguagem. A primeira carga é maior.
- Exige: um contrato de API tipado entre os dois projetos (OpenAPI, D-004) e testes dos dois lados.
- Revisitar se: o Python deixar de ser preferido; um app nativo entrar no MVP, o que contradiz D-001; ou páginas públicas precisarem de bom posicionamento em buscadores, o que se resolve com uma página inicial estática, sem mudar o núcleo.

## Atualização da Etapa 6, bloco 6 (2026-11-24)

Conforme D-034: "revisão do usuário" inclui ler e revisar o código de todos os pull requests. O frontend é feito pelo Claude e revisado pelo usuário também no código, com o merge sempre manual, feito por ele.
