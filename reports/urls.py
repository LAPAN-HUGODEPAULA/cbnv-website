from django.urls import path

from . import views

app_name = "reports"

urlpatterns = [
    path("", views.ReportsDashboardView.as_view(), name="dashboard"),
    path("revisoes/progresso/", views.review_progress, name="review_progress"),
    path("decisoes/exportar/", views.export_decisions, name="export_decisions"),
    path(
        "indicadores/exportar/",
        views.IndicatorsExportView.as_view(),
        name="export_indicators",
    ),
    path(
        "submissoes/exportar/",
        views.SubmissionsExportView.as_view(),
        name="export_submissions",
    ),
    path(
        "revisoes/exportar/",
        views.ReviewsExportView.as_view(),
        name="export_reviews",
    ),
    path(
        "proceedings/exportar/",
        views.ProceedingsExportView.as_view(),
        name="export_proceedings",
    ),
    path(
        "autores/exportar/",
        views.AuthorsExportView.as_view(),
        name="export_authors",
    ),
]
