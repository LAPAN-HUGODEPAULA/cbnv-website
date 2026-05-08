from django.urls import path

from . import views

app_name = "proceedings"

urlpatterns = [
    path("materiais/comissao/materiais/", views.commission_materials, name="commission_materials"),
    path("materiais/comissao/materiais/<int:submission_id>/solicitar/", views.request_materials, name="request_materials"),
    path("materiais/comissao/materiais/<int:submission_id>/validar/", views.validate_materials, name="validate_materials"),
    path("materiais/comissao/materiais/<int:submission_id>/publicar/", views.publish_proceedings, name="publish_proceedings"),
    path("materiais/autor/materiais/<int:submission_id>/", views.author_upload_materials, name="author_upload"),
    path("anais/", views.proceedings_list, name="proceedings_list"),
    path("anais/<str:submission_id>/", views.proceedings_detail, name="proceedings_detail"),
    path("anais/<str:submission_id>/pdf/", views.proceedings_download_pdf, name="proceedings_download_pdf"),
]
