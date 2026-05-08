from django.conf import settings
from django.template.loader import render_to_string

from core.email import send_transactional_email


def send_submission_confirmation(submission):
    corresponding = submission.get_corresponding_author()
    if not corresponding:
        return
    subject = f"Submissão recebida — {submission.submission_id}"
    context = {
        "submission": submission,
        "corresponding_author": corresponding,
    }
    html_body = render_to_string("notifications/email/submission_confirmation.html", context)
    text_body = render_to_string("notifications/email/submission_confirmation.txt", context)
    send_transactional_email(
        subject=subject,
        message=text_body,
        recipient_list=[corresponding.email],
        from_email=settings.DEFAULT_FROM_EMAIL,
        html_message=html_body,
    )


def notify_reviewer_assigned(submission, reviewer):
    subject = f"Nova atribuição de revisão — {submission.submission_id}"
    context = {
        "reviewer": reviewer,
        "submission": submission,
    }
    html_body = render_to_string("notifications/email/reviewer_assigned.html", context)
    text_body = render_to_string("notifications/email/reviewer_assigned.txt", context)
    send_transactional_email(
        subject=subject,
        message=text_body,
        recipient_list=[reviewer.email],
        from_email=settings.DEFAULT_FROM_EMAIL,
        html_message=html_body,
    )


def build_decision_bundle(submission):
    from reviews.models import Review

    reviews = Review.objects.filter(assignment__submission=submission).select_related("assignment__reviewer")
    bundle = {
        "submission": submission,
        "chair_notes": submission.decision_notes,
        "reviews": [],
    }
    for review in reviews:
        bundle["reviews"].append({
            "recommendation": review.get_recommendation_display(),
            "comments": review.comments,
        })
    return bundle


def notify_decision(submission):
    corresponding = submission.get_corresponding_author()
    if not corresponding:
        return

    bundle = build_decision_bundle(submission)
    bundle["corresponding_author"] = corresponding

    is_accepted = submission.status.startswith("accepted")
    prefix = "Aprovado" if is_accepted else "Rejeitado"
    subject = f"Decisão da submissão — {submission.submission_id}"

    context = bundle

    html_body = render_to_string("notifications/email/decision_notification.html", context)
    text_body = render_to_string("notifications/email/decision_notification.txt", context)
    send_transactional_email(
        subject=subject,
        message=text_body,
        recipient_list=[corresponding.email],
        from_email=settings.DEFAULT_FROM_EMAIL,
        html_message=html_body,
    )


def notify_materials_requested(submission):
    corresponding = submission.get_corresponding_author()
    if not corresponding:
        return
    subject = f"Materiais finais solicitados — {submission.submission_id}"
    context = {
        "submission": submission,
        "corresponding_author": corresponding,
        "upload_url": settings.BASE_URL + f"/materiais/autor/materiais/{submission.pk}/",
    }
    html_body = render_to_string("notifications/email/materials_requested.html", context)
    text_body = render_to_string("notifications/email/materials_requested.txt", context)
    send_transactional_email(
        subject=subject,
        message=text_body,
        recipient_list=[corresponding.email],
        from_email=settings.DEFAULT_FROM_EMAIL,
        html_message=html_body,
    )


def notify_materials_received(submission):
    corresponding = submission.get_corresponding_author()
    if not corresponding:
        return
    subject = f"Materiais finais recebidos — {submission.submission_id}"
    context = {
        "submission": submission,
        "corresponding_author": corresponding,
    }
    html_body = render_to_string("notifications/email/materials_received.html", context)
    text_body = render_to_string("notifications/email/materials_received.txt", context)
    send_transactional_email(
        subject=subject,
        message=text_body,
        recipient_list=[corresponding.email],
        from_email=settings.DEFAULT_FROM_EMAIL,
        html_message=html_body,
    )


def notify_materials_validated(submission):
    corresponding = submission.get_corresponding_author()
    if not corresponding:
        return
    subject = f"Materiais finais validados — {submission.submission_id}"
    context = {
        "submission": submission,
        "corresponding_author": corresponding,
    }
    html_body = render_to_string("notifications/email/materials_validated.html", context)
    text_body = render_to_string("notifications/email/materials_validated.txt", context)
    send_transactional_email(
        subject=subject,
        message=text_body,
        recipient_list=[corresponding.email],
        from_email=settings.DEFAULT_FROM_EMAIL,
        html_message=html_body,
    )


def notify_proceedings_published(submission):
    corresponding = submission.get_corresponding_author()
    if not corresponding:
        return
    subject = f"Publicado nos anais — {submission.submission_id}"
    context = {
        "submission": submission,
        "corresponding_author": corresponding,
        "proceedings_url": settings.BASE_URL + f"/anais/{submission.submission_id}/",
    }
    html_body = render_to_string("notifications/email/proceedings_published.html", context)
    text_body = render_to_string("notifications/email/proceedings_published.txt", context)
    send_transactional_email(
        subject=subject,
        message=text_body,
        recipient_list=[corresponding.email],
        from_email=settings.DEFAULT_FROM_EMAIL,
        html_message=html_body,
    )
