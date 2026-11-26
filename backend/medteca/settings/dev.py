"""Configurações do desenvolvimento, no contêiner do computador do usuário."""

from .base import *  # noqa: F403

DEBUG = True

# Segredo fictício, só para o desenvolvimento; a produção exige o seu.
SECRET_KEY = "dev-inseguro-so-para-desenvolvimento"  # noqa: S105

# "api" é o nome do serviço no Compose, usado pelo repasse do Vite.
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "api"]

MEDTECA_DOCS_DA_API = True
