from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from .decorators import author_required, chair_required, reviewer_required
from .forms import ProfileForm, RegistrationForm


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("dashboard:redirect")

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
    if user.is_chair:
        return redirect("dashboard:chair")
    if user.is_reviewer:
        return redirect("dashboard:reviewer")
    return redirect("dashboard:author")


@login_required
@author_required
def author_dashboard(request):
    user = request.user
    if not user.has_complete_author_profile:
        messages.warning(
            request,
            "Complete seu perfil antes de enviar submissões.",
        )
        missing = []
        if not user.first_name.strip():
            missing.append("nome")
        if not user.last_name.strip():
            missing.append("sobrenome")
        if not user.institution.strip():
            missing.append("instituição")
        if not user.country.strip():
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
    return render(request, "dashboard/reviewer.html")


@login_required
@chair_required
def chair_dashboard(request):
    from submissions.models import Submission

    total = Submission.objects.count()
    in_review = Submission.objects.filter(
        status__in=[
            "admin_screening", "assigned_to_reviewers",
            "under_review", "reviews_completed", "decision_pending",
        ]
    ).count()
    decisions = Submission.objects.filter(
        status__in=["accepted_oral", "accepted_poster", "accepted_video", "rejected"]
    ).count()
    pending_materials = Submission.objects.filter(status="final_materials_pending").count()
    validated = Submission.objects.filter(status="ready_for_proceedings").count()
    published = Submission.objects.filter(status="published_in_proceedings").count()

    return render(
        request,
        "dashboard/chair.html",
        {
            "total": total,
            "in_review": in_review,
            "decisions": decisions,
            "pending_materials": pending_materials,
            "validated": validated,
            "published": published,
        },
    )


@login_required
@author_required
def profile_edit(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso.")
            return redirect("dashboard:author")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "accounts/profile_edit.html", {"form": form})
