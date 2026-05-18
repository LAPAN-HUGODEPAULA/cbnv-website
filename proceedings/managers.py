from django.db import models
from django.db.models import Count, Q


ACCEPTED_STATUSES = [
    "accepted_oral",
    "accepted_poster",
    "accepted_video",
    "final_materials_pending",
    "ready_for_proceedings",
    "published_in_proceedings",
]


class FinalMaterialQuerySet(models.QuerySet):
    def materials_status(self, submission_filters=None):
        from submissions.models import Submission

        accepted = Submission.objects.filter(
            status__in=ACCEPTED_STATUSES
        )
        if submission_filters:
            accepted = accepted.filter(**submission_filters)

        total_accepted = accepted.distinct().count()
        with_materials = (
            accepted.filter(final_material__isnull=False)
            .distinct()
            .count()
        )
        with_video = (
            accepted.filter(
                final_material__isnull=False,
                final_material__video_url__gt="",
            )
            .distinct()
            .count()
        )
        validated = (
            accepted.filter(
                final_material__isnull=False,
                final_material__validated_at__isnull=False,
            )
            .distinct()
            .count()
        )
        missing_authorization = (
            accepted.filter(
                final_material__isnull=False,
                final_material__publication_authorized=False,
            )
            .distinct()
            .count()
        )
        published = accepted.filter(
            status="published_in_proceedings"
        ).distinct().count()
        promoted_videos = (
            accepted.filter(
                final_material__isnull=False,
                final_material__video_resource__isnull=False,
            )
            .distinct()
            .count()
        )
        return {
            "total_accepted": total_accepted,
            "with_materials": with_materials,
            "pending_materials": total_accepted - with_materials,
            "validated": validated,
            "missing_authorization": missing_authorization,
            "with_video": with_video,
            "promoted_videos": promoted_videos,
            "published": published,
        }

    def export_queryset(self, submission_filters=None):
        qs = self.select_related(
            "submission__thematic_axis"
        ).prefetch_related("submission__authors").order_by("-received_at")
        if submission_filters:
            qs = qs.filter(submission__in=self._submission_queryset(submission_filters))
        return qs.distinct()

    def _submission_queryset(self, submission_filters):
        from submissions.models import Submission

        return Submission.objects.filter(**submission_filters).distinct()


FinalMaterialManager = FinalMaterialQuerySet.as_manager
