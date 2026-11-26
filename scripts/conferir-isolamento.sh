#!/bin/sh
# Confere, de dentro do contêiner, que nada do computador do usuário que dê
# acesso ao GitHub, à AWS ou a outras máquinas entrou nele, e que o código
# rodando aqui não consegue gravar no que o Windows executa (FUND-03 e
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

# 1. Montagens: só o repositório, os volumes do projeto e o que o próprio
# Docker monta. Qualquer outra, como uma pasta do usuário, é achado.
montagens_permitidas="/
/workspace
/workspace/backend
/workspace/frontend
/workspace/scripts
/workspace/backend/.venv
/workspace/frontend/node_modules
/home/dev/.cache/uv
/home/dev/.local/share/pnpm
/etc/hosts
/etc/hostname
/etc/resolv.conf
/usr/sbin/docker-init"

while read -r _ alvo _; do
  case "$alvo" in
    /proc | /proc/* | /dev | /dev/* | /sys | /sys/*) continue ;;
  esac
  if ! printf '%s\n' "$montagens_permitidas" | grep -qxF "$alvo"; then
    achou "montagem fora da lista: $alvo"
  fi
done < /proc/self/mounts

# 2. A raiz do repositório e o .git ficam só para leitura: o Windows executa
# hooks e configurações do .git, e o Claude Code lê o .claude.
for alvo in /workspace /workspace/.git; do
  if [ -w "$alvo" ]; then achou "gravável, mas devia ser só leitura: $alvo"; fi
done

# 3. Chaves SSH, credenciais da AWS e do GitHub e configuração do Git.
for caminho in \
  "$HOME/.ssh" \
  "$HOME/.aws" \
  "$HOME/.config/gh" \
  "$HOME/.gitconfig" \
  "$HOME/.config/git/config" \
  "$HOME/.config/git/credentials" \
  "$HOME/.git-credentials" \
  "$HOME/.netrc" \
  "$HOME/.docker/config.json"
do
  if [ -e "$caminho" ]; then achou "arquivo presente: $caminho"; fi
done

if [ -f /etc/gitconfig ] && grep -qi credential /etc/gitconfig; then
  achou "auxiliar de credenciais do Git em /etc/gitconfig"
fi

# 4. Agente SSH repassado (pela variável ou pelo soquete que o VS Code cria)
# e soquete do Docker, que daria controle sobre a máquina.
if [ -n "${SSH_AUTH_SOCK:-}" ]; then achou "variável SSH_AUTH_SOCK definida"; fi
for soquete in /tmp/vscode-ssh-auth-*.sock /var/run/docker.sock; do
  if [ -e "$soquete" ]; then achou "soquete presente: $soquete"; fi
done

# 5. Variáveis de ambiente: tokens do GitHub, chaves da AWS, qualquer
# configuração do Git (GIT_CONFIG_*, GIT_SSH_COMMAND, GIT_ASKPASS) e o canal
# do VS Code que pede credenciais do Git ao computador. Os nomes vêm do awk,
# para que um valor com várias linhas não pareça outra variável.
# O REMOTE_CONTAINERS_IPC não entra: é o canal geral do VS Code (terminal,
# portas); o repasse de credenciais por ele depende de uma configuração do
# Git, que os itens 3 e 5 já procuram.
for variavel in $(awk 'BEGIN { for (nome in ENVIRON) print nome }' | grep -E '^(GH_|GITHUB_|AWS_|GIT_|VSCODE_GIT_)'); do
  achou "variável $variavel definida"
done

if [ -z "$achados" ]; then
  echo "ok - FUND-03: contêiner sem credenciais, chaves SSH ou configuração do Git do usuário, e sem escrita no que o Windows executa"
  exit 0
fi

echo "falha - FUND-03: o contêiner recebeu algo do computador do usuário:${achados}"
exit 1
