from django.db import models
from django.db.models import Count, Max, Min


class SubmissionQuerySet(models.QuerySet):
    def for_user(self, user):
        return self.filter(submitter=user)

    def by_status(self):
        return (
            self.values("status")
            .annotate(count=Count("id"))
            .order_by("-count")
        )

    def by_topic(self):
        return (
            self.values("thematic_axis__name", "thematic_axis__id")
            .annotate(count=Count("id"))
            .order_by("-count")
        )

    def by_modality(self):
        return (
            self.values("final_modality")
            .annotate(count=Count("id"))
            .order_by("-count")
        )

    def by_institution(self):
        return (
            self.values("authors__institution")
            .annotate(count=Count("id"))
            .order_by("-count")
        )

    def summary_stats(self):
        agg = self.aggregate(
            total=Count("id"),
            first_created=Min("created_at"),
            last_created=Max("created_at"),
        )
        by_status = dict(self.by_status().values_list("status", "count"))
        agg["by_status"] = by_status
        return agg

    def export_queryset(self, filters=None):
        qs = self.select_related("thematic_axis", "submitter").prefetch_related(
            "authors"
        )
        if filters:
            qs = qs.filter(**filters)
        return qs


SubmissionManager = SubmissionQuerySet.as_manager
