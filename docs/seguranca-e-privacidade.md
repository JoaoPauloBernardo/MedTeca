# Segurança e privacidade: MedTeca

**Situação**: Etapa 6 aprovada em 2026-11-26. Blocos 1 (contas e acesso), 2 (permissões e privacidade), 3 (LGPD), 4 (registros e monitoramento), 5 (infraestrutura e operação) e 6 (qualidade e cadeia de suprimentos) aprovados e registrados; o bloco 5, com ressalvas. As quatro inconsistências da seção 5.P foram resolvidas em 2026-11-25. As verificações e as questões jurídicas seguem abertas e impedem o beta, não a implementação.

**Aprovado (Etapa 6)**: 2026-11-26 - usuário: "Aprovar Etapa 6"

**Aprovado (bloco 1)**: 2026-11-24 - usuário: "Aprovar bloco 1"

**Aprovado (bloco 2)**: 2026-11-24 - usuário: "Aprovar bloco 2"

**Aprovado (bloco 3)**: 2026-11-24 - usuário: "Aprovar bloco 3"

**Aprovado (bloco 4)**: 2026-11-24 - usuário: "Aprovo integralmente o Bloco 4 — Registros e Monitoramento, na versão revisada apresentada."

**Aprovado (bloco 5)**: 2026-11-24 - usuário: "Aprovo o Bloco 5 — Infraestrutura e Operação — conforme a proposta apresentada, incluindo as decisões P5-01 a P5-25, com as ressalvas e condições abaixo."

**Aprovado (bloco 6)**: 2026-11-24 - usuário: "Aprovar bloco 6"

Documento da Etapa 6 (segurança, LGPD, qualidade e infraestrutura). Reúne, por bloco, as decisões de segurança e privacidade, ligadas aos requisitos de `docs/requisitos-mvp.md` e às decisões de `docs/decisions.md`. Aprovar o que está aqui não autoriza implementação (D-017).

## Blocos da Etapa 6

| Bloco | Tema | Situação |
|---|---|---|
| 1 | Contas e acesso | Aprovado em 2026-11-24 ("Aprovar bloco 1") e registrado em 2026-11-25 (D-007); seção 1 |
| 2 | Permissões e privacidade | Aprovado em 2026-11-24 ("Aprovar bloco 2") e registrado em 2026-11-25; seção 2 |
| 3 | LGPD (D-009) | Aprovado em 2026-11-24 ("Aprovar bloco 3") e registrado em 2026-11-25 (D-009); seção 3. Critérios e modelo conceitual registrados em 2026-11-26 (seção 3.I) |
| 4 | Registros e monitoramento | Aprovado e registrado em 2026-11-24 (D-032); seção 4 |
| 5 | Infraestrutura e operação | Aprovado com ressalvas e registrado em 2026-11-24 (D-033); seção 5 |
| 6 | Qualidade e cadeia de suprimentos | Aprovado e registrado em 2026-11-24 (D-034); seção 6 e seção 5.4 |

O bloco 4 cita decisões dos blocos 1 a 3 que já foram aprovadas mas ainda não estavam registradas. As do bloco 1 (o cookie de aparelho confiável, os limites de tentativas, a tabela de tokens e o procedimento de emergência do único administrador) estão na seção 1 desde 2026-11-25. As do bloco 2 (a matriz de permissões e as regras de privacidade) estão na seção 2 desde 2026-11-25. As do bloco 3 (entre elas, a tabela B.12, com o destino de cada registro na exclusão da conta, e a revisão semestral de privilégios) estão na seção 3 desde 2026-11-25.

## Convenções

- **Doc**: confirmado em documentação oficial, conferida em 2026-11-24 (fontes nas seções 4.N, 5.R e 6.Q).
- **Inferência**: conclusão técnica do consultor, sem confirmação em documentação.
- **Testar**: só uma prova na implementação confirma.
- **V-n**: verificação técnica. A V1 a V21 vêm do bloco 4 (seção 4.L), e a V22 a V34, do bloco 5; a situação dessas está na seção 5.M. A V35 a V51 vêm do bloco 6 (seção 6.L), e a V52 a V55, das resoluções da seção 5.P. Nenhuma foi concluída.
- **Jur-n**: questão para o advogado (seções 3.E, 4.M, 5.N e 6.M). A Jur-01 a Jur-16 vêm do bloco 3. A análise jurídica deste documento é preliminar.
- **Inconsistência**: divergência entre blocos aprovados, registrada para avaliação do usuário sem resolução unilateral (seção 5.P). As quatro registradas no bloco 5 foram resolvidas pelo usuário em 2026-11-25.

## 1. Contas e acesso (bloco 1, D-007)

### 1.1 Como o bloco foi decidido

- **Duas rodadas de perguntas** em 2026-11-24, com as escolhas resumidas na seção A. O usuário pediu facilidade de login para o estudante: o público é da saúde e pouco familiarizado com tecnologia, e "se ficar pedindo muita autenticação e fazendo eles saírem muito do site eles vão abandonar".
- **Duas revisões externas**, trazidas pelo usuário, corrigiram a proposta. Na segunda, dois erros do consultor foram corrigidos: a descrição do CSRF, que ele tinha ligado à sessão, e a da passkey, que não deixa de valer sozinha quando o aparelho se perde.
- **Aprovação:** "Aprovar bloco 1" (2026-11-24), sobre a versão final.
- **Registro autorizado** em 2026-11-25, depois do registro dos blocos 4 a 6. A seção D traz o que blocos posteriores mudaram.

### A. Decisões aprovadas

1. **Meta:** ASVS L2, com exceções escritas (seção C).
2. **Senha:** de 15 a 64 caracteres, sem regras de composição, aceita colar e o gerenciador de senhas, sem troca periódica e recusando senhas vazadas.
3. **Segundo fator:**
   - obrigatório para a equipe (editor, revisor e administrador), com a passkey como fator preferencial, por ser resistente a sites falsos;
   - app autenticador (TOTP) como alternativa;
   - o estudante entra só com senha (exceção E1).
4. **Sessão:** estudante até 30 dias; equipe até 24 h, saindo depois de 1 h sem uso.
5. **Sessões simultâneas:** sem limite (ASVS 7.1.2). O estudante usa celular, tablet e computador, e todas as sessões aparecem na Conta para encerrar. A conta compartilhada é um risco de negócio, a tratar com a D-011.
6. **Troca ou recuperação de senha:** encerra as outras sessões e avisa por e-mail.
7. **"Conta" no pé da barra lateral a partir de 600 px**, com o Sair à vista. Isso acrescenta um item à navegação da D-030 (nota na D-030 e em `docs/design-e-ux.md`).

### B. Ajustes técnicos

**B.1 Senhas vazadas, com alternativa local.** Três camadas, nesta ordem:

- **Lista local de senhas proibidas, sempre conferida:** senhas comuns com 15 ou mais caracteres e palavras do contexto (ASVS 6.2.4 e 6.2.11).
- **Pwned Passwords, por consulta:** recebe só os 5 primeiros caracteres do resumo da senha e espera no máximo 2 s (6.2.12). O serviço está na lista de destinos externos do bloco 5 (5.H.6).
- **Subconjunto local de vazadas, quando o serviço cair:**
  - **o que é:** os cerca de 10 milhões de resumos que mais aparecem na base pública do próprio Pwned Passwords;
  - **tamanho:** algumas centenas de megabytes, ou menos num filtro compacto;
  - **atualização:** preparado fora do servidor e atualizado a cada trimestre;
  - **por que não a base inteira:** ela ocupa dezenas de gigabytes e não cabe com folga no servidor aprovado (D-010). O tamanho exato e a licença de uso da base são conferidos na implementação.

As vazadas raras, fora do subconjunto, passam sem checagem enquanto o serviço estiver fora (exceção E3). Na próxima entrada da pessoa, a checagem completa é refeita e, se a senha estiver vazada, aparece um aviso sugerindo trocar, sem bloquear.

**B.2 CSRF, como o Django funciona.** Cookie de CSRF separado, o padrão do Django; `CSRF_USE_SESSIONS` não é usado.

- **O segredo:** fica no cookie `__Host-csrftoken` (Secure, SameSite=Lax, Path=/). Esse cookie é legível pelo JavaScript, e a documentação do Django diz que torná-lo HttpOnly não traz ganho prático.
- **Ida ao servidor:** o app lê o cookie e envia o token no cabeçalho `X-CSRFToken` de toda alteração. O token é mascarado a cada envio, uma proteção do próprio Django.
- **Independência da sessão:** o segredo não depende da sessão, e o Django troca o segredo a cada login.
- **Origem:** o Django confere o cabeçalho Origin contra o próprio endereço; sem Origin, em HTTPS, confere o Referer.
- **Na API:** a autenticação por sessão do Django Ninja exige o token. A configuração exata é conferida na especificação de CONTA.
- **Proibições e testes:** nenhuma alteração por GET; nenhum CORS; testes que enviam alterações sem token e esperam recusa (D-007).
- **Por que não `CSRF_USE_SESSIONS`:** pediria um endpoint só para entregar o token e um pedido a mais ao abrir o app, sem ganho real. Se houver uma falha de script injetado (XSS), o atacante age dentro da página de qualquer jeito.

**B.3 Sessão.**

- **Cookie:** `__Host-sessionid` (Secure, HttpOnly, Path=/, SameSite=Lax).
- **Força da chave:** a chave do Django tem cerca de 165 bits; o ASVS pede 128 (7.2.3).
- **Guarda e renovação:** a sessão fica no servidor, é renovada a cada login (7.2.4) e é apagada ao sair (7.4.1).
- **Por que Lax:** com Strict, quem chegasse por um link de e-mail apareceria deslogado.

**B.4 Passkey: registro, perda, revogação e remoção.**

- **No cadastro da equipe:** cada passkey recebe um nome e uma data (por exemplo, "iPhone, nov. 2026"), e 10 códigos de recuperação são gerados na hora, para guardar. Recomendação: registrar dois fatores, como duas passkeys, ou passkey e app.
- **O servidor só guarda a chave pública.** Face ID e digital ficam no aparelho, então o MedTeca não trata dado biométrico.
- **Perder o aparelho não revoga a passkey.** Ela continua registrada no servidor e, se for sincronizada (iCloud ou Google), continua também nos outros aparelhos da pessoa. Quem pegar o aparelho ainda precisa desbloqueá-lo.
- **Revogar:** a pessoa entra com outro fator; na Conta, remove a passkey perdida, o que vale para todos os aparelhos sincronizados; encerra a sessão daquele aparelho na lista. Remover um fator pede reautenticação (7.5.1) e encerra as outras sessões.
- **Sem nenhum outro fator:** o administrador reabilita a conta depois de confirmar a identidade (6.4.4).
- **Auditoria:** registro e remoção de fatores viram eventos de segurança (seção 4.C).

**B.5 Emergência do único administrador.** Vale quando ele perdeu todos os fatores ou há suspeita de que a conta foi tomada.

1. **Confirmação de identidade:** controle das duas contas da infraestrutura, a da AWS com o segundo fator dela e a chave SSH individual do servidor. São dois controles independentes da conta no MedTeca. Atualização da resolução da 5.P.3 (2026-11-25): se a chave SSH também tiver sido perdida, o terminal pelo navegador do Lightsail é a alternativa, ligado com alerta, com registro e revisão depois; em seguida, ele é desligado, uma chave nova é cadastrada e a antiga é revogada. A fronteira real é a conta da AWS, protegida por passkey: a chave SSH protege contra erro e contra roubo isolado, mas não é barreira independente contra quem controla a conta da AWS (Inferência). O prazo de 7 dias para a revisão segue como proposta não aprovada.
2. **Autorização:** o responsável pelo projeto autoriza por escrito, com o motivo, no registro de incidentes. Enquanto houver um só administrador, é a mesma pessoa. Recomendação: ter um segundo administrador antes da abertura ao público, para que cada um aprove a emergência do outro.
3. **Execução, por comando no servidor** (por SSH ou, na alternativa acima, pelo terminal do navegador):
   - o comando não roda sem um motivo escrito;
   - remove todos os fatores da conta e encerra todas as sessões dela;
   - exige troca de senha;
   - gera um link de recadastro de uso único, válido por 30 minutos, mostrado no terminal e nunca enviado por e-mail;
   - no recadastro, cria passkey e códigos novos.
4. **Auditoria:**
   - o comando grava um evento só de inclusão (M-34), com o usuário e a chave SSH usados, a data, a conta e o motivo; o procedimento também entra na auditoria de ações sensíveis (4.C.2);
   - o login no servidor fica registrado (RNF-20); a abertura do terminal pelo navegador fica na trilha do CloudTrail, e o alerta dela não substitui esse registro (5.P.3, V54);
   - depois, o administrador revisa os eventos recentes da conta: logins, papéis, publicações e autorizações;
   - se houver sinal de que a conta foi tomada, abre o processo de incidente (bloco 3).
5. **Prevenção:** códigos de recuperação impressos em local seguro e duas passkeys, uma no celular e outra no computador.

**B.6 Limite de tentativas sem permitir trancar a conta de outra pessoa.** Usa o padrão de "cookie de aparelho" descrito pela OWASP:

- **Aparelho confiável:** depois de um login certo, o aparelho recebe um cookie `__Host-` assinado e HttpOnly; o servidor guarda só o resumo dele.
- **Falhas por conta e por aparelho ou endereço:** 5 falhas seguidas daquele aparelho ou endereço levam a uma espera de 30 s, que dobra até 15 min, só para aquele par. Um terceiro não afeta o celular do estudante.
- **Aparelho confiável tem limite próprio:** 10 falhas. Ele não sofre as esperas causadas por outros.
- **Ataque espalhado por muitos endereços:** acima de 100 falhas por hora numa conta, só aparelhos não confiáveis passam a esperar 15 min. O evento é registrado e gera alerta (bloco 4).
- **Por endereço de rede:** 50 falhas em 15 min, um limite alto por causa da rede da faculdade.
- **Nunca há bloqueio permanente.**
- **Recuperação de senha:** limite por conta e endereço, com resposta sempre igual; teto de 5 e-mails de recuperação por hora por conta, para ninguém lotar a caixa de alguém. Risco residual: um terceiro pode esgotar esse teto e atrasar em até uma hora a recuperação legítima.
- **Trocar a senha** invalida os aparelhos confiáveis, menos o atual.
- **Outros:** código do app autenticador, 5 tentativas e depois espera; mensagens genéricas e tempo de resposta igual; sem CAPTCHA.

**B.7 Tokens.**

| Token | Gerado como | Guardado como | Validade | Deixa de valer |
|---|---|---|---|---|
| Sessão | Django, cerca de 165 bits | No servidor | 30 dias para o estudante; 24 h e 1 h sem uso para a equipe | Sair, expirar, troca de senha, desativação, administrador |
| CSRF | Django, mascarado a cada envio | Cookie `__Host-csrftoken` | Até o próximo login | Troca no login |
| Aparelho confiável | Aleatório de 256 bits | Resumo SHA-256 | 90 dias | Troca de senha, sair de todas, exclusão |
| Recuperação de senha | Aleatório de 256 bits | Resumo SHA-256 | 30 min | Uso, novo pedido, troca de senha |
| Convite | Aleatório de 256 bits | Resumo SHA-256 | 7 dias | Uso, novo convite (CONTA-23) |
| Recadastro de emergência | Aleatório de 256 bits | Resumo SHA-256 | 30 min | Uso |
| Códigos de recuperação | Aleatórios, 10 | Argon2id, por terem pouca entropia (6.5.2) | Até o uso | Uso único; gerar novos anula os antigos |
| Segredo do app autenticador | Aleatório | Cifrado, com a chave fora do banco | Até remover | Remoção do fator |
| Passkey | No aparelho | Só a chave pública | Até remover | Remoção pela pessoa ou pelo administrador |

- **Links de e-mail:** a página que recebe o link não repassa o endereço adiante (`Referrer-Policy: no-referrer`), troca o código por uma sessão curta e vai para um endereço limpo. Atualizado pelo bloco 4: o token vai no fragmento do link e só segue ao servidor no corpo de uma requisição POST com CSRF (RNF-36).
- **Logs:** gravam o caminho sem o código (RNF-12).

**B.8 Reautenticação.**

- **Pedem a senha de novo:** trocar a senha (com a senha atual); mexer em fatores; encerrar outras sessões; excluir a conta; exportar os dados, que também gera um aviso por e-mail.
- **Trocar o e-mail:** o MVP não prevê. Se entrar, pede senha, confirmação no e-mail novo e aviso no antigo.
- **Equipe:** atribuir papéis, conceder permissões sensíveis e atestar autorização pedem a passkey de novo.

**B.9 Outros.**

- Não existe conta padrão; o primeiro administrador nasce por comando (6.3.2).
- O administrador encerra sessões de alguém (7.4.5).
- Desativar ou excluir uma conta encerra todas as sessões dela (7.4.2).

### C. Exceções ao ASVS

**E1. Sem segundo fator para estudantes (6.3.3, L2).**

- **Dados da conta do estudante:** e-mail, apelido, tentativas, desempenho, marcações, reportes e sessões. São dados pessoais (LGPD, art. 5º, I). Não são, pela natureza, dados pessoais sensíveis (art. 5º, II: origem racial ou étnica, convicção religiosa, opinião política, filiação sindical ou a organização religiosa, filosófica ou política, saúde, vida sexual, dado genético ou biométrico).
- **Ressalvas:** um reporte em texto livre pode trazer dado de saúde, apesar do aviso para não escrever dados pessoais (M-22); a passkey não envolve biometria no servidor; tudo continua sujeito ao dever de segurança (art. 46) e à comunicação de incidentes (art. 48).
- **Risco, sem minimizar:**
  - **como acontece:** senha reaproveitada de outro vazamento ou capturada num site falso; o limite de tentativas não protege contra site falso;
  - **o que o invasor consegue:** ver histórico, desempenho, marcações e reportes; exportar os dados (com aviso por e-mail); trocar a senha e tirar o acesso do dono; enviar reportes falsos; excluir a conta, o que é irreversível, porque as respostas são desvinculadas e não dá para restaurar;
  - **consequência:** pode ser um incidente que exige comunicação.
- **Compensações:** senha de 15 caracteres; lista local, Pwned Passwords e subconjunto local; limites com cookie de aparelho; aviso na troca de senha e na exportação; reautenticação para excluir e exportar; lista de sessões.
- **Quem aceita o risco:** o responsável pelo projeto, na aprovação deste bloco.
- **Rever:** na abertura ao público, na cobrança, após qualquer incidente ou se o app passar a guardar dados sensíveis. O primeiro passo seria passkey opcional para estudantes.

**E2. Sair fora de vista no celular (7.4.4, L2).**

- **Escopo:** abaixo de 600 px, o Sair fica na Conta, a dois toques. A partir de 600 px, ele está no pé do trilho ou da barra lateral, como o usuário aprovou.
- **Risco residual:** no celular de outra pessoa, a sessão pode ficar aberta até 30 dias.
- **Compensação:** encerrar a sessão a distância pela lista da Conta.
- **Rever:** se o uso mostrar acesso frequente em aparelhos de terceiros.

**E3. Senhas vazadas raras durante a falta do serviço (6.2.12, L2), temporária.**

- **Escopo:** só enquanto o Pwned Passwords estiver fora. A lista local e o subconjunto seguem valendo.
- **Compensações:** a checagem completa é refeita na próxima entrada; o evento é registrado; se a falta passar de 24 h, gera alerta (alerta 5 do bloco 4).
- **Fim da exceção:** encerra sozinha quando o serviço volta.

### D. O que blocos posteriores mudaram

- **Bloco 4 (D-032):** os tokens dos links de e-mail vão no fragmento do endereço (RNF-36); os eventos de segurança, os limites e os alertas do bloco 1 entram nos registros e alertas da seção 4; o procedimento de emergência entra na auditoria de ações sensíveis (4.C.2).
- **Bloco 5 (D-033):** a chave que cifra os segredos do app autenticador fica no Parameter Store, com cifra AES-256-GCM e a versão da chave junto do dado (5.F); o Pwned Passwords está na lista de destinos externos (5.H.6).
- **Resolução da 5.P.3 (2026-11-25):** o terminal pelo navegador é a alternativa à chave SSH perdida no procedimento de emergência (B.5).
- **Bloco 6 (D-034):** a revisão do código, o fluxo por pull request e as autorizações de operação valem também para tudo o que implementar este bloco.

### E. Critérios no catálogo

