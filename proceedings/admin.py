from django.contrib import admin

from .models import FinalMaterial


@admin.register(FinalMaterial)
class FinalMaterialAdmin(admin.ModelAdmin):
    list_display = (
        "submission",
        "publication_authorized",
        "received_at",
        "validated_at",
        "validated_by",
    )
    list_filter = (
        "publication_authorized",
        "received_at",
        "validated_at",
        "submission__status",
    )
    search_fields = (
        "submission__submission_id",
        "submission__title",
        "submission__submitter__email",
    )
    raw_id_fields = ("submission", "validated_by", "video_resource")
    readonly_fields = ("created_at", "updated_at")
