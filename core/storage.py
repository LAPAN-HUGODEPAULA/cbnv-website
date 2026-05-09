from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.deconstruct import deconstructible


@deconstructible(path="core.storage.ProtectedMediaStorage")
class ProtectedMediaStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("location", settings.PROTECTED_MEDIA_ROOT)
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        return ("core.storage.ProtectedMediaStorage", [], {})
