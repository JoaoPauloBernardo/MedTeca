# D-007: Autenticação e sessões: sessão do Django em cookie

- **Status**: Aprovada
- **Data**: 2026-11-23
- **Aprovação**: "Sessão do Django em cookie" (2026-11-23); registro autorizado com "Sim, com ADR" (2026-11-23)
- **Relacionadas**: D-004, D-009, D-018, D-020; requisitos CONTA em `docs/requisitos-mvp.md`

## Contexto

- O frontend React e a API em Python são servidos no mesmo endereço (D-020). O backend é Django (D-004).
- O catálogo exige:
  - login com e-mail e senha e contas criadas só por convite durante o beta (CONTA-01 a CONTA-04);
  - sessão encerrada após 30 dias sem uso (CONTA-06);
  - "Sair" encerrando a sessão na hora (CONTA-07);
  - exclusão de conta (CONTA-11);
  - permissões com bloqueio por padrão (CONTA-20).
- Referência usada: OWASP ASVS 5.0, na skill de segurança do projeto:
  - a sessão encerrada não pode mais ser usada (7.4.1);
  - todas as sessões terminam quando a conta é excluída (7.4.2);
  - cookie de sessão invisível ao JavaScript (3.3.4);
  - cookies com Secure e prefixo __Host- (3.3.1, 3.3.3);
  - token contra CSRF (3.5.1).
- Fatos conferidos em 2026-11-23:
  - o django-allauth (versão 65.22.1, de 13/11/2026) tem um modo "headless" com clientes "browser" e "app";
  - o allauth suporta MFA por TOTP, por códigos de recuperação e por WebAuthn, inclusive login por passkey.
  - A documentação lida **não confirmou** que o cliente "browser" usa cookie de sessão nem que passkeys funcionam no modo headless.

## Opções consideradas

### Sessão do Django em cookie (escolhida)

- Prós:
  - "Sair" e a exclusão da conta encerram a sessão na hora;
  - o JavaScript não lê o cookie, então uma falha de XSS não rouba a sessão;
  - os 30 dias de inatividade são só configuração;
  - encaixa naturalmente com app e API no mesmo endereço.
- Contras: uma consulta às sessões a cada requisição, o que é irrelevante na escala do beta; o frontend precisa enviar o token contra CSRF.
- Custo e complexidade: a completar.

### Tokens JWT no navegador

- Prós: sem estado no servidor; comum em APIs para apps móveis.
- Contras: encerrar a sessão na hora exige uma lista de revogação; se o token ficar acessível ao JavaScript, um XSS o rouba; mais peças para errar, sem ganho num app no mesmo domínio.
- Custo e complexidade: a completar.

### Provedor externo de identidade

- Prós: senhas, MFA e login social terceirizados.
- Contras: custo por usuário; dependência do fornecedor; dados pessoais guardados onde o fornecedor operar, o que precisa ser avaliado pela LGPD; fluxo de convite feito sob medida.
- Custo e complexidade: a completar.

## Decisão

- **Sessão:** a sessão do Django fica guardada no servidor. O navegador recebe um cookie protegido (HttpOnly, Secure, prefixo __Host-, SameSite), e todo pedido que altera dados exige o token contra CSRF.
- **Senhas:** guardadas com Argon2id.
- **Política de senha:** alinhada ao ASVS 5.0 (mínimo de 8 caracteres, com 15 recomendados; sem regras de composição; rejeição de senhas comuns; aceita 64 caracteres ou mais; permite colar e usar gerenciadores de senha). Os números finais são fixados na Etapa 6.
- **Fluxos de login, convite e recuperação de senha:** a biblioteca é escolhida na spec de CONTA, entre o django-allauth em modo headless e fluxos próprios montados com as peças do Django. O que ficou sem confirmação na documentação será verificado em teste.

## Consequências

- Ganhamos: encerramento imediato de sessões e proteção do identificador de sessão contra scripts, usando mecanismos maduros do Django.
- Exige: o frontend envia o token contra CSRF em todo pedido que altera dados.
- Pendências para a Etapa 6:
  - teto absoluto de duração da sessão (ASVS 7.3.2), já que hoje só existe o limite de inatividade;
  - MFA ou passkeys (ASVS 6.3.3), definindo para quem e quando.
- Revisitar se: um app nativo entrar no MVP (contradiz D-001), ou se login social se tornar obrigatório.

## Observações do encerramento da Etapa 3 (2026-11-23)

- **CSRF obrigatório**: a proteção contra CSRF vale para toda operação que altera dados com autenticação por cookie, inclusive na API do Django Ninja, e **não pode ser desabilitada**. Como o Django Ninja aplica essa proteção na versão adotada é conferido na implementação.
- **Testes negativos**: para as operações que alteram dados, há testes que enviam a requisição sem token CSRF ou com token inválido e esperam que ela seja recusada.
- **Cookies**:
  - o cookie de sessão é Secure, HttpOnly e SameSite, com o prefixo __Host-;
  - o token CSRF precisa chegar ao frontend, por cookie legível ou por um endpoint. Se for por cookie, esse cookie é Secure e SameSite, mas não HttpOnly, porque o frontend precisa lê-lo para reenviá-lo. Segundo a documentação do Django (configuração CSRF_COOKIE_HTTPONLY), isso não reduz a proteção.
