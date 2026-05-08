from django.urls import path

from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.dashboard_redirect, name="redirect"),
    path("autor/", views.author_dashboard, name="author"),
    path("revisor/", views.reviewer_dashboard, name="reviewer"),
    path("comissao/", views.chair_dashboard, name="chair"),
]
