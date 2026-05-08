from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from core.views import healthcheck

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("conta/", include("accounts.urls")),
    path("painel/", include("accounts.dashboard_urls")),
    path("health/", include("core.urls")),
    path("design-system/", include("core.design_urls")),
    path("submissoes/", include("submissions.urls")),
    path("revisoes/", include("reviews.urls")),
    path("relatorios/", include("reports.urls")),
    path("", include("proceedings.urls")),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

urlpatterns = urlpatterns + i18n_patterns(
    # For anything not caught by a more specific rule, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    prefix_default_language=False,
)
