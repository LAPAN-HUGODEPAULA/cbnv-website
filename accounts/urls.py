from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("registrar/", views.register, name="register"),
    path(
        "entrar/",
        auth_views.LoginView.as_view(
            template_name="accounts/login.html",
            redirect_authenticated_user=True,
            extra_context={"title": "Entrar", "subtitle": "Acesse sua conta do CBNV 2026."},
        ),
        name="login",
    ),
    path("sair/", views.logout_view, name="logout"),
    path(
        "recuperar-senha/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset_form.html",
            email_template_name="accounts/password_reset_email.html",
            success_url="/conta/recuperar-senha/enviado/",
        ),
        name="password_reset",
    ),
    path(
        "recuperar-senha/enviado/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "recuperar-senha/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",
            success_url="/conta/recuperar-senha/completo/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "recuperar-senha/completo/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
    path("perfil/", views.profile_detail, name="profile"),
    path("perfil/editar/", views.profile_edit, name="profile_edit"),
]
