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
    def materials_status(self):
        from submissions.models import Submission

        accepted = Submission.objects.filter(
            status__in=ACCEPTED_STATUSES
        )
        total_accepted = accepted.count()
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
        published = accepted.filter(
            status="published_in_proceedings"
        ).count()
        return {
            "total_accepted": total_accepted,
            "with_materials": with_materials,
            "pending_materials": total_accepted - with_materials,
            "with_video": with_video,
            "published": published,
        }

    def export_queryset(self):
        return self.select_related(
            "submission__thematic_axis"
        ).prefetch_related("submission__authors").order_by("-received_at")


FinalMaterialManager = FinalMaterialQuerySet.as_manager
