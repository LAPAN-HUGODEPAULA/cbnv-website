import csv

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from accounts.decorators import AdminOrChairMixin, chair_required
from proceedings.managers import ACCEPTED_STATUSES
from reviews.models import ReviewerAssignment
from submissions.models import MODALITY_CHOICES, STATUS_CHOICES, Submission, SubmissionAuthor

from .export import export_csv, export_json, export_xlsx


FINAL_MATERIAL_STATUS_CHOICES = [
    ("pending", "Materiais pendentes"),
    ("received", "Materiais recebidos"),
    ("validated", "Materiais validados"),
    ("missing_authorization", "Sem autorização"),
]

PROCEEDINGS_STATUS_CHOICES = [
    ("ready_for_proceedings", "Pronto para anais"),
    ("published_in_proceedings", "Publicado nos anais"),
]


def build_report_filters(request):
    filters = {}

    status_filter = request.GET.get("status")
    if status_filter:
        filters["status"] = status_filter

    thematic_axis = request.GET.get("thematic_axis")
    if thematic_axis:
        filters["thematic_axis_id"] = thematic_axis

    final_modality = request.GET.get("final_modality")
    if final_modality:
        filters["final_modality"] = final_modality

    created_after = request.GET.get("created_after")
    if created_after:
        filters["created_at__date__gte"] = created_after

    created_before = request.GET.get("created_before")
    if created_before:
        filters["created_at__date__lte"] = created_before

    institution = request.GET.get("institution")
    if institution:
        filters["authors__institution"] = institution

    country = request.GET.get("country")
    if country:
        filters["submitter__profile__country"] = country

    final_material_status = request.GET.get("final_material_status")
    if final_material_status == "pending":
        filters["final_material__isnull"] = True
    elif final_material_status == "received":
        filters["final_material__isnull"] = False
    elif final_material_status == "validated":
        filters["final_material__validated_at__isnull"] = False
    elif final_material_status == "missing_authorization":
        filters["final_material__publication_authorized"] = False

    proceedings_status = request.GET.get("proceedings_status")
    if proceedings_status:
        filters["status"] = proceedings_status

    return filters


def filter_querystring(request):
    query = request.GET.copy()
    query.pop("format", None)
    return query.urlencode()


class ReportsDashboardView(AdminOrChairMixin, TemplateView):
    template_name = "reports/dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        filters = build_report_filters(self.request)

        submission_stats = Submission.objects.summary_stats(filters=filters)
        ctx.update(submission_stats)

        ctx["by_topic"] = list(Submission.objects.by_topic(filters=filters))
        ctx["by_modality"] = list(Submission.objects.by_modality(filters=filters))
        ctx["by_status"] = list(Submission.objects.by_status(filters=filters))
        ctx["by_country"] = list(Submission.objects.by_country(filters=filters))

        review_stats = ReviewerAssignment.objects.completion_stats() # Reviews don't support these filters yet
        ctx.update(review_stats)
        ctx["top_reviewers"] = list(ReviewerAssignment.objects.top_reviewers(limit=10))

        filtered_subs = Submission.objects.export_queryset(filters=filters)
        ctx["institutions"] = list(filtered_subs.by_institution())
        
        ctx["unique_authors"] = (
            SubmissionAuthor.objects.filter(submission__in=filtered_subs)
            .values("email").distinct().count()
        )
        ctx["unique_institutions"] = (
            SubmissionAuthor.objects.filter(submission__in=filtered_subs)
            .exclude(institution="")
            .values("institution").distinct().count()
        )
        ctx["unique_countries"] = (
            filtered_subs.exclude(submitter__profile__country="")
            .values("submitter__profile__country")
            .distinct()
            .count()
        )

        from proceedings.models import FinalMaterial
        ctx.update(FinalMaterial.objects.materials_status(submission_filters=filters))

        from submissions.models import ThematicAxis
        ctx["thematic_axes"] = ThematicAxis.objects.all()
        ctx["status_choices"] = STATUS_CHOICES
        ctx["modality_choices"] = MODALITY_CHOICES
        ctx["final_material_status_choices"] = FINAL_MATERIAL_STATUS_CHOICES
        ctx["proceedings_status_choices"] = PROCEEDINGS_STATUS_CHOICES
        ctx["institution_choices"] = (
            SubmissionAuthor.objects.exclude(institution="")
            .values_list("institution", flat=True)
            .distinct()
            .order_by("institution")
        )
        ctx["country_choices"] = (
            Submission.objects.exclude(submitter__profile__country="")
            .values_list("submitter__profile__country", flat=True)
            .distinct()
            .order_by("submitter__profile__country")
        )
        ctx["selected_filters"] = self.request.GET
        ctx["filter_querystring"] = filter_querystring(self.request)

        return ctx


