# D-033: Infraestrutura e operação

- **Status**: Aprovada, com ressalvas
- **Data**: 2026-11-24
- **Aprovação**: respostas das três rodadas do bloco 5 (2026-11-24); versão final aprovada com "Aprovo o Bloco 5 — Infraestrutura e Operação — conforme a proposta apresentada, incluindo as decisões P5-01 a P5-25, com as ressalvas e condições abaixo." (2026-11-24)
- **Muda**: o mecanismo da credencial de envio de registros de P4-15 (D-032); o trecho de D-010 sobre os backups
- **Completa**: D-005, D-022 e D-027
- **Relacionadas**: D-004, D-010, D-020, D-023, D-024, D-026, D-032; RNF-08 a RNF-11, RNF-24, RNF-45 e RNF-46 a RNF-69 em `docs/requisitos-mvp.md`; decisões P5-01 a P5-25, verificações V1 a V34 e a questão Jur-24 em `docs/seguranca-e-privacidade.md`, seção 5

## Contexto

- **Decisões anteriores:**
  - um servidor Lightsail de 2 GB em São Paulo com Docker Compose (D-010);
  - PostgreSQL no próprio servidor (D-005);
  - imagens no armazenamento de objetos do Lightsail (D-022);
  - CI no GitHub Actions, com o deploy automático deixado para a Etapa 6 (D-027);
  - registros também no CloudWatch (D-032).
- **Requisitos:** backup diário guardado por 30 dias, com teste mensal de restauração (RNF-08 a RNF-10); HTTPS obrigatório (RNF-11).
- **Meta:** OWASP ASVS 5.0 no nível L2. Os requisitos que mais pesaram:
  - 13.2.1: componentes se autenticam com contas individuais, credenciais temporárias ou certificados, e não com credenciais fixas;
  - 13.3.1: os segredos ficam numa solução própria de gestão;
  - 12.3.1: as conexões, inclusive com o banco, são cifradas;
  - 3.4.x: cabeçalhos de segurança;
  - 11.1.1 e 11.1.2: política de chaves e inventário criptográfico.
- **Restrições do usuário:** dados no Brasil; orçamento de R$ 50 a 150 por mês; operação feita por uma pessoa; o estudante não deve perceber as atualizações.

## Opções consideradas

| Tema | Escolhida | Outras opções apresentadas |
|---|---|---|
| Acesso do servidor à AWS | Certificado trocado por credenciais temporárias (IAM Roles Anywhere) | Chave de acesso fixa restrita ao IP do servidor, como na P4-15, com exceção ao ASVS 13.2.1 |
| Segredos | AWS Systems Manager Parameter Store | Arquivos protegidos no servidor, com exceção ao ASVS 13.3.1; AWS Secrets Manager, a US$ 0,40 por segredo por mês |
| Backups | S3 em São Paulo, cifrado e travado por 30 dias | Bucket do Lightsail com versões, que o servidor invadido poderia apagar; snapshots do Lightsail, guardados só 7 dias e com os registros dentro |
| Montagem | Infraestrutura como código (OpenTofu) | Scripts e passo a passo; console com documento |
| Domínio | .com.br no Registro.br | .com internacional; .app; um domínio já existente |
| SSH | Porta fechada, aberta sob demanda | Só pelo terminal do console da AWS; SSH aberto só com chave |
| Deploy | Por um comando do usuário | Automático com aprovação no GitHub, que no plano gratuito exige repositório público e uma chave guardada no GitHub; o servidor se atualizar sozinho |
| Ambiente de teste | Criado e apagado sob demanda | Permanente, por mais US$ 12 por mês; só no computador do usuário, levando dados reais para fora da AWS |
| Monitor externo | Route 53 da AWS | UptimeRobot gratuito |
| Atualizações do sistema | Automáticas, com reinício às 4h | Automáticas com reinício manual; tudo manual, toda semana |
| Versão nova | Sem queda para o estudante | Com página de manutenção |
| Conexão com o banco | Socket local, sem senha (peer) | TLS com certificados; senha pela rede interna, com exceções ao ASVS |

