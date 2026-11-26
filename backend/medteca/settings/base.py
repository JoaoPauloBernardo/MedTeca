"""Configurações comuns a todos os ambientes do MedTeca.

Cada ambiente tem o seu arquivo (dev, test e prod), que importa este e
muda só o que precisa.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    # O Django Ninja serve os arquivos da documentação da API a partir do
    # próprio servidor, sem CDN (RNF-96), e traz o comando que exporta o
    # OpenAPI para o contrato com o frontend.
    "ninja",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "medteca.urls"
WSGI_APPLICATION = "medteca.wsgi.application"
ASGI_APPLICATION = "medteca.asgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    },
]

# Banco pelas variáveis padrão do PostgreSQL (PGHOST, PGDATABASE...). Se o
# banco não responder em 2 s, a conexão falha em vez de prender a requisição.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("PGDATABASE", "medteca"),
        "USER": os.environ.get("PGUSER", ""),
        "PASSWORD": os.environ.get("PGPASSWORD", ""),
        "HOST": os.environ.get("PGHOST", ""),
        "PORT": os.environ.get("PGPORT", ""),
        "OPTIONS": {"connect_timeout": 2},
    },
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Interface só em português do Brasil (D-016, RNF-02).
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# Os arquivos estáticos ficam sob /api/, o único caminho que o Vite repassa
# ao Django no desenvolvimento.
STATIC_URL = "/api/static/"

# Documentação da API (/api/docs e /api/openapi.json): ligada só no
# desenvolvimento e nos testes; desligada na produção (FUND-19).
MEDTECA_DOCS_DA_API = False