class IndicatorsExportView(AdminOrChairMixin, TemplateView):
    template_name = None

    def get(self, request, *args, **kwargs):
        fmt = request.GET.get("format", "csv")
        filters = build_report_filters(request)
        submission_stats = Submission.objects.summary_stats(filters=filters)
        by_topic = list(Submission.objects.by_topic(filters=filters))
        by_modality = list(Submission.objects.by_modality(filters=filters))
        by_status = list(Submission.objects.by_status(filters=filters))
        by_country = list(Submission.objects.by_country(filters=filters))
        review_stats = ReviewerAssignment.objects.completion_stats()
        top_reviewers = list(ReviewerAssignment.objects.top_reviewers(limit=10))
        institutions = list(Submission.objects.by_institution(filters=filters))

        from proceedings.models import FinalMaterial
        material_stats = FinalMaterial.objects.materials_status(submission_filters=filters)

        data = {
            "resumo_geral": {
                "total_submissoes": submission_stats["total"],
                "por_status": {s["status"]: s["count"] for s in by_status},
                "por_eixo": [
                    {"eixo": t["thematic_axis__name"], "count": t["count"]}
                    for t in by_topic
                ],
                "por_modalidade": [
                    {"modalidade": m["final_modality"], "count": m["count"]}
                    for m in by_modality
                ],
                "por_pais": [
                    {"pais": c["submitter__profile__country"], "count": c["count"]}
                    for c in by_country
                ],
            },
            "revisoes": {
                "total_atribuicoes": review_stats["total_assigned"],
                "concluidas": review_stats["completed"],
                "pendentes": review_stats["pending"],
                "tempo_medio": str(review_stats["avg_completion_time"] or ""),
                "top_revisores": [
                    {
                        "nome": f"{r['reviewer__first_name']} {r['reviewer__last_name']}",
                        "instituicao": r["reviewer__profile__institution"],
                        "atribuidas": r["assigned"],
                        "concluidas": r["completed"],
                    }
                    for r in top_reviewers
                ],
            },
            "autores_e_instituicoes": {
                "total_autores": SubmissionAuthor.objects.values("email").distinct().count(),
                "total_instituicoes": SubmissionAuthor.objects.values("institution").distinct().count(),
                "ranking_instituicoes": [
                    {"instituicao": i["authors__institution"], "count": i["count"]}
                    for i in institutions
                ],
            },
            "materiais": material_stats,
        }

        if fmt == "json":
            return export_json(data, "indicadores_cbnv_2026.json")

        headers = [
            "tipo", "categoria", "valor", "contagem",
        ]
        rows = []

        for s in by_status:
            rows.append(["submissao", "status", s["status"], s["count"]])
        for t in by_topic:
            rows.append(["submissao", "eixo", t["thematic_axis__name"], t["count"]])
        for m in by_modality:
            rows.append(["submissao", "modalidade", m["final_modality"], m["count"]])
        for c in by_country:
            rows.append(["submissao", "pais", c["submitter__profile__country"], c["count"]])
        rows.append(["revisao", "total_atribuicoes", "", review_stats["total_assigned"]])
        rows.append(["revisao", "concluidas", "", review_stats["completed"]])
        rows.append(["revisao", "pendentes", "", review_stats["pending"]])
        for i in institutions:
            rows.append(["instituicao", "ranking", i["authors__institution"], i["count"]])
        rows.append(["materiais", "total_aceitos", "", material_stats["total_accepted"]])
        rows.append(["materiais", "entregues", "", material_stats["with_materials"]])
        rows.append(["materiais", "pendentes", "", material_stats["pending_materials"]])
        rows.append(["materiais", "validados", "", material_stats["validated"]])
        rows.append(["materiais", "sem_autorizacao", "", material_stats["missing_authorization"]])
        rows.append(["materiais", "com_video", "", material_stats["with_video"]])
        rows.append(["materiais", "videos_na_galeria", "", material_stats["promoted_videos"]])
        rows.append(["materiais", "publicados", "", material_stats["published"]])

        if fmt == "xlsx":
            return export_xlsx(rows, headers, "indicadores_cbnv_2026.xlsx", "Indicators")

        return export_csv(rows, headers, "indicadores_cbnv_2026.csv")


