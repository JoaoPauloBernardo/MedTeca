# D-010: Hospedagem: um servidor em São Paulo

- **Status**: Aprovada
- **Data**: 2026-11-23
- **Aprovação**: "Um servidor em SP" (2026-11-23); registro autorizado com "Sim, como descrito" (2026-11-23)
- **Relacionadas**: D-005, D-020, D-022, D-023, D-024, D-025; requisitos RNF-08 a RNF-10, RNF-13, RNF-17 e RNF-20 em `docs/requisitos-mvp.md`

## Contexto

- Orçamento informado enquanto não há receita: R$ 50 a 150 por mês. O usuário quer servidor e dados no Brasil e tem experiência com deploy e infraestrutura.
- A arquitetura é um único serviço com o app e a API (D-020), mais PostgreSQL (D-005) e um processo de tarefas (D-024).
- Requisitos:
  - backup diário guardado por 30 dias, com teste mensal de restauração (RNF-08 a RNF-10);
  - sem meta formal de disponibilidade no beta;
  - meta de desempenho sensível à latência (RNF-13).
- Câmbio usado: PTAX de venda do Banco Central em 19/11/2026, R$ 5,8889. Não houve cotação no dia 20 (feriado) nem no dia 21 (sábado). O orçamento equivale a cerca de US$ 8,50 a 25,50 por mês, antes do IOF.
- Fatos conferidos nas páginas oficiais em 2026-11-23:
  - **AWS Lightsail**: tem a região de São Paulo (sa-east-1). Instâncias de US$ 5 (0,5 GB), US$ 7 (1 GB), US$ 12 (2 GB, 60 GB de SSD) e US$ 24 (4 GB). Em São Paulo, a franquia de transferência é a metade. Armazenamento de objetos a partir de US$ 1 por mês (5 GB). Banco gerenciado de US$ 15 por mês (1 GB, "Sem criptografia de dados") ou de US$ 30 por mês (2 GB, dados criptografados).
  - **Neon**: tem região em São Paulo (aws-sa-east-1). Plano grátis com 1 GB por projeto, 100 horas de computação por mês e suspensão após 5 minutos parado. Plano pago cobrado pelo uso; o próprio Neon cita cerca de US$ 15 por mês para um banco pequeno de uso intermitente.
  - **Fly.io**: tem a região de São Paulo (gru) e banco gerenciado nela, mas "Machine prices vary by region" e o preço de São Paulo não está publicado. Nos EUA, a máquina de 1 GB custa US$ 6,70. O banco gerenciado custa US$ 4 (256 MB) ou US$ 38 (1 GB).
  - **Supabase**: tem São Paulo. O plano pago custa a partir de US$ 25 por mês, e o grátis é pausado após uma semana sem uso.
  - **Railway e Render**: sem região na América do Sul.
  - **Não conferidos**: a Vultr e a Oracle recusaram o acesso; as páginas de preço do Google Cloud vieram vazias; o simulador da Magalu Cloud, que cobra em reais, não carregou; e a Akamai não mostrou o preço de São Paulo.

## Opções consideradas

### Um servidor em São Paulo com tudo dentro (escolhida)

- **Como é**: AWS Lightsail de 2 GB, com app, processo de tarefas e PostgreSQL organizados com Docker Compose, mais armazenamento de objetos em São Paulo para imagens e backups.
- **Prós**: o mais barato e simples; uma máquina; todos os dados no Brasil; preço fixo e previsível; aproveita a experiência do usuário com infraestrutura; o acesso aos logs passa pelo acesso ao servidor (D-025).
- **Contras**: o projeto opera tudo (atualizações do sistema e do PostgreSQL, firewall, chaves de acesso, backups com teste de restauração), o que aumenta a carga de segurança da Etapa 6. Uma máquina só é ponto único de falha, aceitável num beta sem meta de disponibilidade.
- **Custo**: US$ 12 + US$ 1 = US$ 13 por mês, cerca de R$ 77, antes do IOF.

### Servidor para o app e banco gerenciado

- **Prós**: o fornecedor atualiza o banco e faz as cópias; menos operação.
- **Contras**: dois fornecedores para contratar e documentar na LGPD. O plano grátis do Neon desliga o banco após 5 minutos parado. O plano pago cobra pelo uso, então a conta varia. O tempo de guarda dos backups do Neon não foi conferido. Com o banco gerenciado do Lightsail, o plano com criptografia (US$ 30) mais o app passam do orçamento.
- **Custo**: de cerca de R$ 41 (app de 1 GB com o Neon grátis) a cerca de R$ 130 (com o Neon pago).

### Plataforma gerenciada (Fly.io)

- **Prós**: deploy simples, com certificado e reversão de versão prontos.
- **Contras**: o preço de São Paulo não é publicado; o banco gerenciado é pequeno demais ou caro demais; ferramentas próprias do fornecedor.
- **Custo**: indeterminado para São Paulo.

## Decisão

Um servidor AWS Lightsail em São Paulo (2 GB de RAM, 60 GB de SSD), com app, processo de tarefas e PostgreSQL via Docker Compose, mais armazenamento de objetos do Lightsail em São Paulo para imagens (D-022) e backups.

## Consequências

- **Ganhamos**: custo baixo e fixo dentro do orçamento, dados no Brasil e uma topologia simples de entender e de restaurar.
- **Abrimos mão de**: um banco operado pelo fornecedor e de redundância.
- **Exige, na Etapa 6**:
  - atualizações de segurança automáticas;
  - firewall;
  - acesso SSH só com chave individual;
  - backups diários cifrados no armazenamento de objetos, com 30 dias de retenção e teste mensal de restauração;
  - verificar se os discos e o armazenamento de objetos são criptografados em repouso;
  - monitor externo de disponibilidade.
- **Riscos aceitos**: cobrança em dólar, sujeita ao câmbio e ao IOF; ponto único de falha durante o beta.
- **Revisitar se**: a abertura ao público exigir meta de disponibilidade; a operação do servidor pesar demais; os preços mudarem; ou pagar em real se tornar prioridade (cotar a Magalu Cloud).

## Observações do encerramento da Etapa 3 (2026-11-23)

- **Banco autogerenciado**: o PostgreSQL roda no próprio servidor (D-005), e o banco gerenciado do Lightsail não é usado. Não se presume que o banco gerenciado do Lightsail ofereça PostgreSQL 18; se um dia houver migração para ele, a versão disponível é conferida antes.
- **Validação antes do beta**:
  - dimensionamento da instância: memória e CPU do app, do processo de tarefas e do PostgreSQL rodando juntos em 2 GB;
  - custo total, incluindo armazenamento, transferência (em São Paulo a franquia é a metade), backups, e-mail (D-023), impostos (IOF sobre a cobrança em dólar) e domínio.
- **Backup**: o teste mensal de restauração (RNF-10) restaura de fato uma cópia num banco separado e confere os dados e o funcionamento do app (D-026).
