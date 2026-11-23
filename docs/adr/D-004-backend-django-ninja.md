# D-004: Backend: Django com Django Ninja

- **Status**: Aprovada
- **Data**: 2026-11-23
- **Aprovação**: "Django + Django Ninja" (2026-11-23); registro autorizado com "Autorizo como está" (2026-11-23)
- **Relacionadas**: D-005, D-006, D-007, D-020

## Contexto

- A arquitetura tem uma API em Python consumida por um frontend React (D-020).
- O catálogo exige, entre outros:
  - contas criadas por convite e sessões de 30 dias (CONTA);
  - permissões com bloqueio por padrão (CONTA-20, CONTA-21);
  - histórico, versões e trilha de auditoria (FLUXO, CONT);
  - recálculos consistentes quando o gabarito muda (CONT-09, CONT-15, REV-05);
  - exportação e exclusão de conta (CONTA-10, CONTA-11).
- O usuário pediu a melhor escolha para o caso de uso, sem se prender ao que já sabe: "Se eu não souber, eu aprendo."
- Fatos conferidos nos sites oficiais em 2026-11-23:
  - Django 6.1 é a versão mais recente; a 5.2 LTS tem suporte até abril de 2028, e a 6.2 LTS está prevista para abril de 2027;
  - Django Ninja e Django REST Framework publicaram versões nas semanas anteriores.

## Opções consideradas

### Django com Django Ninja (escolhida)

- Prós: o Django traz prontos e maduros contas, sessões, proteção contra CSRF, senhas com hash forte, permissões, banco com migrações, transações e um painel interno de operação. O Django Ninja dá à API validação tipada (Pydantic) e documentação OpenAPI automática, de onde sai o cliente TypeScript tipado do frontend.
- Contras: dois frameworks para aprender. O Django Ninja depende muito do autor principal; o risco é pequeno, porque é uma camada fina e trocável.
- Custo e complexidade: a completar.

### FastAPI com SQLAlchemy e Alembic

- Prós: API tipada excelente, ecossistema grande, skill disponível no projeto.
- Contras: contas, sessões, CSRF, permissões e painel interno ficam por conta do projeto, o que significa mais código de segurança escrito à mão (Etapa 6).
- Custo e complexidade: a completar.

### Django com Django REST Framework

- Prós: o caminho mais maduro para APIs em Django.
- Contras: mais verboso; a tipagem e o OpenAPI dependem de pacotes extras.
- Custo e complexidade: a completar.

## Decisão

Backend em Python com Django e Django Ninja. A versão exata é fixada no início da implementação, conferida na página oficial de versões suportadas.

## Consequências

- Ganhamos: a segurança de contas e sessões parte de componentes maduros e testados; a API tem contrato tipado e documentado, compartilhado com o frontend.
- Riscos aceitos: aprender dois frameworks; depender do Django Ninja como camada de API.
- Revisitar se: o Django Ninja deixar de ser mantido (troca da camada de API, por exemplo pelo Django REST Framework), ou se a versão escolhida do Django se aproximar do fim do suporte.
