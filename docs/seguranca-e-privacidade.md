# Segurança e privacidade: MedTeca

**Situação**: Etapa 6 em andamento. Bloco 4 (registros e monitoramento) aprovado e registrado.

**Aprovado (bloco 4)**: 2026-11-24 - usuário: "Aprovo integralmente o Bloco 4 — Registros e Monitoramento, na versão revisada apresentada."

Documento da Etapa 6 (segurança, LGPD, qualidade e infraestrutura). Reúne, por bloco, as decisões de segurança e privacidade, ligadas aos requisitos de `docs/requisitos-mvp.md` e às decisões de `docs/decisions.md`. Aprovar o que está aqui não autoriza implementação (D-017).

## Blocos da Etapa 6

| Bloco | Tema | Situação |
|---|---|---|
| 1 | Contas e acesso | Aprovado em 2026-11-24 ("Aprovar bloco 1"); registro pendente |
| 2 | Permissões e privacidade | Aprovado em 2026-11-24 ("Aprovar bloco 2"); registro pendente |
| 3 | LGPD (D-009) | Aprovado em 2026-11-24 ("Aprovar bloco 3"); registro pendente |
| 4 | Registros e monitoramento | Aprovado e registrado em 2026-11-24 (D-032); seção 4 |
| 5 | Infraestrutura e operação | Não iniciado; recebe as verificações V1 a V21 |
| 6 | Qualidade | Não iniciado |

O bloco 4 cita decisões dos blocos 1 a 3 que já foram aprovadas mas ainda não estão registradas: o cookie de aparelho confiável, os limites de tentativas, a tabela de tokens, a tabela B.12 (destino de cada registro na exclusão da conta), a revisão semestral de privilégios e o procedimento de emergência do único administrador. Elas entram neste documento quando o registro desses blocos for autorizado.

## Convenções

- **Doc**: confirmado em documentação oficial, conferida em 2026-11-24 (fontes na seção 4.N).
- **Inferência**: conclusão técnica do consultor, sem confirmação em documentação.
- **Testar**: só uma prova na implementação confirma.
- **V-n**: verificação reservada ao bloco 5 (seção 4.L).
- **Jur-n**: questão para o advogado (seção 4.M). A análise jurídica deste documento é preliminar.

## 4. Registros e monitoramento (bloco 4, D-032)

### 4.1 Como o bloco foi decidido

- **Escolhas do usuário (2026-11-24):**
  - "AWS CloudWatch em São Paulo (Recomendado)";
  - "6 meses, com IP completo (Recomendado)";
  - "Sem serviço externo (Recomendado)".
- **Revisão:** três rodadas de revisão externa, trazidas pelo usuário em 2026-11-24, corrigiram a proposta. Os pontos tratados foram imutabilidade e ASVS, IP e Marco Civil, cópia local e fila, erros do navegador, CloudTrail, credencial no Lightsail, custos, perda por categoria, confirmação de envio, sinais de vida, PostgreSQL, IP real, uso de sessão, token no fragmento, auditoria, contingência, disco, HMAC e alertas.
- **Aprovação da versão final:** "Aprovo integralmente o Bloco 4 — Registros e Monitoramento, na versão revisada apresentada." (2026-11-24).

### 4.2 Decisões aprovadas

| ID | Decisão | Seção |
|---|---|---|
| P4-01 | Classificação dentro do RNF-18 e os quatro grupos | B |
| P4-02 | Lista de eventos, com perdas e lacunas como eventos de segurança | C.1 |
| P4-03 | Três caminhos por categoria, com falha fechada nas operações de autenticação | H.2 |
| P4-04 | Espaço reservado de 2 GB para os eventos críticos e prioridades de disco | H.3 |
| P4-05 | Regras de envio e confirmação, sem promessa de entrega exatamente uma vez | H.4 |
| P4-06 | Sem cópia de contingência; críticos não enviados guardados no espaço reservado | H.5 |
| P4-07 | Sinais de vida independentes e dado ausente tratado como falha | F.2 |
| P4-08 | Parâmetros de log do PostgreSQL | D.6 |
| P4-09 | IP real atrás do proxy e prefixo /64 nos limites do IPv6 | D.5 |
| P4-10 | Registro de uso de sessão com regra exata, condicionado ao Jur-19 | C.3 |
| P4-11 | Tokens dos links de e-mail no fragmento, com sete proteções | D.4 |
| P4-12 | Auditoria de ações sensíveis no banco: papéis, leitura pelo servidor, mesma transação | C.2 |
| P4-13 | Regras do HMAC de e-mails sem conta | D.3 |
| P4-14 | Alertas como sinal de risco; relatos do navegador só com alerta de volume | F.1 |
| P4-15 | Identidades da AWS, proteção contra exclusão e restrição por IP | E.2, E.3 |
| P4-16 | Endpoint de erros do navegador | G.2 |
| P4-17 | Mensagem de erro genérica com código, "não encontrado", DEBUG e e-mail de erro do Django desligados | G.1 |
| P4-18 | Backups e cópias de disco sem os registros | H.6 |
| P4-19 | Sem declaração de conformidade com o ASVS até haver provas; riscos residuais listados | E.5 |
| P4-20 | D-025 substituída por D-032, com ADR, preservando o monitor externo de disponibilidade | A |

### A. Escolhas

- **Escolhido:** os registros vão também ao AWS CloudWatch Logs em São Paulo, com alertas que não dependem do servidor. Isso substitui a D-025, e o monitor externo de disponibilidade que ela previa continua obrigatório.
- **Escolhido:** registros de segurança por 6 meses (180 dias), com IP completo.
- **Escolhido:** registros de aplicação por 30 dias, sem IP.
- **Escolhido:** o Sentry fica fora do MVP.
- A situação no ASVS está em E.5. Não há declaração de conformidade.

### B. Inventário (ASVS 16.1.1 e 16.2.3)

O app só escreve nos destinos desta seção.

**B.1 Fontes e destinos**

