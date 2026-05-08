from .base import *

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

MEDIA_ROOT = "/tmp/cbnv-test-media"

STATIC_ROOT = "/tmp/cbnv-test-static"

AXES_BACKEND = "axes.backends.AxesStandaloneBackend"
AXES_FAILURE_LIMIT = 9999
AXES_LOCKOUT_CALLABLE = None