class SubmissionsExportView(AdminOrChairMixin, TemplateView):
    template_name = None

    def get(self, request, *args, **kwargs):
        fmt = request.GET.get("format", "csv")
        filters = build_report_filters(request)

        qs = Submission.objects.export_queryset(filters=filters)

        if fmt == "json":
            data = [
                {
                    "id": s.submission_id,
                    "titulo": s.title,
                    "eixo": s.thematic_axis.name if s.thematic_axis else "",
                    "modalidade": s.get_final_modality_display() or "",
                    "status": s.status_label,
                    "submetedor": s.submitter.get_full_name() or s.submitter.username,
                    "autores": ", ".join(
                        a.full_name for a in s.authors.all()
                    ),
                    "data_criacao": s.created_at.isoformat() if s.created_at else "",
                    "data_atualizacao": s.updated_at.isoformat() if s.updated_at else "",
                }
                for s in qs
            ]
            return export_json(data, "submissoes_cbnv_2026.json")

        headers = [
            "ID", "Título", "Eixo", "Modalidade", "Status",
            "Submetedor", "Autores", "Data criação", "Data atualização",
        ]
        rows = [
            [
                s.submission_id,
                s.title,
                s.thematic_axis.name if s.thematic_axis else "",
                s.get_final_modality_display() or "",
                s.status_label,
                s.submitter.get_full_name() or s.submitter.username,
                ", ".join(a.full_name for a in s.authors.all()),
                s.created_at.strftime("%Y-%m-%d %H:%M") if s.created_at else "",
                s.updated_at.strftime("%Y-%m-%d %H:%M") if s.updated_at else "",
            ]
            for s in qs
        ]
        
        if fmt == "xlsx":
            return export_xlsx(rows, headers, "submissoes_cbnv_2026.xlsx", "Submissions")
            
        return export_csv(rows, headers, "submissoes_cbnv_2026.csv")


class ReviewsExportView(AdminOrChairMixin, TemplateView):
    template_name = None

    def get(self, request, *args, **kwargs):
        fmt = request.GET.get("format", "csv")
        qs = ReviewerAssignment.objects.export_queryset()

        if fmt == "json":
            data = [
                {
                    "revisor": a.reviewer.get_full_name() or a.reviewer.username,
                    "instituicao": a.reviewer.profile.institution if hasattr(a.reviewer, "profile") else "",
                    "submissao_id": a.submission.submission_id,
                    "titulo": a.submission.title,
                    "recomendacao": (
                        a.review.get_recommendation_display()
                        if hasattr(a, "review")
                        else "Pendente"
                    ),
                    "data_atribuicao": a.assigned_at.isoformat() if a.assigned_at else "",
                    "data_conclusao": (
                        a.review.submitted_at.isoformat()
                        if hasattr(a, "review")
                        else ""
                    ),
                }
                for a in qs
            ]
            return export_json(data, "revisoes_cbnv_2026.json")

        headers = [
            "Revisor", "Instituição", "Submissão ID", "Título",
            "Recomendação", "Data atribuição", "Data conclusão",
        ]
        rows = [
            [
                a.reviewer.get_full_name() or a.reviewer.username,
                a.reviewer.profile.institution if hasattr(a.reviewer, "profile") else "",
                a.submission.submission_id,
                a.submission.title,
                a.review.get_recommendation_display() if hasattr(a, "review") else "Pendente",
                a.assigned_at.strftime("%Y-%m-%d %H:%M") if a.assigned_at else "",
                a.review.submitted_at.strftime("%Y-%m-%d %H:%M") if hasattr(a, "review") else "",
            ]
            for a in qs
        ]
        
        if fmt == "xlsx":
            return export_xlsx(rows, headers, "revisoes_cbnv_2026.xlsx", "Reviews")
            
        return export_csv(rows, headers, "revisoes_cbnv_2026.csv")


