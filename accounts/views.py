from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .decorators import author_required, chair_required, reviewer_required
from .forms import ProfileForm, RegistrationForm
from .models import get_or_create_profile, user_has_complete_author_profile, user_has_role


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("dashboard:redirect")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault("title", "Criar conta")
        context.setdefault(
            "subtitle",
            "Preencha seus dados para acessar o painel do CBNV 2026.",
        )
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object, backend=settings.AUTHENTICATION_BACKENDS[0])
        messages.success(
            self.request,
            f"Bem-vindo(a), {self.object.first_name}! Seu cadastro foi realizado com sucesso.",
        )
        return response


register = RegisterView.as_view()


@login_required
def dashboard_redirect(request):
    user = request.user
    profile = get_or_create_profile(user)
    roles = [
        {
            "key": "author",
            "label": "Autor",
            "description": "Área para acompanhar submissões quando o fluxo científico estiver disponível.",
            "url": reverse_lazy("dashboard:author"),
            "enabled": user_has_role(user, "is_author"),
        },
        {
            "key": "reviewer",
            "label": "Revisor",
            "description": "Área reservada para futuras avaliações atribuídas pela comissão.",
            "url": reverse_lazy("dashboard:reviewer"),
            "enabled": user_has_role(user, "is_reviewer"),
        },
        {
            "key": "chair",
            "label": "Comissão científica",
            "description": "Área reservada para futuras ferramentas de coordenação científica.",
            "url": reverse_lazy("dashboard:chair"),
            "enabled": user_has_role(user, "is_chair"),
        },
    ]
    return render(
        request,
        "dashboard/index.html",
        {
            "profile": profile,
            "roles": roles,
            "available_roles": [role for role in roles if role["enabled"]],
        },
    )


@login_required
@author_required
def author_dashboard(request):
    user = request.user
    profile = get_or_create_profile(user)
    if not user_has_complete_author_profile(user):
        messages.warning(
            request,
            "Complete seu perfil antes de enviar submissões.",
        )
        missing = []
        if not user.first_name.strip():
            missing.append("nome")
        if not user.last_name.strip():
            missing.append("sobrenome")
        if not profile.institution.strip():
            missing.append("instituição")
        if not profile.country.strip():
            missing.append("país")
        return redirect("accounts:profile_edit")

    submissions = user.submissions.all()
    return render(
        request,
        "dashboard/author.html",
        {"submissions": submissions},
    )


@login_required
@reviewer_required
def reviewer_dashboard(request):
    return redirect("reviews:reviewer_submissions")


@login_required
@chair_required
def chair_dashboard(request):
    return redirect("reviews:manage_submissions")


@login_required
def profile_detail(request):
    profile = get_or_create_profile(request.user)
    return render(request, "accounts/profile_detail.html", {"profile": profile})


@login_required
def profile_edit(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso.")
            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "accounts/profile_edit.html", {"form": form})


@login_required
def logout_view(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    logout(request)
    messages.success(request, "Você saiu da sua conta.")
    return redirect(settings.LOGOUT_REDIRECT_URL)
