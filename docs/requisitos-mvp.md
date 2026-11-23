# Requisitos do MVP: MedTeca

**Situação**: aprovado. Etapa 2 encerrada.

**Aprovado**: 2026-11-23 - usuário: "Aprovar Etapa 2"

Catálogo de requisitos do MVP definido em D-001, organizado conforme D-017. Cada funcionalidade tem um prefixo de ID. As specs da TLC (`.specs/features/<funcionalidade>/spec.md`) só são escritas antes de implementar cada funcionalidade e citam estes IDs. Aprovar um requisito aqui não autoriza implementação.

## Convenções

- **Critérios em EARS**: palavras-chave em inglês e o restante em português, para que os critérios passem pelo validador da TLC sem reescrita.
  - `WHEN <evento> THEN the system SHALL <resposta>`: resposta a um evento.
  - `IF <condição indesejada> THEN the system SHALL <resposta>`: erro ou falha.
  - `WHILE <estado> the system SHALL <resposta>`: comportamento durante um estado.
  - `WHERE <recurso presente> the system SHALL <resposta>`: recurso opcional.
  - `The system SHALL <resposta>`: regra que vale sempre.
- **Situação de cada requisito**:
  - **Confirmado**: o usuário confirmou; a data e a resposta aparecem na coluna Fonte.
  - **Proposto**: escrito pelo consultor, aguardando o usuário.
  - **Pendente**: a pergunta existe e ainda não tem resposta.
  - **Proposta separada**: lacuna encontrada pelo consultor fora do que foi pedido. Fica em seção própria até o usuário decidir se entra no catálogo.
- **Fonte**: cada requisito cita a decisão (`D-NNN`) ou a resposta do usuário que o originou.
- **Revisão externa**: revisão crítica feita por outra IA e trazida pelo usuário em 2026-11-23. Os ajustes que vêm dela são citados assim e ficaram como Proposto até a aprovação formal da Etapa 2.
- **Aprovação formal**: em 2026-11-23, todos os critérios que estavam como Proposto passaram a Confirmado. A coluna Fonte de cada um registra a origem e a aprovação formal ("Aprovar Etapa 2").

## Mapa de funcionalidades

Situação do mapa: **Aprovado** na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23).

| Prefixo | Funcionalidade | Origem |
|---|---|---|
| CONT | Integridade do conteúdo: situação do gabarito, publicação, retirada de circulação | D-014, bloco 1 |
| CONTA | Cadastro, login, sessão, recuperação de senha, aceite dos termos, exportar e excluir conta | D-001 (a recuperação de senha é proposta, não consta em D-001) |
| CAT | Classificação grande área → tema e filtros | D-001, D-013 |
| TREINO | Resolução com correção imediata | D-001 |
| SIM | Simulado cronometrado com correção no fim | D-001 |
| REV | Revisão dos erros e "marcar" | D-001 |
| DES | Desempenho por área e tema | D-001 |
| REP | Reportar erro na questão | D-001 |
| EDIT | Painel do editor: questão, origem, autorização de uso, referências, versões, imagens | D-001 |
| FLUXO | Status editorial e revisão antes de publicar | D-001, D-003 |
| RNF | Requisitos não funcionais: segurança, LGPD, acessibilidade, desempenho, responsividade, backup | D-001, D-009 |

## CONT: integridade do conteúdo

### Origem do gabarito e revisão

As três situações do gabarito indicam **de onde vem a resposta**. A revisão humana da questão inteira é um registro separado, obrigatório para publicar. As três situações não são equivalentes entre si (observação do usuário registrada em D-014).

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| CONT-01 | The system SHALL registrar, para cada questão, a origem do gabarito em exatamente uma de três situações: (a) publicado oficialmente pela banca; (b) definido por uma pessoa, quando não existe gabarito oficial; (c) preliminar, ainda não confirmado oficialmente. | Confirmado | Resposta "De onde vem o gabarito" (2026-11-23); D-014 |
| CONT-02 | The system SHALL exibir ao estudante, em cada questão, a situação do gabarito, com um rótulo distinto para cada uma das três situações. | Confirmado | D-014 ("origem, gabarito oficial e nível de revisão visíveis") |
| CONT-03 | IF uma questão não tiver revisão humana registrada (revisor e data) THEN the system SHALL impedir sua publicação. | Confirmado | Resposta "De onde vem o gabarito" (2026-11-23): "obrigatória para publicar"; regra do projeto |

### Gabarito preliminar

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| CONT-04 | WHILE o gabarito de uma questão publicada estiver na situação preliminar the system SHALL exibir junto à questão um aviso de que o gabarito ainda não foi confirmado oficialmente. | Confirmado | Resposta "Sim, com aviso" (2026-11-23) |
| CONT-05 | The system SHALL incluir no desempenho do estudante as respostas a questões com gabarito preliminar. | Confirmado | Resposta "Sim, com aviso" (2026-11-23): "conta no desempenho" |
| CONT-09 | WHEN a banca publica um gabarito definitivo diferente do preliminar THEN the system SHALL recalcular, pelo gabarito definitivo, o desempenho dos estudantes que já responderam a questão. | Confirmado | Resposta "Recalcular e avisar" (2026-11-23) |
| CONT-10 | WHEN um estudante consulta uma questão cujo gabarito mudou depois que ele respondeu THEN the system SHALL exibir um aviso de que o gabarito mudou após a resposta dele. | Confirmado | Resposta "Recalcular e avisar" (2026-11-23) |

Cada resposta continua ligada à versão da questão que o estudante respondeu; o recálculo muda o desempenho, não o registro da resposta.

O sistema só fica sabendo do gabarito definitivo quando o editor registra a nova versão (FLUXO-04), que precisa de revisão antes de ser exibida (FLUXO-05). Por isso o recálculo de CONT-09 acontece na publicação dessa versão, como diz CONT-15.

