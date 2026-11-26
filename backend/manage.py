#!/usr/bin/env python
"""Ponto de entrada dos comandos do Django no desenvolvimento."""

import os
import sys


def main() -> None:
    # Sem configuração padrão: no desenvolvimento, o compose.yaml define
    # DJANGO_SETTINGS_MODULE. Um comando rodado na produção sem a variável
    # falha, em vez de subir com o segredo público do desenvolvimento.
    if not os.environ.get("DJANGO_SETTINGS_MODULE"):
        sys.exit("Defina DJANGO_SETTINGS_MODULE (no desenvolvimento, o compose.yaml já define).")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