| Fonte | Destino |
|---|---|
| App: eventos críticos de acesso e de segurança, gravados no arquivo próprio (H.2) | `acesso`, `seguranca` |
| App: auditoria de ações sensíveis, exportada do banco (C.2) | banco e `seguranca` |
| App: requisições, erros, tarefas e erros do navegador saneados | `aplicacao` |
| Proxy: requisições e erros, sem IP, query string ou fragmento (V13) | `aplicacao` |
| SSH, sudo e autenticação do sistema | `servidor` |
| Docker, serviços do sistema, PostgreSQL (D.6), enviadores e tarefa de backup | `aplicacao` |
| Batimento do servidor (F.2) | `servidor` |
| CloudTrail | AWS (E.4) |

**B.2 Categorias, dentro do RNF-18**

| Categoria do RNF-18 | Onde fica | Tem IP? | Prazo |
|---|---|---|---|
| Registros de segurança | grupos `medteca/acesso`, `medteca/seguranca` e `medteca/servidor`, mais a auditoria de ações sensíveis no banco | sim, exceto a auditoria | 180 dias |
| Logs de aplicação | grupo `medteca/aplicacao` | não | 30 dias |
| Trilha de auditoria editorial | banco (M-23) | não | permanente |

A exclusão efetiva no CloudWatch acontece em até cerca de 72 h depois do prazo (H.6).

**B.3 Outros registros**

| Registro | Onde | Prazo |
|---|---|---|
| Cópias locais | servidor | H.3 |
| Histórico do CloudTrail | AWS | 90 dias, só eventos de gerenciamento (E.4) |
| Registro de incidentes | documento privado | 5 anos (Res. CD/ANPD 15/2024, art. 10) |

### C. Eventos

**C.1 Eventos registrados (16.3.1 a 16.3.4)**

- **`acesso`:**
  - entrada com sucesso, que é o início da sessão, com o fator usado (senha, passkey ou TOTP) e se o aparelho é confiável;
  - uso de sessão (C.3);
  - saída e encerramento de sessões (uma ou todas, inclusive por troca ou recuperação de senha);
  - reautenticação.
- **`seguranca`:**
  - **Autenticação:** entrada com falha e o motivo; bloqueio por limite; estado de ataque espalhado; troca e recuperação de senha; senha recusada por vazamento, com a camada que recusou.
  - **Fatores e conta:** passkey ou TOTP cadastrado ou removido; códigos de reserva gerados ou usados; e-mail alterado; conta criada; exportação pedida; exclusão pedida e concluída.
  - **Autorização (16.3.2 e 16.3.3):** acesso negado, com rota, tipo e identificador do recurso, papel e motivo; falha de CSRF ou de Origin; limite de requisições atingido.
  - **Poderes e consultas sensíveis:** vão além do L2, por decisão do bloco 2, e também ficam na auditoria de C.2. São eles: papel concedido, removido ou suspenso, inclusive de forma automática; concessão sensível usada ou expirada; consulta ao autor de um reporte; consulta a estudo individual a pedido do estudante; consulta à correspondência entre código e nome; procedimento de emergência; consulta à auditoria.
  - **Falhas de controle (16.3.4):** Pwned Passwords fora do ar; falha de envio pelo SES; falha no armazenamento de objetos; falha da fila; falha de backup.
  - **Integridade dos próprios registros:** `registros.descartados`, `registros.lacuna`, `registros.rejeitados` e `registros.falha_de_escrita`. Este último é gravado quando a gravação volta a funcionar.
- **`servidor`:** entradas por SSH, uso de sudo, autenticação do sistema e batimento do servidor.

**C.2 Auditoria de ações sensíveis no banco (M-39)**

- **O que entra:**
  - concessões, remoções e suspensões de papel;
  - uso de concessão sensível;
  - consultas ao autor de um reporte, ao estudo individual e à correspondência entre código e nome;
  - o procedimento de emergência;
  - consultas à própria auditoria.
- **O que cada registro guarda:** quem agiu (identificador interno da conta), papel, ação, alvo (tipo e identificador), motivo quando exigido, código da requisição e hora. Não guarda IP: o IP fica em `seguranca`, e os dois se ligam pelo código da requisição.
- **Mesma transação:**
  - numa ação que grava dados, o registro de auditoria entra na mesma transação;
  - efeitos externos, como um e-mail, vão para a fila na mesma transação (V17);
  - numa consulta, o registro é gravado antes, e os dados só são devolvidos se a gravação der certo;
  - no procedimento de emergência, o comando grava um registro antes de agir e outro com o resultado.
- **Papéis no banco (V17):**

| Papel | Pode |
|---|---|
| `medteca_app` | só inserir; se o ORM exigir, também ler o identificador do registro inserido |
| `medteca_exportador` | só ler a auditoria e atualizar a própria posição de exportação |
| `medteca_retencao` | só apagar registros com mais de 180 dias |
| Nenhum papel | alterar registros |
| Dono do esquema | tudo, mas usado só nas migrações, com credencial fora do app em execução (risco residual) |

- **Leitura humana:** só o administrador, por um comando no servidor que exige o motivo e grava o próprio registro. É o mesmo padrão "pelo servidor" do bloco 2. Não existe tela de auditoria no MVP.
- **Uso das concessões sensíveis:** o controle de uso, que serve à expiração após 90 dias sem uso do bloco 3, fica na própria concessão, não na auditoria.

**C.3 Uso de sessão (condicionado ao Jur-19)**

- **Regra:** o sistema grava `sessao.uso` (conta, código da sessão, IP e hora) em dois momentos:
  - na primeira requisição autenticada da sessão em cada dia civil UTC em que ela é usada;
  - na primeira requisição autenticada depois de cada mudança do IP em relação ao último IP registrado para aquela sessão.
- O início da sessão já conta como o primeiro registro do dia.
- **Três tipos de registro:**
  - **acesso:** início, uso e fim de sessão;
  - **segurança:** falhas, negados, limites, mudanças de fator e poderes;
  - **operacional:** requisições, erros e infraestrutura, sem IP.
- Não se conclui que esses registros atendem ao Marco Civil da Internet. A aplicabilidade e a interpretação ficam com o advogado (Jur-18 e Jur-19).

### D. Formato e o que nunca entra

**D.1 Serialização**

