from django.urls import path

from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.reviewer_submissions, name="reviewer_submissions"),
    path("atribuicao/<int:assignment_id>/", views.review_detail, name="review_detail"),
    path(
        "comissao/submissoes/",
        views.manage_submissions,
        name="manage_submissions",
    ),
    path(
        "comissao/submissoes/<int:submission_id>/atribuir/",
        views.assign_reviewers,
        name="assign_reviewers",
    ),
    path(
        "comissao/submissoes/<int:submission_id>/decisao/",
        views.issue_decision,
        name="issue_decision",
    ),
]
