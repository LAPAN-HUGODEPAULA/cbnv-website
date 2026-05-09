from django.db import models
from django.db.models import Count, Avg, F, Q


class ReviewerAssignmentQuerySet(models.QuerySet):
    def by_reviewer(self):
        return (
            self.values(
                "reviewer__id",
                "reviewer__first_name",
                "reviewer__last_name",
                "reviewer__profile__institution",
            )
            .annotate(
                assigned=Count("id"),
                completed=Count("id", filter=Q(review__isnull=False)),
            )
            .order_by("-completed")
        )

    def by_status(self):
        return (
            self.values("review__isnull")
            .annotate(count=Count("id"))
        )

    def completion_stats(self):
        total = self.count()
        completed = self.filter(review__isnull=False).count()
        avg_time = (
            self.filter(review__isnull=False).annotate(
                duration=F("review__submitted_at") - F("assigned_at")
            ).aggregate(avg=Avg("duration"))
        )["avg"]
        return {
            "total_assigned": total,
            "completed": completed,
            "pending": total - completed,
            "avg_completion_time": avg_time,
        }

    def top_reviewers(self, limit=10):
        return self.by_reviewer()[:limit]

    def export_queryset(self):
        return self.select_related(
            "reviewer__profile", "submission", "review"
        ).order_by("-assigned_at")


class ReviewQuerySet(models.QuerySet):
    def by_recommendation(self):
        return (
            self.values("recommendation")
            .annotate(count=Count("id"))
            .order_by("-count")
        )

    def export_queryset(self):
        return self.select_related(
            "assignment__reviewer", "assignment__submission"
        ).order_by("-submitted_at")


ReviewerAssignmentManager = ReviewerAssignmentQuerySet.as_manager
ReviewManager = ReviewQuerySet.as_manager
