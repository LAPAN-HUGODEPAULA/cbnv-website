from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from accounts.decorators import chair_required, reviewer_required
from .forms import ReviewForm
from .models import Review, ReviewerAssignment


@login_required
@reviewer_required
def reviewer_submissions(request):
    assignments = (
        ReviewerAssignment.objects.filter(reviewer=request.user)
        .select_related("submission")
        .prefetch_related("submission__authors")
        .order_by("-assigned_at")
    )
    return render(request, "reviews/reviewer_submissions.html", {"assignments": assignments})


@login_required
@reviewer_required
def review_detail(request, assignment_id):
    assignment = get_object_or_404(
        ReviewerAssignment, pk=assignment_id, reviewer=request.user
    )
    submission = assignment.submission

    try:
        review = assignment.review
    except Review.DoesNotExist:
        review = None

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.assignment = assignment
            new_review.save()
            messages.success(request, "Avaliação enviada com sucesso.")
            return redirect("reviews:reviewer_submissions")
    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        "reviews/review_detail.html",
        {"assignment": assignment, "submission": submission, "form": form, "review": review},
    )


@login_required
@chair_required
def assign_reviewers(request, submission_id):
    from submissions.models import Submission

    submission = get_object_or_404(Submission, pk=submission_id)

    if request.method == "POST":
        reviewer_ids = request.POST.getlist("reviewers")
        from django.contrib.auth import get_user_model

        User = get_user_model()
        reviewers = User.objects.filter(pk__in=reviewer_ids, profile__is_reviewer=True)
        created_count = 0
        for reviewer in reviewers:
            _, created = ReviewerAssignment.objects.get_or_create(
                reviewer=reviewer, submission=submission
            )
            if created:
                created_count += 1

        if created_count > 0:
            from notifications.services import notify_reviewer_assigned

            for reviewer in reviewers.filter(
                review_assignments__submission=submission
            ):
                notify_reviewer_assigned(submission, reviewer)

            if submission.status == "admin_screening":
                submission.transition_to("assigned_to_reviewers")

            messages.success(
                request, f"{created_count} revisor(es) atribuído(s) com sucesso."
            )
        return redirect("reviews:manage_submissions")

    from django.contrib.auth import get_user_model

    User = get_user_model()
    all_reviewers = User.objects.filter(profile__is_reviewer=True)
    existing_assignments = submission.reviewer_assignments.values_list(
        "reviewer_id", flat=True
    )

    return render(
        request,
        "reviews/assign_reviewers.html",
        {
            "submission": submission,
            "all_reviewers": all_reviewers,
            "existing_assignments": existing_assignments,
        },
    )


@login_required
@chair_required
def manage_submissions(request):
    from submissions.models import Submission

    submissions = (
        Submission.objects.filter(
            status__in=[
                "submitted",
                "admin_screening",
                "assigned_to_reviewers",
                "under_review",
                "reviews_completed",
                "decision_pending",
                "accepted_oral",
                "accepted_poster",
                "accepted_video",
                "rejected",
            ]
        )
        .prefetch_related("reviewer_assignments__reviewer", "reviewer_assignments__review")
        .order_by("-created_at")
    )
    return render(
        request, "reviews/manage_submissions.html", {"submissions": submissions}
    )


@login_required
@chair_required
def issue_decision(request, submission_id):
    from submissions.models import Submission

    submission = get_object_or_404(Submission, pk=submission_id)

    if request.method == "POST":
        action = request.POST.get("action")
        modality = request.POST.get("modality", "")
        decision_notes = request.POST.get("decision_notes", "")

        if action in ("accepted_oral", "accepted_poster", "accepted_video", "rejected"):
            submission.decision_notes = decision_notes
            if action != "rejected":
                modality_map = {
                    "accepted_oral": "oral",
                    "accepted_poster": "poster",
                    "accepted_video": "video",
                }
                submission.final_modality = modality_map[action]
            submission.save(update_fields=["final_modality", "decision_notes"])
            submission.transition_to(action)

            from notifications.services import notify_decision

            notify_decision(submission)
            messages.success(request, "Decisão registrada com sucesso.")
            return redirect("reviews:manage_submissions")

    reviews = Review.objects.filter(assignment__submission=submission)
    return render(
        request,
        "reviews/issue_decision.html",
        {"submission": submission, "reviews": reviews},
    )
