from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "institution", "country", "is_author", "is_reviewer", "is_chair")
    list_filter = ("is_author", "is_reviewer", "is_chair", "country")
    search_fields = ("user__username", "user__first_name", "user__last_name", "user__email", "institution")