class ProceedingsExportView(AdminOrChairMixin, TemplateView):
    template_name = None

    def get(self, request, *args, **kwargs):
        fmt = request.GET.get("format", "csv")
        from proceedings.models import FinalMaterial

        filters = build_report_filters(request)
        qs = FinalMaterial.objects.export_queryset(submission_filters=filters)

        if fmt == "json":
            data = [
                {
                    "submissao_id": fm.submission.submission_id,
                    "titulo": fm.submission.title,
                    "resumo": fm.submission.abstract,
                    "palavras_chave": ", ".join(fm.submission.keywords),
                    "eixo": fm.submission.thematic_axis.name if fm.submission.thematic_axis else "",
                    "modalidade": fm.submission.get_final_modality_display() or "",
                    "status": fm.submission.status_label,
                    "autores": ", ".join(
                        a.full_name for a in fm.submission.authors.all()
                    ),
                    "afiliacoes": ", ".join(
                        sorted(set(a.institution for a in fm.submission.authors.all()))
                    ),
                    "video_url": fm.video_url or "",
                    "autorizado": fm.publication_authorized,
                    "data_recebimento": (
                        fm.received_at.isoformat() if fm.received_at else ""
                    ),
                    "validado": bool(fm.validated_at),
                }
                for fm in qs
            ]
            return export_json(data, "proceedings_cbnv_2026.json")

        headers = [
            "Submissão ID", "Título", "Resumo", "Palavras-chave", "Eixo",
            "Modalidade", "Status", "Autores", "Afiliações", "Vídeo URL",
            "Autorizado", "Data recebimento", "Validado",
        ]
        rows = [
            [
                fm.submission.submission_id,
                fm.submission.title,
                fm.submission.abstract,
                ", ".join(fm.submission.keywords),
                fm.submission.thematic_axis.name if fm.submission.thematic_axis else "",
                fm.submission.get_final_modality_display() or "",
                fm.submission.status_label,
                ", ".join(a.full_name for a in fm.submission.authors.all()),
                ", ".join(sorted(set(a.institution for a in fm.submission.authors.all()))),
                fm.video_url or "",
                "Sim" if fm.publication_authorized else "Não",
                fm.received_at.strftime("%Y-%m-%d %H:%M") if fm.received_at else "",
                "Sim" if fm.validated_at else "Não",
            ]
            for fm in qs
        ]
        
        if fmt == "xlsx":
            return export_xlsx(rows, headers, "proceedings_cbnv_2026.xlsx", "Proceedings")
            
        return export_csv(rows, headers, "proceedings_cbnv_2026.csv")


