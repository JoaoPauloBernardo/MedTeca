#!/bin/sh
# Confere, de dentro do contêiner, que nada do computador do usuário que dê
# acesso ao GitHub, à AWS ou a outras máquinas entrou nele (FUND-03 e
# FUND-34; RNF-85).
#
#   docker compose run --rm dev scripts/conferir-isolamento.sh
#
# Sai com 0 e imprime "ok - FUND-03: ..." quando está tudo limpo; sai com 1
# e lista o que achou, se não estiver.

achados=""
achou() {
  achados="${achados}
  - $1"
}

# Chaves SSH, credenciais da AWS e do GitHub e configuração do Git.
for caminho in \
  "$HOME/.ssh" \
  "$HOME/.aws" \
  "$HOME/.config/gh" \
  "$HOME/.gitconfig" \
  "$HOME/.config/git/config" \
  "$HOME/.git-credentials" \
  "$HOME/.docker/config.json"
do
  if [ -e "$caminho" ]; then achou "arquivo presente: $caminho"; fi
done

# Auxiliar de credenciais do Git configurado para o sistema todo.
if [ -f /etc/gitconfig ] && grep -qi credential /etc/gitconfig; then
  achou "auxiliar de credenciais do Git em /etc/gitconfig"
fi

# Agente SSH repassado e soquete do Docker do computador, que daria
# controle sobre a máquina.
if [ -n "${SSH_AUTH_SOCK:-}" ]; then achou "variável SSH_AUTH_SOCK definida"; fi
if [ -e /var/run/docker.sock ]; then achou "soquete do Docker montado: /var/run/docker.sock"; fi

# Tokens do GitHub e chaves da AWS em variáveis de ambiente, e o canal do
# VS Code que pede credenciais do Git ao computador (GIT_ASKPASS).
for variavel in $(env | cut -d= -f1 | grep -E '^(GH_|GITHUB_|AWS_|VSCODE_GIT_)|^GIT_ASKPASS$'); do
  achou "variável $variavel definida"
done

if [ -z "$achados" ]; then
  echo "ok - FUND-03: contêiner sem credenciais, chaves SSH ou configuração do Git do usuário"
  exit 0
fi

echo "falha - FUND-03: o contêiner recebeu algo do computador do usuário:${achados}"
exit 1