## Decisão

- O detalhamento está em `docs/seguranca-e-privacidade.md`, seção 5, com as decisões P5-01 a P5-25 e as correções e mudanças da seção B.
- **Servidor:** Lightsail de 2 GB em São Paulo, aprovado inicialmente.
- **Disco:** um disco adicional cifrado de 16 GB guarda os dados do banco, as chaves e o espaço reservado dos registros críticos.
- **Banco:** PostgreSQL sem porta de rede, com autenticação `peer`.
- **AWS e segredos:** acesso à AWS por IAM Roles Anywhere, com autoridade própria e um certificado por componente; segredos no Parameter Store.
- **Backups:** cifrados no S3 em São Paulo, com Object Lock em modo compliance por 30 dias.
- **Imagens:** versionamento no bucket e cópia semanal travada.
- **Restauração:** teste mensal em ambiente sob demanda, com reaplicação das exclusões de conta.
- **Domínio, HTTPS e cabeçalhos:** .com.br com DNSSEC; Caddy com HTTPS automático, TLS 1.2 e 1.3 e os cabeçalhos de segurança.
- **SSH:** porta aberta sob demanda e terminal pelo navegador desligado por padrão.
- **Deploy:** por comando do usuário, sem queda, com a imagem do CI publicada no ECR via OIDC.
- **Ambiente de teste:** sem e-mail e com segredos próprios.
- **Monitoramento:** Route 53 por HTTPS; trilha do CloudTrail por 180 dias; os alertas novos do bloco 5.
- **Conformidade:** sem declaração de conformidade com o ASVS.

## Ressalvas da aprovação

1. **Memória e orçamento.**
   - A configuração de 2 GB fica aprovada inicialmente. O consumo de 1,3 a 1,7 GB é uma inferência, não uma medição.
   - A V28 comprova o consumo real durante a operação, inclusive durante o deploy sem queda.
   - Não há aumento automático para o plano de 4 GB. Se os 2 GB forem insuficientes, o consultor apresenta os resultados, o impacto financeiro e as alternativas para a decisão do usuário, considerando que o plano de 4 GB pode ultrapassar o orçamento de R$ 50 a 150.
2. **Cifragem do disco.**
   - O disco adicional cifrado de 16 GB está aprovado.
   - A falta de cifragem no disco do sistema não é um fato confirmado: a documentação disponível não foi conclusiva, e a V24 segue pendente.
   - A separação dos dados é justificativa própria do disco adicional.
3. **Backups e LGPD.**
   - A política com Object Lock em modo compliance, 30 dias de retenção e cifragem está aprovada conceitualmente.
   - Os dados de contas excluídas podem ficar nos backups durante esse prazo, com a exclusão reaplicada na restauração.
   - A Jur-24 segue pendente e não se considera resolvida só por constar na política de privacidade.
   - O uso de dados reais no teste mensal de restauração fica documentado para análise jurídica.

## Consequências

- **Ganhamos:**
  - nenhuma chave permanente da AWS no servidor;
  - segredos fora do disco e da imagem;
  - backups que nem um servidor invadido nem a conta raiz apagam antes do prazo;
  - banco sem exposição de rede;
  - infraestrutura reproduzível e conferível;
  - atualizações sem queda para o estudante.
- **Abrimos mão de:**
  - simplicidade: há uma autoridade de certificados, um certificado por componente, migrações em duas fases e mais alarmes;
  - parte do orçamento: a estimativa sobe de cerca de R$ 77 para R$ 104 a 135 por mês, perto do teto.
- **Exige:**
  - as verificações V1 a V34, nenhuma concluída;
  - uma prova por critério (D-026);
  - a resposta jurídica à Jur-24;
  - a renovação anual dos certificados com a chave da autoridade, que fica com o usuário;
  - a guarda segura da chave privada dos backups.