- JSON gerado pela biblioteca de registro a partir de campos estruturados, sem montar linhas concatenando texto.
- O escape do serializador é a proteção contra injeção nos registros (16.4.1). O corte em 200 caracteres dos campos vindos do usuário só controla o volume.
- Cada evento leva um `id`; os eventos críticos levam também um `seq` (H.4).
- Hora em UTC, com relógio sincronizado (16.2.2; V10).
- Exemplo com dados fictícios: `{"ts":"2026-11-24T14:03:12.481Z","evento":"auth.login.falha","resultado":"negado","motivo":"senha_incorreta","fator":"senha","conta":"c_7f3a","aparelho":"d_91c2","ip":"203.0.113.7","rota":"POST /api/sessao","req":"7F3A91C2","versao":"a1b2c3d"}`.

**D.2 O que nunca entra (16.2.5, RNF-12 e RNF-16)**

- senhas e códigos (TOTP, reserva e e-mail);
- tokens e cookies, incluindo os links de convite e de recuperação de senha;
- o corpo das requisições;
- as respostas do estudante;
- o que a pessoa digita;
- e-mail e apelido.

O campo `aparelho` é um identificador derivado, nunca o valor do cookie. A rota é registrada só como modelo, sem query string e sem fragmento.

**D.3 HMAC de e-mail sem conta**

- O e-mail digitado nunca é guardado.
- **O que se guarda:** `HMAC-SHA256(chave, e-mail normalizado)`, truncado em 128 bits e com prefixo de versão (por exemplo, `v1:…`).
- **Normalização:** tirar os espaços das pontas, aplicar a forma Unicode NFC e passar tudo para minúsculas, sem remover pontos nem o sufixo "+…".
- **Natureza:** é dado pseudonimizado, não anônimo (LGPD, art. 13, §4º). Quem tem a chave consegue testar e-mails candidatos.
- **Chave:** é um segredo do bloco 5 (V18), guardado fora do banco.
  - A rotação é anual, ou imediata se houver suspeita de vazamento.
  - A chave antiga só é mantida até o último evento que a usa expirar, e então é destruída.
- **Prazo e finalidade:** 180 dias, como `seguranca`, e uso só para detectar tentativas repetidas (Jur-23).

**D.4 Tokens dos links de e-mail no fragmento**

- **Fato do protocolo HTTP:** o fragmento de um endereço não é enviado ao servidor.
- **Vale para:** a recuperação de senha, o convite e qualquer link futuro com token. Isso complementa a tabela de tokens do bloco 1 (resumo SHA-256; 30 minutos na recuperação; 7 dias no convite), que não define o formato do link.
- **As sete proteções:**
  1. A página lê o token e o apaga do endereço com `history.replaceState` antes de montar o React e antes de qualquer registro de erro.
     - **Inferência a testar:** o histórico global do navegador pode guardar o endereço original. O uso único e a validade curta reduzem esse risco.
  2. O token vai ao servidor só no corpo de um POST, com CSRF, e o corpo nunca é registrado (D.2).
  3. O relato de erros do navegador nunca usa `location.href`, só o modelo da rota, e o saneamento remove fragmentos (G.2).
  4. Nenhum script, fonte, análise ou recurso de terceiros, em todo o site.
  5. CSP restrita em todo o app (V21): `script-src 'self'`, sem script embutido, `connect-src 'self'`, `object-src 'none'`, `base-uri 'none'`, `frame-ancestors 'none'` e `form-action 'self'`.
  6. `Referrer-Policy: no-referrer` nas páginas com token.
  7. A página de redefinição não exibe conteúdo vindo de fora, como HTML de questões.
- **Limite:** um XSS em qualquer ponto da mesma origem conseguiria ler o token. A CSP e o escape do React são a defesa.
- **Inferência:** leitores automáticos de links em e-mails, que abrem endereços por GET, não consomem o token, porque o consumo exige POST.

**D.5 IP de origem**

- **Proxy confiável:** um só, o proxy do servidor, que é o único serviço publicado nas portas 80 e 443. A porta do app não é publicada.
- **Cabeçalho:** o proxy sobrescreve o cabeçalho de IP com o endereço da conexão TCP e descarta o que o cliente enviou (V13).
- **No app:** o cabeçalho só é aceito quando a requisição vem do endereço interno do proxy, numa rede do Docker com endereço fixo. Nos demais casos, vale o endereço da conexão.
- **Cabeçalho ausente ou inválido:** o IP fica como "desconhecido", e a requisição cai no limite mais restrito.
- **Mudança futura:** se uma CDN ou um balanceador entrar na frente do servidor, a lista de proxies confiáveis muda por decisão nova.
- **Onde o IP é usado:**
  - nos registros de acesso e de segurança, completo;
  - nos limites de tentativas. No IPv6, os limites contam o prefixo /64, porque um aparelho costuma ter um /64 inteiro (inferência). Isso complementa a contagem "por endereço" do bloco 1.
  - Os logs de aplicação não têm IP.

**D.6 PostgreSQL**

Todos os parâmetros abaixo são definidos de forma explícita, sem confiar no valor padrão.

| Parâmetro | Valor | Motivo |
|---|---|---|
| `log_min_error_statement` | `panic` | Doc: o padrão `ERROR` registra o comando que falhou; `PANIC` desliga esse registro na prática |
| `log_error_verbosity` | `terse` | Doc: omite DETAIL, HINT, QUERY e CONTEXT. Inferência: o DETAIL de um erro de unicidade traz o valor da chave, como um e-mail |
| `log_parameter_max_length_on_error` | `0` | Doc: já é o padrão; fica explícito |
| `log_parameter_max_length` | `0` | Doc: o padrão `-1` registra os parâmetros inteiros quando um comando é registrado |
| `log_statement` | `none` | explícito |
| `log_min_duration_statement` | `-1` | explícito |
| `log_connections` | vazio | explícito |
| `log_disconnections` | `off` | explícito |
| `logging_collector` | `off` | a saída vai pelo stderr ao caminho operacional. Doc: o coletor evita perder mensagens, mas pode bloquear processos sob carga extrema |

- **Resíduo (inferência):** a mensagem principal de alguns erros, como uma conversão inválida, ainda pode conter um valor. A validação no app antes do banco reduz esse risco.
- **Prova:** V14.

### E. Proteção e acesso (16.4.2 e 16.4.3)

