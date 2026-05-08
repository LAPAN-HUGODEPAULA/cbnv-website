from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from accounts.decorators import author_required, chair_required
from submissions.models import Submission

from .forms import FinalMaterialForm
from .models import FinalMaterial


@login_required
@chair_required
def request_materials(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    accepted_statuses = ["accepted_oral", "accepted_poster", "accepted_video"]
    if submission.status not in accepted_statuses:
        messages.error(request, "Materiais finais só podem ser solicitados para trabalhos aprovados.")
        return redirect("proceedings:commission_materials")

    if request.method == "POST":
        try:
            submission.transition_to("final_materials_pending")
            FinalMaterial.objects.get_or_create(submission=submission)

            from notifications.services import notify_materials_requested

            notify_materials_requested(submission)
            messages.success(request, f"Materiais finais solicitados para {submission.submission_id}.")
        except Exception as e:
            messages.error(request, str(e))
        return redirect("proceedings:commission_materials")

    return render(
        request,
        "proceedings/commission/request_materials.html",
        {"submission": submission},
    )


@login_required
@chair_required
def commission_materials(request):
    submissions = (
        Submission.objects.filter(
            status__in=[
                "final_materials_pending",
                "ready_for_proceedings",
                "published_in_proceedings",
            ]
        )
        .select_related("final_material", "thematic_axis")
        .prefetch_related("authors")
        .order_by("-updated_at")
    )
    pending = submissions.filter(status="final_materials_pending")
    validated = submissions.filter(status="ready_for_proceedings")
    published = submissions.filter(status="published_in_proceedings")

    return render(
        request,
        "proceedings/commission/materials_list.html",
        {
            "pending": pending,
            "validated": validated,
            "published": published,
            "all_submissions": submissions,
        },
    )


@login_required
@chair_required
def validate_materials(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id, status="final_materials_pending")
    material = get_object_or_404(FinalMaterial, submission=submission)

    if request.method == "POST":
        notes = request.POST.get("notes", "")
        material.notes = notes
        material.validated_at = timezone.now()
        material.validated_by = request.user
        material.save()

        submission.transition_to("ready_for_proceedings")

        from notifications.services import notify_materials_validated

        notify_materials_validated(submission)
        messages.success(request, f"Materiais de {submission.submission_id} validados com sucesso.")
        return redirect("proceedings:commission_materials")

    return render(
        request,
        "proceedings/commission/validate_materials.html",
        {"submission": submission, "material": material},
    )


@login_required
@chair_required
def publish_proceedings(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id, status="ready_for_proceedings")

    if request.method == "POST":
        submission.transition_to("published_in_proceedings")

        from notifications.services import notify_proceedings_published

        notify_proceedings_published(submission)
        messages.success(request, f"Trabalho {submission.submission_id} publicado nos anais.")
        return redirect("proceedings:commission_materials")

    return render(
        request,
        "proceedings/commission/publish_confirm.html",
        {"submission": submission},
    )


@login_required
@author_required
def author_upload_materials(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id, submitter=request.user)

    if submission.status != "final_materials_pending":
        messages.warning(request, "Materiais finais não são necessários para esta submissão no momento.")
        return redirect("dashboard:author")

    material, _ = FinalMaterial.objects.get_or_create(submission=submission)
    show_video = submission.final_modality in ("oral", "video")

    if request.method == "POST":
        form = FinalMaterialForm(request.POST, request.FILES, instance=material, show_video=show_video)
        if form.is_valid():
            material = form.save(commit=False)
            material.received_at = timezone.now()
            material.save()

            from notifications.services import notify_materials_received

            notify_materials_received(submission)
            messages.success(request, "Materiais enviados com sucesso!")
            return redirect("proceedings:author_upload", submission.pk)
    else:
        form = FinalMaterialForm(instance=material, show_video=show_video)

    return render(
        request,
        "proceedings/author/upload.html",
        {"submission": submission, "material": material, "form": form, "show_video": show_video},
    )


def proceedings_list(request):
    submissions = (
        Submission.objects.filter(status="published_in_proceedings")
        .select_related("final_material", "thematic_axis")
        .prefetch_related("authors")
        .order_by("title")
    )

    modality_filter = request.GET.get("modality", "")
    axis_filter = request.GET.get("axis", "")

    if modality_filter:
        submissions = submissions.filter(final_modality=modality_filter)
    if axis_filter:
        submissions = submissions.filter(thematic_axis_id=axis_filter)

    from submissions.models import ThematicAxis

    axes = ThematicAxis.objects.all()

    return render(
        request,
        "proceedings/public/proceedings_list.html",
        {
            "submissions": submissions,
            "axes": axes,
            "modality_filter": modality_filter,
            "axis_filter": axis_filter,
        },
    )


def proceedings_detail(request, submission_id):
    submission = get_object_or_404(
        Submission.objects.select_related("thematic_axis").prefetch_related("authors"),
        submission_id=submission_id,
        status="published_in_proceedings",
    )
    material = getattr(submission, "final_material", None)
    return render(
        request,
        "proceedings/public/proceedings_detail.html",
        {"submission": submission, "material": material},
    )


def proceedings_download_pdf(request, submission_id):
    submission = get_object_or_404(
        Submission.objects.select_related("final_material"),
        submission_id=submission_id,
    )
    if submission.status != "published_in_proceedings":
        raise PermissionDenied("Este trabalho não está publicado nos anais.")

    material = get_object_or_404(FinalMaterial, submission=submission)
    if not material.final_pdf:
        raise Http404

    filename = f"{submission.submission_id}_final.pdf"
    return FileResponse(
        material.final_pdf.open("rb"),
        as_attachment=True,
        filename=filename,
    )
