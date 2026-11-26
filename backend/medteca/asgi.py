"""Entrada ASGI, usada só pelo servidor da produção.

Sem DJANGO_SETTINGS_MODULE definido, carrega as configurações de produção,
que exigem o segredo: um servidor mal configurado falha em vez de subir em
modo de desenvolvimento.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medteca.settings.prod")

application = get_asgi_application()