**E.1 Três proteções**

| Proteção | Contra o quê | Como | Risco que sobra |
|---|---|---|---|
| Adulteração local | alguém no servidor mexer nos registros antes do envio | envio contínuo (meta de segundos, no máximo poucos minutos); cópia local e espaço reservado legíveis só pelo root e pelo enviador; os contêineres do app não acessam a pasta | quem tem root no servidor pode alterar ou suprimir o que ainda não foi enviado e enviar eventos falsos dali em diante |
| Alteração do que já foi enviado | mudar eventos que já estão no CloudWatch | a credencial de envio só acrescenta; não existe ação para editar ou apagar um evento individual (Doc, via resumo da referência de autorização; V6) | identidades administrativas com permissões amplas continuam sendo um risco |
| Exclusão | apagar grupos ou fluxos, ou encurtar o prazo | proteção contra exclusão ligada nos quatro grupos desde a criação; apagar, mudar o prazo e desligar a proteção só pela identidade administrativa, com MFA; alerta quando isso acontece (F.1) | a identidade administrativa e a conta raiz podem desligar a proteção e apagar; encurtar o prazo apaga eventos em até cerca de 72 h e não é bloqueado pela proteção, pelo que diz a documentação (V1) |

**Alternativa considerada:** exportar o grupo de segurança para um armazenamento com bloqueio de objeto (S3 Object Lock, modo compliance), que impede a exclusão até pela conta raiz durante o prazo. Fica fora do MVP pelo custo e pela complexidade; reavaliar quando o projeto virar empresa.

**E.2 Identidades e ações do IAM**

As linhas da tabela vêm em parte de um resumo da referência de autorização e precisam ser conferidas (V6).

| Identidade | Ações permitidas | Proibidas |
|---|---|---|
| `medteca-envio` (usuário IAM) | `logs:CreateLogStream` e `logs:PutLogEvents` nos quatro grupos; `logs:DescribeLogStreams` só se o enviador exigir | leitura de eventos; `CreateLogGroup`; `Delete*`; `PutRetentionPolicy`; `PutLogGroupDeletionProtection`; filtros; transformações; outros serviços |
| Papel `leitor-de-registros` | `DescribeLogGroups`, `DescribeLogStreams`, `GetLogEvents`, `FilterLogEvents`, `StartQuery`, `GetQueryResults`, `StopQuery` e `GetLogRecord` | escrita; `Unmask`, se houver mascaramento |
| Papel `administrador-de-registros` | `PutRetentionPolicy`, `DeleteRetentionPolicy`, `PutLogGroupDeletionProtection`, `DeleteLogGroup`, `DeleteLogStream`, filtros de métrica e alarmes | nada além disso |
| Conta raiz | tudo | com MFA e fora do uso diário |

- Os dois papéis são assumidos pelo usuário individual do administrador, com MFA (RNF-17).
- **Doc:** a proteção contra exclusão "blocks all deletion operations until it is explicitly disabled", e o exemplo da documentação é apagar o grupo.
- As páginas de `DeleteLogStream` e `PutRetentionPolicy` não citam a proteção. Por isso, considera-se que encurtar o prazo não é bloqueado; se apagar um fluxo é bloqueado fica para V1.

**E.3 Credencial no Lightsail**

- A credencial de envio é um segredo persistente guardado no servidor, e não uma credencial temporária obtida por um perfil de instância. Fontes antigas indicam que o Lightsail não oferece papel de instância (V4).
- O uso da credencial fica restrito ao IP fixo do servidor, por condição da política do IAM (V5).
- Fica para o bloco 5 (V5): armazenamento, permissões no sistema operacional, rotação, revogação e troca sem interromper o envio.

**E.4 CloudTrail**

- **Doc:** o histórico de eventos guarda 90 dias de eventos de gerenciamento por região, sem custo. Não é uma auditoria completa nem permanente.
- **Doc:** eventos de dados vêm desligados por padrão, são pagos e não aparecem no histórico.
- **Doc:** a página da AWS sobre o CloudTrail no CloudWatch Logs lista as consultas entre as ações registráveis, mas não diz se são eventos de gerenciamento ou de dados (V2).

| Camada | Registra | Prazo | Limite |
|---|---|---|---|
| Histórico de gerenciamento do CloudTrail | mudanças na conta da AWS: apagar grupo, mudar prazo, mudar políticas e assumir papel (V2) | 90 dias | não cobre eventos de dados; vale por região |
| Eventos de dados do CloudTrail | operações sobre os dados, quando ligados | conforme a trilha | desligados e pagos; a cobertura das consultas ao CloudWatch Logs precisa ser conferida |
| Registros do próprio app (C) | ações dentro do MedTeca, inclusive consultas sensíveis | 180 dias, no CloudWatch ou no banco | não veem o que acontece no console da AWS |

- **Atendimento do RNF-20** (quem acessou os logs e quando):
  - a entrada individual no papel de leitor, registrada no histórico do CloudTrail (V2);
  - as entradas por SSH, registradas em `servidor`;
  - a leitura da auditoria pelo servidor, com registro próprio.
- Se V2 mostrar que a entrada no papel não fica registrada, a lacuna volta como decisão.
- **Opção para o bloco 5 (V16):** uma trilha do CloudTrail que guarde os eventos de gerenciamento por mais de 90 dias. Pela documentação, uma cópia desses eventos não tem custo de CloudTrail, só o do armazenamento.

**E.5 Situação no ASVS**

- **16.4.2 e 16.4.3:** atendimento proposto, condicionado à arquitetura final, às verificações V1, V2, V6 e V7 e a uma prova por item (D-026). Ainda não há evidência, e não há declaração de conformidade.
- **Riscos residuais que podem virar exceção:**
  - uma janela de até cerca de 1 s de eventos críticos que se perdem numa queda do servidor, porque a gravação em disco é forçada a cada segundo, e não a cada evento (inferência; testar);
  - adulteração local por quem tem root, antes do envio;
  - identidades administrativas e a conta raiz da AWS.
- **Perda de eventos operacionais:** é aceita por desenho e não é exceção, porque eles não são registros de segurança.
- Não se declara ausência de exceções.

### F. Alertas