Os critérios CONTA-26 a CONTA-55 de `docs/requisitos-mvp.md` transcrevem as decisões e os ajustes deste bloco no formato EARS. O CONTA-06 (30 dias sem uso) continua valendo; o teto de 30 dias desde o login é o CONTA-32.

### F. Efeitos nos documentos

Registrado em 2026-11-25, numa branch de trabalho, para revisão e merge do usuário:

- `docs/decisions.md`: notas na D-007 (pendências resolvidas: teto de sessão, segundo fator e entrega do CSRF) e na D-030 (Conta no pé do trilho e da barra lateral); notas de atualização nos ADRs das duas.
- `docs/requisitos-mvp.md`: critérios CONTA-26 a CONTA-55.
- `docs/design-e-ux.md` e `docs/design/navegacao.html`: a Conta no pé do trilho e da barra lateral, com o Sair à vista.
- Este documento: seção 1 e cabeçalho.
- `README.md`.

## 2. Permissões e privacidade (bloco 2)

### 2.1 Como o bloco foi decidido

- **Quatro escolhas do usuário** em 2026-11-24, todas iguais à recomendação, na seção A.
- **Proposta completa** com a matriz de permissões e as regras de privacidade.
- **Aprovação:** "Aprovar bloco 2" (2026-11-24).
- **Registro** em 2026-11-25, depois dos blocos 1, 4, 5 e 6. A seção G traz o que blocos posteriores mudaram.

### A. Decisões aprovadas

1. **Números agregados para a equipe:** só aparecem com 10 pessoas ou mais (resolve o CONTA-19).
2. **Autor do reporte:** o editor não vê quem reportou. Só o administrador vê, para tratar abuso, e a consulta fica registrada (resolve a pendência de REP).
3. **Estudo individual:** ninguém vê pelo painel, nem o administrador. A exceção é um pedido do próprio estudante, atendido pelo servidor e registrado.
4. **Pessoa da equipe que exclui a conta:** o nome vira um código. A correspondência fica à parte, só para o administrador (resolve o M-31; o prazo de guarda fica para o bloco 3).

### B. Matriz de permissões (CONTA-20, ASVS 8.1.1)

Uma conta pode acumular papéis (CONTA-15), mas cada ação segue a própria regra (CONTA-21).

| Ação | Estudante | Editor | Revisor | Administrador |
|---|---|---|---|---|
| Resolver questões, treinar, fazer simulado, marcar, ver o próprio histórico e desempenho | Sim | — | — | — |
| Reportar erro | Sim | — | — | — |
| Cuidar da própria conta: apelido, sessões, exportar, excluir, sair | Sim | Sim | Sim | Sim |
| Criar e editar rascunhos: origem, gabarito e situação, comentário, referências, imagens | — | Sim | — | — |
| Enviar para revisão | — | Sim | — | — |
| Aprovar ou devolver uma versão | — | — | Sim, nunca de que seja autor ou cadastrador (FLUXO-03, RM-05) | — |
| Confirmar gabarito preliminar como oficial, com o documento da banca (CONT-16, CONT-21) | — | Sim | — | — |
| Retirar de circulação, com motivo (FLUXO-09) | — | Sim | — | — |
| Fila de reportes: ler e concluir, sem ver o autor | — | Sim | — | — |
| Ver números agregados das questões, a partir de 10 pessoas | — | Sim | Sim | — |
| Registrar a fonte do conteúdo e anexar a evidência | — | Sim | — | — |
| Atestar a autorização de uso ou marcar como não autorizada | — | — | — | Sim, com concessão individual (EDIT-06, M-19) |
| Convidar, reenviar convite, atribuir papéis, cadastrar a pessoa editorial | — | — | — | Sim (D-018) |
| Desativar conta e encerrar as sessões de alguém | — | — | — | Sim |
| Ver o autor de um reporte | — | — | — | Só para tratar abuso, com registro |
| Ver o estudo individual de alguém | — | — | — | Só pelo servidor, a pedido do estudante, com registro |
| Ver a correspondência entre código e nome | — | — | — | Só com concessão individual, com registro |
| Ver os logs | Só quem tiver concessão individual, inclusive entre administradores (RNF-17) | | | |

**Sem login:** a pessoa só consegue entrar, recuperar a senha, aceitar um convite e ler os termos e a política de privacidade. **Nenhuma questão é pública.**

### C. Como as regras são aplicadas

- **Negado por padrão:** o que a matriz não permite é recusado (CONTA-20).
- **Conferência no servidor:** a cada requisição e para cada objeto, verifica-se se aquele dado é da pessoa e se o papel permite a ação. Nada fica só escondido na tela (ASVS 8.2.1, 8.2.2, 8.3.1; CONTA-22).
- **Conferência campo a campo:** o editor recebe o reporte sem o campo do autor, e a remoção acontece no servidor, não só na tela (8.2.3).
- **Mudança de papel na hora:** como os papéis são lidos a cada requisição, retirar um papel corta o acesso imediatamente, sem esperar a sessão acabar.
- **Papel de equipe exige segundo fator:** se uma conta de estudante ganha papel de equipe, ela precisa cadastrar o segundo fator no próximo login, antes de usar qualquer função da equipe (bloco 1, CONTA-31).
- **Toda recusa vira evento de segurança** (ASVS 16.3.2), tratado no bloco 4 (seção 4.C, RNF-23).

### D. Regras de privacidade

1. **Números agregados:**
   - contam pessoas distintas, não respostas;
   - abaixo de 10, aparece "poucas respostas para mostrar";
   - na contagem por alternativa, números abaixo de 3 aparecem como "menos de 3";
   - os números da equipe são atualizados uma vez por dia, e não a cada resposta, para que ninguém compare o antes e o depois e descubra o que um colega acabou de marcar. O desempenho do estudante continua calculado na hora (M-09). A visão diária da equipe é a "visão pré-calculada" que o M-09 já permite, sem mudar o modelo.
2. **Reportes:**
   - o sistema guarda o vínculo com o autor só para devolver a resposta (REP-03);
   - se a conta for excluída, o reporte fica sem autor (M-22);
   - **risco residual:** o texto livre pode trazer dado pessoal apesar do aviso da tela.
3. **Atendimento ao estudante:**
   - o pedido precisa vir do e-mail da própria conta;
   - a consulta só lê os dados, nunca altera uma tentativa (RM-09);
   - o motivo fica registrado.
4. **Saída de alguém da equipe:**
   - a trilha editorial não muda, porque já aponta para a pessoa editorial (M-31);
   - o nome no cadastro vira um código;
   - quem pode ver a correspondência é o administrador com concessão individual, e cada consulta fica registrada.
5. **Respostas desvinculadas** (a pendência "avaliar se a anonimização é real"):
   - **o que fica:** depois da exclusão de uma conta, ficam a versão da questão, a alternativa, o resultado, a modalidade e o mês (M-21, M-36), sem nenhum identificador;
   - **o risco:** num beta pequeno, entre colegas que se conhecem, alguém de dentro ainda poderia deduzir de quem eram aquelas respostas. A LGPD só considera anonimizado o dado que não pode ser revertido por meios razoáveis (art. 12);
   - **decisão:** durante o beta, essas respostas são tratadas como **dado pessoal desvinculado**, e não como dado anônimo. Elas nunca aparecem uma a uma para ninguém e só alimentam os números agregados, com o limite de 10. A política de privacidade diz "desvinculadas e usadas só para estatística", sem prometer anonimato (bloco 3). Rever quando a base de usuários crescer.

### E. O que ficou para outros blocos

- **Bloco 3:** guardar ou não a prova de aceite dos termos depois da exclusão (M-21); prazo de guarda da correspondência entre código e nome. Registrado na seção 3: os dois seguem para o advogado (Jur-05 e Jur-06).
- **Consulta jurídica (D-002):** que metadados de uma questão retirada por licenciamento podem aparecer no histórico.
- **Bloco 4:** formato dos eventos de segurança e dos registros de consulta. Resolvido na D-032: eventos na seção 4.C e auditoria de ações sensíveis no banco (4.C.2, M-39).
- **Dependência operacional que já existia (D-015):** publicar exige um revisor diferente do autor (FLUXO-03). No beta, se o usuário for autor e administrador, outra pessoa precisa ser revisora.

### F. Exceções ao ASVS

Nenhuma neste bloco.

### G. O que blocos posteriores mudaram

- **Bloco 1 (D-007):** o segundo fator exigido do papel de equipe é o do CONTA-31 (passkey preferencial, app autenticador como alternativa).
- **Bloco 4 (D-032):** as consultas ao autor de um reporte, ao estudo individual e à correspondência entre código e nome entram na auditoria de ações sensíveis, gravada na mesma transação da consulta (4.C.2, M-39, RNF-37).
- **Bloco 3 (aprovado em 2026-11-24; detalhes na seção 3):**
  - na exclusão da conta, as respostas viram contagens de pessoas distintas por versão e alternativa, e as tentativas são apagadas; as contagens continuam tratadas como dado pessoal desvinculado, e o item D.5 passa a valer para elas;
  - a estatística da equipe ganha regras contra dedução: população definida, sem filtro de período nem de modalidade, contagens nunca exibidas à parte e supressão complementar (se uma alternativa aparece como "menos de 3", a segunda menor também é ocultada);
  - concessões sensíveis expiram depois de 90 dias sem uso, papéis de equipe parados são suspensos depois de 6 meses e os privilégios passam por revisão semestral;
  - o item D.2 muda para quem exclui a conta: o reporte aberto fica sem autor até ser concluído, e o concluído perde o texto livre (M-41, REP-04 a REP-06);
  - os critérios e as decisões do modelo foram registrados em 2026-11-26 (seção 3.I).

### H. Critérios no catálogo

Os critérios CONTA-56 a CONTA-69 de `docs/requisitos-mvp.md` transcrevem as decisões deste bloco no formato EARS. O CONTA-19 continua valendo e ganhou o limiar e o método nos CONTA-56 a CONTA-59.

### I. Efeitos nos documentos

Registrado em 2026-11-25, numa branch de trabalho, para revisão e merge do usuário:

- `docs/requisitos-mvp.md`: critérios CONTA-56 a CONTA-69; pendências resolvidas: CONTA-19, a matriz de permissões, o M-31, o autor do reporte e a análise da anonimização.
- `docs/modelo-conceitual.md`: notas nas pendências da Etapa 6 (M-31 e respostas desvinculadas).
- Este documento: seção 2 e cabeçalho.
- `docs/decisions.md` (histórico) e `README.md`.

## 3. LGPD (bloco 3, D-009)

### 3.1 Como o bloco foi decidido

- **Quatro escolhas do usuário** em 2026-11-24, todas iguais à recomendação: "Você, pessoa física, no beta"; "Guardar só contagens"; "Excluir após 24 meses sem uso"; "Claude rascunha, advogado revisa".
- **Revisão externa** trazida pelo usuário ("Vamos revisar certinho pra eu nao ter problemas futuros"). O consultor conferiu as Resoluções CD/ANPD nº 15/2024 e nº 2/2022 em republicações (LegisWeb e Normas Brasil, não no Diário Oficial), o que corrigiu três afirmações dele: os critérios de comunicação de incidente, os prazos em dobro e os prazos dos direitos do titular.
- **Seis ajustes pedidos pelo usuário** antes da aprovação: a exceção desatualizada do prazo em dobro; a população da estatística da equipe; a garantia de que sair não muda os números; a supressão também nas alternativas removidas; o destino de todos os registros na exclusão (B.12); a revisão periódica de privilégios inativos.
- **Aprovação:** "Aprovar bloco 3" (2026-11-24), sobre a versão consolidada com os seis ajustes.
- **Registro** em duas partes, como o usuário escolheu ("Dois PRs (Recomendado)"): esta seção e a D-009 em 2026-11-25; os critérios do catálogo e as decisões do modelo conceitual em 2026-11-26 (seção I). A seção F traz o que blocos posteriores mudaram.
- **A análise jurídica deste bloco é preliminar.** As bases legais são propostas para o advogado, e nenhuma pergunta da seção E impede fechar o bloco no planejamento; elas impedem abrir o beta.

### B.1 Decisões aprovadas

- **Controlador:** o usuário, pessoa física, no beta.
- **Na exclusão da conta, as respostas viram contagens.**
- **Exclusão após 24 meses sem uso**, com aviso 30 dias antes.
- **Termos e política:** o Claude rascunha; um advogado revisa.

### B.2 Exclusão de conta: contagens e reportes

**Contagens.** Na mesma transação da exclusão, o sistema primeiro soma e depois apaga as tentativas.

- **Pessoas distintas:** para cada versão da questão, conta quantas pessoas responderam e quantas escolheram cada alternativa.
- **Qual resposta conta:** a primeira resposta de cada pessoa em cada versão, por coerência com o DES-01. Não muda nenhuma regra de desempenho do estudante.
- **Quem entra na estatística da equipe:** para cada versão de uma questão, as **pessoas distintas** cuja **primeira resposta naquela versão** foi dada no treino ou no simulado.
  - **Entram:** contas ativas e desativadas; a soma das contas excluídas, pela mesma regra; respostas dadas com gabarito preliminar.
  - **Ficam de fora:** questões em branco no simulado, porque não são tentativas (SIM-07); quem é autor, cadastrou ou revisou qualquer versão daquela questão, porque já sabia a resposta, regra que a ligação com a pessoa editorial permite (M-38); conteúdo de teste (M-29), que nunca é publicado.
  - **Período:** desde sempre, sem recorte.
- **Recálculo:** uma mudança de gabarito sempre cria versão nova (FLUXO-04, CONT-15). As contagens de cada versão continuam válidas, e a contagem por alternativa permite reavaliar as respostas antigas pelo gabarito novo, pela identidade das alternativas (M-30). Alternativa que não existe mais fica fora do cálculo, com a quantidade à vista, como no M-37.
- **Limites do bloco 2:** 10 pessoas no mínimo, "menos de 3" por alternativa e atualização diária (seção 2.D.1).
- **Proteção contra dedução:**
  - a equipe nunca vê as contagens separadas das respostas das contas ativas;
  - a estatística da equipe não tem filtro por período nem por modalidade, já que as contagens não têm data nem modalidade e um filtro permitiria subtrair;
  - **supressão complementar:** se uma alternativa aparece como "menos de 3", a segunda menor também é ocultada, para que o total menos as outras não revele o valor;
  - **alternativas removidas:** ao reavaliar respostas antigas pelo gabarito novo, a quantidade de respostas a alternativas que não existem mais aparece como "fora do cálculo" e segue as mesmas regras: abaixo de 3, "menos de 3"; se um valor oculto puder ser deduzido pela subtração, o segundo menor também é ocultado. Isso vale também ao exibir a distribuição de versões antigas.
- **Sair não muda os números:**
  - uma só função calcula as respostas das contas ativas e soma a contribuição de quem sai; na exclusão, a primeira resposta da pessoa em cada versão passa do lado "contas ativas" para o lado "contagens", com a mesma alternativa;
  - quem estava fora pela regra acima continua fora e não entra nas contagens;
  - o total exibido fica igual, tanto na saída voluntária quanto na exclusão por inatividade;
  - os números da equipe também não mudam por causa dos reportes, porque o reporte concluído guarda o registro;
  - **prova:** um critério testável, que vira teste automático (D-026), diz que a estatística da equipe antes e depois de qualquer exclusão é idêntica.
- **Depois da exclusão:** nenhuma resposta individual pode ser consultada, por construção.
- **Natureza das contagens:** agregar não é, automaticamente, anonimizar. Enquanto houver possibilidade razoável de identificação indireta (art. 12), as contagens são tratadas como dado pessoal desvinculado.
- **Tensão que fica para o advogado (Jur-04):** se elas não contarem como anonimizadas, guardá-las depois da exclusão também esbarra no art. 16, IV. O plano B é apagar a contribuição de quem saiu, e o desenho guarda as contagens à parte justamente para permitir isso.

**Reportes de quem exclui a conta.**

- **Aberto:** o texto fica sem autor até o editor concluir.
- **Concluído:** o texto livre é apagado. Ficam questão, versão, situação e mês.
- **Exceção:** obrigação legal, exercício regular de direitos ou investigação legítima, como um abuso. O administrador marca o reporte antes de concluir, com o motivo; o acesso fica restrito e registrado; o prazo é definido na marcação e revisto a cada 6 meses, com teto a definir com o advogado (Jur-06).
- **O REP-03 continua valendo para contas ativas.** Sem conta, não há a quem devolver a resposta.

### B.3 Inventário dos dados

As bases legais são todas **propostas para o advogado** (Jur-01).

| Dado | Para quê | Base legal proposta | Guarda |
|---|---|---|---|
| E-mail, senha (Argon2id), apelido | Conta e acesso | Execução de contrato (art. 7º, V) | Enquanto a conta existir |
| Tentativas, desempenho, marcações, sessões de estudo | Serviço de estudo | Execução de contrato | Enquanto a conta existir; depois, só as contagens (B.2) |
| Contagens de contas excluídas | Estatística das questões | Legítimo interesse (art. 7º, IX), se não forem anonimizadas | Por tempo indefinido; plano B em B.2 |
| Reportes | Corrigir conteúdo e responder | Execução de contrato | Conforme B.2 |
| Aceite dos termos | Prova do aceite | Exercício regular de direitos (art. 7º, VI) | Enquanto a conta existir; depois, pergunta para o advogado (Jur-05) |
| Convites | Permitir o cadastro | Procedimentos preliminares de contrato a pedido do titular (art. 7º, V), se o convite for a pedido; senão, legítimo interesse | Ver B.9 e B.12 |
| Sessões e aparelhos confiáveis | Segurança da conta | Legítimo interesse | 30 dias a sessão do estudante, 90 dias o aparelho |
| Logs e registros de segurança | Segurança e prevenção de fraude | Legítimo interesse, com avaliação escrita | Bloco 4 (seção 4) |
| Pessoa editorial e correspondência entre código e nome | Autoria e auditoria | Legítimo interesse e exercício regular de direitos | Prazo da correspondência: advogado (Jur-06) |
| Arquivo de exportação | Atender acesso e portabilidade (arts. 18 e 19) | Cumprimento de obrigação legal (art. 7º, II) | 7 dias |
| Lista de exclusões | Reaplicar exclusões após restaurar backup | Cumprimento de obrigação legal (eliminação, arts. 16 e 18) | Substituída em 2026-11-25 pelos eventos de exclusão do grupo `seguranca`, de 180 dias (resolução da 5.P.1; ver B.8) |
| Backups | Recuperação | Legítimo interesse | 30 dias (RNF-09) |

### B.4 Quem mais toca nos dados

- **AWS:** guardar em São Paulo **não elimina** fluxos internacionais.
  - Esses fluxos podem vir do suporte técnico, de subprocessadores, de acesso remoto e de serviços globais da conta.
  - Ação: conferir os termos de serviço, o adendo de proteção de dados e a lista de subprocessadores da AWS.
  - Avaliar se cabe o regulamento de transferência internacional da ANPD. O consultor acredita que seja a Resolução CD/ANPD nº 19/2024, sem ter confirmado (Jur-09).
- **Pwned Passwords:**
  - a senha continua guardada só como Argon2id;
  - na consulta, o SHA-1 da senha digitada é calculado só na memória, e só os 5 primeiros caracteres vão para o endpoint de faixa;
  - a resposta, com o cabeçalho que pede preenchimento para não revelar nada pelo tamanho, é comparada no servidor;
  - o SHA-1 completo nunca é transmitido, guardado nem registrado em log;
  - o endpoint NTLM não é usado;
  - a consulta complementa as verificações locais do bloco 1 (seção 1.B.1) e não as substitui;
  - se o prefixo é dado pessoal fica para o advogado (Jur-07).
- **Fontes:**
  - Literata e Figtree ficam no servidor do MedTeca, com a versão fixada e o arquivo de licença conferido na hora de baixar;
  - regra geral: nenhuma chamada a terceiro sem necessidade, inclusive scripts e CDNs;
  - as páginas de referência em `docs/design/` usam Google Fonts, mas são documentação, não o app.
- **Rastreamento de erros:** resolvido no bloco 4, sem serviço externo (D-032).
- **Cookies:** só os essenciais (sessão, CSRF e aparelho confiável), informados na política, sem banner. O advogado confirma (Jur-08).

### B.5 Direitos do titular

