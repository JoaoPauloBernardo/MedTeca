"""Configurações de produção.

Só carregam com as variáveis de ambiente da produção: sem um DJANGO_SECRET_KEY
de pelo menos 50 caracteres, o Django não sobe (FUND-21). O banco por socket com autenticação peer
(D-005, D-033) entra com a funcionalidade de publicação.
"""

import os

from django.core.exceptions import ImproperlyConfigured

from .base import *  # noqa: F403

DEBUG = False

# O segredo precisa ter pelo menos 50 caracteres, o mínimo que o Django
# cobra no check --deploy (W009); espaços nas pontas não contam.
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "").strip()
if len(SECRET_KEY) < 50:
    raise ImproperlyConfigured(
        "Defina DJANGO_SECRET_KEY com pelo menos 50 caracteres: as configurações de "
        "produção não sobem sem um segredo forte."
    )

# Hosts separados por vírgula; espaços em volta de cada um são ignorados.
ALLOWED_HOSTS = [
    host.strip() for host in os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",") if host.strip()
]

# Cookies só por HTTPS (D-007). Os nomes com __Host- e o resto da sessão
# entram com a funcionalidade Contas.
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Sem documentação da API na produção (FUND-19, ASVS 13.4.5).
MEDTECA_DOCS_DA_API = False

# Avisos do check --deploy que ficam a cargo do Caddy, na frente do Django
# (seção 5.H de docs/seguranca-e-privacidade.md): o HSTS de 1 ano (5.H.4,
# V26) e o redirecionamento de HTTP para HTTPS (5.H.3). Mandar o HSTS também
# daqui duplicaria o cabeçalho.
SILENCED_SYSTEM_CHECKS = [
    "security.W004",
    "security.W008",
]