**F.1 Alertas por e-mail**

O caminho é: alarme do CloudWatch, depois SNS, depois o e-mail do administrador. Funciona com o servidor fora do ar, e os e-mails não levam dados pessoais, só o nome do alarme e números.

| # | Alerta | Observação |
|---|---|---|
| 1 | Ataque espalhado | o estado de ataque do bloco 1 foi ligado |
| 2 | Sinal de risco: equipe entrou sem aparelho reconhecido | o e-mail diz que não é confirmação de invasão e pede que o administrador confirme se foi ele; se não foi, segue o plano de incidentes |
| 3 | Mudança de poder | papel concedido, fator da equipe removido ou procedimento de emergência |
| 4 | Pico de negados ou de falhas de CSRF e Origin | mais de 50 em 10 minutos |
| 5 | Pwned Passwords fora por mais de 24 h | |
| 6 | Erro novo do servidor | no máximo 5 por hora e 20 por dia, com um resumo do que foi suprimido |
| 7 | Pico de respostas 5xx | mais de 20 em 5 minutos |
| 8 a 10 | Batimentos | F.2 |
| 11 | Descarte, lacuna, recusa ou falha de escrita de registros | C.1 |
| 12 | Volume anormal de registros | pode indicar custo fora do esperado ou credencial roubada (V11) |
| 13 | Mudança na proteção, no prazo ou na política da credencial de envio | mecanismo em V3 |
| 14 | Pico de relatos do navegador | operacional: front-end quebrado ou abuso do endpoint |
| 15 | Silêncio prolongado de 24 h | segundo aviso |
| 16 em diante | Infraestrutura (backup, disco, certificado, servidor fora) | bloco 5 |

- Os limites são pontos de partida, para ajustar com o uso real do beta.
- **Inferência:** o alarme avisa só na mudança de estado (V11), e por isso existe o alerta 15.
- Relatos do navegador nunca geram alerta de segurança nem alerta de erro novo.

**F.2 Sinais de vida independentes**

| Sinal | O que prova | O que não prova |
|---|---|---|
| Monitor externo de disponibilidade (da D-025), que chama `/saude` por HTTPS a cada 5 minutos (V19) | proxy, TLS, app web, banco e espaço crítico gravável: a rota responde 503 se o arquivo crítico não aceitar gravação | fila e envio |
| `batimento.fila`, no caminho crítico, a cada 5 minutos | fila de tarefas, banco, caminho crítico e CloudWatch | app web |
| `batimento.operacional`, pelo Docker | caminho operacional | |
| `batimento.servidor`, por temporizador do sistema | servidor ativo, registro do sistema e enviador | app e fila |
| Alarme de estado da instância do Lightsail | a máquina | |

- **Leitura combinada:**
  - batimento do servidor chegando sem o da fila: a fila parou;
  - nenhum batimento chegando, mas o monitor externo vendo o site no ar: parou o envio ou a credencial;
  - nada chegando de lugar nenhum: o servidor está fora.
- **Dado ausente:** os alarmes de batimento tratam dado ausente como falha (`breaching`). Doc: o padrão `missing` leva ao estado INSUFFICIENT_DATA, sem alerta.
- Cada alarme é testado parando o componente que ele vigia (V11).

### G. Erros (16.5.1 a 16.5.3)

**G.1 No servidor**

- **Mensagem genérica com código** de referência, no tom de D-029: "Algo deu errado do nosso lado. Tente de novo em instantes. Se continuar, fale com a gente e informe o código 7F3A91C2." O código é o da requisição, e basta buscá-lo nos registros.
- **API:** a resposta traz mensagem e código, nunca a pilha, consultas ou dados internos.
- O modo DEBUG fica desligado, e o e-mail de erro padrão do Django também, porque ele leva dados da requisição.
- **Recurso de outra pessoa:** o app responde "não encontrado", e não "proibido", para não revelar que ele existe.
- **Erro novo:** o servidor tira uma assinatura de cada erro (o tipo e o ponto do código) e guarda as que já viu.
- **Falhar fechado:** se a checagem de login, permissão, CSRF ou limite der erro, o pedido é recusado. A única abertura controlada é a do Pwned Passwords (exceção E3 do bloco 1).

**G.2 Erros do navegador**

1. **Entrada:** `POST /api/erros-do-navegador`, só no mesmo domínio, sem CORS, com o Origin conferido.
   - Com sessão: exige a sessão e o CSRF.
   - Sem sessão (telas de entrada, cadastro e recuperação): exige o CSRF e aplica limite por endereço. O IP fica só no contador do limite, por minutos, e nunca vai para o log de aplicação.
2. **Frequência:**
   - até 10 relatos a cada 10 minutos por sessão;
   - até 5 a cada 10 minutos por endereço, sem sessão;
   - teto geral de 300 por hora;
   - relatos repetidos com a mesma assinatura, na mesma sessão, contam uma vez a cada 10 minutos;
   - acima dos limites, o relato é descartado e só a contagem é registrada.
3. **Resposta:** sempre 204, sem detalhes.
4. **Tamanho e formato:** o corpo tem até 8 KB e é recusado antes de ser interpretado se passar disso. O esquema é estrito: campos desconhecidos são recusados. O navegador e o sistema são resumidos pelo servidor a partir do cabeçalho; o cliente não os envia.

| Campo | Limite |
|---|---|
| tipo | lista fechada: erro, promessa rejeitada, falha de componente |
| mensagem | 300 caracteres |
| pilha | 30 linhas de até 200 caracteres |
| pilha de componentes | 20 linhas de até 100 caracteres |
| rota | modelo de rota conhecido; outro valor vira "desconhecida" |
| versão | identificador da versão, hexadecimal, de 7 a 40 caracteres |

5. **Saneamento no servidor.** A passada feita no navegador é só a primeira, e o servidor não confia nela.
   - **URLs:** sem query string e sem fragmento; trechos com cara de identificador ou token viram `:id`; endereços de outros domínios viram `[externo]`.
   - **Dados pessoais e sensíveis:** e-mails, sequências longas de dígitos, tokens longos e valores depois de chaves como senha, password, token, code ou código viram `[removido]`.
   - **Dados digitados:** o relato não inclui valores de formulário, estado de componentes nem conteúdo da página.
   - **Caracteres:** os de controle são removidos, e o texto é normalizado antes do corte.
   - Se o saneamento falhar, o relato é descartado e só a contagem é registrada. Nada que vem do navegador é registrado sem passar por ele.