| Pedido | Prazo pela LGPD | Para pequeno porte, se o enquadramento for confirmado |
|---|---|---|
| Confirmação ou acesso, formato simplificado (art. 19, I) | Imediatamente | Até 15 dias (Res. 2, art. 15) |
| Declaração clara e completa (art. 19, II) | Até 15 dias | Em dobro, até 30 dias (Res. 2, art. 14, III) |
| Demais direitos do art. 18 (correção, eliminação, portabilidade, informação, oposição) | "Nos prazos e nos termos previstos em regulamento" (art. 18, §5º); o consultor não confirmou se a ANPD já publicou esse regulamento (Jur-13) | Em dobro, "nos termos de regulamentação específica" (Res. 2, art. 14, I) |

- **No app:** acesso, exportação, exclusão e apelido são atendidos na hora.
- **Pelo canal de privacidade:** a meta interna é 15 dias para qualquer pedido, sem contar com o prazo em dobro, o que cumpre o prazo mais curto confirmado.
- **Correção de e-mail:** pelo canal, depois de confirmar o endereço antigo e o novo.
- **Revogação de consentimento:** não se aplica, porque nenhum tratamento usa consentimento.

### B.6 Incidentes (Res. CD/ANPD nº 15/2024)

**Quando é preciso comunicar (art. 5º).** Só quando o incidente puder afetar significativamente os titulares **e**, ao mesmo tempo, envolver ao menos um destes: dados sensíveis; dados de crianças, adolescentes ou idosos; dados financeiros; dados de autenticação em sistemas; dados sob sigilo; dados em larga escala.

"Afetar significativamente" inclui impedir o exercício de direitos ou o uso do serviço, ou causar dano material ou moral (discriminação, dano à imagem, fraude, roubo de identidade).

**No MedTeca:** o critério mais provável é **dados de autenticação**: e-mails com resumos de senha, sessões e segredos de segundo fator. Um vazamento disso que permita tomar contas tende a exigir comunicação. Uma queda curta sem acesso a dados, ou um incidente contido sem dados afetados, tende a não exigir. **Todo incidente é registrado mesmo assim.**

| Etapa | Prazo geral | Pequeno porte, se confirmado |
|---|---|---|
| Comunicar a ANPD (art. 6º) | 3 dias úteis a partir de quando se soube que dados pessoais foram afetados | 6 dias úteis (art. 6º, §8º) |
| Comunicar os titulares (art. 9º) | 3 dias úteis | 6 dias úteis (art. 9º, §6º) |
| Complementar a comunicação à ANPD (art. 6º, §3º) | 20 dias úteis | 40 dias úteis (art. 6º, §8º) |
| Declarar à ANPD que os titulares foram avisados (art. 9º, §4º) | Até 3 dias úteis depois do fim do prazo dos titulares | O texto não fala em dobro |
| Registrar o incidente, comunicado ou não (art. 10) | Por no mínimo 5 anos, com o conteúdo mínimo do §1º, inclusive o motivo de não comunicar | Igual |

- **Exceção ao prazo em dobro:** a Resolução 15 (art. 2º) reescreveu o art. 14, II da Resolução 2, e a exceção de integridade física ou moral saiu da redação. Por isso ela não é aplicada.
- **Regra prática:** trabalhar sempre com os prazos gerais.

### B.7 Exclusão por inatividade e revisão de privilégios

- **O que conta como uso:** um login com sucesso, ou qualquer ação feita pela própria pessoa já conectada, como abrir uma questão. Uma sessão aberta sem uso não conta. O "último uso" é guardado só com a data do dia.
- **Estudante:** 24 meses sem uso. O aviso sai 30 dias antes, e a exclusão segue o mesmo procedimento da exclusão voluntária (CONTA-11 e B.2).
- **Equipe:** não há exclusão automática, porque a conta está ligada a responsabilidades editoriais. Os privilégios seguem a revisão abaixo, que substitui a regra de 24 meses para eles.
- **Aviso que não chega:** a exclusão segue mesmo assim, porque o aviso é uma cortesia e não uma condição. A falha de entrega fica registrada. O advogado confirma (Jur-11).
- **Cancelar:** qualquer login ou uso no período cancela. O e-mail leva à tela de entrada, sem link de cancelamento com código.
- **Depois de excluída:** a conta não volta. Um novo convite cria uma conta vazia.
- **Revisão periódica de privilégios inativos:**
  - **concessões sensíveis** (ver logs, atestar autorização, ver a correspondência entre código e nome, ver o autor de reporte) expiram sozinhas depois de **90 dias sem uso**; conceder de novo pede a passkey (bloco 1);
  - **papéis de equipe** (editor, revisor) ficam suspensos depois de **6 meses sem uso**, e só o administrador reativa; a parte de estudante da conta continua normal;
  - **revisão a cada 6 meses:** o administrador revê a lista de papéis e concessões, com a data do último uso, retira o que não é mais necessário e registra a revisão na trilha só de inclusão;
  - **o administrador** não se suspende sozinho, para ninguém trancar o sistema; o sistema avisa se ele passar 90 dias sem uso; com um único administrador, a revisão é dele mesmo; quando houver um segundo, um revisa o outro.

### B.8 Backups e lista de exclusões

Texto aprovado em 2026-11-24:

- **Finalidade:** um dado excluído pode ficar nos backups por até 30 dias. Ao restaurar um backup, o sistema reaplica todas as exclusões feitas depois dele.
- **Conteúdo:** identificador interno da conta e data da exclusão. Nada mais.
- **Onde fica:** fora do banco e fora dos backups do banco, porque um backup restaurado traria uma lista velha. Fica cifrada, com acesso só para o procedimento de restauração, e cada uso é registrado.
- **Prazo e descarte:** cada linha é apagada sozinha quando não houver mais backup anterior àquela exclusão, ou seja, 30 dias depois dela.
- **Não é anônima:** junto com um backup antigo, o identificador leva à pessoa. Por isso é tratada como dado pessoal, com acesso restrito, até ser apagada.

**Substituída em 2026-11-25 (resolução da 5.P.1).** A lista própria não é criada. A fonte única para reaplicar exclusões são os eventos de exclusão solicitada e concluída do grupo `seguranca`, guardados por 180 dias, com o marco do backup, processamento idempotente e bloqueio em caso de lacuna (seção 5.P.1; RNF-90 a RNF-94). A finalidade continua a mesma.

### B.9 Controlador, encarregado, convites e idade

- **Controlador:** o usuário, pessoa física, no beta.
  - A LGPD vale para o beta. Ele não é uso "exclusivamente particular e não econômico" (Res. 2, art. 1º, parágrafo único), porque há intenção comercial. O advogado confirma (Jur-03).
  - A passagem para uma empresa é formalizada: instrumento de transferência da base; revisão dos contratos com operadores; definição de responsabilidades; aviso aos titulares; nova política.
- **Encarregado:** a pessoa física é agente de pequeno porte (Res. 2, art. 2º) e pode não nomear encarregado (art. 11), desde que tenha canal de contato.
  - **A dispensa não se aplica a tratamento de alto risco:** um critério geral (larga escala; afetar significativamente) mais um específico (tecnologia emergente; vigilância de área pública; decisão só automatizada; dados sensíveis ou de crianças, adolescentes e idosos).
  - **Hipótese, não conclusão:** o MedTeca não se enquadra, já que é um beta pequeno, sem dado sensível e sem decisão automatizada com efeito sobre a pessoa. O advogado avalia (Jur-02).
  - O canal de privacidade existe de qualquer jeito, e a dispensa não tira as demais obrigações.
  - A Resolução 2 também permite registro de operações simplificado (art. 9º).
- **Convites:**
  - só se convida quem pediu para participar, e o convite registra quando e por onde foi o pedido;
  - o e-mail do convite diz quem convidou e por quê, traz o link da política e como pedir a exclusão do endereço;
  - o convite não usado é apagado 30 dias depois de vencer.
- **Idade:**
  - 18 anos é decisão de produto, e não garante que nenhum menor se cadastre;
  - o aceite dos termos inclui "Declaro ter 18 anos ou mais", e o beta por convite reduz o risco;
  - se o MedTeca souber de um menor, suspende o acesso, avisa por e-mail e exclui pelo procedimento normal, a menos que o advogado oriente outro caminho (art. 14; Jur-12).

### B.10 Documentos da Etapa 7

Todos são rascunhos do Claude, revisados pelo advogado antes do beta: política de privacidade; termos de uso; registro das operações de tratamento; avaliação do legítimo interesse dos registros de segurança; plano de resposta a incidentes.

Nota de 2026-11-26: a Etapa 7 foi resumida à ordem de construção e à spec da fundação. Pela ordem de construção aprovada (D-036), estes documentos passam para a preparação do beta, com o mesmo rascunho do Claude e a mesma revisão do advogado. As outras menções à "Etapa 7" neste documento seguem essa nota.

### B.11 Exceções ao ASVS

Nenhuma neste bloco.

### B.12 Destino de cada registro na exclusão da conta

| Registro | Na exclusão da conta |
|---|---|
| Tentativas, com a fotografia histórica, os horários do aparelho e do servidor e a situação de aceitação (M-07, M-32) | Somadas às contagens e apagadas, na mesma transação |
| Sessões de treino e a sequência delas (M-10) | Apagadas |
| Simulados: questões sorteadas, início, pausas, entrega e questões em branco (M-11, M-12) | Apagados; questões em branco não entram em nenhuma contagem |
| Marcações | Apagadas |
| Desempenho | Não existe guardado, porque é calculado na consulta (M-09). Regra: nenhum cache por pessoa pode sobreviver à exclusão |
| Riscos | Só existem no aparelho (RISC-06). O app apaga os dados locais da conta ao sair, e também quando percebe que a sessão deixou de existir |
| Arquivo de exportação | Apagado na hora, sem esperar os 7 dias |
| Registro de respostas afetadas por mudança de gabarito (CONT-20) | Os identificadores da pessoa saem da lista, e a quantidade total de respostas afetadas é mantida, para o registro do evento continuar verdadeiro |
| Reportes | Como em B.2 |
| Sessões de login, aparelhos confiáveis, "último uso" | Apagados |
| Aceite dos termos | Apagado, salvo orientação contrária do advogado (Jur-05) |
| Convite já usado | Apagado; o convite usado também é apagado 30 dias depois do uso |
| Tarefas pendentes da conta (e-mails e exportação, D-024) | Canceladas e apagadas |
| Logs e registros de segurança com o identificador interno | Seguem o prazo do bloco 4, sem prazo extra |
| Auditoria de ações sensíveis (M-39) e HMACs de e-mails sem conta (4.D.3) | Expiram nos prazos normais do bloco 4, sem exclusão antecipada (linhas acrescentadas no registro, conforme 4.H.8) |
| E-mails já enviados pela AWS | Seguem a guarda do operador. Conferir na consulta, junto com o adendo da AWS (Jur-09) |
| Backups | Até 30 dias; na restauração, as exclusões são reprocessadas pelos eventos do grupo `seguranca` (resolução da 5.P.1) |
| Pessoa editorial, se a conta era da equipe | Vira código (seção 2.D.4) |
| Estatística da equipe | Sem dado por pessoa; não muda (B.2) |

### C. Mudanças em decisões anteriores

Aprovadas com o bloco e registradas em 2026-11-26, com ID novo para cada regra mudada e a regra antiga mantida, marcada como substituída ou removida: o CONTA-12 foi substituído pelo CONTA-70; o CONTA-25 foi removido; M-21 e M-36 foram substituídas por M-40 (e M-21 também por M-42); M-07 e M-22 foram substituídas em parte por M-40 e M-41; a RM-13 foi substituída pela RM-19. O bloco 2 recebeu uma nota na seção 2.G.

| ID | Regra anterior | Regra aprovada | Justificativa |
|---|---|---|---|
| CONTA-12 | Manter as respostas sem identificação, para estatística | Somar em contagens de pessoas distintas por versão e alternativa, depois apagar as tentativas | Art. 16, IV e art. 12 |
| CONTA-25 | Reduzir ao mês as datas das tentativas preservadas | Removido: não sobra tentativa | Consequência do CONTA-12 |
| M-07 | Na exclusão, a fotografia histórica "continua intacta" | A tentativa e sua fotografia são apagadas depois da contagem | Consequência do CONTA-12 |
| M-21 | Tentativas preservadas e desvinculadas | Tentativas apagadas depois da contagem; o resto não muda | Idem |
| M-22 | O reporte "continua, sem autor" | Aberto: sem autor até concluir. Concluído: texto apagado, ficam questão, versão, situação e mês. Exceções restritas | Texto livre pode identificar; art. 16 |
| M-36 | Datas das tentativas reduzidas ao mês | Substituída: não sobra tentativa | Consequência |
| RM-13 | A exclusão desvincula tentativas e reportes | A exclusão soma e apaga as tentativas; os reportes seguem o M-22 novo | Idem |
| Bloco 2, respostas desvinculadas | Tratadas como dado pessoal desvinculado | O mesmo tratamento passa a valer para as contagens | Art. 12 |

**Sem mudança de regra:**

- **M-09:** o desempenho continua calculado na consulta. Conta excluída não tem desempenho, e a estatística da equipe é a visão pré-calculada que o M-09 já permite.
- **DES-01, DES-11 a DES-13, M-37:** valem como estão para contas ativas.
- **RM-09:** a fotografia nunca muda. Apagar não é alterar.
- **REP-03:** sem mudança.
- **CONT-20:** os registros de respostas afetadas por mudança de gabarito perdem os identificadores da pessoa e mantêm a quantidade total (B.12, CONTA-87).

### D. Propostas aprovadas junto com o bloco

1. A estatística da equipe usa a primeira resposta de cada pessoa em cada versão.
2. A proteção contra dedução: sem filtro de período nem de modalidade, contagens nunca exibidas à parte e supressão complementar.
3. A regra dos reportes concluídos e as exceções de guarda.
4. A definição de uso, a regra da equipe e do administrador, o aviso que não chega e o cancelamento na inatividade.
5. A lista de exclusões: conteúdo, local, prazo e acesso. Substituída pela resolução da 5.P.1 (B.8).
6. Convite só a pedido, com aviso de privacidade, apagado 30 dias depois de vencer.
7. A declaração de idade e o tratamento de menor identificado.
8. A meta interna de 15 dias para pedidos pelo canal.
9. O detalhe técnico do Pwned Passwords: SHA-1 só em memória, cabeçalho de preenchimento, sem NTLM.
10. As bases legais da tabela B.3, como proposta ao advogado.
11. A formalização da passagem para uma empresa.
12. A população da estatística da equipe e a garantia de que ela não muda com a exclusão.
13. O destino de cada registro na exclusão, inclusive limpar os dados locais do aparelho e apagar o convite usado.
14. A expiração das concessões sensíveis, a suspensão dos papéis parados e a revisão semestral.

### E. Perguntas para o advogado

Pendentes de avaliação profissional; acompanham a consulta jurídica de D-002 e as questões Jur-17 a Jur-25. Nenhuma impede fechar o bloco no planejamento, mas impedem abrir o beta.

- **Jur-01.** Bases legais de cada tratamento (B.3).
- **Jur-02.** Enquadramento como agente de pequeno porte e avaliação de alto risco (Res. 2, arts. 3º e 4º).
- **Jur-03.** Se o beta pode ser considerado não econômico, o que o consultor propõe que não seja.
- **Jur-04.** Se as contagens contam como anonimizadas (art. 12) e se podem ser guardadas depois da exclusão (art. 16, IV).
- **Jur-05.** Guarda da prova de aceite depois da exclusão.
- **Jur-06.** Prazo de guarda da correspondência entre código e nome, e teto das exceções de reportes.
- **Jur-07.** Se o prefixo enviado ao Pwned Passwords é dado pessoal.
- **Jur-08.** Cookies essenciais sem consentimento.
- **Jur-09.** AWS: transferência internacional, adendo, subprocessadores e suporte; aplicabilidade da Resolução CD/ANPD nº 19/2024, se for esse o número.
- **Jur-10.** Convites: base legal, para quem pediu e para quem não pediu.
- **Jur-11.** Exclusão por inatividade quando o aviso não chega.
- **Jur-12.** Tratamento de menor identificado (art. 14).
- **Jur-13.** Prazos dos demais direitos do art. 18: há regulamento publicado?
- **Jur-14.** Conferir no Diário Oficial o texto das Resoluções CD/ANPD nº 15/2024 e nº 2/2022, lidas em republicações.
- **Jur-15.** Metadados de questão retirada por licenciamento (D-002).
- **Jur-16.** Revisão dos termos de uso e da política de privacidade.

Na versão aprovada eram 17 perguntas; a que tratava da exceção de integridade física ou moral saiu no primeiro ajuste, e a numeração acima segue a ordem das 16 que ficaram.

### F. O que blocos posteriores mudaram

- **Bloco 4 (D-032):** o rastreamento de erros ficou sem serviço externo; os registros de segurança têm prazos e base próprios (seção 4); a auditoria de ações sensíveis e os HMACs entraram na tabela B.12, conforme 4.H.8.
- **Bloco 5 (D-033):** a AWS passa a incluir também CloudWatch Logs, S3, ECR, SSM e IAM Roles Anywhere, todos em São Paulo; a Jur-09 vale para eles. A Jur-24 trata dos backups travados e do teste de restauração com dados reais.
- **Resolução da 5.P.1 (2026-11-25):** a lista de exclusões (B.8) foi substituída pelos eventos do grupo `seguranca`.
- **Bloco 6 (D-034):** o repositório é público, e nenhum conteúdo real de questão nem dado pessoal real entra nele (seção 6.J.2).

### G. Efeitos nos documentos

Neste registro (2026-11-25), numa branch de trabalho, para revisão e merge do usuário:

- `docs/decisions.md`: D-009 aprovada, com ADR.
- `docs/adr/D-009-tratamento-de-dados-pessoais.md`: novo.
- Este documento: seção 3, cabeçalho e notas nas seções 2.E e 4.H.8.
- `docs/design-e-ux.md`: nota sobre as fontes servidas pelo próprio servidor.
- `README.md`: a D-009 sai da lista de decisões pendentes.

Na segunda parte (2026-11-26), também numa branch de trabalho, para revisão e merge do usuário:

- `docs/requisitos-mvp.md`: critérios CONTA-70 a CONTA-97, REP-04 a REP-06 e RNF-95 a RNF-97; o CONTA-12 substituído pelo CONTA-70 e o CONTA-25 removido, com as duas situações novas nas convenções; notas no CONT-20 e no CONTA-69; pendências atualizadas.
- `docs/modelo-conceitual.md`: M-40 a M-42 e RM-19; M-21, M-36 e RM-13 substituídas, e M-07 e M-22 substituídas em parte; entidade CONTAGEM no diagrama; rastreabilidade e pendências da Etapa 6.
- `docs/decisions.md`: notas na D-008 e na D-009; notas nos ADRs das duas.
- Este documento: seção I, notas nas seções 2.G e 5.P e cabeçalho.
- `README.md`: situação da Etapa 6.

### H. Fontes

Conferidas pelo consultor em 2026-11-24, em republicações:

