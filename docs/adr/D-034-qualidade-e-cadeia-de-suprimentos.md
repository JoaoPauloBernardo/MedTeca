# D-034: Qualidade e cadeia de suprimentos

- **Status**: Aprovada
- **Data**: 2026-11-24
- **Aprovação**: respostas das três rodadas do bloco 6 (2026-11-24); correções do usuário antes da aprovação (2026-11-24); "Aprovar bloco 6" (2026-11-24); registro autorizado com "Sim. Autorizo o registro documental do Bloco 6 agora, em uma branch de trabalho." (2026-11-24)
- **Completa**: D-017, D-026, D-027 e D-033
- **Relacionadas**: D-006, D-020, D-022, D-028, D-032; RNF-70 a RNF-88 em `docs/requisitos-mvp.md`; decisões P6-01 a P6-28, verificações V35 a V51 e a questão Jur-25 em `docs/seguranca-e-privacidade.md`, seção 6; autorizações recorrentes na seção 5.4 do mesmo documento

## Contexto

- **Decisões anteriores:**
  - testes em pirâmide, com uma prova por critério (D-026);
  - CI no GitHub Actions (D-027);
  - spec da TLC antes de cada funcionalidade (D-017);
  - imagem publicada no ECR via OIDC e deploy por comando do usuário (D-033).
- **Fato conferido em 2026-11-24:** o repositório no GitHub é público. Isso torna gratuitos CodeQL, varredura de segredos com bloqueio no envio, revisão de dependências, atestados de origem e regras de proteção de branch. Em troca, logs e artefatos do CI ficam visíveis para qualquer conta do GitHub.
- **Ameaças concretas recentes:**
  - versões de ações do GitHub redirecionadas para código malicioso que roubava segredos do CI (tj-actions, em março de 2025; trivy-action, em março de 2026);
  - pacotes do npm adulterados que roubavam tokens do GitHub e chaves de nuvem na instalação (Shai-Hulud, em 2025).
- **Meta:** OWASP ASVS 5.0 no nível L2. Os requisitos que mais pesaram:
  - 15.1.1 e 15.2.1: prazos de correção escritos e nenhum componente fora deles;
  - 15.1.2: inventário dos componentes de terceiros e repositórios confiáveis;
  - 15.1.3 e 15.2.2: funções pesadas documentadas e defendidas;
  - 15.2.3 e 13.4.x: nada de código de teste, documentação da API ou metadados do Git em produção.
- **Papel do usuário:** estudante de Engenharia de Software e desenvolvedor júnior. Ele lê e revisa o código de todos os pull requests e decide o merge; o Claude implementa, testa, documenta e explica.
- **Restrições:** orçamento de R$ 50 a 150 por mês; operação feita por uma pessoa; uma só identidade no GitHub para o usuário e o Claude.

## Opções consideradas

| Tema | Escolhida | Outras opções apresentadas |
|---|---|---|
| Fluxo até a `main` | Pull request com checagens e regra na `main` | Commits direto na `main`, com trava só na publicação; pull request sem regra |
| Revisão | O usuário revisa o código de todo pull request; revisão por outra sessão do Claude e revisão de segurança como camadas adicionais | Só o CI e o Claude revisando |
| Garantia da aprovação | Identidade única, com merge exclusivamente manual pelo usuário | Conta separada para o Claude, com aprovação obrigatória do usuário |
| Dependências | Espera de 7 dias para versões novas e travas | Padrão das ferramentas, com a espera de 3 dias só no Dependabot |
| Prazos de correção | Crítica ou já explorada 3 dias, alta 14, média 30 | 1, 7 e 14 dias; 7, 30 e 90 dias |
| Inventário (SBOM) | Junto da imagem, reconferido todo dia | Só a cada versão; varredura contínua do Amazon Inspector |
| Verificação de segurança | Matriz do ASVS e OWASP ZAP; teste de invasão decidido antes da abertura | Teste de invasão já antes do beta; só testes automáticos |
| Prévia | No computador do usuário | Cópia na AWS por pull request; só capturas e vídeos |
| Licenças | Permissivas livres; copyleft com aval do usuário | Só registrar, sem barrar |
| Desenvolvimento local | Código de terceiros só em contêineres | Direto no Windows |
| Mutação | Nas regras críticas, antes de cada versão | Não usar agora; em todo o código, toda semana |
| Problema em produção | Voltar primeiro, com autorização do usuário | Corrigir no ar; volta automática |
| Carga | Teste antes do beta e antes da abertura | Só antes da abertura |

## Decisão

