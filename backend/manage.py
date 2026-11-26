#!/usr/bin/env python
"""Ponto de entrada dos comandos do Django no desenvolvimento."""

import os
import sys


def main() -> None:
    # Por padrão, as configurações de desenvolvimento. A produção define
    # DJANGO_SETTINGS_MODULE explicitamente.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medteca.settings.dev")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