6. **Origem marcada:** o evento separa um bloco `cliente` (o que veio do navegador, já saneado, com `confiavel: false`) de um bloco `servidor` (hora de recebimento, código da requisição, conta e versão em produção).
7. **Mapas de código:** não são publicados.
8. **Alertas:** os relatos do navegador não alimentam o alerta de erro novo, só o de volume (F.1).
9. **Prioridade:** num excesso de relatos, eles são os primeiros a serem descartados (H.2).

O saneamento por padrões reduz o risco, mas não garante que nenhum dado pessoal escape do texto livre. Por isso esses relatos ficam só 30 dias, sem IP e com acesso restrito (Jur-22).

**G.3 Quando uma peça falha**

| Falha | Comportamento |
|---|---|
| SES fora | a fila tenta de novo, e a tela mostra a mesma mensagem de sempre |
| Armazenamento de objetos fora | a imagem mostra o estado de erro do componente (D-029) |
| CloudWatch fora | H.5 |
| Pwned Passwords fora | a verificação usa o subconjunto local (bloco 1) |
| Banco fora | página de manutenção; nada mais funciona |

### H. Prazos, caminhos e preservação

**H.1 Prazos.** Os da seção B.

**H.2 Três caminhos**

| Categoria | Como é gravada | Pode perder? | Como a perda aparece |
|---|---|---|---|
| Auditoria (C.2) | no banco, na mesma transação da ação | não: sem a gravação, a ação não acontece | a ação falha; uma falta no CloudWatch aparece como lacuna para o exportador |
| Críticos de acesso e de segurança | arquivo próprio, com gravação síncrona e um arquivo por processo, levando `id` e `seq`; gravação forçada no disco a cada 1 s; em espaço reservado | só na janela de queda de E.5 | se a gravação falhar, a operação de autenticação é recusada com mensagem genérica e `/saude` responde 503 (o monitor externo alerta); quando a gravação volta, o app registra `registros.falha_de_escrita`; falhas na sequência de `seq` aparecem nas consultas |
| Operacionais | saída padrão, com Docker em modo não bloqueante e buffer de 4 MB | sim | descartes do app contados num evento crítico; descartes do Docker não são contados (V8) |
| Navegador | dentro do caminho operacional, depois dos limites de G.2 | sim, e são os primeiros a sair | contagem por hora |

**Doc:** no modo não bloqueante do Docker, as mensagens novas não entram no buffer quando ele está cheio. Não há promessa de entrega garantida para nenhuma categoria; a promessa é que a perda de um evento crítico não é silenciosa, salvo os riscos residuais de E.5.

**H.3 Disco**

| Espaço | Limites |
|---|---|
| Espaço reservado dos críticos | 2 GB, tamanho fixo, separado do disco principal (V9) |
| Logs operacionais no disco principal | 500 MB e no máximo 7 dias |
| Registro do sistema | 500 MB e 7 dias (V20) |

Prioridades:

1. Os eventos críticos não disputam espaço: o espaço deles é reservado.
2. Abaixo de 10 GB livres no disco principal, os logs operacionais deixam de ser gravados. A contagem do que foi descartado, com o motivo "disco", vai a cada minuto para o caminho crítico, que continua gravando mesmo com o disco principal cheio.
3. No espaço reservado:
   - **a partir de 70%:** os arquivos já enviados mais antigos são apagados antes dos 7 dias, porque já estão no CloudWatch;
   - **a partir de 80%:** alerta;
   - **em 100%:** vale a falha fechada de H.2, com alerta pelo monitor externo.
4. O banco fica no disco principal, com os alarmes de disco do bloco 5.

**H.4 Envio e confirmação**

O que a documentação diz (Doc):
- o sequence token não é mais usado, e envios paralelos ao mesmo fluxo são permitidos;
- o lote precisa estar em ordem cronológica, cobrir no máximo 24 h, ter até 10.000 eventos e até 1.048.576 bytes, contando 26 bytes por evento;
- eventos com mais de 14 dias, anteriores ao prazo do grupo ou mais de 2 h no futuro são recusados, e os demais são processados.

Regras do enviador:

1. Ordenar o lote pela hora antes de enviar, guardando a posição original de cada `id`.
2. **Resposta 200 sem recusas:** a posição salva avança até o fim do lote.
3. **Resposta 200 com `rejectedLogEventsInfo`:** converter os índices em `id`.
   - `tooOldLogEventEndIndex` é exclusivo e `tooNewLogEventStartIndex` é inclusivo (Doc); a inclusividade de `expiredLogEventEndIndex` não está documentada (V7).
   - Os eventos recusados vão para a quarentena local, com o motivo, e geram `registros.rejeitados`.
   - Os "muito novos" são tentados de novo depois que o relógio for corrigido, com alerta.
   - Os "muito antigos" e os "expirados" não são reenviados.
   - Só então a posição avança.
4. **`rejectedEntityInfo`:** registrar como aviso. Doc: os eventos ainda podem ter sido aceitos.
5. **Falha de rede, tempo esgotado, erro 5xx ou limitação:** reenviar o mesmo lote, esperando cada vez mais, sem avançar a posição.
   - O reenvio pode duplicar eventos; a documentação não fala em deduplicação, então as consultas eliminam duplicatas pelo `id`.
6. **`InvalidParameterException`:** dividir o lote. Um evento inválido sozinho vai para a quarentena, e nada trava para sempre.
7. **Fluxo inexistente:** criar o fluxo. **Grupo inexistente:** alerta, sem criar o grupo.
8. **Credencial recusada:** guardar tudo localmente e tentar devagar; o alerta de silêncio cobre o caso.
9. A posição salva é gravada de forma atômica: arquivo temporário, depois renomear, depois forçar a gravação no disco.
10. Não há promessa de envio exatamente uma vez. O envio é pelo menos uma vez, com detecção de duplicatas e de lacunas.