### Gabarito na correção e rastreabilidade de mudanças

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| CONT-11 | WHEN o estudante vê a correção de uma questão com gabarito preliminar, no treino ou no simulado, THEN the system SHALL identificar o gabarito como preliminar na própria tela de correção, com rótulo distinto do gabarito oficial definitivo. | Confirmado | Observação do usuário sobre gabarito preliminar (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CONT-12 | WHEN o estudante responde uma questão com gabarito preliminar THEN the system SHALL apresentar o acerto ou o erro como resultado provisório. | Confirmado | Observação do usuário sobre gabarito preliminar (2026-11-23): não confundir com resultado definitivo da banca; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CONT-13 | WHEN o estudante responde uma questão THEN the system SHALL registrar, junto à resposta, a versão da questão, o gabarito e a situação do gabarito vigentes naquele momento. | Confirmado | Observação do usuário sobre mudança de gabarito (2026-11-23); situação do gabarito explicitada na revisão externa (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CONT-14 | WHEN o gabarito de uma questão ou a situação dele muda, inclusive na confirmação oficial sem mudança de resposta (CONT-16), THEN the system SHALL registrar no histórico da questão o valor anterior, o novo, a data, o responsável e o motivo. | Confirmado | Observação do usuário sobre mudança de gabarito (2026-11-23); confirmações oficiais incluídas e lista de respostas afetadas movida para CONT-20 na revisão externa (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CONT-15 | WHEN é publicada uma nova versão de questão com gabarito diferente, por qualquer motivo (inclusive correção pelo editor), THEN the system SHALL aplicar a ela CONT-09 e CONT-10. | Confirmado | Resposta "Sim, mesma regra" (2026-11-23) |
| CONT-16 | WHEN a banca confirma o gabarito preliminar sem mudar a resposta THEN the system SHALL mudar a situação do gabarito para oficial sem criar nova versão e sem exigir revisão. | Confirmado | Resposta "Mudança de metadado" (2026-11-23); a mudança fica registrada com autor e data (FLUXO-08) |
| CONT-17 | WHEN a situação do gabarito passa de preliminar para oficial THEN the system SHALL deixar de apresentar como provisórios os resultados das respostas já dadas. | Confirmado | Resposta "Mudança de metadado" (2026-11-23) |
| CONT-18 | The system SHALL manter inalterados a versão, o gabarito e a situação do gabarito registrados em uma resposta, mesmo depois que o gabarito ou sua situação mudarem. | Confirmado | Revisão externa (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CONT-19 | WHEN o estudante consulta uma resposta dada quando a situação do gabarito era diferente da atual THEN the system SHALL mostrar a situação no momento da resposta e a situação atual. | Confirmado | Revisão externa (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CONT-20 | WHEN o gabarito de uma questão muda THEN the system SHALL registrar quais respostas foram afetadas, identificando-as apenas pelos identificadores internos das respostas. | Confirmado | Revisão externa (2026-11-23): não duplicar dados pessoais; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CONT-21 | WHEN a situação do gabarito passa a "publicado oficialmente pela banca" THEN the system SHALL exigir a referência do documento oficial da banca (gabarito definitivo ou ato equivalente, com data). | Confirmado | Proposta separada do consultor (2026-11-23), aprovada na resposta "Aprovar" (2026-11-23) |
| CONT-22 | IF uma questão com gabarito na situação "publicado oficialmente pela banca" não tiver a referência verificável do documento oficial da banca, inclusive quando é cadastrada já nessa situação, THEN the system SHALL impedir sua publicação. | Confirmado | Verificação final pedida pelo usuário (2026-11-23): deixa explícito que CONT-21 vale desde o cadastro. Essa evidência não comprova o direito de uso do conteúdo (ver "Duas comprovações que não se substituem", em EDIT); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |

**As três camadas do gabarito**, que não se confundem:

1. **Na resposta** (CONT-13, CONT-18): versão, gabarito e situação vigentes quando o estudante respondeu. Nunca são sobrescritos.
2. **Atual** (CONT-02): a situação exibida hoje em cada questão.
3. **Histórico** (CONT-14, CONT-20): cada mudança de gabarito e cada confirmação oficial, com o responsável e as respostas afetadas.

CONT-17 e CONT-19 convivem: depois da confirmação oficial, o resultado deixa de ser provisório, mas o histórico continua mostrando que a resposta foi dada com gabarito preliminar. Se CONT-13 não registrasse a situação, essa informação se perderia, porque a confirmação de CONT-16 não cria nova versão.

### Questões anuladas ou desatualizadas

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| CONT-06 | WHEN uma questão é marcada como anulada ou desatualizada THEN the system SHALL excluí-la de novos treinos, novos simulados e dos resultados de filtro. | Confirmado | Resposta "Sai de circulação" (2026-11-23) |
| CONT-07 | WHEN um estudante que já respondeu uma questão anulada ou desatualizada consulta seu histórico THEN the system SHALL exibir a questão com o motivo da retirada. | Confirmado | Resposta "Sai de circulação" (2026-11-23) |
| CONT-08 | The system SHALL manter inalterado o gabarito oficial registrado de uma questão anulada ou desatualizada. | Confirmado | Premissa da pergunta sobre retirada (2026-11-23) |

### Em aberto neste tema

| Questão | Para onde vai |
|---|---|
| Texto exato dos rótulos das três situações e do aviso de gabarito preliminar. | Etapa 5 |

## CONTA: contas, acesso e dados pessoais

### Acesso durante o beta fechado

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| CONTA-01 | WHILE o beta fechado estiver ativo the system SHALL permitir criar conta somente a partir de um convite válido. | Confirmado | Resposta "Convite por e-mail" (2026-11-23); D-001 |
| CONTA-02 | WHEN o administrador cria um convite THEN the system SHALL enviar ao e-mail convidado um link de uso único com prazo de validade. | Confirmado | Resposta "Convite por e-mail" (2026-11-23) |
| CONTA-03 | IF o link de convite estiver expirado ou já tiver sido usado THEN the system SHALL recusar o cadastro. | Confirmado | Resposta "Convite por e-mail" (2026-11-23) |
| CONTA-04 | The system SHALL considerar comprovada a posse do e-mail quando o cadastro é feito pelo link de convite. | Confirmado | Resposta "Convite por e-mail" (2026-11-23) |
| CONTA-14 | WHEN um convite completa 7 dias desde o envio THEN the system SHALL torná-lo inválido. | Confirmado | Proposta do consultor; validade de 7 dias mantida na revisão do usuário (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CONTA-17 | WHEN o administrador reenvia ou renova um convite expirado THEN the system SHALL enviar ao mesmo e-mail um novo link de uso único válido por 7 dias. | Confirmado | Revisão do usuário em CONTA-14 (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CONTA-23 | WHEN um novo link de convite é enviado para um e-mail THEN the system SHALL invalidar qualquer link de convite anterior ainda válido para esse e-mail. | Confirmado | Revisão externa (2026-11-23). Um convite expirado já é inválido por CONTA-14; esta regra cobre o caso de existir um link anterior ainda válido; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |

### Cadastro e sessão

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| CONTA-05 | The system SHALL coletar no cadastro apenas e-mail, senha e, opcionalmente, um apelido. | Confirmado | Resposta "Só apelido opcional" (2026-11-23) |
| CONTA-06 | WHEN uma sessão completa 30 dias sem uso THEN the system SHALL encerrá-la e exigir novo login. | Confirmado | Resposta "Até 30 dias sem uso" (2026-11-23) |
| CONTA-07 | WHEN o estudante usa "Sair" THEN the system SHALL encerrar a sessão naquele aparelho imediatamente. | Confirmado | Resposta "Até 30 dias sem uso" (2026-11-23) |
| CONTA-08 | WHEN o estudante pede recuperação de senha THEN the system SHALL enviar ao e-mail cadastrado um link de redefinição de uso único e validade curta. | Confirmado | Consequência do login com e-mail e senha (D-001); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CONTA-09 | WHEN o estudante aceita os termos de uso e a política de privacidade THEN the system SHALL registrar a versão dos textos aceitos e a data do aceite. | Confirmado | D-001 (termos e privacidade no MVP); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |

### Exportação e exclusão

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| CONTA-10 | WHEN o estudante pede a exportação dos seus dados THEN the system SHALL gerar um arquivo em formato estruturado e legível por máquina com os dados pessoais e o histórico de atividades pertencentes a ele (tentativas em treino e simulado, questões marcadas e reportes enviados). | Confirmado | Revisado conforme revisão do usuário (2026-11-23); "pertencentes a ele" acrescentado na revisão externa (2026-11-23); a lista entre parênteses é detalhamento do consultor. Sem relatórios elaborados no MVP; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CONTA-18 | The system SHALL excluir da exportação dados pessoais de outros usuários e informações a que o estudante não tem direito de acesso. | Confirmado | Revisão externa (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CONTA-24 | The system SHALL incluir na exportação, para cada tentativa, o identificador da questão, a classificação (área, tema, banca, ano), a resposta dada, o resultado e a data, sem o texto da questão. | Confirmado | Resposta "Não, só identificadores" (2026-11-23) |
| CONTA-11 | WHEN o estudante exclui a própria conta THEN the system SHALL apagar a conta, o e-mail e todo vínculo entre a pessoa e suas respostas. | Confirmado | Resposta "Anonimizar respostas" (2026-11-23) |
| CONTA-12 | WHEN uma conta é excluída THEN the system SHALL manter as respostas dessa conta somente sem identificação, para estatísticas das questões. | Confirmado | Resposta "Anonimizar respostas" (2026-11-23) |

### Privacidade entre papéis

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| CONTA-13 | The system SHALL impedir que editores e revisores vejam respostas individuais de estudantes, mostrando a eles apenas números agregados. | Confirmado | Minimização (LGPD); proposta do consultor; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CONTA-19 | IF um número agregado mostrado a editores ou revisores se basear em um grupo de estudantes pequeno o bastante para permitir deduzir quem respondeu THEN the system SHALL suprimir ou agrupar esse número, conforme a política de supressão de grupos pequenos definida na Etapa 6. | Confirmado | Revisão externa (2026-11-23); limiar e método ficam para a Etapa 6; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CONTA-22 | The system SHALL impedir que um estudante veja ou altere tentativas, marcações, reportes ou dados de conta de outro estudante. | Confirmado | Revisão externa sobre marcações individuais (2026-11-23), generalizada pelo consultor; OWASP ASVS 5.0, requisito 8.2.2 (acesso por item de dado); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |

### Papéis

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| CONTA-15 | The system SHALL atribuir a cada conta um ou mais destes papéis: estudante, editor, revisor, administrador. | Confirmado | Proposta do consultor; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CONTA-16 | WHILE o beta fechado estiver ativo the system SHALL permitir somente ao administrador enviar convites e atribuir papéis. | Confirmado | Revisado conforme revisão do usuário (2026-11-23): decisão operacional do beta, não limitação permanente da plataforma; revisitar na abertura ao público (D-001). Entra no índice `docs/decisions.md` como decisão operacional do beta quando a Etapa 2 for aprovada formalmente (resposta "Sim, na aprovação", 2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CONTA-20 | The system SHALL negar qualquer ação que a matriz de permissões não permita explicitamente aos papéis da conta. | Confirmado | Revisão externa (2026-11-23): menor privilégio e bloqueio por padrão; OWASP ASVS 5.0, requisito 8.2.1; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CONTA-21 | WHEN uma conta tem mais de um papel THEN the system SHALL aplicar a cada ação as restrições próprias dela, mesmo que outro papel da conta a permitisse (por exemplo, FLUXO-03 impede o autor de aprovar a própria versão). | Confirmado | Revisão externa (2026-11-23): acumular papéis não libera tudo automaticamente; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |

A matriz de permissões (que papel faz o quê, sobre quais dados) será definida nas Etapas 3 e 6. Permissões sensíveis, como acesso a logs (RNF-17) e atestar a autorização de uso de conteúdo (EDIT-06), são concedidas de forma específica, não por acúmulo de papéis.

### Em aberto neste tema

| Questão | Para onde vai |
|---|---|
| Validade do link de recuperação de senha e proteções contra abuso (limite de tentativas, não revelar se um e-mail existe). | Etapa 6 |
| Com poucos usuários no beta, respostas "anonimizadas" podem ser reidentificáveis pelo contexto; avaliar se a anonimização é real. | Etapa 6 |
| Formato específico do arquivo de exportação (por exemplo, JSON ou CSV). | Etapa 6 |
| Política de supressão de grupos pequenos em números agregados (limiar e método), com análise de risco de reidentificação (CONTA-19). | Etapa 6 |
| Matriz de permissões por papel, com menor privilégio e bloqueio por padrão (CONTA-20, CONTA-21). | Etapas 3 e 6 |

## CAT: classificação e filtros

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| CAT-01 | The system SHALL classificar cada questão em exatamente uma grande área e exatamente um tema. | Confirmado | D-013; resposta "Um tema só" (2026-11-23) |
| CAT-02 | WHEN o estudante aplica mais de um filtro (área, tema, banca, ano, não resolvidas, erradas) THEN the system SHALL mostrar apenas as questões publicadas que atendem a todos eles. | Confirmado | D-001 (lista de filtros); combinação proposta pelo consultor; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CAT-03 | WHERE o filtro "não resolvidas" estiver ativo the system SHALL mostrar apenas questões que o estudante nunca respondeu. | Confirmado | D-001; definição proposta; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| CAT-04 | WHERE o filtro "erradas" estiver ativo the system SHALL mostrar apenas questões cuja tentativa mais recente do estudante está errada. | Confirmado | Coerente com REV-01; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |

### Em aberto neste tema

| Questão | Para onde vai |
|---|---|
| Identidade da questão × versão respondida: uma questão respondida numa versão anterior conta como resolvida em CAT-03? A resposta fica preservada na versão em que foi dada (CONT-13); falta definir como "não resolvidas" e "erradas" tratam versões novas, sem produzir resultados contraditórios. | Etapa 4 e spec de CAT |

## TREINO: resolução com correção imediata

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| TREINO-01 | WHEN o estudante inicia um treino THEN the system SHALL apresentar as questões publicadas que atendem ao filtro escolhido, em ordem aleatória. | Confirmado | Proposta do consultor; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| TREINO-02 | WHEN o estudante responde uma questão no treino THEN the system SHALL exibir imediatamente: se ele acertou; o gabarito, identificado pela situação dele (CONT-02, CONT-11, CONT-12); o comentário e as referências que o fundamentam, quando houver; e a origem da questão (banca e ano, ou autoria própria). | Confirmado | D-001 (correção imediata), D-014 (origem e gabarito visíveis); a lista completa é proposta; situação do gabarito e referências reforçadas na revisão externa (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| TREINO-03 | WHEN o estudante responde de novo uma questão já respondida THEN the system SHALL registrar uma nova tentativa sem apagar as anteriores. | Confirmado | Resposta "1ª no desempenho, última nos erros" (2026-11-23) |
| TREINO-04 | WHILE um treino estiver em andamento the system SHALL manter a mesma ordem de questões, inclusive depois de a página ser recarregada. | Confirmado | Revisão externa (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| TREINO-05 | IF a página for recarregada durante um treino THEN the system SHALL manter as respostas já dadas e retomar o treino na primeira questão ainda não respondida da sequência. | Confirmado | Revisão externa (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |

## SIM: simulado cronometrado

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| SIM-01 | WHEN o estudante cria um simulado THEN the system SHALL permitir escolher a quantidade de questões e a duração. | Confirmado | Proposta do consultor; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| SIM-02 | WHILE um simulado estiver em andamento the system SHALL ocultar a correção das questões. | Confirmado | D-001 ("correção no fim") |
| SIM-03 | WHEN o estudante pausa o simulado THEN the system SHALL parar o cronômetro até ele retomar. | Confirmado | Resposta "Com pausa, entrega no fim" (2026-11-23) |
| SIM-04 | WHEN o tempo do simulado chega a zero THEN the system SHALL entregar o simulado com as respostas dadas até aquele momento. | Confirmado | Resposta "Com pausa, entrega no fim" (2026-11-23) |
| SIM-05 | WHEN o simulado é entregue THEN the system SHALL exibir a correção de todas as questões do simulado. | Confirmado | D-001 ("correção no fim") |
| SIM-06 | WHEN o estudante responde uma questão em um simulado THEN the system SHALL registrar a resposta como uma tentativa individual, identificada como de simulado. | Confirmado | Proposta do consultor; reformulado na revisão externa (2026-11-23) para não criar regra de métrica própria; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| SIM-07 | IF uma questão do simulado ficar sem resposta, inclusive quando o tempo acaba, THEN the system SHALL tratá-la como em branco, sem registrar tentativa. | Confirmado | Resposta "Em branco, à parte" (2026-11-23) |
| SIM-08 | WHEN o simulado é entregue THEN the system SHALL mostrar a quantidade de acertos, de erros e de questões em branco, e a nota como acertos sobre o total de questões do simulado. | Confirmado | Resposta "Em branco, à parte" (2026-11-23) |
| SIM-09 | WHEN o estudante cria um simulado THEN the system SHALL sortear a quantidade de questões definida entre as questões publicadas que atendem aos filtros escolhidos (área, tema, banca, ano). | Confirmado | Resposta "Filtros + sorteio" (2026-11-23) |

SIM-06 só registra a tentativa. O uso dela segue as regras que já existem: histórico com a origem (DES-05), desempenho geral pela primeira tentativa (DES-01), visão de simulados com todas as respostas (DES-09) e lista de erros pela tentativa mais recente (REV-01).

## REV: revisão dos erros e "marcar"

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| REV-01 | The system SHALL incluir na lista de erros as questões cuja tentativa mais recente do estudante está errada. | Confirmado | Resposta "1ª no desempenho, última nos erros" (2026-11-23) |
| REV-02 | WHEN o estudante acerta uma questão da lista de erros THEN the system SHALL retirá-la da lista. | Confirmado | Resposta "1ª no desempenho, última nos erros" (2026-11-23) |
| REV-03 | WHEN o estudante marca uma questão THEN the system SHALL mantê-la na lista de marcadas desse estudante até que ele a desmarque, sem alterar as listas de outros estudantes. | Confirmado | D-001 ("marcar" unifica favoritos e "para revisar"); comportamento proposto; marcação individual explicitada na revisão externa (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| REV-04 | WHILE uma questão marcada estiver retirada de circulação the system SHALL mantê-la na lista de marcadas do estudante, identificada como retirada e com o motivo, sem exibir o conteúdo quando a retirada for por licenciamento (FLUXO-16). | Confirmado | Revisão externa (2026-11-23). O uso em novos treinos e simulados já é impedido por CONT-06 e FLUXO-14. Exceção de licenciamento acrescentada na verificação final (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| REV-05 | WHEN o gabarito de uma questão muda (CONT-09, CONT-15) THEN the system SHALL reavaliar pelo gabarito novo a presença da questão na lista de erros e no filtro "erradas" de cada estudante que a respondeu. | Confirmado | Resposta "Sim, usam o novo" (2026-11-23) |
| REV-06 | WHEN uma questão é retirada de circulação THEN the system SHALL removê-la da lista de erros de cada estudante. | Confirmado | Resposta "Sai da lista de erros" (2026-11-23); exceção explícita a REV-01 |

REV-06 é uma exceção a REV-01: a questão retirada sai da lista de erros, mas continua no histórico (FLUXO-15) e, se estiver marcada, na lista de marcadas (REV-04). Se ela voltar a circular (FLUXO-12), REV-01 volta a valer. REV-05 muda só a avaliação da resposta; o registro dela continua inalterado (CONT-18).

As listas de marcadas e de erros são listas pessoais do estudante, não resultados de filtro (CAT-02). Por isso REV-04 não conflita com CONT-06 e FLUXO-14, que tiram a questão retirada dos filtros, treinos e simulados.

## DES: desempenho

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| DES-01 | The system SHALL calcular o desempenho com base apenas na primeira tentativa de cada questão. | Confirmado | Resposta "1ª no desempenho, última nos erros" (2026-11-23) |
| DES-02 | The system SHALL exibir a taxa de acerto do estudante por grande área e por tema. | Confirmado | D-001 |
| DES-03 | The system SHALL destacar como "mais fracos" apenas temas em que o estudante respondeu pelo menos 5 questões. | Confirmado | Resposta "5 respostas" (2026-11-23) |
| DES-04 | The system SHALL ordenar os temas "mais fracos" da menor para a maior taxa de acerto. | Confirmado | Proposta do consultor; o ajuste pedido na revisão do usuário está em DES-07 e DES-08; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| DES-05 | WHEN o estudante responde uma questão em treino ou em simulado THEN the system SHALL registrar a tentativa no histórico do estudante, identificando a origem (treino ou simulado). | Confirmado | Observação do usuário sobre treino e simulado (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| DES-06 | WHEN o estudante consulta o desempenho THEN the system SHALL oferecer três visões: geral (regra de DES-01), só treino (regra a definir na spec de DES) e só simulados (regra de DES-09). | Confirmado | Observação do usuário sobre treino e simulado (2026-11-23); regras de cada visão explicitadas na revisão externa (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| DES-07 | The system SHALL exibir, junto a cada taxa de acerto e em todas as visões, a quantidade de respostas consideradas no cálculo. | Confirmado | Revisão do usuário em DES-04 (2026-11-23); "em todas as visões" e "respostas consideradas" acrescentados na revisão externa (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| DES-08 | IF uma taxa de acerto se basear em menos de 10 respostas THEN the system SHALL sinalizá-la como baseada em poucas respostas. | Confirmado | Revisão do usuário em DES-04 (2026-11-23): não apresentar amostra pequena como conclusão robusta; limiar confirmado na resposta "10 respostas" (2026-11-23) |
| DES-09 | WHEN o estudante consulta o desempenho só de simulados THEN the system SHALL calcular a taxa com todas as respostas dadas em simulados, inclusive de questões já respondidas no treino. | Confirmado | Resposta "Todas as do simulado" (2026-11-23) |
| DES-10 | The system SHALL exibir os temas "mais fracos" (DES-03, DES-04) somente na visão geral do desempenho. | Confirmado | Resposta "Só na visão geral" (2026-11-23) |

DES-09 é uma exceção a DES-01 válida só na visão de simulados. A visão geral continua usando apenas a primeira tentativa de cada questão.

**Como cada visão conta as respostas** (DES-06):

| Visão | O que entra no cálculo | Regra |
|---|---|---|
| Geral | A primeira tentativa de cada questão, feita em treino ou em simulado. A quantidade exibida coincide com o número de questões respondidas. | DES-01 |
| Só treino | A definir na spec de DES (pendência abaixo). | — |
| Só simulados | Todas as respostas dadas em simulados, inclusive repetições da mesma questão. A quantidade exibida conta respostas, não questões. | DES-09 |

Por isso o catálogo diz "respostas consideradas no cálculo" (DES-07), e não "questões respondidas".

### Em aberto nestes temas

| Questão | Para onde vai |
|---|---|
| A pausa do simulado tem limite (quantidade ou duração)? E se o estudante fechar o app sem pausar, o cronômetro continua? | Spec de SIM |
| Período do desempenho: todo o histórico ou com recorte de tempo (por exemplo, últimos 30 dias)? | Spec de DES |
| Quantidade máxima de questões por simulado. | Spec de SIM |
| Na visão só de treino (DES-06), vale a primeira tentativa entre as feitas no treino ou a primeira tentativa geral (que pode ter sido num simulado)? | Spec de DES |
| Quando um treino termina: ao responder todas as questões, quando o estudante encerra ou quando inicia outro treino? Ele pode ser retomado depois de fechar o app (TREINO-04)? | Spec de TREINO |
| No sorteio do simulado (SIM-09): o que acontece se houver menos questões que a quantidade pedida, e o sorteio dá preferência a questões ainda não respondidas? | Spec de SIM |

## EDIT: painel do editor

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| EDIT-01 | The system SHALL registrar em cada questão: enunciado; alternativas na ordem original; gabarito e sua origem (CONT-01); comentário (opcional); referências; origem da questão (banca, ano e número, ou autoria própria com o autor); situação de autorização de uso com a evidência correspondente (EDIT-04); classificação (CAT-01). | Confirmado | D-001 (origem, licença, referências); regras de integridade do projeto; comentário opcional segundo um dos caminhos de D-003; "licença" substituída por situação de autorização com evidência na revisão externa (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| EDIT-02 | IF o editor tentar salvar uma imagem sem origem, sem situação de autorização de uso (EDIT-04) ou sem classificação (informativa, objeto de avaliação ou decorativa) THEN the system SHALL recusar a imagem e indicar o campo que falta. | Confirmado | D-001 (imagens); licenciamento; o texto alternativo passou para EDIT-07 a EDIT-09 conforme a revisão externa (2026-11-23); as três categorias foram confirmadas na resposta "Três categorias" (2026-11-23), o restante do critério segue proposto; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| EDIT-03 | The system SHALL oferecer o painel do editor (cadastro, revisão e reportes) para uso em computador. | Confirmado | Resposta "Só computador" (2026-11-23) |
| EDIT-04 | The system SHALL registrar, para cada questão e cada imagem, uma situação de autorização de uso entre: não verificada; autorizada com evidência registrada (documento, licença ou permissão por escrito); não autorizada. | Confirmado | Revisão externa (2026-11-23): preencher um campo de licença não comprova o direito de uso; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| EDIT-05 | IF a situação de autorização de uso de uma questão ou de uma de suas imagens não for "autorizada com evidência registrada" THEN the system SHALL impedir a publicação. | Confirmado | Revisão externa (2026-11-23); confirmado, inclusive para o beta fechado, na resposta "Regra vale; consulta jurídica" (2026-11-23) |
| EDIT-06 | The system SHALL permitir somente ao administrador registrar uma questão ou imagem como "autorizada com evidência registrada". | Confirmado | Proposta do consultor ligada à revisão externa (2026-11-23): separar quem cadastra de quem atesta a autorização; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| EDIT-07 | IF o editor tentar salvar uma imagem informativa sem texto alternativo que descreva seu conteúdo THEN the system SHALL recusar a imagem. | Confirmado | Revisão externa (2026-11-23); WCAG 2.2, critério 1.1.1; confirmado na resposta "Três categorias" (2026-11-23) |
| EDIT-08 | WHERE uma imagem for classificada como decorativa the system SHALL apresentá-la de forma que tecnologias assistivas a ignorem, com texto alternativo vazio. | Confirmado | Revisão externa (2026-11-23); WCAG 2.2, critério 1.1.1; confirmado na resposta "Três categorias" (2026-11-23) |
| EDIT-09 | WHERE uma imagem for o próprio objeto de avaliação da questão (por exemplo, um ECG ou uma radiografia a interpretar) the system SHALL exigir texto alternativo com a identificação descritiva da imagem, sem a interpretação dos achados. | Confirmado | Contraproposta do consultor à revisão externa, com base na exceção para testes do critério 1.1.1 da WCAG 2.2; confirmada na resposta "Três categorias" (2026-11-23) |
| EDIT-10 | WHEN a correção de uma questão cuja imagem é objeto de avaliação (EDIT-09) é exibida THEN the system SHALL mostrar a descrição dos achados da imagem, quando o editor a tiver registrado. | Confirmado | Proposta separada do consultor (2026-11-23), aprovada na resposta "Aprovar" (2026-11-23) |
| EDIT-11 | IF uma questão com comentário não tiver ao menos uma referência THEN the system SHALL impedir sua publicação. | Confirmado | Proposta separada do consultor (2026-11-23), aprovada na resposta "Aprovar" (2026-11-23) |

Funcionar em tablet ou celular não é requisito do MVP para o painel do editor. RNF-04 trata só das funcionalidades do estudante.

**Imagens: por que três categorias.** A revisão externa pede que o texto alternativo de imagens clínicas essenciais transmita a informação relevante. Isso vale para as imagens **informativas** (EDIT-07). Quando a imagem é o que está sendo avaliado, porém, descrever os achados entrega a resposta. A WCAG 2.2 prevê esse caso no critério 1.1.1: em testes que seriam invalidados se apresentados em texto, o texto alternativo deve trazer pelo menos a identificação descritiva do conteúdo ("at least descriptive identification"). A W3C não cita imagens médicas; aplicar a exceção a elas é interpretação do consultor, por analogia com o exemplo de exercício de habilidade visual que a própria W3C dá.

### Duas comprovações que não se substituem

| | Autorização de uso do conteúdo | Origem e situação do gabarito |
|---|---|---|
| O que comprova | Que a plataforma pode usar e reproduzir enunciado, alternativas, comentário e imagens | De onde vem a questão e se o gabarito é oficial, preliminar ou definido por uma pessoa |
| Evidência | Documento, licença ou permissão por escrito do titular (EDIT-04) | Origem da questão (EDIT-01) e, quando o gabarito é oficial, referência verificável ao documento da banca (CONT-21, CONT-22) |
| Quem registra | Somente o administrador atesta a autorização (EDIT-06) | O editor |
| Bloqueia a publicação | Sim, se não estiver "autorizada com evidência registrada" (EDIT-05) | Sim, se o gabarito oficial não tiver a referência (CONT-22) |
| Decisão pendente ligada | D-002 | — |

Uma comprovação não substitui a outra. O gabarito oficial publicado pela banca não dá direito de reproduzir a questão, e uma licença de uso não comprova que o gabarito é oficial.

### Dependências jurídicas

Não é parecer jurídico. São os pontos que precisam de esclarecimento por advogado antes da abertura ao público (D-001), alguns já antes do beta:

| Tema | Ligação | Antes do beta? |
|---|---|---|
| Uso de questões de provas anteriores: enunciado, alternativas e gabarito oficial | D-002, EDIT-04, EDIT-05 | Sim, se o beta usar provas anteriores |
| Imagens de provas e de terceiros, inclusive imagens clínicas que possam identificar pacientes (dado referente à saúde é dado pessoal sensível, LGPD art. 5º, II) | D-002, EDIT-04 | Sim, se o beta usar essas imagens |
| Autorização por escrito de autores próprios e colaboradores para questões e comentários | D-002, EDIT-04 | Sim |
| Termos de uso e política de privacidade | D-009, CONTA-09 | Sim |
| Anonimização com poucos usuários e supressão de grupos pequenos | CONTA-12, CONTA-19 | Não; Etapa 6 |
| Atendimento a pedidos de retirada feitos por titulares de direitos | FLUXO-09 | Não; antes da abertura |

O beta fechado não autoriza, por si só, reproduzir provas de terceiros.

**Conteúdo do beta** (resposta "Regra vale; consulta jurídica", 2026-11-23): EDIT-05 vale também no beta. Até uma consulta jurídica, o beta usa questões próprias com autorização por escrito do autor ou conteúdo licenciado. Provas anteriores só entram se a consulta permitir, com a evidência registrada (EDIT-04).

## FLUXO: status editorial, revisão e versões

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| FLUXO-01 | The system SHALL manter cada versão de questão em um destes status: rascunho, em revisão, publicada, retirada. | Confirmado | Proposta do consultor; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| FLUXO-02 | WHEN o revisor reprova uma versão THEN the system SHALL devolvê-la ao status rascunho com o motivo da reprovação. | Confirmado | Proposta do consultor; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| FLUXO-03 | IF o revisor for a mesma pessoa que escreveu ou cadastrou a versão THEN the system SHALL impedir que ele a aprove. | Confirmado | Resposta "Não, revisor diferente" (2026-11-23) |
| FLUXO-04 | WHEN o enunciado, as alternativas, o gabarito, o comentário, as referências ou as imagens de uma questão publicada são alterados THEN the system SHALL criar uma nova versão e manter a anterior no histórico. | Confirmado | Resposta "Qualquer mudança de conteúdo" (2026-11-23) |
| FLUXO-05 | IF uma nova versão não tiver revisão aprovada THEN the system SHALL impedir que ela seja exibida aos estudantes. | Confirmado | Resposta "Qualquer mudança de conteúdo" (2026-11-23) |
| FLUXO-06 | WHILE uma nova versão aguarda revisão the system SHALL continuar exibindo aos estudantes a versão publicada anterior, exceto se a questão tiver sido retirada de circulação (FLUXO-09). | Confirmado | Proposta do consultor; exceção da retirada explicitada na revisão externa (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| FLUXO-07 | WHEN só a classificação ou os metadados de uma questão são alterados THEN the system SHALL aplicar a mudança sem criar nova versão. | Confirmado | Resposta "Qualquer mudança de conteúdo" (2026-11-23) |
| FLUXO-08 | The system SHALL registrar, para cada alteração em uma questão, inclusive de classificação e metadados: quem a fez, quando, a versão envolvida, o campo alterado, o valor anterior e o novo valor. | Confirmado | Rastreabilidade (regras de integridade do projeto); campo, valores e versão acrescentados na revisão externa (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| FLUXO-09 | WHEN um editor retira uma questão de circulação, por anulação, desatualização, erro que exija ação imediata, problema de licenciamento ou suspeita de falta de autorização de uso, THEN the system SHALL efetivar a retirada na hora, sem exigir nova revisão. | Confirmado | Revisado conforme revisão do usuário (2026-11-23); motivos de licenciamento acrescentados na revisão externa (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| FLUXO-10 | WHEN uma questão é retirada de circulação THEN the system SHALL registrar quem a retirou, quando e o motivo. | Confirmado | Revisão do usuário em FLUXO-09 (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| FLUXO-11 | IF o editor tentar retirar uma questão sem informar o motivo THEN the system SHALL recusar a retirada. | Confirmado | Revisão do usuário em FLUXO-09 (2026-11-23): o motivo precisa existir para ser registrado; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| FLUXO-12 | WHEN uma questão retirada por erro é corrigida THEN the system SHALL permitir que ela volte a circular somente como nova versão aprovada em revisão por pessoa diferente do autor. | Confirmado | Resposta "Sim, como nova versão" (2026-11-23) |
| FLUXO-13 | WHEN uma questão retirada volta a circular THEN the system SHALL manter o registro da retirada no histórico da questão. | Confirmado | Resposta "Sim, como nova versão" (2026-11-23) |
| FLUXO-14 | WHEN uma questão é retirada de circulação por qualquer motivo THEN the system SHALL excluí-la de novos treinos, novos simulados e dos resultados de filtro. | Confirmado | Revisão cruzada do consultor (2026-11-23): CONT-06 cobre só anulação e desatualização, e FLUXO-09 tem mais motivos; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| FLUXO-15 | WHEN um estudante que já respondeu uma questão retirada consulta seu histórico THEN the system SHALL exibir o registro da resposta com o motivo da retirada. | Confirmado | Revisão cruzada do consultor (2026-11-23): estende CONT-07 a todos os motivos de retirada; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| FLUXO-16 | WHEN uma questão é retirada por problema de licenciamento THEN the system SHALL deixar de exibir o conteúdo dela também no histórico dos estudantes, mantendo só o registro da resposta e o motivo. | Confirmado | Proposta separada do consultor (2026-11-23), aprovada na resposta "Aprovar" (2026-11-23). Anulação e desatualização seguem CONT-07 |
| FLUXO-17 | WHEN uma questão é retirada de circulação, por qualquer motivo, THEN the system SHALL preservar todas as tentativas e respostas já registradas para ela. | Confirmado | Verificação final pedida pelo usuário (2026-11-23): o histórico continua preservado; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |

**Retirada de circulação, em resumo:**

| Efeito | Qualquer motivo | Retirada por licenciamento |
|---|---|---|
| Sai de novos treinos, simulados e filtros | Sim (CONT-06 para anulação e desatualização; FLUXO-14 para os demais motivos) | Sim |
| Sai da lista de erros | Sim (REV-06) | Sim |
| Continua na lista de marcadas, identificada como retirada | Sim (REV-04) | Sim, sem o conteúdo (REV-04) |
| Tentativas e respostas preservadas | Sim (FLUXO-17, CONT-18) | Sim |
| O histórico mostra | A questão, na anulação e na desatualização (CONT-07); o registro da resposta e o motivo, nos demais casos (FLUXO-15) | Só o registro da resposta e o motivo, sem o conteúdo (FLUXO-16). Quais metadados entram nesse registro depende da consulta jurídica |

No histórico editorial (FLUXO-08), o responsável é identificado pela conta, sem e-mail nem outros dados pessoais desnecessários. Nas mudanças de conteúdo, os valores anteriores já ficam guardados nas versões (FLUXO-04), e o histórico pode apontar para elas em vez de copiar o conteúdo. Como representar isso é assunto da Etapa 4.

## REP: reportar erro

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| REP-01 | WHEN o estudante reporta um erro em uma questão THEN the system SHALL registrar o reporte, com o motivo informado, na fila do editor. | Confirmado | Resposta "Fila + resposta ao aluno" (2026-11-23) |
| REP-02 | WHEN o editor conclui um reporte THEN the system SHALL registrá-lo como procedente ou não procedente. | Confirmado | Resposta "Fila + resposta ao aluno" (2026-11-23) |
| REP-03 | WHEN um reporte é concluído THEN the system SHALL mostrar o resultado ao estudante que o enviou. | Confirmado | Resposta "Fila + resposta ao aluno" (2026-11-23) |

### Em aberto nestes temas

| Questão | Para onde vai |
|---|---|
| O editor vê quem enviou cada reporte, ou os reportes chegam sem identificação? | Etapa 6 |
| Campos de referência bibliográfica (livro, diretriz, artigo, link com data de acesso). | Etapa 4 |
| Quais metadados de uma questão retirada por licenciamento podem continuar visíveis no histórico (por exemplo, área, tema, banca, ano, alternativa marcada, resultado e data) (FLUXO-16). | Etapa 6, com a consulta jurídica (D-002) |

## RNF: requisitos não funcionais

### Acessibilidade, idioma e dispositivos

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| RNF-01 | The system SHALL cumprir a WCAG 2.2 no nível AA. | Confirmado | Resposta "WCAG 2.2 nível AA" (2026-11-23) |
| RNF-02 | The system SHALL apresentar a interface somente em português do Brasil. | Confirmado | Resposta "Só pt-BR" (2026-11-23); D-016 |
| RNF-03 | The system SHALL funcionar nas duas versões principais mais recentes do Safari no iOS e no iPadOS, do Chrome no Android e do Chrome e do Edge em computadores. | Confirmado | Proposta do consultor; uso principal em celular e tablet (D-014); lista reduzida na revisão externa (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| RNF-04 | The system SHALL oferecer todas as funcionalidades do estudante em celulares, tablets (em retrato e em paisagem) e computadores, adaptando o layout ao tamanho da tela. | Confirmado | Revisado conforme revisão do usuário (2026-11-23); breakpoints ficam para a Etapa 5; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| RNF-14 | WHEN o aparelho muda de orientação THEN the system SHALL preservar as respostas já dadas, a alternativa selecionada, a posição na sequência de questões e o tempo restante do simulado, sem reiniciar o cronômetro. | Confirmado | Revisão do usuário em RNF-04 (2026-11-23); itens explicitados na revisão externa (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| RNF-15 | The system SHALL permitir todas as ações do estudante por toque, sem depender de passar o cursor sobre elementos. | Confirmado | Revisão do usuário em RNF-04 (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |

RNF-04, RNF-14 e RNF-15 tratam da experiência do estudante; o painel do editor é só para computador no MVP (EDIT-03). Firefox e Safari no macOS não têm garantia formal (RNF-03), mas o desenvolvimento segue padrões web e evita recursos sem suporte amplo, o que tende a mantê-los funcionando.

### Conectividade

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| RNF-05 | The system SHALL exigir conexão com a internet para uso. | Confirmado | Resposta "Sempre online" (2026-11-23) |
| RNF-06 | IF a conexão cair THEN the system SHALL exibir um aviso de que o aparelho está sem conexão. | Confirmado | Resposta "Sempre online" (2026-11-23) |
| RNF-07 | IF a conexão cair durante um simulado THEN the system SHALL manter as respostas já dadas e registrá-las quando a conexão voltar. | Confirmado | Resposta "Sempre online" (2026-11-23): "uma queda curta não faz perder respostas do simulado" |

### Backup e recuperação

Durante o beta não há meta formal de disponibilidade (resposta "Até 24 horas", 2026-11-23).

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| RNF-08 | The system SHALL ter backup completo do banco de dados ao menos uma vez a cada 24 horas. | Confirmado | Resposta "Até 24 horas" (2026-11-23) |
| RNF-09 | The system SHALL guardar cada backup por 30 dias. | Confirmado | Resposta "Até 24 horas" (2026-11-23) |
| RNF-10 | The system SHALL ter a restauração de backup testada ao menos uma vez por mês. | Confirmado | Teste periódico confirmado na resposta "Até 24 horas"; frequência mensal proposta pelo consultor; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |

### Segurança

O detalhamento de segurança e LGPD é da Etapa 6.

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| RNF-11 | The system SHALL servir a aplicação somente por HTTPS, redirecionando para HTTPS qualquer acesso por HTTP. | Confirmado | Proposta do consultor; redação ajustada na revisão cruzada (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |

HTTPS é condição básica e não substitui os demais controles de segurança da Etapa 6.

### Política de registros (logs)

Os logs servem a diagnóstico e auditoria, sem expor credenciais e com o mínimo de dados pessoais. Há três categorias de registro: logs de aplicação (diagnóstico técnico), registros de segurança (eventos como logins e acessos negados; quais eventos entram é assunto da Etapa 6, conforme a seção 16.3 do OWASP ASVS 5.0) e a trilha de auditoria editorial (FLUXO-08, FLUXO-10), que faz parte do histórico das questões.

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| RNF-12 | The system SHALL omitir dos logs senhas, tokens de sessão, links de convite e de recuperação de senha e quaisquer outras credenciais. | Confirmado | Revisado conforme revisão do usuário (2026-11-23); aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| RNF-16 | The system SHALL identificar o usuário nos logs pelo identificador interno da conta, nunca pelo e-mail ou pelo apelido. | Confirmado | Revisão do usuário em RNF-12 (2026-11-23): minimizar dados pessoais; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| RNF-17 | The system SHALL permitir acesso aos logs somente a pessoas com autorização individual e explícita para isso, inclusive entre administradores. | Confirmado | Revisão do usuário em RNF-12 (2026-11-23): controle de acesso; menor privilégio aplicado na revisão externa (2026-11-23); OWASP ASVS 5.0, requisito 16.4.2; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| RNF-18 | The system SHALL manter separadas as três categorias de registro (logs de aplicação, registros de segurança e trilha de auditoria editorial), cada uma com prazo de retenção próprio. | Confirmado | Revisão do usuário em RNF-12 (2026-11-23): retenção; reformulado na revisão externa (2026-11-23). Os prazos ficam para a Etapa 6; os 90 dias antes propostos para logs de aplicação são só hipótese inicial; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| RNF-20 | WHEN alguém acessa os logs THEN the system SHALL registrar quem acessou e quando. | Confirmado | Revisão externa (2026-11-23); depende da ferramenta de logs escolhida na Etapa 3; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |

### Desempenho

| ID | Critério | Situação | Fonte |
|---|---|---|---|
| RNF-13 | WHEN o estudante toca em "Próxima questão" THEN the system SHALL exibir o enunciado e as alternativas prontos para resposta em até 1 s no percentil 75 e em até 2 s no percentil 95, nas condições de medição abaixo. | Confirmado | Revisado conforme revisão do usuário (2026-11-23); meta provisória até a medição na Etapa 3; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |
| RNF-19 | WHEN uma questão tem imagem THEN the system SHALL exibir o enunciado e as alternativas sem esperar o carregamento da imagem, reservando o espaço dela na tela. | Confirmado | Revisão do usuário em RNF-13 (2026-11-23): tratamento das imagens; aprovado na aprovação formal da Etapa 2 ("Aprovar Etapa 2", 2026-11-23) |

**Condições de medição de RNF-13** (proposta, revisada em 2026-11-23):

- **Intervalo**: do toque em "Próxima questão" até o enunciado estar visível e as alternativas aceitarem toque, medido por marcas de tempo registradas pelo próprio app. O carregamento de imagens fica fora do intervalo (RNF-19); é medido e relatado à parte, sem meta até o protótipo.
- **Percentis**: p75 até 1 s e p95 até 2 s.
- **Estado**: treino já iniciado; cache do navegador no estado normal de uso, sem limpeza entre transições; servidor na região prevista para produção; acervo de teste fictício, com tamanho registrado no relatório.
- **Rede (laboratório)**: limitação aplicada no navegador com os valores que a documentação do Lighthouse indica para reproduzir seu perfil móvel padrão, "Slow 4G", nesse modo: latência de 562,5 ms por requisição, download de 1.474,56 kbit/s e upload de 675 kbit/s. Os valores mais conhecidos, 150 ms e 1,6 Mbit/s, servem à simulação interna do Lighthouse, não à limitação aplicada. Fonte conferida em 2026-11-23: `docs/throttling.md` do repositório oficial do Lighthouse.
- **CPU (laboratório)**: desaceleração de 4 vezes, o multiplicador do mesmo perfil.
- **Aparelhos reais**: um celular Android intermediário e um iPad, com modelo e versão do sistema registrados no relatório. Confirmam o laboratório, mas não aprovam nem reprovam a meta.
- **Amostra**: pelo menos 300 transições por cenário automatizado (celular e tablet) e 100 por aparelho real. Com 100 amostras, só 5 ficam acima do p95, e o intervalo de 95% de confiança do p95 vai aproximadamente do 91º percentil medido até o maior valor. Com 300, fica aproximadamente entre o 93º e o 98º percentil medido.
- **Relatório**: p75 e p95 de cada cenário, com o intervalo de confiança.
- **Viabilidade**: com o perfil acima, cada requisição ao servidor custa pelo menos meio segundo de latência simulada. A meta de 1 s no p75 só é realista se a próxima questão for carregada com antecedência ou depender de uma única requisição pequena. Isso entra como critério na Etapa 3, e a meta só é fixada depois de medir um protótipo.

### Em aberto neste tema

| Questão | Para onde vai |
|---|---|
| Breakpoints e layout por tamanho de tela (por exemplo, questão e correção lado a lado no tablet em paisagem). | Etapa 5 |
| Registro do endereço IP em eventos de segurança e retenção específica para esses eventos. | Etapa 6 |
| Meta definitiva de RNF-13, depois de medir um protótipo. | Etapa 3 |
| Prazos de retenção de cada categoria de registro (RNF-18), considerando necessidade operacional, segurança, privacidade e obrigações legais. | Etapa 6 |
| Quais eventos de segurança são registrados (por exemplo, logins e acessos negados), conforme a seção 16.3 do OWASP ASVS 5.0. | Etapa 6 |
| A ferramenta de logs permite registrar quem acessou os logs (RNF-20)? | Etapa 3 |
| Conferir os aparelhos e as versões reais dos participantes do beta (por exemplo, iPads presos em versões antigas do iPadOS) e ajustar RNF-03 se preciso. | Antes do beta |

## Propostas separadas

Lacunas que o consultor encontrou na revisão cruzada, fora do que foi pedido. Só entram no catálogo se o usuário aprovar.

As quatro propostas separadas da revisão de consenso (CONT-21, EDIT-10, EDIT-11 e FLUXO-16) foram aprovadas pelo usuário em 2026-11-23 e movidas para as seções de origem como confirmadas. Não há propostas separadas pendentes.

## Aprovação da Etapa 2

Aprovada em 2026-11-23 ("Aprovar Etapa 2"). Os itens 2 a 4 alteram `docs/decisions.md` e só são feitos com autorização explícita do usuário.

1. Feito: os propostos passaram a confirmados, com as palavras do usuário e a data, e este catálogo passou a aprovado.
2. Feito: **D-018** (Aprovada), convites e papéis centralizados no administrador durante o beta fechado (CONTA-16), como decisão operacional, não limitação permanente.
3. Feito: **D-019** (Aprovada), conteúdo permitido no beta fechado (EDIT-05), com ADR em `docs/adr/D-019-conteudo-permitido-no-beta.md`.
4. Feito: **D-002** (continua Pendente), resumo atualizado para separar a autorização de uso do conteúdo da comprovação do gabarito, apontar para D-019 e manter pendente o uso de conteúdo de terceiros sem autorização comprovada.
5. Feito: Etapa 2 encerrada no histórico abaixo.

Itens 2 a 4 autorizados pelo usuário na resposta "Autorizo como está" (2026-11-23).

## Histórico

- 2026-11-23: catálogo criado na Etapa 2, com os blocos 1 a 5.
- 2026-11-23: revisão crítica do usuário. Oito propostos ajustados (CONTA-10, CONTA-14, CONTA-16, DES-04, FLUXO-09, RNF-04, RNF-12, RNF-13), com novos critérios CONTA-17, DES-07, DES-08, FLUXO-10, FLUXO-11 e RNF-14 a RNF-19. Três observações incorporadas em CONT-11 a CONT-14, DES-05 e DES-06. O catálogo ainda não foi aprovado como um todo.
- 2026-11-23: sete dúvidas respondidas pelo usuário. Novos critérios confirmados: CONT-15 a CONT-17, DES-09, FLUXO-12, FLUXO-13 e EDIT-03. DES-08 passou a confirmado (limiar de 10 respostas). CONTA-16 entra no índice na aprovação formal da Etapa 2.
- 2026-11-23: revisão de consenso a partir da revisão externa trazida pelo usuário. 19 propostos ajustados, 21 critérios novos propostos e 4 propostas separadas. Valores do Lighthouse conferidos na documentação oficial e exceção de testes da WCAG 2.2 conferida no site da W3C. Nenhum critério confirmado foi alterado e nada foi aprovado.
- 2026-11-23: oito dúvidas e quatro propostas separadas respondidas pelo usuário. Novos critérios confirmados: REV-05, REV-06, DES-10, SIM-07, SIM-08, SIM-09 e CONTA-24. EDIT-05, EDIT-07, EDIT-08 e EDIT-09 passaram de propostos a confirmados. Propostas separadas aprovadas e movidas para as seções de origem: CONT-21, EDIT-10, EDIT-11 e FLUXO-16. O catálogo ainda não foi aprovado como um todo.
- 2026-11-23: verificações finais pedidas pelo usuário. Novos propostos: CONT-22 (gabarito oficial exige referência desde o cadastro) e FLUXO-17 (retirada preserva tentativas e respostas). REV-04 ajustado para não exibir conteúdo retirado por licenciamento. Acrescentados o quadro "Duas comprovações que não se substituem" e o resumo da retirada de circulação. Nenhum critério confirmado foi alterado.
- 2026-11-23: **Etapa 2 aprovada formalmente** ("Aprovar Etapa 2"). Os 64 critérios propostos passaram a confirmados, totalizando 131 critérios confirmados. Os 67 confirmados anteriores não mudaram. Índice atualizado com autorização do usuário: D-018 e D-019 aprovadas (D-019 com ADR) e D-002 atualizada, ainda pendente.
