# D-032: Registros e monitoramento

- **Status**: Aprovada
- **Data**: 2026-11-24
- **Aprovação**: escolhas "AWS CloudWatch em São Paulo (Recomendado)", "6 meses, com IP completo (Recomendado)" e "Sem serviço externo (Recomendado)" (2026-11-24); versão final aprovada com "Aprovo integralmente o Bloco 4 — Registros e Monitoramento, na versão revisada apresentada." (2026-11-24)
- **Substitui**: D-025, preservando o monitor externo de disponibilidade
- **Relacionadas**: D-005, D-007, D-010, D-017, D-022, D-023, D-024, D-026, D-029; RNF-11, RNF-12, RNF-16, RNF-17, RNF-18, RNF-20 e RNF-21 a RNF-45 em `docs/requisitos-mvp.md`; M-19, M-23, M-34 e M-39 em `docs/modelo-conceitual.md`; decisões P4-01 a P4-20 em `docs/seguranca-e-privacidade.md`

## Contexto

- A D-025 (Etapa 3) deixou os logs no próprio servidor, com acesso por SSH e um monitor externo de disponibilidade, e passou para a Etapa 6 o rastreamento de erros e o registro da leitura dos logs.
- A Etapa 6 adotou como meta o OWASP ASVS 5.0 no nível L2. No capítulo V16, os requisitos 16.4.2 (registros protegidos e sem alteração) e 16.4.3 (envio a um sistema logicamente separado, para que uma invasão do app não comprometa os registros) não se cumprem com os registros só no servidor.
- Requisitos já confirmados: RNF-12 (sem credenciais nos logs), RNF-16 (identificador interno), RNF-17 (acesso individual e explícito), RNF-18 (três categorias com prazos próprios) e RNF-20 (registrar quem acessou os logs).
- Dados no Brasil, como em D-010, D-022 e D-023, e a LGPD.
- Servidor de 2 GB de RAM (D-010).

## Opções consideradas

### Onde ficam os registros

- **AWS CloudWatch Logs em São Paulo (escolhida):** o servidor envia os registros em poucos minutos com uma credencial que só acrescenta, e os alertas rodam fora do servidor, mesmo que ele seja invadido. Fica na mesma AWS e na mesma região. Estimativa de poucos dólares por mês no beta, a conferir.
- **Cópia no S3 com trava:** guarda bem, mas os alertas continuariam rodando no próprio servidor, justamente o que pode ser invadido.
- **Só no servidor, com exceção:** mantém a D-025 e registra exceções ao ASVS 16.4.2 e 16.4.3. Uma invasão pode apagar os rastros.

### Prazo dos registros de segurança

- **6 meses, com IP completo (escolhida):** tempo para investigar um incidente percebido tarde. Os logs de aplicação ficam sem IP, por 30 dias.
- **90 dias:** guarda menos dado pessoal, mas pode não alcançar um incidente descoberto meses depois.
- **1 ano:** mais histórico, com mais dado pessoal guardado.

### Rastreamento de erros

- **Sem serviço externo (escolhida):** erros nos próprios registros, sem dados pessoais, com alerta de erro novo; erros do navegador chegam por um endereço do próprio app.
- **Sentry com dados mascarados:** painel pronto e bom para investigar, mas é um serviço de fora do país, com transferência internacional e mais um operador na política de privacidade.
- **Ferramenta própria no servidor:** painel parecido com o Sentry, instalado pelo projeto; gasta memória que o servidor de 2 GB não tem sobrando.

### Correções das revisões externas

A proposta passou por três rodadas de revisão externa trazidas pelo usuário em 2026-11-24. As principais correções foram estas:

- A descrição da opção escolhida dizia que a credencial "só consegue acrescentar, nunca alterar ou apagar". A versão final separa três proteções: a credencial de envio não lê, não apaga e não muda prazos; identidades administrativas com permissões suficientes ainda podem apagar ou encurtar o prazo; e o que está no servidor antes do envio pode ser adulterado por quem tem acesso de root.
- Registros críticos não podem ser descartados em silêncio. Por isso, passaram a ter caminho próprio, gravação síncrona e espaço reservado.
- O envio trata a aceitação parcial do CloudWatch evento por evento.
- O sinal de vida passou a ser feito por sinais independentes.
- A conformidade com o ASVS não é declarada antes das provas.

## Decisão

- Os registros vão também ao CloudWatch Logs em São Paulo, em quatro grupos:
  - `acesso`, `seguranca` e `servidor`, que são registros de segurança, guardados por 180 dias, com IP;
  - `aplicacao`, com os logs de aplicação, guardados por 30 dias, sem IP.
- A auditoria de ações sensíveis fica no banco (M-39), também por 180 dias. A trilha editorial continua permanente (M-23).
- Três caminhos, conforme a categoria:
  - os críticos são gravados no banco ou num arquivo próprio, em espaço reservado; se a gravação falhar, a operação de autenticação falha fechada, sem perda silenciosa;
  - os operacionais podem ser perdidos, e a perda é contada;
  - os relatos do navegador têm a menor prioridade.
- O envio só avança a posição depois de processar a resposta do CloudWatch, separa os eventos recusados e não promete envio exatamente uma vez.
- Identidades separadas na AWS e proteção contra exclusão nos grupos.
- Sinais de vida independentes, incluindo o monitor externo de disponibilidade da D-025, com dado ausente tratado como falha.
- O Sentry fica fora do MVP.
- O conjunto completo está em `docs/seguranca-e-privacidade.md`, seção 4:
  - decisões P4-01 a P4-20;
  - verificações V1 a V21 para o bloco 5;
  - questões jurídicas Jur-17 a Jur-23.

## Consequências

- **Ganhamos:**
  - o que já foi enviado fica fora do alcance de uma invasão do app;
  - os alertas funcionam mesmo com o servidor fora do ar;
  - a perda de um evento crítico nunca é silenciosa, salvo os riscos residuais listados;
  - os dados continuam no Brasil;
  - nenhum terceiro recebe dados de erros.
- **Abrimos mão de:**
  - um painel pronto de erros;
  - envio exatamente uma vez, porque reenvios podem duplicar eventos, que são detectados pelo identificador;
  - disponibilidade do login quando o caminho crítico não consegue gravar, em troca da falha fechada;
  - simplicidade: há mais papéis, um enviador com regras próprias e um espaço reservado.
- **Exige:**
  - as verificações V1 a V21 no bloco 5;
  - uma prova por critério (D-026);
  - as respostas jurídicas Jur-17 a Jur-23;
  - a AWS listada como operadora na política de privacidade e no registro das operações de tratamento.
- **Riscos residuais, que podem virar exceção ao ASVS:**
  - uma janela de cerca de 1 s de eventos críticos que se perdem numa queda do servidor;
  - adulteração local por quem tem root, antes do envio;
  - identidades administrativas e a conta raiz da AWS.
- **Revisitar se:**
  - o advogado indicar outros prazos ou outras bases legais;
  - a verificação V2 mostrar que a entrada no papel de leitor não fica registrada (o RNF-20 depende disso);
  - o custo em São Paulo sair do orçamento;
  - o projeto virar empresa, quando valem reavaliar o armazenamento com bloqueio contra exclusão e a aplicação do Marco Civil.
