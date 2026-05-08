from django.urls import path

from .views import design_system

urlpatterns = [
    path("", design_system, name="design_system"),
]
