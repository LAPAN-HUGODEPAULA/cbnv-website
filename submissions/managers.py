from django.db import models
from django.db.models import Count, Max, Min


class SubmissionQuerySet(models.QuerySet):
    def for_user(self, user):
        return self.filter(submitter=user)

    def by_status(self, filters=None):
        qs = self
        if filters:
            qs = qs.filter(**filters)
        return (
            qs.values("status")
            .annotate(count=Count("id", distinct=True))
            .order_by("-count")
        )

    def by_topic(self, filters=None):
        qs = self
        if filters:
            qs = qs.filter(**filters)
        return (
            qs.values("thematic_axis__name", "thematic_axis__id")
            .annotate(count=Count("id", distinct=True))
            .order_by("-count")
        )

    def by_modality(self, filters=None):
        qs = self
        if filters:
            qs = qs.filter(**filters)
        return (
            qs.values("final_modality")
            .annotate(count=Count("id", distinct=True))
            .order_by("-count")
        )

    def by_institution(self, filters=None):
        qs = self
        if filters:
            qs = qs.filter(**filters)
        return (
            qs.values("authors__institution")
            .annotate(count=Count("id", distinct=True))
            .order_by("-count")
        )

    def by_country(self, filters=None):
        qs = self
        if filters:
            qs = qs.filter(**filters)
        return (
            qs.values("submitter__profile__country")
            .annotate(count=Count("id", distinct=True))
            .order_by("-count")
        )

    def summary_stats(self, filters=None):
        qs = self
        if filters:
            qs = qs.filter(**filters)
        agg = qs.aggregate(
            total=Count("id", distinct=True),
            first_created=Min("created_at"),
            last_created=Max("created_at"),
        )
        by_status = dict(qs.by_status().values_list("status", "count"))
        agg["by_status"] = by_status
        return agg

    def export_queryset(self, filters=None):
        qs = self.select_related("thematic_axis", "submitter").prefetch_related(
            "authors"
        )
        if filters:
            qs = qs.filter(**filters)
        return qs.distinct()


SubmissionManager = SubmissionQuerySet.as_manager