- [Resolução CD/ANPD nº 15/2024 (LegisWeb)](https://www.legisweb.com.br/legislacao/?id=458235)
- [Resolução CD/ANPD nº 15/2024 (Normas Brasil)](https://www.normasbrasil.com.br/norma/resolucao-15-2024_458235.html)
- [Resolução CD/ANPD nº 2/2022 (Normas Brasil)](https://www.normasbrasil.com.br/norma/resolucao-2-2022_426801.html)
- [Resolução CD/ANPD nº 2/2022 (gov.br)](https://www.gov.br/palmares/pt-br/midias/arquivos-menu-acesso-a-informacao/legislacao/resolucao-cd-anpd-n2-2022.pdf)
- [Mattos Filho: regulamento de comunicação de incidente](https://www.mattosfilho.com.br/unico/regulamento-incidente-seguranca/)
- [Migalhas: agentes de tratamento de pequeno porte](https://www.migalhas.com.br/depeso/360989/a-lgpd-e-os-agentes-de-tratamento-de-pequeno-porte)
- [Agência Gov: comunicar incidente é preciso, mas nem sempre](https://agenciagov.ebc.com.br/noticias/202507/incidentes-de-seguranca-com-dados-pessoais-comunicar-e-preciso-mas-nem-sempre)

### I. Critérios no catálogo e decisões do modelo

Registrados em 2026-11-26. Os critérios de `docs/requisitos-mvp.md` transcrevem as decisões e as propostas aprovadas deste bloco no formato EARS, e as decisões de `docs/modelo-conceitual.md` substituem as da tabela C.

| Tema | Critérios | Modelo |
|---|---|---|
| Contagens na exclusão da conta (B.2) | CONTA-70, que substitui o CONTA-12 | M-40, RM-19 |
| Estatística da equipe: população, invariância na exclusão e proteção contra dedução (B.2) | CONTA-71 a CONTA-77 | M-40 |
| Datas das tentativas preservadas | CONTA-25 removido | M-36 substituída por M-40 |
| Reportes de quem exclui a conta (B.2) | REP-04 a REP-06 | M-41 |
| Inatividade (B.7) | CONTA-78 a CONTA-81 | — |
| Revisão de privilégios inativos (B.7) | CONTA-82 a CONTA-85 | — |
| Destino de cada registro na exclusão (B.12) | CONTA-86 a CONTA-90 | M-42 |
| Convites (B.9) | CONTA-90 a CONTA-92 | — |
| Idade (B.9) | CONTA-93 e CONTA-94 | — |
| Canal de privacidade e exportação (B.3, B.5) | CONTA-95 e CONTA-96 | — |
| Pwned Passwords (B.4) | CONTA-97, que detalha o CONTA-28 | — |
| Fontes, chamadas a terceiros e cookies (B.4) | RNF-95 a RNF-97 | — |

**Fora dos critérios**, por serem metas de processo ou dependerem do advogado: a meta interna de 15 dias pelo canal e a correção de e-mail (B.5); os prazos de comunicação de incidentes e o registro de todo incidente (B.6); as bases legais (B.3); os documentos da Etapa 7 (B.10).

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
- **Atualização do bloco 5 (D-033; P5-01 e P5-24):** a identidade `medteca-envio` deixa de ser um usuário IAM e passa a ser o papel `medteca-envio-registros`, assumido por certificado via IAM Roles Anywhere. As permissões e a restrição ao IP do servidor continuam as mesmas (seção 5.E).
- **Doc:** a proteção contra exclusão "blocks all deletion operations until it is explicitly disabled", e o exemplo da documentação é apagar o grupo.
- As páginas de `DeleteLogStream` e `PutRetentionPolicy` não citam a proteção. Por isso, considera-se que encurtar o prazo não é bloqueado; se apagar um fluxo é bloqueado fica para V1.

**E.3 Credencial no Lightsail**

- A credencial de envio é um segredo persistente guardado no servidor, e não uma credencial temporária obtida por um perfil de instância. Fontes antigas indicam que o Lightsail não oferece papel de instância (V4).
- O uso da credencial fica restrito ao IP fixo do servidor, por condição da política do IAM (V5).
- Fica para o bloco 5 (V5): armazenamento, permissões no sistema operacional, rotação, revogação e troca sem interromper o envio.
- **Atualização do bloco 5 (D-033):** a chave persistente foi trocada por um certificado de componente, que vale 1 ano e gera credenciais temporárias de 1 hora. Ele fica no disco adicional cifrado, só no contêiner do enviador, e a revogação é feita por lista de certificados revogados. O desenho da V5 está na seção 5.E; a prova continua pendente.

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
| Espaço reservado dos críticos | 2 GB, tamanho fixo, separado do disco principal (V9). Bloco 5: arquivo de tamanho fixo no disco adicional cifrado (seção 5.C) |
| Logs operacionais no disco principal | 500 MB e no máximo 7 dias. Resolução da 5.P.4 (2026-11-25): passam para o disco adicional cifrado, com limite técnico de tamanho (V52) |
| Registro do sistema | 500 MB e 7 dias (V20) |

Prioridades:

1. Os eventos críticos não disputam espaço: o espaço deles é reservado.
2. Abaixo de 10 GB livres no disco principal, os logs operacionais deixam de ser gravados. A contagem do que foi descartado, com o motivo "disco", vai a cada minuto para o caminho crítico, que continua gravando mesmo com o disco principal cheio. Resolução da 5.P.4 (2026-11-25): com os logs no disco cifrado, o limite de espaço e o mecanismo que protege os 2 GB reservados são definidos e provados na V52.
3. No espaço reservado:
   - **a partir de 70%:** os arquivos já enviados mais antigos são apagados antes dos 7 dias, porque já estão no CloudWatch;
   - **a partir de 80%:** alerta;
   - **em 100%:** vale a falha fechada de H.2, com alerta pelo monitor externo.
4. O banco fica no disco principal, com os alarmes de disco do bloco 5. Correção (2026-11-25): desde a D-033, o banco fica no disco adicional cifrado (5.C.2).

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

**H.7 Preservação por incidente.** Se houver um incidente, os registros do período são copiados para o registro do incidente e ficam 5 anos. Resolução da 5.P.2 (2026-11-25): além disso, só um snapshot de preservação para investigação, com autorização do usuário e cifragem provada para o tipo exato de snapshot (RNF-89, V53).

**H.8 Exclusão de conta.** Os registros, a auditoria de C.2 e os HMACs de D.3 expiram nos prazos normais, sem exclusão antecipada. Isso entra como linhas novas na tabela B.12 do bloco 3 quando ela for registrada (Jur-21). Feito em 2026-11-25 (seção 3.B.12).

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

Todas pendentes. A triagem aprovada no bloco 5 deu um destino a cada uma, sem concluir nenhuma; a situação atual está na seção 5.M.

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

## 5. Infraestrutura e operação (bloco 5, D-033)

### 5.1 Como o bloco foi decidido

- **Três rodadas de perguntas** em 2026-11-24. As doze escolhas estão na seção A.
- **Proposta** com as decisões P5-01 a P5-25.
- **Aprovação:** "Aprovo o Bloco 5 — Infraestrutura e Operação — conforme a proposta apresentada, incluindo as decisões P5-01 a P5-25, com as ressalvas e condições abaixo." (2026-11-24). As ressalvas estão em 5.3.

### 5.2 Decisões aprovadas

Todas aprovadas, respeitando as ressalvas de 5.3.

| ID | Decisão | Seção |
|---|---|---|
| P5-01 | IAM Roles Anywhere com autoridade própria, um certificado por componente, modo `credential-process`, validade de 1 ano e lista de certificados revogados | E |
| P5-02 | Papéis e permissões por componente, com condição no nome do componente e no IP de origem | E |
| P5-03 | Segredos no AWS Systems Manager Parameter Store, com inventário e política de chaves | F |
| P5-04 | Backup diário cifrado com age, num bucket S3 em São Paulo travado em modo compliance por 30 dias; o servidor só grava | G.2 |
| P5-05 | Imagens com versionamento e cópia semanal travada | G.3 |
| P5-06 | Teste mensal de restauração com reaplicação das exclusões de conta | G.4 |
| P5-07 | Disco adicional cifrado de 16 GB para dados e chaves; zram | C.2 |
| P5-08 | PostgreSQL sem porta de rede, com autenticação peer e um papel por componente | G.1 |
| P5-09 | Ubuntu LTS, Docker com configuração restrita, firewall com 80 e 443, atualizações automáticas com reinício às 4h | C |
| P5-10 | SSH com chave e porta aberta sob demanda; terminal pelo navegador desligado por padrão | D |
| P5-11 | Conta raiz da AWS com dois fatores e fora do uso diário | D |
| P5-12 | Domínio .com.br com DNSSEC, CAA e registros de e-mail | H.1, H.2 |
| P5-13 | Caddy com HTTPS automático, TLS 1.2 e 1.3 e os cabeçalhos de segurança | H.3, H.4 |
| P5-14 | Painel interno do Django só por túnel SSH; documentação da API desligada em produção | H.5 |
| P5-15 | Lista de destinos externos permitidos | H.6 |
| P5-16 | CI publicando no ECR via OIDC, com tags imutáveis e as 10 imagens mais recentes | I.1 |
| P5-17 | Deploy por comando, sem queda, com migrações em duas fases e evento de deploy | I.2, I.3 |
| P5-18 | Ambiente de teste sob demanda, sem e-mail e com segredos próprios | I.4 |
| P5-19 | Monitor Route 53 por HTTPS sem busca de texto e verificação diária do certificado | J.1, J.2 |
| P5-20 | Trilha do CloudTrail por 180 dias e regras do EventBridge | J.3 |
| P5-21 | Alertas novos do bloco 5 | J.4 |
| P5-22 | Planos de recuperação | K |
| P5-23 | Triagem das verificações V1 a V21 e verificações novas V22 a V34 | M |
| P5-24 | Mudanças em P4-15, D-027, D-010, D-005 e D-022 | B |
| P5-25 | Nenhuma declaração de conformidade com o ASVS; leitura do 12.3.1 registrada | O |

### 5.3 Ressalvas da aprovação

1. **Memória e orçamento.**
   - A configuração de 2 GB do Lightsail fica aprovada inicialmente.
   - A estimativa de consumo entre 1,3 e 1,7 GB é uma inferência, não uma medição.
   - A V28 deve comprovar o consumo real durante a operação, inclusive durante o deploy sem queda.
   - Não há aumento automático para o plano de 4 GB. Se os 2 GB forem insuficientes, o consultor apresenta os resultados, o impacto financeiro e as alternativas para decisão do usuário, considerando que o plano de 4 GB pode ultrapassar o orçamento mensal de R$ 50 a 150.
2. **Cifragem do disco.**
   - O disco adicional cifrado de 16 GB está aprovado.
   - Não está confirmado que o disco do sistema do Lightsail seja sem cifragem: a documentação disponível não foi conclusiva, e a V24 segue pendente até a confirmação técnica.
   - A separação dos dados é justificativa própria do disco adicional, que não depende só dessa hipótese.
3. **Backups e LGPD.**
   - A política de backups com Object Lock em modo compliance, 30 dias de retenção e cifragem está aprovada conceitualmente.
   - Os dados de contas excluídas podem permanecer nos backups durante o prazo de retenção, com a exclusão reaplicada na restauração.
   - A Jur-24 segue pendente de análise jurídica e não se considera resolvida só pela inclusão da informação na política de privacidade.
   - O uso de dados reais no teste mensal de restauração fica documentado para análise jurídica (5.N).
4. **Registro.**
   - A triagem das verificações está aprovada, mas nenhuma verificação foi concluída. A V22 a V34 seguem sujeitas às verificações indicadas, e a V24, em especial, segue pendente de confirmação.
   - A aprovação não é declaração de conformidade com o OWASP ASVS.

### 5.4 Autorizações recorrentes e operações sensíveis (bloco 6, 2026-11-24)

Registrado no bloco 6 (D-034), a pedido do usuário. Não aprova rotina nova nem mudança de infraestrutura.

**5.4.1 Regras do usuário** (2026-11-24):

1. **Autorizações recorrentes:** uma rotina automática aprovada pode continuar executando dentro dos parâmetros, horários, escopo e limites originalmente aprovados.
2. **Alterações nas políticas:** qualquer alteração relevante na frequência, horário, escopo, permissões, retenção ou comportamento dessas rotinas exige aprovação prévia do usuário.
3. **Novas operações:** uma operação automatizada que não esteja contemplada nas políticas aprovadas exige autorização específica.
4. **Operações manuais sensíveis:** deploy, volta da versão em produção, restauração de dados, alterações de infraestrutura, segredos, IAM e as demais operações sensíveis dependem de autorização explícita a cada operação.
5. **Revogação:** o usuário pode suspender ou revogar uma autorização recorrente a qualquer momento. A suspensão é registrada com a data e as palavras dele. Se a rotina proteger um requisito, o consultor aponta o risco, e a decisão continua do usuário.

**5.4.2 Rotinas automáticas aprovadas** (continuam autorizadas como estão):

| Rotina | Parâmetros aprovados | Origem |
|---|---|---|
| Atualizações de segurança do sistema | Instaladas todo dia; reinício às 04:00 de Brasília, só quando necessário | D-033, C.4 |
| Backup do banco | `pg_dump` às 03:00, cifrado com age, num bucket S3 em São Paulo travado por 30 dias; o ciclo de vida apaga depois do prazo | D-033, G.2 |
| Imagens das questões | Versionamento ligado e cópia completa semanal num bucket travado por 30 dias | D-033, G.3; D-022 |
| Certificado TLS | Renovação automática pelo Caddy | D-033, H.2 |
| Verificação do certificado | Diária, com aviso a 21 dias do vencimento | D-033, J.2 |
| Monitor externo | Route 53 chamando `/saude` por HTTPS a cada 30 segundos | D-033, J.1; D-032 |
| Trilha do CloudTrail | Eventos de gerenciamento guardados por 180 dias | D-033, J.3 |
| Alertas por e-mail | A lista da J.4 e os alertas do bloco 4, sem dado pessoal | D-033, J.4; D-032 |
| Credenciais temporárias da AWS | Obtidas por certificado, válidas por 1 hora | D-033, E |
| Retenção no ECR | Versão em produção e as duas anteriores que estiveram em produção, mais as 10 imagens mais recentes da `main` (ajuste do bloco 6, seção 6.F.3) | D-033, P5-16; D-034 |
| Publicação da imagem | Pelo CI, via OIDC, depois do merge na `main` | D-033, I.1; D-027; D-034 |
| Envio de registros | Contínuo, com confirmação por evento | D-032 |
| Retenção dos registros | 180 dias para `acesso`, `seguranca` e `servidor`; 30 dias para `aplicacao`; 180 dias para a auditoria no banco | D-032 |
| Cópia local dos registros | No máximo 7 dias e 500 MB; limpeza do espaço reservado a partir de 70%; eventos não enviados apagados aos 180 dias | D-032, 4.H.3 e 4.H.5 |
| Batimentos | A cada 5 minutos | D-032 |

As rotinas automáticas aprovadas nos blocos 2 e 3 (recálculo dos agregados, exclusão de contas paradas, limpeza de convites e exportações, expiração de concessões e papéis, limpeza da lista de exclusões) entram nesta tabela, com os parâmetros conferidos, quando esses blocos forem registrados.

**5.4.3 Operações periódicas manuais.** A frequência é política aprovada, mas cada execução depende de autorização explícita do usuário (regra 4):

| Operação | Frequência aprovada | Por que cada execução pede autorização |
|---|---|---|
| Teste de restauração | Mensal (RNF-10; G.4) | Cria infraestrutura e restaura dados reais (Jur-24 pendente) |
| Troca da chave do Django e das chaves do HMAC | Anual (F) | Mexe em segredos |
| Renovação dos certificados dos componentes | Anual, com aviso 30 dias antes (E) | Mexe em IAM e em certificados |

Se o teste de restauração não for autorizado num mês, o consultor avisa que o RNF-10 fica em risco.

**5.4.4 Operações sensíveis sob demanda** (autorização explícita a cada operação):

- deploy;
- volta da versão em produção;
- restauração de dados;
- migração;
- abertura da porta SSH e ligação do terminal pelo navegador;
- mudança de segredos;
- OpenTofu e qualquer recurso na AWS, inclusive o ambiente de teste e o teste de carga;
- IAM;
- DNS e domínio;
- configuração do proxy;
- reinício manual;
- mudança de plano da instância (vale a ressalva 1: sem aumento automático para 4 GB);
- o procedimento de emergência do bloco 1;
- o snapshot de preservação para investigação (5.P.2).

O Claude pode preparar e explicar essas operações, mas só as executa com a autorização explícita do usuário.

### A. Escolhas

| Tema | Escolha do usuário |
|---|---|
| Acesso do servidor à AWS | "Certificado, acesso temporário" (IAM Roles Anywhere) |
| Segredos | "Cofre da AWS" (Parameter Store) |
| Backups | "S3 em SP, travado e cifrado" |
| Montagem | "Infraestrutura como código" (OpenTofu) |
| Domínio | ".com.br no Registro.br" |
| SSH | "Porta fechada, aberta sob demanda" |
| Deploy | "Por um comando seu" |
| Ambiente de teste | "Sob demanda, criado e apagado" |
| Monitor | "Route 53 da AWS" |
| Atualizações do sistema | "Automáticas, reinício às 4h" |
| Versão nova | "Sem queda" |
| Banco | "Socket local, sem senha" |

### B. Correções e mudanças em decisões aprovadas

1. **Terminal pelo navegador.** Ele entra só com o login da AWS, sem a chave SSH. Por isso fica desligado por padrão; ligá-lo é uma mudança no firewall, que exige o console com MFA e dispara alerta. No dia a dia valem os dois portões do bloco 1 (MFA da AWS e chave SSH); numa emergência, um só, registrado. A relação com o procedimento de emergência do bloco 1 está em 5.P.3, resolvida em 2026-11-25: o terminal é a alternativa à chave SSH perdida, e o alerta não substitui a trilha do CloudTrail.
2. **Monitor.** O Route 53 verifica por HTTPS sem busca de texto, porque `/saude` responde 503 quando algo falha.
3. **P4-15 (bloco 4).** A credencial de envio de registros passa a ser um papel assumido por certificado. O RNF-24 continua valendo.
4. **D-027.** O deploy automático não é adotado; o deploy é por comando (I).
5. **D-010.** Os backups saem do bucket do Lightsail e vão para o S3 travado; o custo foi revisto (L).
6. **D-005.** O PostgreSQL fica sem porta de rede, com os dados no disco adicional cifrado.

### C. Servidor

- **C.1 Instância.** Lightsail com 2 GB em São Paulo, aprovado inicialmente (ressalva 1), com IP fixo, que não tem custo enquanto está anexado (Doc). Ubuntu LTS na versão mais recente oferecida pelo Lightsail (V22).
- **C.2 Disco adicional cifrado (16 GB, US$ 1,60 por mês).**
  - **Doc:** os discos adicionais e os snapshots do Lightsail são cifrados em repouso por padrão.
  - A documentação consultada não é conclusiva sobre o disco do sistema. Relatos em fóruns indicam que ele não seria cifrado, o que não está confirmado (V24, pendente).
  - **Justificativa:** o disco adicional separa os dados sensíveis do disco do sistema. Ele guarda, em `/srv/medteca`, os dados do PostgreSQL, o espaço reservado dos registros críticos (um arquivo de 2 GB de tamanho fixo, desenho da V9), os certificados dos componentes e o certificado TLS. Pela resolução da 5.P.4 (2026-11-25), guarda também os logs operacionais do app.
  - A área de troca de memória fica comprimida na RAM (zram), para que páginas de memória não sejam gravadas no disco do sistema (inferência).
- **C.3 Rede.** O firewall do Lightsail abre só as portas 80 e 443; a 22 abre sob demanda (D). O PostgreSQL não escuta em porta nenhuma.
- **C.4 Atualizações.** As atualizações de segurança são instaladas todo dia. Quando exigem reinício, o servidor reinicia às 04:00 de Brasília (07:00 UTC). O backup roda às 03:00.
- **C.5 Docker.**
  - contêineres sem root, com IDs de usuário fixos;
  - sistema de arquivos só de leitura onde der;
  - sem ganho de privilégio e com o mínimo de capacidades;
  - limite de memória por serviço;
  - imagens pelo digest;
  - nenhum contêiner com acesso ao socket do Docker.
- **C.6 Serviços.**
  - Caddy;
  - app web, com duas cópias durante a troca de versão;
  - executor de tarefas;
  - PostgreSQL;
  - enviadores de registros críticos e operacionais;
  - tarefas agendadas: backup, retenção, exportação da auditoria e batimentos.
- **C.7 Memória.** A estimativa é de 1,3 a 1,7 GB em uso, mais a versão nova durante a troca (inferência). A V28 mede na operação. Não há aumento automático: vale a ressalva 1.

### D. Acesso administrativo

- **SSH:** só com chave ed25519 protegida por senha (FIDO2 é opcional). Sem login por senha nem como root; um usuário administrativo, com sudo registrado no grupo `servidor`.
- **Porta 22:** fechada. O administrador a abre só para o próprio IP, pelo console ou pelo OpenTofu, com MFA, e fecha ao sair; cada abertura gera alerta (J.4).
- **Terminal pelo navegador:** desligado por padrão (B.1); ligá-lo gera alerta.
- **Conta raiz da AWS:** dois fatores de MFA cadastrados, passkey e reserva, e fora do uso diário. No dia a dia, o administrador usa o próprio usuário com MFA e os papéis do bloco 4.
- O procedimento de emergência do bloco 1 continua como aprovado (5.P.3).

### E. Credenciais da AWS (IAM Roles Anywhere)

- **Autoridade própria:** criada no computador do administrador, com a chave privada guardada com ele (gerenciador de senhas e cópia de reserva cifrada). **Doc:** o certificado da autoridade precisa ter `CA: true` e assinatura SHA-256 ou mais forte.
- **Certificados dos componentes:** um por componente, com validade de 1 ano e aviso 30 dias antes do vencimento. Cada um fica no disco cifrado, legível só pelo dono (permissão 0400), e montado só no contêiner do componente. A revogação é feita importando uma lista de certificados revogados (Doc).
- **Credenciais:** cada contêiner obtém as suas pelo modo `credential-process`. O modo `serve` não é usado, porque nele qualquer processo local pode ler as credenciais (Doc). As credenciais valem 1 hora; o serviço aceita de 15 minutos a 12 horas (Doc).
- **Custo e região:** o serviço não tem custo próprio e tem endpoint em São Paulo (fontes da seção R).

| Papel | Quem usa | Pode |
|---|---|---|
| `medteca-envio-registros` | enviadores | criar fluxos e acrescentar eventos nos quatro grupos (bloco 4) |
| `medteca-backup` | tarefa de backup | só gravar objetos no bucket de backups |
| `medteca-email` | executor de tarefas | enviar e-mail pelo SES, só com o remetente do domínio |
| `medteca-imagem` | deploy | baixar imagens do repositório no ECR |
| `medteca-segredos-<componente>` | app web e executor de tarefas | ler só os parâmetros do próprio componente |

- **Condições:** o nome do componente no certificado e o IP fixo do servidor.
- **Bucket de imagens do Lightsail:** acesso anexando a instância ao bucket, sem chave. Isso dá acesso total ao bucket (Doc), e por isso existe a cópia travada (G.3).
- Se a V4 mostrar que o Lightsail oferece papel de instância, essa opção é reavaliada.

### F. Segredos e inventário de chaves (ASVS 11.1.1, 11.1.2, 13.3.1)

| Segredo ou chave | Onde fica | Quem acessa | Troca |
|---|---|---|---|
| Chave do Django | Parameter Store, cifrada | app web e executor de tarefas | anual, aceitando a chave anterior durante a transição |
| Chaves do HMAC de e-mails sem conta | Parameter Store | app web | anual (4.D.3) |
| Chave que cifra os segredos de TOTP da equipe | Parameter Store; cifra AES-256-GCM, com a versão da chave junto do dado | app web | com nova cifragem |
| Chave pública dos backups (age, X25519) | repositório (não é segredo) | tarefa de backup | em caso de perda ou suspeita |
| Chave privada dos backups | com o administrador; nunca no servidor | administrador | idem |
| Chave privada da autoridade dos certificados | com o administrador | administrador | idem |
| Certificados dos componentes | disco cifrado, só no contêiner de cada um | o componente | anual |
| Certificado TLS público | Caddy | Caddy | automática (Doc) |
| Chave SSH | computador do administrador, com senha | administrador | em caso de perda ou suspeita |
| Senha do banco | não existe (peer) | | |

- **Política de chaves:** ciclo de vida segundo o NIST SP 800-57 (gerar, distribuir, guardar, trocar, revogar e destruir). Um segredo compartilhado fica com no máximo duas partes; uma chave privada, com uma só.
- **Leitura:** o app lê os segredos ao iniciar e os mantém só na memória. Nada em arquivo de ambiente, no Git ou na imagem.
- **Ambiente de teste:** caminhos e segredos próprios, nunca os de produção.
- **Custo:** parâmetros padrão sem custo; chave gerenciada pela AWS sem custo mensal, com franquia de 20 mil pedidos por mês (Doc).
- **Dependência:** reiniciar o app exige a AWS no ar; o que já está rodando continua funcionando.

### G. Banco e backups

**G.1 PostgreSQL**

- `listen_addresses` fica vazio: o banco não escuta em nenhuma porta de rede e só aceita conexões pelo socket local (Doc).
- O socket tem permissão 0770 para um grupo próprio (Doc).
- O banco só aceita autenticação `peer`, que funciona só em conexões locais no Linux (Doc).
- Um mapa liga o usuário do sistema de cada contêiner ao papel no banco: `medteca_app`, `medteca_exportador`, `medteca_retencao`, `medteca_dono` e `medteca_backup` (leitura de tudo, para o backup). Os IDs de usuário precisam ser iguais entre os contêineres (V34).
- **ASVS 12.3.1:** fica registrada a leitura de que não há tráfego de rede a cifrar. Se uma revisão discordar, isso vira exceção.

**G.2 Backup diário (RNF-08, RNF-09)**

- Cópia completa do banco com `pg_dump` às 03:00, cifrada com age para a chave pública.
- O destino é um bucket S3 em São Paulo, com versionamento e Object Lock em modo compliance com retenção padrão de 30 dias. **Doc:** nesse modo, ninguém apaga antes do prazo, nem a conta raiz.
- Uma regra de ciclo de vida apaga os backups depois do prazo (V25).
- O bucket bloqueia acesso público e recusa conexões sem TLS.
- O servidor só grava: não lista, não lê e não apaga.
- Aprovado conceitualmente (ressalva 3).

**G.3 Imagens.** Versionamento ligado no bucket do Lightsail (Doc) e cópia completa semanal no bucket travado, por 30 dias.

**G.4 Teste mensal de restauração (RNF-10)**

1. Acontece no ambiente de teste sob demanda.
2. O administrador assume o papel de restauração, com MFA, e a chave privada dele é carregada só na memória do ambiente.
3. O backup é restaurado e passa pelas conferências do app.
4. As exclusões de conta solicitadas ou concluídas depois do backup são reprocessadas a partir dos eventos do grupo `seguranca`, que ficam 180 dias. Resolvido em 2026-11-25 (5.P.1): os eventos são a fonte única, com o marco do backup, processamento idempotente e bloqueio em caso de lacuna (RNF-92 a RNF-94).
5. O resultado é registrado: data, backup usado, duração e achados.
6. O ambiente é apagado no mesmo dia e nunca envia e-mail.

O uso de dados reais nesse teste fica documentado para análise jurídica (Jur-24).

**G.5 Metas.** Perda máxima de 24 horas de dados (RNF-08) e recuperação em até 24 horas (resposta "Até 24 horas").

**G.6 Contas excluídas nos backups.** Os dados podem ficar até 30 dias nos backups, sem poder ser apagados antes por causa da trava, e uma restauração reaplica a exclusão. A Jur-24 segue pendente.

### H. Domínio, HTTPS e cabeçalhos

**H.1 Domínio.** .com.br no Registro.br, no CPF do usuário, registrado por vários anos e com aviso de renovação. Segundo fator na conta do Registro.br e DNSSEC no DNS gratuito (V27).

**H.2 DNS.**
- o endereço do servidor;
- IPv6, se for usado;
- CAA limitado às autoridades de certificação usadas pelo Caddy (V26);
- SPF, DKIM e DMARC, e um MAIL FROM próprio para o SES (D-023).

**H.3 Caddy**

- Certificados automáticos (Let's Encrypt, com ZeroSSL como reserva), renovação automática e redirecionamento de HTTP para HTTPS (Doc; RNF-11).
- TLS mínimo 1.2 e máximo 1.3, com padrões modernos (Doc).
- Ignora os cabeçalhos X-Forwarded-* de clientes não confiáveis e, por padrão, não confia em nenhum proxy (Doc). Isso atende a 4.D.5; a V13 confirma o cabeçalho que chega ao app.

**H.4 Cabeçalhos (V21; ASVS 3.4.x)**

- HSTS de 1 ano com subdomínios (3.4.1). Precisa ser configurado (V26). A pré-carga nos navegadores fica para depois que o site estiver estável (3.7.4, que é L3).
- CSP do bloco 4 (4.D.4).
- `nosniff`.
- `Referrer-Policy: strict-origin-when-cross-origin`, com `no-referrer` nas páginas com token.
- `frame-ancestors 'none'`.
- `Permissions-Policy` fechando câmera, microfone e localização.
- COOP e CORP `same-origin`.
- `Cache-Control: no-store` nas respostas da API com dados pessoais (14.3.2).
- `Clear-Site-Data` ao sair (14.3.1).
- Sem o cabeçalho `Server` (V26).

**H.5 Exposição (13.4.x)**

- DEBUG desligado.
- Sem listagem de diretórios; o método TRACE é recusado.
- A imagem não leva o `.git`.
- A documentação da API (OpenAPI) fica desligada em produção.
- O painel interno do Django, a administração técnica, só abre por túnel SSH. Ele é diferente do painel do editor (EDIT), que continua no app.

**H.6 Destinos externos permitidos (13.1.1, 13.2.4)**

- serviços da AWS: SSM, IAM Roles Anywhere, CloudWatch Logs, S3, ECR, SES e o bucket do Lightsail;
- Pwned Passwords;
- Let's Encrypt e ZeroSSL;
- servidores de hora;
- repositórios de pacotes do sistema.

O app só se conecta a destinos dessa lista.

### I. Deploy e ambientes

- **I.1 CI (D-027).**
  - Testes e imagem montada sem segredos.
  - A imagem é publicada no ECR em São Paulo via OIDC, com a condição de que o pedido venha do repositório do projeto e do ramo principal (Doc).
  - O ECR usa tags imutáveis e guarda as 10 imagens mais recentes. Bloco 6: a retenção foi ajustada (6.F.3).
- **I.2 Deploy por comando.** Bloco 6: o administrador é o usuário, e cada deploy ou volta de versão só acontece com a autorização explícita dele (5.4).
  1. O administrador abre a porta e roda `deploy <digest>`.
  2. O servidor baixa a imagem pelo digest e roda a fase "expandir" das migrações.
  3. A versão nova sobe ao lado da antiga, e o proxy troca para ela quando `/saude` responde bem.
  4. A versão antiga é encerrada, e o evento `deploy` (quem, digest e hora) vai para `seguranca`.

  Voltar uma versão é o mesmo comando com o digest anterior.
- **I.3 Migrações em duas fases.** "Expandir" primeiro e "contrair" numa versão seguinte; uma mudança destrutiva nunca entra junto da versão que ainda depende do formato antigo.
- **I.4 Ambiente de teste.**
  - É criado e apagado pelo OpenTofu, com papéis e segredos próprios.
  - Nunca envia e-mail.
  - Usa dados fictícios, exceto na restauração mensal.

### J. Monitoramento (complementa a seção 4.F)

- **J.1 Route 53.** Chama `/saude` por HTTPS a cada 30 segundos, de vários lugares, sem busca de texto. O alarme e o SNS ficam na região da Virgínia, onde as métricas existem (Doc). Não há dado pessoal envolvido.
- **J.2 Certificado.** O Route 53 não valida certificados (Doc), então uma tarefa diária confere a validade do certificado público e avisa quando faltarem 21 dias.
- **J.3 Trilha do CloudTrail.** Eventos de gerenciamento guardados por 180 dias num bucket em São Paulo. **Doc:** as regras do EventBridge sobre chamadas de API exigem uma trilha ativa. Esse é o desenho da V3 e da V16.
- **J.4 Alertas novos por e-mail, sem dados pessoais:**
  - porta SSH aberta;
  - terminal pelo navegador ligado;
  - mudança em papéis ou políticas do IAM, ou no bucket de backups;
  - backup ausente por mais de 26 horas;
  - certificado TLS vencendo;
  - certificado de componente a 30 dias do vencimento;
  - disco do sistema ou disco de dados acima de 80%;
  - reinício que não voltou, captado pelo monitor;
  - estado da instância (V32).

### K. Planos de recuperação

Os roteiros completos são escritos na implementação.

1. **Servidor comprometido:**
   1. isolar o servidor;
   2. preservar os registros do período no registro do incidente e, só com autorização do usuário e cifragem provada para o tipo exato, um snapshot de preservação para investigação (5.P.2);
   3. revogar os certificados e trocar todos os segredos;
   4. recriar o servidor pelo OpenTofu e restaurar o último backup bom;
   5. reprocessar as exclusões de conta pelo marco do backup (5.P.1);
   6. seguir o plano de incidentes da Etapa 7.
2. **Perda da chave privada dos backups:** gerar um novo par e fazer um backup na hora. Os backups antigos ficam ilegíveis até expirarem.
3. **Perda da chave da autoridade:** criar outra autoridade e reemitir os certificados.
4. **Perda de acesso à AWS:** recuperação pela conta raiz, com o fator de reserva.
5. **Domínio expirado:** prevenido pelo registro por vários anos e pelo aviso de renovação.
6. **Restauração completa:** em até 24 horas.
7. **Região de São Paulo fora do ar:** aguardar, porque o beta não tem segunda região.

### L. Custo estimado

| Item | US$ por mês | Base |
|---|---|---|
| Lightsail 2 GB | 12,00 | D-010 |
| Disco adicional cifrado de 16 GB | 1,60 | Doc |
| Bucket do Lightsail (imagens) | 1,00 | D-010 |
| S3 em São Paulo: backups, cópia das imagens e trilha | 0,30 a 1,00 | estimativa (V12) |
| CloudWatch | 1,00 a 3,00 | estimativa do bloco 4 (4.J) |
| Route 53 por HTTPS sem busca de texto | 1,00 a 2,75 | Doc; depende de o Lightsail contar como endpoint da AWS (V19) |
| ECR | 0 a 0,30 | Doc: US$ 0,10 por GB-mês (preço de São Paulo a confirmar, V51). Correção do bloco 6: a franquia de 500 MB por 12 meses só vale para contas criadas antes de 15/07/2025 |
| SES e ambiente de teste | 0,20 a 0,60 | estimativa |
| Parameter Store, KMS, IAM Roles Anywhere, SNS | 0 | Doc (SNS a conferir) |
| **Total** | **17 a 22** | |

Pela PTAX usada na D-010 (R$ 5,8889), o total fica entre **R$ 104 e 135 por mês**, somando o domínio (R$ 40 por ano). Fora disso ficam o IOF, se a cobrança for em dólar, ou os impostos locais, se a AWS faturar em reais (V29). A estimativa da D-010 era de cerca de R$ 77. O valor continua dentro do orçamento de R$ 50 a 150, mas perto do teto. Um plano de 4 GB não está incluído (ressalva 1).

### M. Verificações

Triagem aprovada no bloco 5. **Nenhuma verificação foi concluída.** "Desenho decidido" quer dizer que o bloco definiu o caminho; falta fazer e provar.

| V | O que verificar | Situação |
|---|---|---|
| V1 | Proteção contra exclusão: se cobre fluxos e mudança de prazo; custo; registro no CloudTrail | Pendente: provar na implementação |
| V2 | Entrada nos papéis e sessões do IAM Roles Anywhere no histórico do CloudTrail; classificação das consultas ao CloudWatch Logs; custo dos eventos de dados. O RNF-20 depende disso | Pendente: provar na implementação |
| V3 | Mecanismo do alerta de mudança na proteção, no prazo ou na política | Desenho decidido (J.3); falta configurar e provar |
| V4 | Papel de instância no Lightsail | Pendente; com o IAM Roles Anywhere adotado, reavaliar só se o papel existir |
| V5 | Credencial de envio: armazenamento, permissões, rotação, revogação, troca sem interrupção e IP | Desenho decidido (E); falta provar |
| V6 | Ações do IAM exatas por identidade e prova negativa | Pendente: descrever no OpenTofu e provar |
| V7 | Enviador que cumpra 4.H.4 | Pendente: escolher e provar na implementação |
| V8 | Modo não bloqueante do Docker e contagem de descartes | Pendente: provar |
| V9 | Mecanismo do espaço reservado | Desenho decidido (C.2); falta provar |
| V10 | Fonte de hora no Lightsail e relógio que volta | Pendente: conferir (chrony; fonte a definir) |
| V11 | Comportamento dos alarmes: dado ausente, mudança de estado, INSUFFICIENT_DATA, filtros, eventos atrasados e volume | Pendente: provar |
| V12 | Preços em São Paulo e nível gratuito | Pendente: estimativa em L; fechar com a calculadora e a primeira fatura |
| V13 | Proxy: cabeçalho de IP; logs sem IP, query string ou fragmento; erros de TLS | Desenho decidido (H.3); falta provar |
| V14 | Parâmetros de log do PostgreSQL | Pendente: provar |
| V15 | Backups e cópias de disco sem registros | Desenho decidido (G.2: só `pg_dump`, sem snapshots); falta provar |
| V16 | Trilha do CloudTrail por mais de 90 dias | Desenho decidido (J.3: 180 dias); falta configurar |
| V17 | Papéis no banco, RETURNING e fila na mesma transação | Pendente: provar |
| V18 | Segredos: chaves do HMAC e credencial de envio | Desenho decidido (F); falta provar |
| V19 | Monitor externo | Desenho decidido (J.1); falta conferir se o Lightsail conta como endpoint da AWS |
| V20 | Limites de taxa e cotas do journald | Pendente: configurar e provar |
| V21 | CSP e cabeçalhos | Desenho decidido (H.4); falta provar |
| V22 | Ubuntu LTS disponível no Lightsail | Pendente: conferir |
| V23 | Como o terminal pelo navegador do Lightsail autentica e se o acesso fica registrado | Pendente: conferir |
| V24 | Cifragem do disco do sistema (não documentada) e dos discos adicionais (documentada) | **Pendente de confirmação técnica** (ressalva 2) |
| V25 | Object Lock com ciclo de vida, marcadores de exclusão e custo em São Paulo | Pendente: conferir |
| V26 | HSTS, cabeçalho `Server` e CAA no Caddy | Pendente: conferir |
| V27 | Registro.br: segundo fator, DNSSEC e dados públicos do titular | Pendente: conferir |
| V28 | Consumo real de memória, inclusive no deploy sem queda | **Pendente: medir na operação** (ressalva 1) |
| V29 | Faturamento da AWS no Brasil: dólar com IOF ou real com impostos locais | Pendente: conferir |
| V30 | Parameter Store: histórico de versões e registro das leituras | Pendente: conferir |
| V31 | Regras do EventBridge para as chamadas do Lightsail | Pendente: conferir |
| V32 | Alarme de estado da instância do Lightsail: custo e limites | Pendente: conferir |
| V33 | ECR: transferência para o Lightsail e varredura de imagens | Pendente: conferir. Bloco 6: a varredura ganhou desenho (6.F.2); a transferência segue sem documentação, com estimativa de pior caso em 6.K |
| V34 | Autenticação peer entre contêineres, com IDs de usuário iguais | Pendente: provar |

### N. Questões jurídicas

Pendente de avaliação profissional; acompanha a consulta jurídica de D-002 e as questões Jur-17 a Jur-23 (4.M).

- **Jur-24.** Duas partes:
  - **(a)** Dados de contas excluídas ficam nos backups por até 30 dias e não podem ser apagados antes por causa da trava (Object Lock em modo compliance). Uma restauração reaplica a exclusão. Isso é compatível com a LGPD (art. 16 e art. 18)?
  - **(b)** O teste mensal de restauração usa dados reais num ambiente temporário, com as mesmas proteções da produção, apagado no mesmo dia. Esse uso precisa de base legal ou de registro próprio?

  A questão não se considera resolvida só pela inclusão dessas informações na política de privacidade.

### O. ASVS

- **Requisitos cobertos pelo desenho deste bloco, sem prova ainda:**
  - 3.4.1 e 3.4.3 a 3.4.6 (cabeçalhos);
  - 11.1.1 e 11.1.2 (política de chaves e inventário, seção F);
  - 12.1.x e 12.2.x (TLS no Caddy);
  - 13.1.1, 13.2.1 a 13.2.4, 13.3.1, 13.3.2 e 13.4.1 a 13.4.5;
  - 14.3.1 e 14.3.2.
- **Leitura registrada, que pode virar exceção:** o 12.3.1, pelo socket local sem rede.
- **A aprovação deste bloco não é declaração de conformidade com o OWASP ASVS.** Nenhuma declaração é feita antes das verificações e das provas (P4-19, P5-25).

### P. Inconsistências registradas para avaliação

Encontradas durante o registro do bloco 5. **Resolvidas pelo usuário em 2026-11-25** ("Aprovar"), depois de duas revisões pedidas por ele. Cada item mantém a descrição original da divergência e traz a resolução aprovada. Os ajustes nos textos dos blocos 1 e 3 entram no registro desses blocos.

1. **Fonte das exclusões reaplicadas na restauração.**
   - **Bloco 3** (seção B.8, aprovada e ainda não registrada): uma lista de exclusões própria, com só o identificador interno e a data. Fica fora do banco e dos backups, cifrada, com acesso só na restauração e registro de cada uso. Cada linha é apagada 30 dias depois da exclusão, e a lista é tratada como dado pessoal.
   - **Bloco 5** (G.4): reaplica a partir dos eventos de exclusão concluída do grupo `seguranca`, que ficam 180 dias.
   - **Divergência:** duas fontes diferentes, com prazos e controles diferentes. O critério RNF-51 vale para qualquer das duas. Pendente: decisão do usuário.
   - **Resolução aprovada (2026-11-25):** a fonte única são os eventos do grupo `seguranca`.
     - **Dois eventos**, gravados pelo caminho crítico do bloco 4: "exclusão solicitada", antes de o pedido ser confirmado, e "exclusão concluída", antes de a exclusão ser dada por concluída (RNF-90).
     - **Conteúdo:** o identificador pseudônimo estável da conta (nunca o e-mail, RNF-16), o identificador do pedido, o horário em UTC e o marco da transação no banco.
     - **Integridade:** gravação só por acréscimo, com `id` único e `seq` por processo; nenhuma identidade do app altera eventos; credencial de envio que só acrescenta; o CloudWatch não tem operação para editar um evento individual (Doc); proteção contra exclusão do grupo (RNF-93). Risco residual: quem tiver root no servidor pode alterar eventos ainda não enviados; o envio rápido limita esse risco, e a `seq` revela lacunas.
     - **Ordem de gravação:** o pedido é gravado no banco, depois o evento, e só então o pedido é confirmado ao estudante. Se o evento falhar, o pedido não é confirmado, e uma reconciliação regrava o evento antes de seguir (V55).
     - **Marco do backup:** o backup exporta o snapshot do banco (`pg_export_snapshot`), e o `pg_dump` usa esse snapshot (`--snapshot`); o manifesto do backup grava o marco do snapshot (`pg_current_snapshot`) e o identificador do cluster; cada evento leva o ID da transação (`pg_current_xact_id`). Na restauração, é reprocessado todo pedido cujo evento não está visível no snapshot do backup (`pg_visible_in_snapshot`, a confirmar na V55), de forma idempotente pelo identificador do pedido e decidindo pelo estado do banco restaurado (RNF-92). Uma margem de 24 horas no horário fica só como rede de segurança, para eventos cujo marco não dê para avaliar. Alternativas descartadas: só o horário UTC, frágil diante do relógio, da duração do dump e de transações longas; e o número sequencial do pedido, porque a ordem dos números não é a ordem dos commits.
     - **Lacunas:** a conferência verifica a continuidade da `seq` no período a reprocessar; se houver lacuna, o banco restaurado fica bloqueado até a conferência manual do usuário (RNF-94).
     - **Acesso:** a leitura dos eventos na restauração usa o papel de leitor dos registros, com MFA, e fica registrada (RNF-20).
     - **Efeitos:** a lista própria do bloco 3 (B.8) sai no registro do bloco 3 (feito em 2026-11-25: seção 3.B.8, marcada como substituída). A Jur-24 passa a considerar também essa fonte: o identificador pseudônimo continua sendo dado pessoal enquanto houver possibilidade de reidentificação, por exemplo pelos backups de até 30 dias.
2. **Preservação de evidências e RNF-45.**
   - **Bloco 5** (K.1): preservar as evidências de um servidor comprometido no registro do incidente.
   - **Bloco 4** (RNF-45 e 4.H.7): o RNF-45 proíbe cópias de disco com a pasta de registros e o espaço reservado; o 4.H.7 só prevê copiar os registros do período para o registro do incidente.
   - **Divergência:** uma cópia forense do disco incluiria os registros, o espaço reservado e dados pessoais. Pendente: se a cópia forense é permitida num incidente, com que prazo e com que acesso.
   - **Resolução aprovada (2026-11-25):** o termo passa a ser "snapshot de preservação para investigação".
     - Por padrão, só os registros do período vão para o registro do incidente (4.H.7).
     - **Nenhum snapshot é tratado como cifrado sem prova para o tipo exato de snapshot** (V53). Até a V53 provar, não se faz snapshot de preservação.
     - **Se só o disco adicional tiver a cifragem provada,** só o snapshot de disco pode ser autorizado, com a limitação escrita: ele preserva o banco, os logs operacionais do app, o espaço reservado dos eventos críticos e os certificados; não preserva o disco do sistema (sistema operacional, binários, configuração, tarefas agendadas, registro do sistema e, se ficarem nele, imagens e contêineres do Docker), onde costumam estar os vestígios de uma invasão.
     - **O snapshot da instância inteira**, que inclui os discos anexados (Doc), só pode ser autorizado depois de provada a cifragem de todos os componentes.
     - **Sempre:** autorização explícita do usuário naquele incidente (5.4); nunca restaurado em produção; apagado ao fechar o incidente ou em até 90 dias; custo de US$ 0,05 por GB por mês enquanto existir (Doc).
     - **Acesso exclusivo, em termos de IAM:** só a identidade administrativa do usuário, com MFA exigido por política, tem as permissões do Lightsail sobre snapshots (criar, listar e ler, criar instância ou disco a partir dele, copiar, exportar e apagar). Nenhum papel de componente (`medteca-*`), nem o papel do CI, nem os papéis do ambiente de teste têm essas permissões. Exportar para o EC2 e copiar para outra região ou conta ficam negados de forma explícita. A conta raiz não pode ser restringida pelo IAM; ela é do usuário, com dois fatores e fora do uso diário (5.D). Se alguma dessas ações não aceitar restrição por recurso ou por etiqueta, a restrição vale para a ação na conta inteira (V53).
     - O RNF-45 mantém o texto; a exceção está no RNF-89.
3. **Procedimento de emergência do bloco 1 e terminal pelo navegador.**
   - **Bloco 1** (aprovado e ainda não registrado): o procedimento de emergência do único administrador exige login na AWS com MFA mais a chave SSH.
   - **Bloco 5** (B.1, P5-10): o terminal pelo navegador fica desligado e é ligado só em emergência. Ele entra só com o login da AWS, um portão, com registro e alerta.
   - **Divergência:** numa emergência sem a chave SSH, o caminho do bloco 5 tem um portão só. Pendente: confirmar se esse caminho vale para o procedimento do bloco 1 e ajustar o texto do bloco 1 no registro dele.
   - **Resolução aprovada (2026-11-25):** o procedimento de emergência fica preservado.
     - A chave SSH local é o caminho normal. Se ela se perder, o terminal pelo navegador é a alternativa: ligado com alerta (J.4), com registro e revisão depois. Em seguida, o terminal é desligado, uma chave nova é cadastrada e a antiga é revogada.
     - O prazo de 7 dias para a revisão é uma **proposta ainda não aprovada**.
     - **O alerta não substitui o registro de auditoria.** Ele depende do EventBridge, que recebe as chamadas de API pelo CloudTrail, e os serviços da AWS entregam eventos ao CloudTrail em regime de melhor esforço (Doc). O registro é a trilha do CloudTrail de 180 dias (J.3) e os registros do servidor; a revisão confere a trilha, não o alerta.
     - O CloudTrail registra a chamada de API que dá o acesso, não os comandos digitados no terminal. Os comandos com `sudo` ficam no grupo `servidor` (5.D).
     - A V54 verifica o evento real da abertura da conexão (candidato: `GetInstanceAccessDetails`, que devolve chaves SSH temporárias, Doc), a identidade da AWS usada, o MFA ou a passkey exigidos e o disparo do alerta.
     - No registro do bloco 1, o texto passa a dizer que a fronteira real é a conta da AWS, protegida por passkey; a chave SSH protege contra erro e contra roubo isolado, mas não é barreira independente contra quem controla a conta da AWS (Inferência).
4. **Disco do sistema e logs operacionais (menor).**
   - **Bloco 5** (C.2): nada sensível fica no disco do sistema.
   - **Bloco 4** (4.H.3 e 4.G.2): os logs operacionais ficam no disco principal, e os relatos do navegador podem guardar resíduo de dado pessoal mesmo depois do saneamento (Jur-22).
   - **Divergência:** pode haver resíduo de dado pessoal no disco do sistema, cuja cifragem segue sem confirmação (V24). Pendente: aceitar o resíduo ou levar os logs operacionais para o disco cifrado.
   - **Resolução aprovada (2026-11-25):** os logs operacionais do app ficam no disco adicional cifrado, com limite técnico de tamanho (RNF-91). O registro do sistema operacional continua no disco do sistema, sem dados de estudantes.
     - O método de implementação fica pendente até a V52.
     - A V52 precisa provar a proteção dos 2 GB reservados aos eventos críticos por um mecanismo técnico verificável (sistema de arquivos próprio, cota ou equivalente), e não só por monitoramento de espaço livre. A prova é um teste de enchimento: os logs chegam ao limite e o resto do disco é ocupado, e a gravação crítica, o banco e o app continuam funcionando. Um arquivo pré-alocado só protege se não for esparso e se o sistema de arquivos não fizer cópia na escrita (Inferência).

**Verificações das resoluções.** Nenhuma foi concluída.

| V | O que verificar | Situação |
|---|---|---|
| V52 | Mecanismo técnico que protege os 2 GB reservados (sistema de arquivos próprio, cota ou equivalente); onde os arquivos ficam gravados; rotação e limites de 500 MB e 7 dias; teste de enchimento provando a gravação crítica, o banco e o app; método de implementação e limites definidos a partir dessa prova | Pendente: provar |
| V53 | Cifragem provada para cada tipo de snapshot (de disco e de instância, incluindo o disco do sistema); permissões do IAM para cada ação sobre snapshots e se elas aceitam restrição por recurso ou por etiqueta; negação de exportar e copiar; consistência do snapshot com a instância ligada; custo; exclusão dentro do prazo | Pendente: provar |
| V54 | Terminal pelo navegador: evento real do CloudTrail na abertura da conexão; identidade usada; MFA ou passkey exigidos; prova do disparo do alerta, sabendo que a entrega é de melhor esforço. Complementa a V23 e a V31 | Pendente: provar |
| V55 | Marco do backup: `pg_export_snapshot` com `pg_dump --snapshot`; marco e identificador do cluster no manifesto; ID da transação em cada evento; teste de visibilidade (`pg_visible_in_snapshot`, a confirmar); ordem de gravação entre pedido e evento; teste de restauração com pedidos em andamento durante o dump e com uma lacuna simulada | Pendente: provar |

### Q. Efeitos nos documentos

Registrado em 2026-11-24:

- `docs/decisions.md`:
  - D-033 aprovada, com ressalvas e com ADR;
  - notas em D-005, D-010 (com o trecho dos backups substituído), D-022, D-027 e D-032.
- ADRs:
  - novo `docs/adr/D-033-infraestrutura-e-operacao.md`;
  - notas de atualização nos ADRs de D-005, D-010 e D-032.
- `docs/requisitos-mvp.md`: critérios RNF-46 a RNF-69 e três pendências novas.
- Este documento:
  - seção 5;
  - notas nas seções 4.E.2, 4.E.3, 4.H.3 e 4.L.
- `README.md`.

Fica para quando o registro dos blocos 1 e 3 for autorizado:

- o ajuste do procedimento de emergência (5.P.3);
- a fonte das exclusões (5.P.1).

As duas divergências foram resolvidas em 2026-11-25 (5.P); o que muda nos textos dos blocos 1 e 3 entra no registro deles (feito em 2026-11-25: seções 1.B.5 e 3.B.8).

### R. Fontes conferidas em 2026-11-24

- **IAM Roles Anywhere:**
  - [introdução](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html);
  - [modelo de confiança](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/trust-model.html);
  - [assistente de credenciais](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/credential-helper.html);
  - [endpoints](https://docs.aws.amazon.com/general/latest/gr/rolesanywhere.html);
  - [anúncio sem custo adicional](https://aws.amazon.com/about-aws/whats-new/2023/12/iam-roles-anywhere-additional-aws-regions/).
- **Lightsail:**
  - [preços](https://aws.amazon.com/lightsail/pricing/);
  - [permissões de bucket](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-understanding-bucket-permissions.html);
  - [snapshots](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-instance-snapshots-in-amazon-lightsail.html);
  - [disco adicional cifrado](https://aws.amazon.com/lightsail/features/highly-available-storage/);
  - [regras de firewall](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-editing-firewall-rules.html).
- **Segredos:** preços do [Parameter Store](https://aws.amazon.com/systems-manager/pricing/), do [Secrets Manager](https://aws.amazon.com/secrets-manager/pricing/) e do [KMS](https://aws.amazon.com/kms/pricing/).
- **S3:** [Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html).
- **Route 53:** [preços](https://aws.amazon.com/route53/pricing/) e [monitoramento das verificações](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-health-checks.html).
- **Eventos:** [EventBridge e CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) e [serviços do CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html).
- **ECR:** [preços](https://aws.amazon.com/ecr/pricing/).
- **GitHub:** [ambientes](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment) e [OIDC com a AWS](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services).
- **Caddy:** [reverse_proxy](https://caddyserver.com/docs/caddyfile/directives/reverse_proxy), [HTTPS automático](https://caddyserver.com/docs/automatic-https) e [TLS](https://caddyserver.com/docs/caddyfile/directives/tls).
- **PostgreSQL 18:** [autenticação peer](https://www.postgresql.org/docs/18/auth-peer.html) e [conexões](https://www.postgresql.org/docs/18/runtime-config-connection.html).
- **Domínio:** [Resolução CGI.br 2008/008](https://cgi.br/resolucoes/documento/2008/CGI.br_Resolucao_2008_008.pdf) e [valor anual do .br](https://teletime.com.br/14/10/2026/br-6-milhoes/), em fontes secundárias a confirmar no site do Registro.br.
- **UptimeRobot:** [termos](https://uptimerobot.com/terms).
- **Cifragem do disco do Lightsail:** [discussão](https://repost.aws/questions/QUdJ1KRZVbSla6QjzytIQ6DA/are-lightsail-system-discs-encrypted), uma fonte não oficial e inconclusiva (V24).

## 6. Qualidade e cadeia de suprimentos (bloco 6, D-034)

### 6.1 Como o bloco foi decidido

- **Fato que moldou o bloco:** o repositório no GitHub é público, conferido em 2026-11-24 com um `git ls-remote` sem credencial. Isso torna gratuitos CodeQL, varredura de segredos com bloqueio no envio, revisão de dependências, atestados de origem e regras de proteção de branch (Doc). Em troca, logs e artefatos do CI ficam visíveis para qualquer conta do GitHub (Doc, na documentação do GitHub Enterprise Server; V48).
- **Três rodadas de perguntas** em 2026-11-24. As escolhas estão na seção A.
- **Correções do usuário antes da aprovação**, em 2026-11-24, na seção B.
- **Aprovação:** "Aprovar bloco 6" (2026-11-24).
- **Registro autorizado:** "Sim. Autorizo o registro documental do Bloco 6 agora, em uma branch de trabalho." (2026-11-24).

### 6.2 Decisões aprovadas

| ID | Decisão | Seção |
|---|---|---|
| P6-01 | Toda mudança entra por pull request, com a regra da `main` configurada pelo usuário; cada fase do `tasks.md` vira um pull request previsto, com no máximo cerca de 400 linhas escritas à mão | C.1, C.7 |
| P6-02 | Publicação só a partir da `main`, depois dos portões; registro de cada versão; atestado de origem conferido no computador do usuário antes do deploy | F |
| P6-03 | O usuário revisa o código de todo pull request; a revisão por outra sessão do Claude e a revisão de segurança são camadas adicionais | C.5 |
| P6-04 | Prévia e ambiente de desenvolvimento no computador do usuário, em contêineres, com dados fictícios | C.8 |
| P6-05 | Definição de pronto em quatro níveis | C.9 |
| P6-06 | Portões do CI | D |
| P6-07 | uv e pnpm, instalação só pelo lockfile, fontes de pacotes fixas | E.1 |
| P6-08 | Espera de 7 dias para versões novas; correção de segurança na hora, com exceção registrada | E.2 |
| P6-09 | Scripts de instalação das dependências bloqueados e travas do pnpm | E.3 |
| P6-10 | Ações do GitHub fixadas pelo commit completo, com política do repositório, zizmor e permissões mínimas | E.4 |
| P6-11 | Dependabot semanal e agrupado, com revisão do usuário | E.5 |
| P6-12 | Prazos de correção, exceções com validade e barreira na publicação | E.6 |
| P6-13 | Política de licenças | E.7 |
| P6-14 | Inventário CycloneDX de cada imagem, varredura e reconferência diária | F.2 |
| P6-15 | CodeQL e regras de segurança no lint | G.1 |
| P6-16 | Segredos: bloqueio no envio, gitleaks e roteiro para vazamento | G.2 |
| P6-17 | Matriz do ASVS L2 com a prova de cada requisito | H.1 |
| P6-18 | Varredura dinâmica com o OWASP ZAP no CI | H.2 |
| P6-19 | Revisão de segurança completa antes do beta; teste de invasão decidido antes da abertura | H.3 |
| P6-20 | Teste de carga antes do beta e antes da abertura | H.4 |
| P6-21 | Testes de mutação nas regras críticas, antes de cada versão | H.5 |
| P6-22 | Volta de código, volta da versão em produção e restauração de dados como operações distintas; checagem automática depois do deploy | I.1 |
| P6-23 | Manutenção mensal | I.2 |
| P6-24 | Código de terceiros só em contêineres no computador de desenvolvimento | J.1 |
| P6-25 | Regras para o repositório público | J.2 |
| P6-26 | `SECURITY.md` e relato privado de vulnerabilidades | J.3 |
| P6-27 | Explicação técnica de cada pull request | C.6 |
| P6-28 | Identidade única no GitHub; merge exclusivamente manual pelo usuário; escopo da autorização dado pela aprovação da spec e do `tasks.md` | C.2 a C.4 |

### 6.3 O que não foi decidido

- **Recomendações pendentes de decisão do usuário**, não aprovadas como decisão:
  - aceitar só o merge por rebase, com histórico linear;
  - ativar a restrição de exclusão da `main`, que não estava ativa em 2026-11-24 (V50);
  - incluir as checagens obrigatórias na regra da `main` quando o CI existir.
- **Sem declaração de conformidade com o ASVS.** Nenhuma declaração é feita antes das verificações e das provas (P4-19, P5-25).
- **A aprovação não autoriza** implementação, mudança no GitHub, recurso na AWS nem deploy (D-017; seção 5.4).
- **Nenhuma verificação da V35 a V51 foi concluída.**

### A. Escolhas

| Tema | Escolha do usuário |
|---|---|
| Fluxo | "Pull request com checagens" |
| Revisão | "Revisor independente + você", corrigida pelo usuário: "EU QUERO LER E REVISAR O CÓDIGO." (B.1) |
| Dependências | "Espera de 7 dias e travas" |
| Prazos de correção | "Crítica 3 dias, alta 14, média 30" |
| Inventário | "Junto da imagem, reconferido todo dia" |
| Segurança | "Matriz ASVS + varredura; teste externo na abertura" |
| Prévia | "No seu computador" |
| Licenças | "Permissivas livres, copyleft com aval" |
| Desenvolvimento local | "Dentro de contêineres" |
| Mutação | "Nas regras críticas" |
| Reversão | "Voltar primeiro" |
| Carga | "Antes do beta e da abertura" |
| Garantia da aprovação | Identidade única, com merge exclusivamente manual pelo usuário (B.2) |
| Escopo da autorização | "Sim": a aprovação da spec e do `tasks.md` autoriza commits, push e pull requests (B.3) |

### B. Correções do usuário antes da aprovação

1. **Revisão do código.** A proposta partiu de uma premissa errada do consultor: que o usuário só conferiria telas. Correção do usuário: "EU QUERO LER E REVISAR O CÓDIGO." Ele é estudante de Engenharia de Software e desenvolvedor júnior e quer aprender com o projeto. A revisão dele passou a ser a principal (C.5), e cada pull request traz explicação técnica (C.6).
2. **Merge.** O usuário escolheu identidade única no GitHub, com merge exclusivamente manual por ele, sem conta separada para o Claude (C.2 a C.4).
3. **Escopo da autorização.** A aprovação explícita da spec e do `tasks.md` autoriza implementar, fazer commits e push na branch de trabalho e criar ou atualizar os pull requests das fases previstas (C.3).
4. **ECR e custos.** Repositório privado, custo revisto e política de retenção (F, K).
5. **Volta de versão.** Volta de código, volta da versão em produção e restauração de dados ficaram separadas; nenhuma operação que altere a produção acontece sem autorização explícita (I.1; seção 5.4).
6. **Regra da `main`.** Registrado o que está ativo; o resto ficou como recomendação pendente (C.1; 6.3).
7. **Autorizações recorrentes.** As rotinas automáticas já aprovadas continuam valendo, com as cinco regras do usuário (seção 5.4).

### C. Fluxo, revisão e definição de pronto

**C.1 Regra da `main`** (P6-01). Configurada pelo usuário e conferida pela API pública em 2026-11-24:

- push forçado bloqueado (`non_fast_forward`);
- pull request obrigatório, com zero aprovações e conversas resolvidas antes do merge;
- métodos de merge permitidos: merge, squash e rebase;
- lista de bypass vazia, informada pelo usuário (não aparece na consulta pública);
- não ativos: restrição de exclusão, histórico linear e checagens obrigatórias (6.3).

| Regra | Garantia |
|---|---|
| Nada de push direto na `main` | Técnica: pull request obrigatório e bypass vazio |
| Nada de push forçado na `main` | Técnica (`non_fast_forward`) |
| Merge só com as conversas resolvidas | Técnica |
| Nada de auto-merge | Técnica, se "Allow auto-merge" ficar desligado nas configurações do repositório (V50) |
| Merge só pelo usuário | Operacional |
| Merge só depois da revisão do usuário e de nova revisão após commits novos | Operacional |
| Checagens do CI antes do merge | Ainda não existe; vira técnica quando o usuário incluir as checagens obrigatórias na regra |

**Limitação técnica.** O usuário e o Claude usam a mesma identidade autenticada no GitHub. Com essas permissões, o Claude conseguiria tecnicamente fazer merge pela API ou pela interface, e a regra da `main` não impede isso, porque não exige aprovação; uma aprovação vinda da mesma conta nem seria possível. A proibição de merge é uma regra operacional explícita, não uma garantia técnica do GitHub. O registro do GitHub também não distingue quem fez o merge.

**C.2 Fluxo de um pull request** (P6-28):

1. O Claude cria uma branch de trabalho e nunca implementa direto na `main`.
2. O Claude implementa, testa, documenta, faz commits e envia as alterações para a branch.
3. O Claude abre ou atualiza o pull request.
4. O Claude apresenta a explicação técnica completa, os arquivos modificados, os testes e os resultados.
5. O usuário lê e revisa o código, pergunta e pede alterações quando necessário.
6. Quando estiver satisfeito, o usuário faz o merge pela interface do GitHub.

**C.3 Escopo da autorização** (P6-28):

| Autorizado pela aprovação explícita da spec e do `tasks.md` | Não autorizado |
|---|---|
| Implementar as tarefas aprovadas | Push direto na `main` |
| Fazer commits na branch de trabalho | Alteração relevante fora do escopo aprovado |
| Enviar os commits para essa branch no repositório remoto | Merge de qualquer pull request |
| Criar e atualizar os pull requests das fases previstas | Ativar auto-merge |
| Fazer, na mesma branch, as alterações pedidas pelo usuário na revisão, e reapresentá-las | Deploy ou publicação sem autorização específica |

- **Alteração relevante fora do escopo:** qualquer mudança que não esteja no `tasks.md` e que mexa em comportamento para o usuário, arquitetura, dependência nova, modelo de dados ou migração, segurança ou permissões, CI, workflows ou infraestrutura. Ajustes triviais nos arquivos já tocados podem entrar e são citados na explicação técnica.
- **Correções sem spec** (falhas de dependências, ajustes em pull requests do Dependabot, manutenção mensal): um pedido explícito do usuário para aquela correção vale como autorização daquele escopo, com as mesmas proibições.
- **Documentos do planejamento:** sem spec, commit e push continuam só a pedido do usuário; o push vira o envio da branch e a abertura do pull request, com merge do usuário.

**C.4 Regras obrigatórias de trabalho** (P6-28; valem também quando o usuário escrever código):

- o Claude nunca faz merge de pull request, nem por comando, nem por chamada de API, nem pela interface;
- o Claude não habilita auto-merge nem "merge when ready";
- o Claude não envia nada direto para a `main`;
- uma revisão não está concluída enquanto o usuário não tiver tido oportunidade de analisar o diff;
- depois de commits novos, o Claude apresenta de novo as alterações para revisão;
- quando um pull request está pronto, o Claude para e espera a decisão do usuário;
- o recurso de correção automática do app (Auto-fix) fica desligado, a menos que o usuário o ligue num pull request específico; mesmo assim, cada envio é reapresentado.

**C.5 Revisão** (P6-03):

- **A revisão do usuário é a principal e não tem substituto.** Ele lê o código de todos os pull requests, analisa as alterações, questiona decisões, sugere mudanças, entende o impacto na arquitetura e nas funcionalidades existentes e pede explicações antes do merge.
- **Camadas adicionais, antes da apresentação ao usuário:**
  - outra sessão do Claude, sem o contexto de quem escreveu, confere a mudança contra a spec e procura testes frouxos;
  - quando a mudança toca autenticação e sessão, permissões (bloco 2), dados pessoais, exportação, exclusão e retenção (bloco 3), registros e auditoria (bloco 4), infraestrutura, segredos e workflows (blocos 5 e 6) ou imagens e arquivos (D-022), há também uma revisão de segurança guiada pelo ASVS;
  - os achados vão para o pull request já respondidos, para o usuário ler e aprender.
- **Quando o usuário escrever código,** o fluxo é o mesmo: o Claude revisa e explica os achados, nunca faz merge, e a decisão continua do usuário.

**C.6 Explicação técnica de cada pull request** (P6-27). Fica na descrição do pull request e sempre traz:

1. o que foi implementado e por quê, com o link da spec e dos requisitos;
2. os arquivos modificados, o papel de cada um e uma ordem sugerida de leitura;
3. como a implementação funciona, com os trechos principais;
4. as decisões técnicas, as alternativas que existiam e o motivo da escolha;
5. os testes executados e os resultados, dizendo qual critério cada teste prova;
6. os riscos, as limitações e os pontos de atenção, inclusive o impacto no que já existe;
7. os conceitos e as tecnologias novos para estudar, com links para a documentação oficial.

A profundidade acompanha o nível do usuário, sem esconder complexidade. O modelo do pull request só é criado na implementação, com autorização do usuário.

**C.7 Tamanho dos pull requests** (P6-01). Uma fase do `tasks.md` por pull request, com no máximo cerca de 400 linhas escritas à mão; código gerado, lockfiles e migrações automáticas ficam em commits separados e marcados. Uma funcionalidade só aparece para o estudante no último pull request; antes disso, o código entra sem rota nem tela ligada. Base: o estudo divulgado pela SmartBear com dados da Cisco indica que a revisão perde eficácia acima de 200 a 400 linhas e de 60 a 90 minutos (fonte do fornecedor).

**C.8 Prévia e ambiente local** (P6-04). O app sobe em contêineres no computador do usuário, com dados fictícios e marcados, e abre no navegador do app do Claude ou no navegador dele. O mesmo ambiente serve para o usuário rodar testes, depurar, experimentar e escrever código. Aparelhos reais, com VoiceOver e TalkBack, ficam na checagem de cada versão (D-026).

**C.9 Definição de pronto** (P6-05):

- **Pull request:**
  - feito numa branch de trabalho, nunca na `main`, dentro do escopo da spec e do `tasks.md` aprovados, numa fase prevista;
  - spec aprovada pelo usuário, se for funcionalidade (D-017);
  - explicação técnica completa (C.6);
  - cada critério com teste que cita o ID (D-026) e CI verde; enquanto o CI não existir, os testes rodam localmente e o resultado vai na explicação;
  - achados da revisão independente e da revisão de segurança respondidos;
  - o usuário teve acesso ao código e condições de revisá-lo antes do merge. Isso não exige domínio prévio das tecnologias; exige ter conseguido estudar a implementação, perguntar e entender o suficiente para decidir com consciência;
  - perguntas respondidas e todas as conversas resolvidas;
  - o que o usuário pediu foi feito, ou discutido até uma decisão dele;
  - cada commit novo depois da revisão foi reapresentado e revisado;
  - telas conferidas na prévia, se a mudança tem tela;
  - documentos, matriz do ASVS e registro de exceções atualizados; migração em duas fases, quando é o caso;
  - o Claude parou e esperou; o merge foi feito manualmente pelo usuário, pela interface do GitHub.
- **Versão:**
  - todos os pull requests da versão revisados pelo usuário;
  - imagem da `main`, com inventário e atestado;
  - nenhum componente com prazo de correção vencido sem exceção;
  - mutações sobreviventes nas regras críticas tratadas;
  - checagem manual e medição do RNF-13, como na D-026;
  - notas da versão, com o que muda e como voltar;
  - deploy autorizado pelo usuário e checagem automática depois dele.
- **Beta:**
  - matriz do ASVS completa;
  - revisão de segurança completa, acompanhada pelo usuário, com os achados fechados;
  - OWASP ZAP sem alerta alto aberto;
  - teste de carga documentado e V28 medida;
  - restauração testada (RNF-10);
  - verificações dos blocos 4 a 6 concluídas ou com plano aceito pelo usuário.
- **Abertura ao público:**
  - tudo o que vale para o beta, refeito na versão da abertura;
  - teste de carga com a meta da abertura;
  - decisão do usuário sobre o teste de invasão profissional;
  - D-002 e D-003 resolvidas, como a D-001 já exige.

### D. Portões do CI (P6-06)

| Portão | Ferramenta | Quando |
|---|---|---|
| Lint e regras de segurança do Python | Ruff, com as regras do Bandit | Todo pull request |
| Tipos do Python | mypy com django-stubs | Todo pull request |
| Lint e tipos do TypeScript | ESLint (typescript-eslint, react-hooks e jsx-a11y), Prettier e `tsc` estrito | Todo pull request |
| Testes do backend | pytest e pytest-django em PostgreSQL 18 real (D-026) | Todo pull request |
| Contrato da API | OpenAPI do Django Ninja comparado com o cliente TypeScript (D-026) | Todo pull request |
| Componentes | Vitest e Testing Library (D-026) | Todo pull request |
| Ponta a ponta e acessibilidade | Playwright em Chromium e WebKit, com perfis de iPhone e iPad; axe-core sem violação séria ou crítica (D-026). Nota de 2026-11-27: o corte passou a ser nenhuma violação das regras WCAG A e AA, de qualquer gravidade, e só as sérias e críticas nas boas práticas ("Barrar qualquer WCAG A/AA") | Todo pull request |
| Migrações | Nada pendente (`makemigrations --check`), Squawk sobre o SQL gerado e regra das duas fases (V44) | Todo pull request |
| Configuração de produção | `check --deploy`; documentação da API fora do ar em produção (ASVS 13.4.5); imagem sem `.git`, sem testes e sem dependências de desenvolvimento (13.4.1 e 15.2.3) | Todo pull request |
| Workflows | zizmor e CodeQL para Actions | Todo pull request |
| Dependências novas | Revisão de dependências do GitHub: falha alta ou crítica, ou licença fora da lista, barra o pull request | Todo pull request |
| Segredos | gitleaks, além do bloqueio no envio do GitHub | Todo pull request |
| Código | CodeQL para Python e JavaScript/TypeScript: alerta alto ou crítico barra o merge (V42) | Todo pull request |
| Imagem | Base fixada por digest; inventário com o Syft; o Grype barra componente com prazo vencido | Todo pull request e cada publicação |
| Varredura dinâmica | OWASP ZAP: varredura de base e da API pelo OpenAPI, contra o app montado como na produção | Pull request que muda o app e cada publicação |
| Mutação | mutmut e Stryker nas regras críticas | Antes de cada versão |

Tudo roda em contêineres. Enquanto as checagens obrigatórias não estiverem na regra da `main` (6.3), o bloqueio do merge depende da regra operacional de C.4.

### E. Dependências e cadeia de suprimentos

**E.1 Gerenciadores e fontes** (P6-07). uv no Python (`uv.lock`, com hash) e pnpm no frontend (`pnpm-lock.yaml`). A instalação usa só o lockfile (`uv sync --locked`, `pnpm install --frozen-lockfile`). As fontes de pacotes são só o PyPI, o registro do npm e as imagens oficiais; nenhuma dependência vem direto de Git ou de arquivo baixado (`blockExoticSubdeps`, padrão no pnpm 11, Doc). As versões das ferramentas ficam fixadas.

Nota de 2026-11-26 (implementação da fundação): o Marketplace do VS Code foi aceito como fonte, só para as extensões do editor que rodam no contêiner de desenvolvimento ("Aceito, com versão fixa"). Cada extensão fica numa versão publicada há mais de 7 dias, fixada em `.devcontainer/devcontainer.json`, com a atualização automática desligada nas configurações do usuário no VS Code. O Dependabot não atualiza essa lista; ela é revista na manutenção mensal (I.2).

**E.2 Espera de 7 dias** (P6-08):

- uv: `exclude-newer = "7 days"` (fonte secundária; V37);
- pnpm: `minimumReleaseAge` de 10.080 minutos; o padrão do pnpm 11 é 1 dia (Doc);
- Dependabot: `cooldown` de 7 dias; o padrão é 3 dias desde 14/07/2026 e não vale para atualizações de segurança (Doc).

Uma correção de segurança dentro da espera entra por exceção: só aquele pacote e aquela versão, com o motivo, removida na manutenção seguinte.

**E.3 Scripts de instalação** (P6-09). Os scripts de instalação das dependências não rodam: no pnpm 11, `allowBuilds` vazio e `strictDepBuilds` ligado (Doc). Cada liberação é aprovada pelo usuário e registrada. O `trustPolicy: no-downgrade` falha a instalação quando um pacote perde o nível de confiança com que era publicado (Doc), sinal comum de conta invadida (Inferência).

**E.4 Ações do GitHub** (P6-10):

- cada ação é fixada pelo SHA completo do commit, com a versão num comentário;
- a política do repositório que recusa ações não fixadas existe desde agosto de 2025 (Doc; V36);
- o zizmor analisa os workflows;
- `permissions: {}` no topo de cada workflow e só o mínimo em cada job;
- `persist-credentials: false` no checkout e nenhum `pull_request_target`;
- quando a tarefa é simples, um comando próprio no lugar de uma ação de terceiros.

Motivo: em março de 2025 (tj-actions) e em março de 2026 (trivy-action), versões de ações populares foram redirecionadas para código que roubava segredos do CI (Doc).

**E.5 Dependabot** (P6-11). Semanal, com as atualizações agrupadas por ecossistema: Python, pnpm, imagens Docker e ações. As atualizações de segurança chegam na hora. Os pull requests do Dependabot passam pelos mesmos portões, pela revisão independente e pela revisão do usuário, e trazem o resumo do que mudou em cada biblioteca, as mudanças incompatíveis e os resultados dos testes. Não há merge automático de atualizações.

**E.6 Prazos de correção** (P6-12; ASVS 15.1.1 e 15.2.1):

| Gravidade | Prazo, contado da publicação do alerta (V45) |
|---|---|
| Crítica, ou já explorada (lista KEV da CISA) | 3 dias |
| Alta | 14 dias |
| Média | 30 dias |
| Baixa | Na manutenção mensal |

- Falha que não alcança o MedTeca, por estar numa função que ele não usa: o motivo fica registrado e vale o prazo da categoria seguinte.
- As exceções têm data de validade, ficam num registro único e são revisadas na manutenção mensal.
- O CI barra a publicação se algum componente passar do prazo sem exceção.
- Os prazos valem também para a imagem base e para os pacotes do sistema dentro dela. O sistema do servidor segue as atualizações automáticas da D-033.
- Os prazos dependem da disponibilidade do usuário para revisar e fazer o merge: uma falha crítica pede a revisão dele em até 3 dias.

**E.7 Licenças** (P6-13):

- entram direto: MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, ISC, 0BSD, PSF-2.0, Zlib, CC0-1.0 e, para fontes, OFL-1.1;
- MPL-2.0 e LGPL entram com o motivo registrado, pacote a pacote;
- qualquer outra, inclusive GPL, AGPL e licença não identificada, barra o pull request até o usuário aprovar com análise; a AGPL alcança até o uso pela rede;
- a revisão de dependências do GitHub faz isso de graça em repositório público (Doc); no Python, isso depende de o GitHub ler o `uv.lock` (V39), e, se não ler, a checagem sai do inventário;
- pergunta para o advogado: Jur-25.

Nota de 2026-11-27 (implementação da fundação): na árvore de dependências do frontend apareceram três licenças fora da lista, todas em ferramentas de desenvolvimento e de build: BlueOak-1.0.0 (`lru-cache`, `minimatch`, `@isaacs/nonrecursive-glob-match`), CC-BY-4.0 (`caniuse-lite`) e Python-2.0 (`argparse`). O usuário aprovou as três só nesse uso ("Aceito nas ferramentas"); o registro, pacote a pacote, está em `frontend/pnpm-workspace.yaml`. O que vai para o app do estudante continua todo MIT.

### F. Publicação, inventário e retenção no ECR

**F.1 O que acontece depois do merge** (P6-02). O repositório do ECR é **privado**, em São Paulo; o ECR Public não é usado. Depois do merge do usuário:

1. o GitHub Actions roda de novo as checagens sobre o commit da `main`;
2. se tudo passar, faz o build da imagem, gera o inventário, aplica a varredura com a barreira de prazos e gera o atestado de origem;
3. envia a imagem e o inventário ao ECR, por OIDC, com um papel que só pode enviar imagens para aquele repositório;
4. cria o registro da versão no GitHub.

Nada além disso acontece: não há OpenTofu, mudança de infraestrutura, contato com o servidor, deploy nem migração (a V6 prova que o papel do CI não tem essas permissões). Publicar no ECR não muda a produção; o deploy é operação separada, que depende de autorização do usuário (5.4).

**F.2 Inventário e varredura** (P6-14; ASVS 15.1.2):

- o Syft gera o inventário de cada imagem no formato CycloneDX, o padrão da OWASP;
- o inventário vai para o ECR junto da imagem, como referência do OCI 1.1, que o ECR aceita (Doc; há relato de recusa num caso, V40), e uma cópia vai para o registro da versão;
- no CI, o Grype varre o inventário e aplica a barreira de E.6;
- uma tarefa diária no GitHub Actions reconfere o inventário da versão em produção, lido do registro da versão, sem acesso de leitura na AWS; uma falha nova abre um aviso no GitHub, que chega por e-mail ao usuário, e o prazo de correção começa a contar;
- a varredura básica do ECR, gratuita, com uma varredura por imagem a cada 24 horas (Doc), dá uma segunda opinião;
- o Amazon Inspector não foi adotado.

**F.3 Retenção no ECR** (ajusta a P5-16):

- manter sempre a versão em produção e as duas anteriores que já estiveram em produção, marcadas com uma etiqueta própria no deploy;
- manter também as 10 imagens mais recentes da `main` e apagar as mais antigas;
- não criar regra genérica para apagar imagens sem etiqueta: inventários e atestados são artefatos sem etiqueta e seriam apagados; quando a regra apaga uma imagem, o ECR já remove as referências dela (Doc), e há relato de que regras por contagem contam essas referências;
- testar a regra com a prévia do ECR antes de aplicar e aplicar só pelo OpenTofu, com autorização do usuário (V40).

**F.4 Registro de versão e atestado.** Cada versão publicada ganha um registro no GitHub (Release) com o commit, o digest, o inventário e as notas. O atestado de origem é gratuito em repositório público (Doc) e é conferido no computador do usuário antes de o comando de deploy mandar o digest ao servidor; o servidor continua sem falar com o GitHub (V41).

### G. Código e segredos

**G.1 Análise de código** (P6-15). O CodeQL roda em todo pull request e uma vez por semana, para Python, JavaScript e TypeScript e os workflows do Actions. Ele é gratuito em repositório público, e a análise de workflows está disponível desde abril de 2025 (Doc). O Ruff roda com as regras do Bandit, e o ESLint barra padrões perigosos, como `eval` e HTML injetado no React.

**G.2 Segredos** (P6-16):

- a varredura de segredos e o bloqueio no envio ficam ligados no repositório (V35);
- o gitleaks roda antes de cada commit, dentro do contêiner, e no CI, para padrões genéricos que o GitHub não reconhece (Inferência);
- se um segredo chegar ao GitHub, ele é tratado como exposto, mesmo depois de apagado: revogar e trocar na hora, registrar como incidente de segurança (bloco 4) e avaliar a comunicação conforme o bloco 3. Reescrever o histórico do Git não desfaz a exposição.

### H. Verificação de segurança e capacidade

**H.1 Matriz do ASVS** (P6-17). Cobre os níveis 1 e 2 do ASVS 5.0; a referência usada lista 217 requisitos, e a contagem oficial fica na V47. Cada linha aponta a prova: um teste com nome, uma verificação manual com data, uma exceção aprovada, ou "não se aplica" com o motivo. A matriz é criada no início da implementação e atualizada em todo pull request.

**H.2 Varredura dinâmica** (P6-18). O OWASP ZAP faz a varredura de base e a varredura da API a partir do OpenAPI, contra o app montado como na produção (Caddy, app e PostgreSQL em contêineres no CI). Um alerta alto barra a publicação; um médio precisa ser tratado antes da versão.

**H.3 Revisão completa e teste de invasão** (P6-19). Antes do beta, uma sessão independente faz uma revisão de segurança completa, guiada pela matriz, acompanhada pelo usuário; os achados são fechados ou viram exceção aprovada. Antes da abertura ao público, o usuário decide, com a cotação em mãos, se contrata um teste de invasão profissional.

**H.4 Teste de carga** (P6-20). O Locust (licença MIT) roda no ambiente de teste sob demanda, com dados fictícios em volume realista. Mede a memória, inclusive durante um deploy sem queda (V28); o tempo até a próxima questão (RNF-13); e o limite das funções pesadas: início e fim do simulado, exportação, filtros e desempenho. O resultado documenta as funções pesadas e as defesas contra sobrecarga (ASVS 15.1.3 e 15.2.2). Antes de cada teste, o usuário define o número de estudantes simultâneos. Criar o ambiente exige autorização (5.4).

**H.5 Testes de mutação** (P6-21). Rodam antes de cada versão, com o mutmut no Python e o Stryker no TypeScript, nas regras críticas:

- correção e pontuação das respostas;
- permissões;
- agregados só com 10 pessoas ou mais e supressão de alternativas com menos de 3 (bloco 2, aprovado e ainda não registrado);
- números que não mudam na exclusão de conta (bloco 3, aprovado e ainda não registrado);
- prazos de retenção e de exclusão;
- no frontend, o cronômetro do simulado e a fila de respostas sem conexão (RNF-07).

Cada mutação que sobrevive vira um teste novo ou o registro de que ela não muda o comportamento. Sem meta de percentual (D-026). O mutmut não roda direto no Windows (Doc), o que não pesa, porque tudo roda em contêiner.

### I. Operação das versões

**I.1 Volta de versão** (P6-22):

| Operação | O que é | Quem executa |
|---|---|---|
| Volta de código | Pull request de reversão numa branch, nunca reset ou push forçado na `main`; o merge publica uma imagem nova no ECR, mas não muda a produção | O Claude prepara quando o usuário pede; o merge é do usuário |
| Volta da versão em produção | O comando de deploy com o digest anterior | Só com autorização explícita do usuário para aquela operação; o Claude pode preparar e explicar, sem executar |
| Restauração de dados | Restaurar um backup em produção; perde o que foi gravado depois do backup e exige reaplicar as exclusões de conta (RNF-51) | Só com autorização explícita do usuário, pelo plano de recuperação da seção 5.K |

- Depois de cada deploy, uma checagem automática só de leitura confere a saúde do sistema, os cabeçalhos de segurança, o certificado e a versão servida.
- Se aparecer erro novo num fluxo crítico (entrar, responder questão, simulado, exportar ou excluir a conta), a recomendação é voltar primeiro, mas a decisão e a autorização são do usuário, a cada vez. A correção vem depois, por pull request.
- Voltar uma versão é sempre possível; voltar duas ou mais só se nenhuma migração passou pela fase "contrair" no meio (5.I.3).

**I.2 Manutenção mensal** (P6-23). Junto do teste de restauração (5.G.4): merge das atualizações agrupadas, imagem base reconstruída, correção das falhas baixas, revisão das exceções que vão vencer e alertas do CodeQL e do Dependabot zerados ou com exceção. Tudo passa pela revisão e pelo merge do usuário.

### J. Desenvolvimento e repositório público

**J.1 Desenvolvimento em contêineres** (P6-24). Instalação de dependências, testes, mutação, Playwright e o próprio app rodam sempre em contêineres. As credenciais do GitHub e da AWS, as chaves SSH e os outros arquivos do usuário nunca entram nos contêineres; o `node_modules` e o ambiente Python ficam em volumes do Docker. Deploy, OpenTofu e Git rodam fora dos contêineres. Os contêineres funcionam com o editor do usuário, com autocompletar, depuração e testes (V49). A Docker recomenda manter o código dentro do WSL 2, por desempenho (Doc); mover a pasta, se a medição pedir (V43), é decisão do usuário na implementação. Motivo: ataques como o Shai-Hulud (npm, 2025) rodavam na instalação de pacotes e roubavam tokens do GitHub e chaves de nuvem de quem desenvolvia (Doc).

**J.2 Regras para o repositório público** (P6-25):

- logs, artefatos e gravações do CI só têm dados fictícios, sem segredo e sem dado pessoal real;
- nenhum conteúdo real de questão entra no repositório, nem em testes, capturas ou gravações (D-019 e bloco 2);
- os artefatos do CI ficam guardados por 14 dias;
- workflows de pull requests de fora rodam sem segredo e sem OIDC, e só depois da aprovação do usuário (V46);
- a conta do GitHub do usuário usa passkey ou segundo fator (V46).

**J.3 Relato de vulnerabilidades** (P6-26). Um `SECURITY.md` explica como relatar uma falha, e o relato privado de vulnerabilidades do GitHub fica ligado, gratuito em repositório público (Doc). Um relato que envolva dado pessoal segue o fluxo de incidentes do bloco 3. O arquivo e a configuração só são criados na implementação, com autorização do usuário.

### K. Custo

O bloco 6 não acrescenta nenhum serviço pago. Estimativa do acréscimo mensal: abaixo de US$ 1, a confirmar.

| Item | Estimativa | Base |
|---|---|---|
| GitHub (Actions, CodeQL, varredura de segredos, revisão de dependências, atestados) | Zero | Doc: gratuito em repositório público |
| Armazenamento no ECR | Cerca de US$ 0,26 por mês no pior caso (13 imagens de cerca de 0,2 GB, sem reaproveitar camadas) | Doc: US$ 0,10 por GB-mês, preço de us-east-1 (São Paulo a confirmar, V51); tamanho da imagem é inferência; já coberto pela linha do ECR em 5.L |
| Inventários no ECR | Menos de US$ 0,01 por mês | Inferência: alguns MB |
| Transferência do ECR para o Lightsail | Abaixo de US$ 0,50 por mês, na pior hipótese | A documentação cita transferência gratuita na mesma região para EC2, Lambda e Fargate, não para o Lightsail (V33); o Lightsail conta entrada e saída na franquia do plano (Doc) |
| Varredura básica do ECR | Zero | Doc |
| Teste de carga | Cerca de US$ 0,02 por hora do ambiente, por teste | Pontual; 5.I.4 |

### L. Verificações

**Nenhuma foi concluída.**

| V | O que verificar | Situação |
|---|---|---|
| V35 | Varredura de segredos e bloqueio no envio ligados no repositório (o anúncio de 2024 e a documentação atual divergem sobre o padrão) | Pendente: conferir |
| V36 | Política de SHA obrigatório em repositório pessoal, com ações locais e reutilizáveis | Pendente: conferir |
| V37 | `exclude-newer` relativo do uv com `uv sync --locked` (há relato de falha) e com o Dependabot | Pendente: provar |
| V38 | Dependabot com a versão do pnpm adotada e respeito ao `minimumReleaseAge` | Pendente: provar |
| V39 | Se o grafo de dependências do GitHub lê o `uv.lock`; se não, licenças e falhas do Python saem do inventário | Pendente: conferir |
| V40 | ECR: inventário aceito como referência da imagem (há relato de recusa); regra de retenção sem apagar inventários de imagens mantidas; regras por contagem que contam referências (relato); teste com a prévia da regra | Pendente: provar |
| V41 | Atestado de origem com a imagem no ECR e conferência pelo digest no computador do usuário (exige o `gh`, a instalar com autorização) | Pendente: provar |
| V42 | Barrar no merge alerta alto do CodeQL, num repositório pessoal público | Pendente: conferir |
| V43 | Desempenho do Docker com a pasta no Windows e no WSL 2 | Pendente: medir |
| V44 | Squawk sobre o SQL do `sqlmigrate`; se o django-migration-linter funciona com a versão do Django usada | Pendente: provar |
| V45 | Data de publicação de cada falha na ferramenta de varredura, para contar o prazo | Pendente: conferir |
| V46 | Passkey ou segundo fator na conta do GitHub, tokens ativos e aprovação de workflows de contribuidores de fora | Pendente: conferir |
| V47 | Contagem oficial dos requisitos de nível 1 e 2 do ASVS 5.0.0 (a referência usada lista 217) | Pendente: conferir |
| V48 | Quem vê logs e artefatos do CI sem login; retenção configurada | Pendente: conferir |
| V49 | Editor do usuário funcionando dentro do contêiner, com autocompletar, depuração e testes | Pendente: provar |
| V50 | Configuração do repositório: auto-merge desligado; métodos de merge; restrição de exclusão, não ativa em 2026-11-24 pela API pública; checagens obrigatórias quando houver CI; bypass vazio | Pendente: conferir; decisões do usuário pendentes (6.3) |
| V51 | Preço do ECR em São Paulo e franquia aplicável à conta da AWS (ligada à V12 e à V29) | Pendente: conferir |

### M. Questão jurídica

Pendente de avaliação profissional; acompanha a consulta jurídica de D-002.

- **Jur-25.** A política de licenças de terceiros atende a um produto pago (D-011)? A política: licenças permissivas entram direto; copyleft fraca (MPL, LGPL) entra com registro; GPL, AGPL e licenças não identificadas ficam barradas até análise; as fontes usam OFL.

### N. ASVS

| Requisito | Como o bloco 6 responde |
|---|---|
| 15.1.1 (L1): prazos de correção documentados | E.6 |
| 15.2.1 (L1): nenhum componente fora do prazo | Barreira de E.6 e reconferência de F.2 |
| 15.1.2 (L2): inventário e repositórios confiáveis | F.2 e E.1 |
| 15.1.3 e 15.2.2 (L2): funções pesadas | H.4 |
| 15.2.3 (L2): nada de teste em produção | Portão de configuração (D) |
| 13.4.1 (L1); 13.4.2 e 13.4.5 (L2) | Portão de configuração (D) |
| 15.2.4 (L3): confusão de dependências | Em parte, por E.1 |
| 15.3.x | Tipos, lint e revisão, provados requisito a requisito na matriz (H.1) |

**A aprovação deste bloco não é declaração de conformidade com o OWASP ASVS.**

### O. Coerência com as decisões anteriores

- Nenhuma contradição encontrada com D-017, D-026, D-027, D-033 ou com os blocos 1 a 5.
- O bloco completa a D-026 (mutação, carga, ZAP e matriz), a D-027 (pull requests, portões, Dependabot e ações fixadas), a D-033 (registro de versão, atestado, volta de versão, checagem depois do deploy, inventário e retenção no ECR) e a D-017 (fases como pull requests, escopo da autorização e definição de pronto).
- A regra de trabalho "commits direto na `main`" deixou de valer: a regra da `main` está ativa desde 2026-11-24, inclusive para documentos.
- **Ponto de atenção:** o RNF-71 (merge barrado por checagem que falha) está aprovado, mas incluir as checagens obrigatórias na regra da `main` é ato do usuário, recomendado para quando o CI existir (6.3, V50). Até lá, não há CI nem checagem a barrar.
- As quatro inconsistências da seção 5.P foram resolvidas pelo usuário em 2026-11-25 (seção 5.P).

### P. Efeitos nos documentos

Registrado em 2026-11-24, numa branch de trabalho, para revisão e merge do usuário:

- `docs/decisions.md`: D-034 aprovada, com ADR; notas em D-006, D-017, D-022, D-026, D-027, D-032 e D-033.
- ADRs: novo `docs/adr/D-034-qualidade-e-cadeia-de-suprimentos.md`; notas de atualização nos ADRs de D-006, D-020, D-028, D-032 e D-033.
- `docs/requisitos-mvp.md`: critérios RNF-70 a RNF-88 e duas pendências novas.
- Este documento: seções 5.4 e 6; notas em 5.I.1, 5.I.2, 5.L e na V33.
- `README.md`.

Nada foi criado no GitHub ou na AWS: o modelo de pull request, o `SECURITY.md`, as configurações, os workflows e a matriz do ASVS nascem na implementação, com autorização do usuário.

### Q. Fontes conferidas em 2026-11-24

- **GitHub:**
  - [recursos de segurança](https://docs.github.com/en/code-security/getting-started/github-security-features);
  - [regras disponíveis nos rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets);
  - [política de SHA obrigatório](https://github.blog/changelog/2025-08-15-github-actions-policy-now-supports-blocking-and-sha-pinning-actions/);
  - [espera padrão do Dependabot](https://github.blog/changelog/2026-07-14-dependabot-version-updates-introduce-default-package-cooldown/);
  - [Dependabot com pnpm 11 e 12](https://github.blog/changelog/2025-01-09-dependabot-now-supports-npm-12-pnpm-11-and-12-and-bun-1-4/);
  - [CodeQL para Actions](https://github.blog/changelog/2025-04-22-github-actions-workflow-security-analysis-with-codeql-is-now-generally-available);
  - [bloqueio no envio](https://docs.github.com/en/code-security/concepts/secret-security/push-protection) e o [anúncio de 2024](https://github.blog/changelog/2024-03-11-secret-scanning-and-push-protection-are-enabled-by-default-on-new-public-repositories/);
  - [revisão de dependências](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/configure-dependency-review-action);
  - [relato privado de vulnerabilidades](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/report-privately);
  - [logs do Actions](https://docs.github.com/en/enterprise-server@3.19/actions/how-tos/monitor-workflows/use-workflow-run-logs) (documentação do GitHub Enterprise Server).
- **pnpm:** [segurança da cadeia de suprimentos](https://pnpm.io/supply-chain-security) e [versão 11.0](https://pnpm.io/blog/releases/11.0).
- **uv:** [espera relativa](https://pydevtools.com/handbook/how-to/how-to-protect-against-python-supply-chain-attacks-with-uv/) (fonte secundária).
- **Incidentes:**
  - [tj-actions (CISA)](https://cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-github-action-cve-2025-30066);
  - [trivy-action (GHSA-69fq-xp46-6x23)](https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23);
  - [Shai-Hulud 2.0](https://blog.checkpoint.com/research/shai-hulud-2-0-inside-the-second-coming-the-most-aggressive-npm-supply-chain-attack-of-2025/).
- **AWS:**
  - [preços do ECR](https://aws.amazon.com/ecr/pricing);
  - [mudança no nível gratuito (julho de 2025)](https://aws.amazon.com/about-aws/whats-new/2025/07/aws-free-tier-credits-month-free-plan);
  - [transferência de dados no Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-faq-data-transfer-allowance.html);
  - [ECR com OCI 1.1](https://aws.amazon.com/about-aws/whats-new/2024/06/amazon-ecr-oci-image-distribution-version-1-1), o [relato de recusa de referência](https://github.com/aws/containers-roadmap/issues/2783) e o [relato sobre contagem de referências](https://github.com/aws/containers-roadmap/issues/2613);
  - [exemplos de regras de retenção](https://docs.aws.amazon.com/AmazonECR/latest/userguide/lifecycle_policy_examples.html);
  - [varredura de imagens](https://docs.aws.amazon.com/inspector/latest/user/scanning-ecr.html) e [preços do Inspector](https://aws.amazon.com/inspector/pricing/).
- **Ferramentas:**
  - [Syft (sbom-action)](https://github.com/anchore/sbom-action);
  - [Grype (scan-action)](https://github.com/marketplace/actions/anchore-container-scan);
  - [OWASP ZAP no GitHub Actions](https://www.zaproxy.org/blog/2020-04-09-automate-security-testing-with-zap-and-github-actions/);
  - [Squawk](https://github.com/sbdchd/squawk);
  - [zizmor](https://pypi.org/p/zizmor);
  - [mutmut](https://mutmut.readthedocs.io);
  - [Stryker com Vitest](https://stryker-mutator.io/docs/stryker-js/vitest-runner/);
  - [Locust](https://pypi.org/project/locust/).
- **Docker:** [licença do Docker Desktop](https://docs.docker.com/subscription/desktop-license/) e [boas práticas com WSL 2](https://docs.docker.com/desktop/features/wsl/best-practices/).
- **Revisão de código:** [boas práticas da SmartBear](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/) (dados da Cisco divulgados pelo próprio fornecedor).
- **Termos do GitHub:** [contas de máquina](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service).

## Histórico

- 2026-11-24: documento criado no registro do bloco 4 da Etapa 6, com autorização do usuário ("Aprovo integralmente o Bloco 4 — Registros e Monitoramento, na versão revisada apresentada."; "Atualize a documentação e os registros de decisão necessários"). Seção 4 registrada. Os blocos 1 a 3 foram aprovados no mesmo dia e aguardam registro.
- 2026-11-24: bloco 5 aprovado com ressalvas ("Aprovo o Bloco 5 — Infraestrutura e Operação — conforme a proposta apresentada, incluindo as decisões P5-01 a P5-25, com as ressalvas e condições abaixo."). Seção 5 registrada, com as ressalvas, a triagem das verificações (nenhuma concluída), a Jur-24 e quatro inconsistências para avaliação do usuário. Notas nas seções 4.E.2, 4.E.3, 4.H.3 e 4.L. Nenhum recurso foi criado na AWS e nenhum código foi implementado.
- 2026-11-24: bloco 6 aprovado ("Aprovar bloco 6"), depois das correções do usuário. Seção 6 registrada (P6-01 a P6-28, V35 a V51, Jur-25) e seção 5.4 (autorizações recorrentes e operações sensíveis). Notas em 5.I.1, 5.I.2, 5.L e na V33. As recomendações sobre a regra da `main` ficam pendentes de decisão. Registro autorizado pelo usuário ("Sim. Autorizo o registro documental do Bloco 6 agora, em uma branch de trabalho."). Nada foi alterado no GitHub ou na AWS e nenhum código foi implementado.
- 2026-11-25: as quatro inconsistências da seção 5.P foram resolvidas pelo usuário ("Aprovar"), depois de duas revisões pedidas por ele. Resoluções registradas na própria 5.P, com as verificações V52 a V55; notas em 4.H.3 (inclusive a correção do item que ainda punha o banco no disco principal), 4.H.7, 5.B.1, 5.C.2, 5.G.4, 5.K.1, 5.Q, 5.4.4 e 6.O. O prazo de 7 dias para a revisão depois de uma emergência segue como proposta não aprovada. Os ajustes nos textos dos blocos 1 e 3 entram no registro deles. Registro autorizado pelo usuário ("Sim, registrar").
- 2026-11-25: bloco 1 (contas e acesso), aprovado em 2026-11-24 ("Aprovar bloco 1"), registrado na seção 1, a partir do texto da versão final aprovada, com a seção D (o que os blocos 4 a 6 e a resolução da 5.P.3 mudaram) e o ajuste do procedimento de emergência (B.5). Critérios CONTA-26 a CONTA-55. Os blocos 2 e 3 seguem aprovados e sem registro. Registro pedido pelo usuário ("vamos pra próxima parte").
- 2026-11-25: bloco 2 (permissões e privacidade), aprovado em 2026-11-24 ("Aprovar bloco 2"), registrado na seção 2, a partir do texto da proposta aprovada, com a seção G (o que os blocos 1, 3 e 4 mudaram). Critérios CONTA-56 a CONTA-69. O bloco 3 segue aprovado e sem registro. Registro pedido pelo usuário ("está perfeito vamos seguir!").
- 2026-11-25: bloco 3 (LGPD), aprovado em 2026-11-24 ("Aprovar bloco 3"), registrado na seção 3, a partir da versão consolidada aprovada com os seis ajustes do usuário. A lista de exclusões (B.8) aparece como substituída pela resolução da 5.P.1; a tabela B.12 recebeu as linhas previstas em 4.H.8; as perguntas ao advogado viraram Jur-01 a Jur-16. Os critérios e o modelo conceitual entram no PR seguinte, como o usuário escolheu ("Dois PRs"). Registro pedido pelo usuário ("vamos").
- 2026-11-26: bloco 3, segunda parte do registro: critérios CONTA-70 a CONTA-97, REP-04 a REP-06 e RNF-95 a RNF-97 no catálogo, com o CONTA-12 substituído e o CONTA-25 removido; decisões M-40 a M-42 e RM-19 no modelo conceitual, que substituem M-21, M-36 e RM-13 e, em parte, M-07 e M-22. Seção 3.I com o mapa de cada tema; notas no cabeçalho e nas seções 2.G, 3.1, 3.C, 3.G e 5.P. Os seis blocos estão registrados por inteiro. Registro pedido pelo usuário ("vamo seguir!").
- 2026-11-26: **Etapa 6 aprovada** ("Aprovar Etapa 6"). Nota na seção 3.B.10: os documentos jurídicos passam para a preparação do beta (D-036).