class AuthorsExportView(AdminOrChairMixin, TemplateView):
    template_name = None

    def get(self, request, *args, **kwargs):
        fmt = request.GET.get("format", "csv")
        filters = build_report_filters(request)
        qs = (
            SubmissionAuthor.objects
            .select_related("submission__thematic_axis")
            .filter(submission__in=Submission.objects.filter(**filters).distinct())
            .order_by("institution", "last_name")
        )

        if fmt == "json":
            data = [
                {
                    "nome": a.full_name,
                    "email": a.email,
                    "instituicao": a.institution,
                    "ordem": a.order,
                    "correspondente": a.is_corresponding,
                    "apresentador": a.is_corresponding,
                    "submissao_id": a.submission.submission_id,
                    "titulo": a.submission.title,
                    "eixo": (
                        a.submission.thematic_axis.name
                        if a.submission.thematic_axis
                        else ""
                    ),
                    "status": a.submission.status_label,
                }
                for a in qs
            ]
            return export_json(data, "autores_cbnv_2026.json")

        headers = [
            "Nome", "E-mail", "Instituição", "Ordem", "Correspondente", "Apresentador",
            "Submissão ID", "Título", "Eixo", "Status",
        ]
        rows = [
            [
                a.full_name,
                a.email,
                a.institution,
                a.order,
                "Sim" if a.is_corresponding else "Não",
                "Sim" if a.is_corresponding else "Não",
                a.submission.submission_id,
                a.submission.title,
                a.submission.thematic_axis.name if a.submission.thematic_axis else "",
                a.submission.status_label,
            ]
            for a in qs
        ]
        
        if fmt == "xlsx":
            return export_xlsx(rows, headers, "autores_cbnv_2026.xlsx", "Authors")
            
        return export_csv(rows, headers, "autores_cbnv_2026.csv")


class InstitutionsExportView(AdminOrChairMixin, TemplateView):
    template_name = None

    def get(self, request, *args, **kwargs):
        fmt = request.GET.get("format", "csv")
        filters = build_report_filters(request)
        
        qs = (
            SubmissionAuthor.objects
            .filter(submission__in=Submission.objects.filter(**filters).distinct())
            .values("institution")
            .annotate(
                total_authors=Count("id", distinct=True),
                total_submissions=Count("submission_id", distinct=True),
            )
            .order_by("-total_submissions", "institution")
        )

        if fmt == "json":
            data = [
                {
                    "instituicao": item["institution"],
                    "total_autores": item["total_authors"],
                    "total_submissoes": item["total_submissions"],
                }
                for item in qs
            ]
            return export_json(data, "instituicoes_cbnv_2026.json")

        headers = ["Instituição", "Total de Autores", "Total de Submissões"]
        rows = [
            [
                item["institution"],
                item["total_authors"],
                item["total_submissions"],
            ]
            for item in qs
        ]
        
        if fmt == "xlsx":
            return export_xlsx(rows, headers, "instituicoes_cbnv_2026.xlsx", "Institutions")
            
        return export_csv(rows, headers, "instituicoes_cbnv_2026.csv")


@login_required
@chair_required
def review_progress(request):
    submissions = (
        Submission.objects.filter(
            status__in=[
                "submitted",
                "admin_screening",
                "assigned_to_reviewers",
                "under_review",
                "reviews_completed",
                "decision_pending",
            ]
        )
        .prefetch_related("reviewer_assignments__review")
        .order_by("-created_at")
    )
    rows = []
    for sub in submissions:
        assignments = sub.reviewer_assignments.all()
        total = assignments.count()
        completed = sum(1 for a in assignments if hasattr(a, "review"))
        rows.append(
            {
                "submission": sub,
                "total_reviewers": total,
                "completed_reviews": completed,
                "all_reviewed": total > 0 and completed == total,
            }
        )
    return render(request, "reports/review_progress.html", {"rows": rows})


@login_required
@chair_required
def export_decisions(request):
    fmt = request.GET.get("format", "csv")
    submissions = (
        Submission.objects.filter(
            status__in=[
                "accepted_oral",
                "accepted_poster",
                "accepted_video",
                "rejected",
            ]
        )
        .prefetch_related("authors")
        .order_by("submission_id")
    )
    
    headers = ["ID", "Título", "Autor correspondente", "Status", "Modalidade"]
    rows = []
    for sub in submissions:
        corresponding = sub.get_corresponding_author()
        author_name = f"{corresponding.first_name} {corresponding.last_name}" if corresponding else ""
        rows.append([
            sub.submission_id,
            sub.title,
            author_name,
            sub.status_label,
            sub.get_final_modality_display() if sub.final_modality else "",
        ])
        
    if fmt == "xlsx":
        return export_xlsx(rows, headers, "decisoes_cbnv_2026.xlsx", "Decisions")
        
    return export_csv(rows, headers, "decisoes_cbnv_2026.csv")
