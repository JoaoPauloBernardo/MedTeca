"""Rotas do MedTeca. Toda a API fica sob /api/."""

from django.urls import URLPattern, URLResolver, path

from medteca.api import api

urlpatterns: list[URLPattern | URLResolver] = [
    path("api/", api.urls),
]
