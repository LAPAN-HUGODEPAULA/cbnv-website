from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Perfil", {"fields": ("institution", "country", "position")}),
        ("Papéis Científicos", {"fields": ("is_author", "is_reviewer", "is_chair")}),
        ("Consentimentos", {"fields": ("consent_privacy", "consent_image")}),
    )
    list_display = BaseUserAdmin.list_display + ("institution",)
    list_filter = BaseUserAdmin.list_filter + ("is_author", "is_reviewer", "is_chair")
