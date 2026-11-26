# D-009: Tratamento de dados pessoais (LGPD)

- **Status**: Aprovada
- **Data**: 2026-11-24 (registro em 2026-11-25; catálogo e modelo em 2026-11-26)
- **Aprovação**: respostas do bloco 3 da Etapa 6, "Você, pessoa física, no beta (Recomendado)", "Guardar só contagens (Recomendado)", "Excluir após 24 meses sem uso (Recomendado)" e "Claude rascunha, advogado revisa (Recomendado)"; versão consolidada aprovada com "Aprovar bloco 3" (2026-11-24); registro pedido com "vamos" (2026-11-25)
- **Muda**: CONTA-12 (substituído por CONTA-70), CONTA-25 (removido), M-21, M-36 e RM-13 (substituídas por M-40, M-42 e RM-19) e M-07 e M-22 (substituídas em parte por M-40 e M-41); registrado em 2026-11-26
- **Critérios**: CONTA-70 a CONTA-97, REP-04 a REP-06 e RNF-95 a RNF-97
- **Relacionadas**: D-001, D-002, D-007, D-008, D-024, D-032, D-033, D-034; `docs/seguranca-e-privacidade.md`, seções 2 e 3; perguntas Jur-01 a Jur-16

## Contexto

- O MVP inclui termos de uso, política de privacidade, exportar e excluir conta (D-001). Cadastro, respostas e desempenho dos estudantes são dados pessoais (LGPD, art. 5º, I).
- A Etapa 4 aprovou guardar as respostas de quem exclui a conta, desvinculadas, para as estatísticas das questões (CONTA-12, M-21). O bloco 2 concluiu que, num beta pequeno, essas respostas podem não ser anônimas de verdade, e a LGPD (art. 16, IV) só permite guardar dados depois do fim do tratamento se forem anonimizados.
- A LGPD pede guardar dados só enquanto forem necessários, e contas esquecidas acumulariam dados sem finalidade.
- Normas consultadas, em republicações, não no Diário Oficial: Resolução CD/ANPD nº 2/2022 (agentes de pequeno porte) e Resolução CD/ANPD nº 15/2024 (comunicação de incidentes). A conferência no Diário Oficial é a Jur-14.
- O usuário prioriza não ter problemas futuros: "Vamos revisar certinho pra eu nao ter problemas futuros".

## Opções consideradas

| Tema | Escolhida | Outras opções apresentadas |
|---|---|---|
| Controlador no beta | O usuário, pessoa física, agente de pequeno porte, com canal de privacidade; empresa antes da cobrança | Empresa (CNPJ) desde já, que separa o patrimônio, mas exige abrir a empresa antes do beta e traz a guarda de registros de acesso do Marco Civil (art. 15) |
| Respostas de quem exclui a conta | Guardar só contagens por versão e alternativa e apagar as tentativas | Manter as respostas desvinculadas até a consulta jurídica, com risco de mudar depois com dados já guardados; apagar tudo, o que tira as respostas de quem saiu das estatísticas |
| Conta parada | Excluir após 24 meses sem uso, com aviso 30 dias antes | Excluir após 12 meses, o que pode apagar quem só deu uma pausa longa; nunca excluir sozinho, o que guarda contas esquecidas para sempre |
| Termos e política | O Claude rascunha, e um advogado revisa antes do beta | O advogado escreve do zero, mais caro e demorado |

## Decisão

- O detalhamento está em `docs/seguranca-e-privacidade.md`, seção 3, que segue a versão consolidada aprovada com os seis ajustes do usuário.
- **Controlador:** o usuário, pessoa física, no beta. A LGPD vale para o beta, que tem intenção comercial. Sem encarregado, com canal de contato, salvo tratamento de alto risco. A passagem para uma empresa é formalizada.
- **Exclusão da conta:** as respostas viram contagens de pessoas distintas por versão e alternativa, pela primeira resposta de cada pessoa em cada versão, e as tentativas são apagadas na mesma transação. A estatística da equipe não muda com a exclusão, tem proteção contra dedução e trata as contagens como dado pessoal desvinculado. Reportes concluídos perdem o texto livre, com exceções restritas.
- **Destino de cada registro na exclusão:** tabela B.12.
- **Inatividade:** estudante excluído após 24 meses sem uso, com aviso 30 dias antes; equipe sem exclusão automática; concessões sensíveis expiram após 90 dias sem uso; papéis de equipe suspensos após 6 meses; revisão semestral dos privilégios.
- **Direitos do titular:** atendidos no app na hora quando possível; meta interna de 15 dias pelo canal.
- **Incidentes:** comunicação pelos critérios do art. 5º da Resolução 15, com os prazos gerais, e registro de todo incidente por 5 anos.
- **Terceiros:** AWS com análise de transferência internacional; Pwned Passwords só com o prefixo do SHA-1 calculado em memória; fontes no próprio servidor; só cookies essenciais.
- **Convites e idade:** convite só a pedido, com aviso de privacidade; declaração de 18 anos ou mais.
- **Documentos jurídicos:** política de privacidade, termos de uso, registro das operações, avaliação do legítimo interesse dos registros de segurança e plano de resposta a incidentes, rascunhados pelo Claude e revisados pelo advogado antes do beta (Etapa 7).

## Registro no catálogo e no modelo (2026-11-26)

Segunda parte do registro, como o usuário escolheu ("Dois PRs (Recomendado)"). Os critérios confirmados que mudaram ganharam ID novo, e os antigos ficaram com a situação "Substituído" ou "Removido" ("ID novo, antigo substituído (Recomendado)"). No modelo, as decisões novas M-40 a M-42 e a regra RM-19 substituem as antigas, que continuam no documento ("Decisões novas que substituem (Recomendado)"). O mapa de cada tema para os critérios e as decisões está em `docs/seguranca-e-privacidade.md`, seção 3.I.

## Atualização da resolução da 5.P.1 (2026-11-25)

A lista própria de exclusões aprovada no bloco 3 (B.8) foi substituída: a fonte única para reaplicar exclusões depois de restaurar um backup são os eventos de exclusão solicitada e concluída do grupo `seguranca`, guardados por 180 dias, com o marco do backup, processamento idempotente e bloqueio em caso de lacuna (RNF-90 a RNF-94).

## Consequências

- **Ganhamos:**
  - a exclusão de conta fica coerente com o art. 16 da LGPD, sem perder a estatística das questões;
  - nenhuma resposta individual sobrevive à exclusão;
  - contas e privilégios parados não acumulam;
  - um plano claro para incidentes e para os pedidos dos titulares.
- **Abrimos mão de:**
  - consultar respostas antigas de contas excluídas, uma a uma;
  - filtros de período e de modalidade na estatística da equipe.
- **Exige:**
  - a consulta jurídica das Jur-01 a Jur-16 antes de abrir o beta;
  - os documentos jurídicos da Etapa 7;
  - um teste automático que prove que a estatística da equipe não muda com a exclusão (D-026).
- **Revisitar se:**
  - o advogado concluir que as contagens não podem ser guardadas (Jur-04), quando vale o plano B de apagar a contribuição de quem saiu;
  - o enquadramento como pequeno porte não se confirmar (Jur-02);
  - o projeto passar para uma empresa ou começar a cobrar;
  - a base de usuários crescer a ponto de mudar a análise de reidentificação.
