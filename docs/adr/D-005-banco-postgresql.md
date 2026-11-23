# D-005: Banco de dados: PostgreSQL

- **Status**: Aprovada
- **Data**: 2026-11-23
- **Aprovação**: "PostgreSQL" (2026-11-23); registro autorizado com "Sim, com ADR" (2026-11-23)
- **Relacionadas**: D-004, D-008, D-010, D-020

## Contexto

- O backend é Django (D-004). O catálogo exige integridade do conteúdo:
  - versões e histórico (FLUXO-04, FLUXO-08);
  - três camadas do gabarito (CONT-13, CONT-14, CONT-18);
  - recálculos consistentes (CONT-09, CONT-15, REV-05);
  - backup diário guardado por 30 dias (RNF-08, RNF-09).
- PostgreSQL era a preferência inicial do usuário, que tem experiência com SQL e PostgreSQL.
- Fatos conferidos nos sites oficiais em 2026-11-23:
  - no Django, as migrações rodam numa única transação no PostgreSQL e no SQLite, e sem transação no MySQL e no Oracle;
  - a documentação de migrações do Django diz que o PostgreSQL é "the most capable" em suporte a esquema;
  - o Django 6.1 aceita PostgreSQL a partir da versão 15;
  - o PostgreSQL 19 foi lançado em 19/11/2026, e a versão 18 tem suporte até novembro de 2030.

## Opções consideradas

### PostgreSQL (escolhida)

- Prós:
  - integridade forte, com restrições e transações;
  - migrações dentro de transação: se falharem, nada fica pela metade;
  - permite regras que impedem estados inválidos;
  - busca de texto em português para quando a busca entrar;
  - campos JSON quando forem úteis;
  - ampla oferta de banco gerenciado;
  - experiência do usuário e skill de boas práticas disponível.
- Contras: é um serviço a mais para operar ou contratar.
- Custo e complexidade: o custo é avaliado com a hospedagem (D-010).

### SQLite

- Prós: nenhuma operação; um único arquivo; muito barato.
- Contras: uma escrita por vez; backup contínuo exige ferramenta extra; a hospedagem precisa de disco persistente; migrar depois para PostgreSQL custa uma migração de dados.
- Custo e complexidade: a completar.

### MySQL ou MariaDB

- Prós: maduro e popular.
- Contras: migrações sem transação; menos recursos de esquema; nenhuma vantagem para este caso.
- Custo e complexidade: a completar.

## Decisão

PostgreSQL, começando na versão 18. A versão exata é fixada na implementação, conforme o que o provedor oferecer.

## Consequências

- Ganhamos: as regras de integridade do conteúdo podem ser garantidas também no banco, não só no código, e as migrações são seguras.
- Exige: escolher na Etapa 3 entre banco gerenciado e banco operado por nós (D-010), cumprindo o backup de RNF-08 e RNF-09.
- Revisitar se: o provedor escolhido não oferecer a versão 18, ou quando for hora de atualizar para a 19.

## Observações do encerramento da Etapa 3 (2026-11-23)

- **Versão**: o projeto mantém o PostgreSQL 18 por enquanto. O PostgreSQL 19 foi lançado em 19/11/2026, e a 18 foi escolhida por maturidade e compatibilidade.
- **Operação**: o banco é autogerenciado, em contêiner no servidor de D-010. O banco gerenciado do Lightsail não é usado. Isso resolve o item "Exige" acima. Se um dia houver migração para um banco gerenciado, conferir antes se ele oferece a versão em uso.