Se nenhuma ferramenta pronta cumprir essas regras, os eventos críticos usam um enviador próprio e pequeno, e os operacionais usam uma ferramenta pronta (V7).

**H.5 Quando o CloudWatch fica fora**

- **Até 15 minutos:** novas tentativas.
- **15 minutos:** alerta de silêncio.
- **24 horas:** segundo alerta.
- **Até 14 dias:** quando o CloudWatch volta, o envio retoma da posição salva.
- **Mais de 14 dias:** os eventos não enviados não podem mais ser enviados (Doc). Eles ficam no espaço reservado até 180 dias contados da hora de cada evento e então são apagados. A lacuna é registrada e vai para o registro de incidentes.
- Depois de qualquer queda, os eventos de segurança do período são revisados manualmente.
- Não existe cópia de contingência no backup. Nenhum local novo é criado, e todo o prazo cabe nos 180 dias aprovados.

**H.6 Exclusão efetiva**

- **Doc:** depois do prazo, a exclusão no CloudWatch acontece em até cerca de 72 h e, raramente, demora mais.
- **Doc:** se o prazo for alongado, eventos que já tinham passado do prazo antigo, mas ainda não tinham sido apagados, podem sobreviver.
- A cópia local sai pela rotação (H.3).
- Backups e cópias de disco não incluem a pasta de registros nem o espaço reservado (V15).
- A política de privacidade fala em "até 6 meses, com a exclusão concluída alguns dias depois", com o texto final revisado pelo advogado (Jur-21).

**H.7 Preservação por incidente.** Se houver um incidente, os registros do período são copiados para o registro do incidente e ficam 5 anos.

**H.8 Exclusão de conta.** Os registros, a auditoria de C.2 e os HMACs de D.3 expiram nos prazos normais, sem exclusão antecipada. Isso entra como linhas novas na tabela B.12 do bloco 3 quando ela for registrada (Jur-21).

### I. Ponto jurídico (análise preliminar, sem conclusão)

**I.1 Dois tipos de registro com IP**

| | Registros de acesso (`acesso`) | Eventos de segurança com IP (`seguranca`, `servidor`) |
|---|---|---|
| O que são | data e hora de uso a partir de um IP (Marco Civil, art. 5º, VIII) | falhas, negados, limites, fatores e SSH |
| Prazo | 6 meses (escolhido) | 6 meses (escolhido) |
| Art. 15 do Marco Civil | vale quando aplicável: provedor constituído como pessoa jurídica, com atividade organizada, profissional e com fins econômicos. No beta, a aplicabilidade é questão jurídica (Jur-18) | não se aplica automaticamente; a guarda precisa de justificativa própria |
| Base provável, a confirmar | no beta, legítimo interesse; como empresa, obrigação legal | legítimo interesse (segurança e prevenção a fraude) |

**I.2 O que a proposta precisa sustentar** (alimenta a avaliação de legítimo interesse da Etapa 7):

- **Finalidade:** proteger contas e o serviço, investigar ataques e incidentes e atender pedidos legais. Nunca perfil, marketing nem localização.
- **Necessidade:** o IP é o que liga tentativas espalhadas por várias contas. Sem ele, o alerta de ataque espalhado do bloco 1 e a investigação ficam cegos. Hipótese: um incidente pode ser descoberto semanas depois, o que justificaria meses de guarda, e não dias.
- **Minimização:** IP só em `acesso`, `seguranca` e `servidor`; os logs de aplicação não têm IP.
- **Acesso restrito:** só pelo papel de leitor, com MFA (E.2).
- **Retenção:** 180 dias configurados, mais a exclusão efetiva (H.6). Guarda além disso, só ligada a um incidente.
- **Transparência:** a política de privacidade explica tudo isso (Etapa 7).
- **HMAC:** é dado pseudonimizado, e o e-mail digitado pode ser de outra pessoa (Jur-23).

### J. Custo (estimativas, sem conferência para São Paulo)

| Dimensão | Referência | Situação |
|---|---|---|
| Franquia | 5 GB por mês, numa franquia única para envio, armazenamento e dados lidos por consultas do Logs Insights | não são 5 GB por categoria; se é um total compartilhado fica para V12 |
| Envio | US$ 0,50 por GB nos EUA | número de um resumo da página de preços, não lido literalmente; São Paulo não aparece |
| Armazenamento | US$ 0,03 por GB por mês nos EUA | idem |
| Consultas do Logs Insights | cobradas pelos dados lidos e contadas na franquia | sem preço confirmado |
| Alarmes | 10 incluídos; acima disso, US$ 0,10 por alarme por mês nos EUA (Doc); o plano tem 15 ou mais | São Paulo a conferir |
| Métricas personalizadas | 10 incluídas; acima disso, US$ 0,30 por métrica por mês nos EUA (Doc); os filtros de métrica provavelmente contam como métricas | São Paulo a conferir |
| SNS | referência de 1.000 e-mails gratuitos por mês | não confirmado; a tabela de preços não carregou |
| Monitor externo, espaço reservado e transferência do Lightsail | | V9, V12 e V19 |

**Hipótese:** abaixo de US$ 5 a 10 por mês no beta. O custo real é fechado no bloco 5.

### K. Efeitos nos documentos

Registrado em 2026-11-24:

- `docs/decisions.md`: D-032 aprovada, com ADR; D-025 substituída, com o monitor externo preservado.
- `docs/adr/D-032-registros-e-monitoramento.md`: ADR novo.
- `docs/requisitos-mvp.md`: critérios RNF-21 a RNF-45; nota sobre a classificação do RNF-18 e o atendimento do RNF-20; pendências de registros resolvidas.
- `docs/modelo-conceitual.md`: entidade AUDITORIA_SENSIVEL (M-39) e regra RM-18.
- `docs/design-e-ux.md`: texto do erro inesperado com código.
- `README.md`: situação da Etapa 6 e a tecnologia de registros.

Fica para o registro dos blocos 1 e 3, quando autorizado:
- o formato do link com fragmento (D.4) e o prefixo /64 (D.5) na tabela de tokens e nos limites do bloco 1;
- as linhas novas da tabela B.12 (H.8).

