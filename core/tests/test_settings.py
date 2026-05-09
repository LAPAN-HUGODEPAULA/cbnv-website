import importlib
import sys

import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured


def reload_production_settings(monkeypatch):
    sys.modules.pop("cbnv.settings.production", None)
    return importlib.import_module("cbnv.settings.production")


def test_default_user_model_is_used(settings):
    assert settings.AUTH_USER_MODEL == "auth.User"
    assert get_user_model()._meta.label == "auth.User"


def test_production_requires_secret_key(monkeypatch):
    monkeypatch.delenv("DJANGO_SECRET_KEY", raising=False)
    with pytest.raises(ImproperlyConfigured):
        reload_production_settings(monkeypatch)


def test_production_parses_csrf_trusted_origins(monkeypatch):
    monkeypatch.setenv("DJANGO_SECRET_KEY", "test-secret")
    monkeypatch.setenv("ALLOWED_HOSTS", "example.com, www.example.com")
    monkeypatch.setenv(
        "CSRF_TRUSTED_ORIGINS",
        "https://example.com, https://www.example.com",
    )

    production = reload_production_settings(monkeypatch)

    assert production.ALLOWED_HOSTS == ["example.com", "www.example.com"]
    assert production.CSRF_TRUSTED_ORIGINS == [
        "https://example.com",
        "https://www.example.com",
    ]