- O detalhamento está em `docs/seguranca-e-privacidade.md`, seção 6, com as decisões P6-01 a P6-28.
- **Fluxo:** toda mudança entra por pull request, inclusive documentos. A regra da `main`, configurada pelo usuário, exige pull request, zero aprovações e conversas resolvidas, bloqueia push forçado e não tem lista de bypass.
- **Merge:** só manual, feito pelo usuário na interface do GitHub. O Claude nunca faz merge, não habilita auto-merge e não envia para a `main`.
- **Autorização:** a aprovação explícita da spec e do `tasks.md` autoriza implementar, fazer commits e push na branch de trabalho e abrir ou atualizar os pull requests das fases previstas.
- **Revisão:** o usuário lê e revisa o código de todo pull request. A revisão por outra sessão do Claude e a revisão de segurança são camadas adicionais, nunca substitutas.
- **Explicação técnica:** todo pull request traz o que foi feito e por quê, os arquivos, como funciona, as decisões e as alternativas, os testes e os resultados, os riscos e os conceitos novos para estudar.
- **Portões do CI:** lint, tipos, testes, contrato da API, acessibilidade, migrações, configuração de produção, workflows, dependências, segredos, código, imagem e varredura dinâmica.
- **Dependências:** uv e pnpm com lockfile; espera de 7 dias para versões novas; scripts de instalação bloqueados; ações fixadas pelo commit completo; Dependabot semanal; prazos de correção; política de licenças.
- **Inventário:** CycloneDX de cada imagem, guardado no ECR e reconferido todo dia.
- **Segurança:** CodeQL, varredura de segredos, matriz do ASVS L2, OWASP ZAP, revisão completa antes do beta e decisão sobre teste de invasão antes da abertura.
- **Rigor e capacidade:** testes de mutação nas regras críticas antes de cada versão; teste de carga antes do beta e antes da abertura.
- **Operação:** volta de código, volta da versão em produção e restauração de dados são operações distintas; as duas últimas só com autorização explícita do usuário a cada operação.
- **Autorizações recorrentes:** as rotinas automáticas já aprovadas continuam dentro dos parâmetros aprovados, com as cinco regras da seção 5.4.
- **Desenvolvimento:** código de terceiros só em contêineres no computador de desenvolvimento.
- **Repositório público:** nada sensível em logs, artefatos ou gravações do CI; nenhum conteúdo real de questão no repositório; `SECURITY.md` e relato privado de vulnerabilidades.
- **Sem declaração de conformidade com o ASVS** enquanto não houver provas (P4-19, P5-25).

## Correções do usuário antes da aprovação

1. **Revisão do código.** A proposta partiu de uma premissa errada do consultor: que o usuário só conferiria telas. Correção do usuário: "EU QUERO LER E REVISAR O CÓDIGO." A revisão dele passou a ser a principal.
2. **Merge.** O usuário escolheu identidade única no GitHub, com merge exclusivamente manual por ele, sem conta separada para o Claude.
3. **Autorização.** A aprovação explícita da spec e do `tasks.md` autoriza commits, push na branch de trabalho e pull requests das fases previstas.
4. **ECR e custos.** Repositório privado; custo revisto; política de retenção definida.
5. **Volta de versão.** Volta de código, volta da versão em produção e restauração de dados ficaram separadas; nenhuma operação que altere a produção acontece sem autorização explícita.
6. **Regra da `main`.** Registrado o que está ativo; as demais configurações ficaram como recomendação pendente.
7. **Autorizações recorrentes.** As rotinas automáticas já aprovadas continuam valendo, com as cinco regras da seção 5.4.

## Limitação técnica registrada

O usuário e o Claude usam a mesma identidade autenticada no GitHub. Com essas permissões, o Claude conseguiria tecnicamente fazer merge pela API ou pela interface, e a regra da `main` não impede isso, porque não exige aprovação; uma aprovação vinda da mesma conta nem seria possível. A proibição de merge é uma regra operacional explícita, não uma garantia técnica do GitHub. O registro do GitHub também não distingue quem fez o merge.

## Recomendações pendentes de decisão do usuário

Não fazem parte do que foi aprovado como decisão:

- aceitar só o merge por rebase, com histórico linear;
- ativar a restrição de exclusão da `main`, que não estava ativa em 2026-11-24 (V50);
- incluir as checagens obrigatórias na regra da `main` quando o CI existir.

## Consequências

- **Ganhamos:**
  - nenhum código entra na `main` sem pull request e sem a revisão do usuário;
  - o usuário aprende com cada mudança, pela explicação técnica e pela revisão;
  - proteção contra os ataques recentes à cadeia de suprimentos;
  - prazos de correção escritos e cobrados pelo CI;
  - nenhum serviço pago novo.
- **Abrimos mão de:**
  - velocidade: cada pull request espera a revisão do usuário;
  - uma garantia técnica contra merge pelo Claude, que fica como regra operacional.
- **Exige:**
  - as verificações V35 a V51, nenhuma concluída;
  - a resposta jurídica à Jur-25;
  - disponibilidade do usuário para revisar as correções de segurança dentro dos prazos;
  - autorização do usuário para cada operação sensível, inclusive o teste mensal de restauração.
- **Revisitar se:**
  - o repositório deixar de ser público, porque CodeQL, varredura de segredos e revisão de dependências passam a ser pagos;
  - a equipe crescer, quando a aprovação obrigatória por outra pessoa volta a fazer sentido;
  - as verificações mostrarem que alguma ferramenta não funciona como documentado.
