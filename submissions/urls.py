from django.urls import path

from . import views

app_name = "submissions"

urlpatterns = [
    path("<int:pk>/", views.submission_detail, name="detail"),
    path("nova/", views.wizard_new, name="wizard_new"),
    path("novo/", views.wizard_step1, name="wizard_step1"),
    path("<int:submission_pk>/editar/", views.wizard_edit, name="wizard_edit"),
    path(
        "<int:submission_pk>/passo-1/",
        views.wizard_step1,
        name="wizard_step1",
    ),
    path(
        "<int:submission_pk>/passo-2/",
        views.wizard_step2,
        name="wizard_step2",
    ),
    path(
        "<int:submission_pk>/passo-3/",
        views.wizard_step3,
        name="wizard_step3",
    ),
    path(
        "<int:submission_pk>/adicionar-autor/",
        views.add_author_row,
        name="add_author_row",
    ),
    path("arquivo/<int:file_id>/", views.download_file, name="download_file"),
]
