import os

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings

from accounts.decorators import complete_profile_required
from notifications.services import send_submission_confirmation

from .forms import AuthorFormSet, SubmissionFileForm, SubmissionMetadataForm
from .models import Submission, SubmissionAuthor, SubmissionFile


def _serve_protected_file(request, submission_file):
    if not submission_file.file:
        raise Http404

    if settings.DEBUG:
        return FileResponse(
            submission_file.file.open("rb"),
            as_attachment=True,
            filename=submission_file.filename,
        )

    response = HttpResponse()
    response["Content-Type"] = ""
    response["X-Accel-Redirect"] = os.path.join(
        "/protected-media/", submission_file.file.name
    )
    response["Content-Disposition"] = f'attachment; filename="{submission_file.filename}"'
    return response


@login_required
def download_file(request, file_id):
    submission_file = get_object_or_404(SubmissionFile, pk=file_id)
    is_owner = submission_file.submission.submitter == request.user
    is_staff = request.user.is_staff or request.user.is_superuser

    if not is_owner and not is_staff:
        raise PermissionDenied

    return _serve_protected_file(request, submission_file)


@login_required
@complete_profile_required
def submission_detail(request, pk):
    submission = get_object_or_404(Submission, pk=pk, submitter=request.user)
    return render(
        request,
        "submissions/submission_detail.html",
        {"submission": submission, "reviews": submission.get_public_reviews()},
    )


@login_required
@complete_profile_required
def wizard_step1(request, submission_pk=None):
    submission = None
    if submission_pk:
        submission = get_object_or_404(
            Submission, pk=submission_pk, submitter=request.user
        )

    if request.method == "POST":
        form = SubmissionMetadataForm(request.POST, instance=submission)
        if not form.is_valid():
            return render(
                request,
                "submissions/wizard/step1_metadata.html",
                {"form": form, "formset": AuthorFormSet(request.POST, prefix="authors"), "submission": submission, "step": 1},
            )

        submission = form.save(commit=False)
        if not submission.submitter_id:
            submission.submitter = request.user
        submission.save()

        formset = AuthorFormSet(request.POST, instance=submission, prefix="authors")
        if formset.is_valid():
            formset.save()

            if not submission.authors.filter(is_corresponding=True).exists():
                first_author = submission.authors.first()
                if first_author:
                    first_author.is_corresponding = True
                    first_author.save(update_fields=["is_corresponding"])

            return redirect("submissions:wizard_step2", submission.pk)

        return render(
            request,
            "submissions/wizard/step1_metadata.html",
            {"form": form, "formset": formset, "submission": submission, "step": 1},
        )
    else:
        form = SubmissionMetadataForm(instance=submission)
        formset = AuthorFormSet(instance=submission, prefix="authors")

        if not submission_pk:
            user = request.user
            initial_data = {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "institution": user.institution,
                "order": 1,
                "is_corresponding": True,
            }
            formset = AuthorFormSet(
                instance=submission,
                initial=[initial_data],
                prefix="authors",
            )

    return render(
        request,
        "submissions/wizard/step1_metadata.html",
        {"form": form, "formset": formset, "submission": submission, "step": 1},
    )


@login_required
@complete_profile_required
def wizard_step2(request, submission_pk):
    submission = get_object_or_404(
        Submission, pk=submission_pk, submitter=request.user
    )
    form = SubmissionFileForm(instance=submission)

    if request.method == "POST":
        form = SubmissionFileForm(request.POST, request.FILES, instance=submission)
        if form.is_valid():
            uploaded_file = form.cleaned_data["file"]
            if uploaded_file:
                SubmissionFile.objects.filter(submission=submission).delete()
                SubmissionFile.objects.create(
                    submission=submission,
                    file=uploaded_file,
                )
            return redirect("submissions:wizard_step3", submission.pk)

    existing_file = submission.files.first()
    return render(
        request,
        "submissions/wizard/step2_upload.html",
        {
            "form": form,
            "submission": submission,
            "existing_file": existing_file,
            "step": 2,
        },
    )


@login_required
@complete_profile_required
def wizard_step3(request, submission_pk):
    submission = get_object_or_404(
        Submission, pk=submission_pk, submitter=request.user
    )
    authors = submission.authors.all()
    uploaded_file = submission.files.first()

    if request.method == "POST":
        if submission.status == "draft":
            try:
                submission.submit()
                send_submission_confirmation(submission)
                messages.success(
                    request,
                    f"Submissão {submission.submission_id} enviada com sucesso!",
                )
                return redirect("dashboard:author")
            except Exception:
                messages.error(
                    request,
                    "Ocorreu um erro ao enviar a submissão. Tente novamente.",
                )
        return redirect("dashboard:author")

    return render(
        request,
        "submissions/wizard/step3_confirm.html",
        {
            "submission": submission,
            "authors": authors,
            "uploaded_file": uploaded_file,
            "step": 3,
        },
    )


@login_required
@complete_profile_required
def wizard_new(request):
    return redirect("submissions:wizard_step1")


@login_required
@complete_profile_required
def wizard_edit(request, submission_pk):
    submission = get_object_or_404(
        Submission, pk=submission_pk, submitter=request.user, status="draft"
    )
    return redirect("submissions:wizard_step1", submission.pk)


@login_required
def add_author_row(request, submission_pk):
    submission = get_object_or_404(
        Submission, pk=submission_pk, submitter=request.user
    )
    total = submission.authors.count()
    if total >= 10:
        raise Http404
    author = SubmissionAuthor(
        submission=submission,
        order=total + 1,
    )
    author.save()
    form = AuthorFormSet(instance=submission, prefix="authors")
    forms_list = list(form)
    return render(
        request,
        "submissions/wizard/partials/author_row.html",
        {
            "form": forms_list[-1],
            "author": author,
        },
    )