- **Inconsistências com blocos anteriores:** quatro ficaram registradas para avaliação do usuário, sem resolução unilateral (seção 5.P do documento de segurança).
- **Revisitar se:**
  - a V28 mostrar memória insuficiente;
  - a V24 confirmar a situação do disco do sistema;
  - a V4 mostrar que o Lightsail oferece papel de instância;
  - o custo real (V12, V29) sair do orçamento;
  - a Jur-24 indicar outra regra para os backups.

## Atualização da Etapa 6, bloco 6 (2026-11-24)

Conforme D-034 (`docs/seguranca-e-privacidade.md`, seções 5.4 e 6):

- **Autorizações recorrentes.** As rotinas automáticas desta decisão continuam valendo, dentro dos parâmetros aprovados: atualizações de segurança com reinício às 04:00, backup diário, cópia semanal das imagens, renovação do certificado TLS, verificação diária do certificado, monitor externo, trilha do CloudTrail, retenção no ECR e publicação da imagem pelo CI depois do merge. As cinco regras do usuário (2026-11-24):
  1. uma rotina automática aprovada pode continuar executando dentro dos parâmetros, horários, escopo e limites originalmente aprovados;
  2. qualquer alteração relevante na frequência, horário, escopo, permissões, retenção ou comportamento exige aprovação prévia do usuário;
  3. uma operação automatizada que não esteja nas políticas aprovadas exige autorização específica;
  4. deploy, volta da versão em produção, restauração de dados, alterações de infraestrutura, segredos, IAM e as demais operações sensíveis dependem de autorização explícita a cada operação;
  5. o usuário pode suspender ou revogar uma autorização recorrente a qualquer momento.
- **Deploy e volta de versão.** O "administrador" que roda o deploy é o usuário. Volta de código (pull request de reversão, com merge do usuário), volta da versão em produção (o comando de deploy com o digest anterior) e restauração de dados são operações distintas; as duas últimas só acontecem com autorização explícita do usuário para aquela operação.
- **Operações periódicas manuais.** O teste mensal de restauração, a troca anual de chaves e a renovação anual dos certificados dos componentes mantêm a frequência aprovada, e cada execução depende de autorização explícita do usuário.
- **Retenção no ECR.** Passa a manter a versão em produção e as duas anteriores que estiveram em produção, além das 10 imagens mais recentes da `main`, sem regra genérica para imagens sem etiqueta. Isso substitui o trecho da P5-16 sobre as 10 imagens.
- **Custo.** A franquia de 500 MB do ECR citada na estimativa só vale para contas criadas antes de 15/07/2025 (V51).

## Atualização das resoluções da seção 5.P (2026-11-25)

As quatro inconsistências com blocos anteriores, que ficaram registradas para avaliação, foram resolvidas pelo usuário ("Aprovar", 2026-11-25). Detalhes em `docs/seguranca-e-privacidade.md`, seção 5.P:

1. **Fonte das exclusões.** Os eventos do grupo `seguranca` são a fonte única. A restauração reprocessa, de forma idempotente, todo pedido de exclusão cujo evento não está visível no snapshot do banco usado pelo backup, e bloqueia o uso se houver lacuna (RNF-92 a RNF-94, V55).
2. **Preservação de evidências.** Snapshot de preservação para investigação só com autorização do usuário e cifragem provada para o tipo exato de snapshot; o da instância inteira só depois de provada a cifragem de todos os componentes; acesso restrito às identidades administrativas do usuário (RNF-89, V53).
3. **Emergência.** O terminal pelo navegador é a alternativa à chave SSH perdida. O alerta depende de entrega de melhor esforço e não substitui a trilha do CloudTrail (V54). O prazo de 7 dias para a revisão segue como proposta não aprovada.
4. **Logs operacionais.** Ficam no disco adicional cifrado, com limite técnico (RNF-91, V52).
