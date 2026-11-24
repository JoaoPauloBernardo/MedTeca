# D-006: Frontend: React com TypeScript e React Aria Components

- **Status**: Aprovada
- **Data**: 2026-11-23
- **Aprovação**: "React + TypeScript + React Aria" (2026-11-23); registro autorizado com "Autorizo como está" (2026-11-23)
- **Relacionadas**: D-001, D-004, D-014, D-020; requisitos RNF-01, RNF-03, RNF-04, RNF-13 a RNF-15 em `docs/requisitos-mvp.md`

## Contexto

- A arquitetura tem um frontend React que conversa com a API em Python (D-020).
- Prioridade máxima à experiência e à beleza da interface, com o iOS como referência. O frontend e o design são responsabilidade do Claude, com revisão e aprovação do usuário.
- Requisitos que pesam aqui:
  - acessibilidade WCAG 2.2 AA (RNF-01);
  - Safari no iOS e no iPadOS entre os navegadores prioritários (RNF-03);
  - funcionamento por toque, sem depender de passar o cursor (RNF-15);
  - o app nativo ficou fora do MVP (D-001).
- Fatos conferidos no site oficial do React Aria em 2026-11-23: a biblioteca não traz estilos ("style-free out of the box"), trata a acessibilidade como prioridade, cobre mouse, toque, teclado e leitor de tela, e segue as práticas de autoria ARIA da W3C.

## Opções consideradas

### React com TypeScript (Vite) e React Aria Components (escolhida)

- Prós: o maior ecossistema; o React Aria cuida do comportamento acessível sem impor visual, então o design é todo do projeto, sem cara de template; TypeScript com tipos gerados da API (D-004); pode virar PWA (instalável na tela inicial do iPhone e do iPad) e serve de base para um eventual React Native.
- Contras: mais peças para combinar (rotas, dados, estilos); exige disciplina de desempenho no celular.
- Custo e complexidade: a completar.

### SvelteKit

- Prós: muito leve e rápido, com código enxuto.
- Contras: ecossistema menor e menos bibliotecas maduras de componentes acessíveis.
- Custo e complexidade: a completar.

### Next.js

- Prós: renderização no servidor e melhor posicionamento em buscadores.
- Contras: mais um runtime para hospedar no Brasil e complexidade de cache sem ganho real num app atrás de login.
- Custo e complexidade: a completar.

## Decisão

Frontend em React com TypeScript, construído com Vite, usando React Aria Components para o comportamento acessível dos componentes. Estilos, componentes visuais e animações são definidos na Etapa 5.

## Consequências

- Ganhamos: design próprio com comportamento acessível já resolvido, tipos compartilhados com a API e caminho aberto para PWA.
- Riscos aceitos: mais peças para combinar; o desempenho no celular precisa de atenção constante (RNF-13).
- Exige: a Etapa 5 define a identidade visual, os componentes e as animações. O Claude implementa, e o usuário revisa e aprova.
- Revisitar se: um app nativo entrar no MVP, ou se páginas públicas precisarem de renderização no servidor para buscadores.

## Observações do encerramento da Etapa 3 (2026-11-23)

- O React Aria Components oferece componentes sem estilos visuais prontos. O sistema visual e os estilos próprios do MedTeca (cores, tipografia, espaçamento, componentes visuais e animações) são construídos pelo projeto, na Etapa 5.

## Atualização da Etapa 6, bloco 6 (2026-11-24)

Conforme D-034: a revisão do usuário inclui ler e revisar o código de todos os pull requests, não só conferir telas. O Claude implementa, testa, documenta e explica as decisões técnicas; o usuário estuda o código, questiona, revisa e decide o merge, que é sempre manual.