Fica para a Etapa 7: a política de privacidade e o registro das operações de tratamento citam a AWS (CloudWatch) como operadora, os prazos, a exclusão efetiva e o HMAC.

### L. Verificações reservadas ao bloco 5

Todas pendentes.

| # | O que verificar |
|---|---|
| V1 | Proteção contra exclusão: se cobre fluxos (testar apagando um fluxo de um grupo protegido) e se bloqueia mudança de prazo (a documentação não diz; considera-se que não); custo; registro no CloudTrail |
| V2 | Se a entrada no papel (AssumeRole) aparece no histórico do CloudTrail e em qual região (o RNF-20 depende disso); como as consultas ao CloudWatch Logs são classificadas; custo dos eventos de dados |
| V3 | Mecanismo do alerta de mudança na proteção, no prazo ou na política |
| V4 | Se o Lightsail continua sem papel de instância (as fontes são antigas) |
| V5 | Credencial de envio: armazenamento, permissões no sistema, rotação com duas chaves ativas, revogação, troca sem interromper o envio e condição de IP de origem |
| V6 | Ações do IAM exatas por identidade, conferidas linha a linha, e a prova negativa de que a credencial de envio não lê, não apaga e não muda prazo |
| V7 | Enviador que cumpra H.4 (ferramenta pronta ou enviador próprio para os críticos), incluindo a inclusividade de `expiredLogEventEndIndex` e o envio por HTTPS |
| V8 | Modo não bloqueante do Docker na versão instalada, e se dá para contar os descartes |
| V9 | Mecanismo do espaço reservado (sistema de arquivos próprio pré-alocado ou disco adicional do Lightsail) e o custo |
| V10 | Fonte de hora no Lightsail e o que acontece se o relógio voltar |
| V11 | Teste de `breaching` em cada batimento; aviso só na mudança de estado; ações no estado INSUFFICIENT_DATA; valor padrão dos filtros de métrica; eventos atrasados; métrica de volume recebido |
| V12 | Preços em São Paulo por dimensão; se a franquia de 5 GB é compartilhada; SNS; transferência de dados do Lightsail; condições do nível gratuito na conta |
| V13 | Proxy: sobrescrever o cabeçalho de IP; sem IP, query string ou fragmento nos logs operacionais; erros de TLS |
| V14 | PostgreSQL 18 na imagem usada: aplicar os parâmetros de D.6 e provocar um erro de unicidade para conferir o log |
| V15 | Backups e cópias de disco sem a pasta de registros nem o espaço reservado |
| V16 | Trilha do CloudTrail para guardar mais de 90 dias: custo e utilidade |
| V17 | Papéis no banco para a auditoria; se o ORM usa RETURNING; se dá para enfileirar a tarefa na mesma transação (D-024) |
| V18 | Segredos: chaves do HMAC, com versões, e credencial de envio |
| V19 | Monitor externo de disponibilidade (da D-025): ferramenta, frequência e custo |
| V20 | Limites de taxa do journald, que podem descartar registros do sistema, e as cotas |
| V21 | CSP e cabeçalhos de segurança do app, com as regras de D.4 |

### M. Questões jurídicas

Pendentes de avaliação profissional. Continuam a lista de 16 perguntas do bloco 3, cujo registro ainda está pendente, e acompanham a consulta jurídica de D-002.

- **Jur-17.** Qual é a base legal para guardar o IP completo por 6 meses, inclusive de contas excluídas, durante o beta e depois como empresa?
- **Jur-18.** O art. 15 do Marco Civil se aplica ao beta? A partir de quando passa a se aplicar: da constituição da empresa ou do início da cobrança?
- **Jur-19.** O que um registro de acesso precisa conter? As entradas e o `sessao.uso` bastam, ou é preciso registrar cada requisição?
- **Jur-20.** O legítimo interesse sustenta 6 meses para os eventos de segurança com IP que não são registros de acesso? Seria recomendável um prazo menor?
- **Jur-21.** Como conciliar a exclusão de conta com a guarda dos registros (LGPD, art. 16 e art. 18)? Como escrever a exclusão efetiva na política de privacidade?
- **Jur-22.** Os relatos de erro do navegador podem ter resíduo de dado pessoal. O tratamento e a transparência propostos bastam?
- **Jur-23.** O HMAC do e-mail digitado para uma conta que não existe pode ser o e-mail de outra pessoa. Qual é a base legal, e como dar transparência a isso?

### N. Fontes conferidas em 2026-11-24

- [PutLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html) e [RejectedLogEventsInfo](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_RejectedLogEventsInfo.html)
- [Proteção de grupos contra exclusão](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/protecting-log-groups-from-deletion.html) e [PutLogGroupDeletionProtection](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogGroupDeletionProtection.html)
- [PutRetentionPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutRetentionPolicy.html) e [DeleteLogStream](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogStream.html)
- [Ações do IAM para o CloudWatch Logs](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoncloudwatchlogs.html)
- [Alarmes e dados ausentes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarms-and-missing-data.html)
- [CloudTrail no CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/logging_cw_api_calls_cwl.html) e [eventos do CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-events.html)
- [Preços do CloudWatch](https://aws.amazon.com/cloudwatch/pricing/) e [do SNS](https://aws.amazon.com/sns/pricing/)
- [PostgreSQL 18: configuração de logs](https://www.postgresql.org/docs/18/runtime-config-logging.html)
- [Docker: configuração de logs](https://docs.docker.com/engine/logging/configure/)
- [CloudWatch no Lightsail com chaves de acesso](https://aws.amazon.com/blogs/compute/monitoring-memory-usage-lightsail-instance/) (fonte antiga)
- [OWASP ASVS 5.0, capítulo V16](https://github.com/OWASP/ASVS/blob/2b300716ebbef654788d0a14d6c878cecc70c2e9/5.0/en/0x25-V16-Security-Logging-and-Error-Handling.md)

## Histórico

- 2026-11-24: documento criado no registro do bloco 4 da Etapa 6, com autorização do usuário ("Aprovo integralmente o Bloco 4 — Registros e Monitoramento, na versão revisada apresentada."; "Atualize a documentação e os registros de decisão necessários"). Seção 4 registrada. Os blocos 1 a 3 foram aprovados no mesmo dia e aguardam registro.
