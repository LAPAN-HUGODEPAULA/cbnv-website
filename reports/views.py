import csv

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from accounts.decorators import AdminOrChairMixin, chair_required
from proceedings.managers import ACCEPTED_STATUSES
from reviews.models import ReviewerAssignment
from submissions.models import Submission, SubmissionAuthor

from .export import export_csv, export_json


class ReportsDashboardView(AdminOrChairMixin, TemplateView):
    template_name = "reports/dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        submission_stats = Submission.objects.summary_stats()
        ctx.update(submission_stats)

        ctx["by_topic"] = list(Submission.objects.by_topic())
        ctx["by_modality"] = list(Submission.objects.by_modality())
        ctx["by_status"] = list(Submission.objects.by_status())

        review_stats = ReviewerAssignment.objects.completion_stats()
        ctx.update(review_stats)
        ctx["top_reviewers"] = list(ReviewerAssignment.objects.top_reviewers(limit=10))

        ctx["institutions"] = list(Submission.objects.by_institution())
        ctx["unique_authors"] = (
            SubmissionAuthor.objects.values("email").distinct().count()
        )
        ctx["unique_institutions"] = (
            SubmissionAuthor.objects.values("institution").distinct().count()
        )

        from proceedings.models import FinalMaterial

        ctx.update(FinalMaterial.objects.materials_status())

        return ctx


class IndicatorsExportView(AdminOrChairMixin, TemplateView):
    template_name = None

    def get(self, request, *args, **kwargs):
        fmt = request.GET.get("format", "csv")
        submission_stats = Submission.objects.summary_stats()
        by_topic = list(Submission.objects.by_topic())
        by_modality = list(Submission.objects.by_modality())
        by_status = list(Submission.objects.by_status())
        review_stats = ReviewerAssignment.objects.completion_stats()
        top_reviewers = list(ReviewerAssignment.objects.top_reviewers(limit=10))
        institutions = list(Submission.objects.by_institution())

        from proceedings.models import FinalMaterial
        material_stats = FinalMaterial.objects.materials_status()

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
            },
            "revisoes": {
                "total_atribuicoes": review_stats["total_assigned"],
                "concluidas": review_stats["completed"],
                "pendentes": review_stats["pending"],
                "tempo_medio": str(review_stats["avg_completion_time"] or ""),
                "top_revisores": [
                    {
                        "nome": f"{r['reviewer__first_name']} {r['reviewer__last_name']}",
                        "instituicao": r["reviewer__institution"],
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
        rows.append(["revisao", "total_atribuicoes", "", review_stats["total_assigned"]])
        rows.append(["revisao", "concluidas", "", review_stats["completed"]])
        rows.append(["revisao", "pendentes", "", review_stats["pending"]])
        for i in institutions:
            rows.append(["instituicao", "ranking", i["authors__institution"], i["count"]])
        rows.append(["materiais", "total_aceitos", "", material_stats["total_accepted"]])
        rows.append(["materiais", "entregues", "", material_stats["with_materials"]])
        rows.append(["materiais", "pendentes", "", material_stats["pending_materials"]])
        rows.append(["materiais", "com_video", "", material_stats["with_video"]])
        rows.append(["materiais", "publicados", "", material_stats["published"]])

        return export_csv(rows, headers, "indicadores_cbnv_2026.csv")


class SubmissionsExportView(AdminOrChairMixin, TemplateView):
    template_name = None

    def get(self, request, *args, **kwargs):
        fmt = request.GET.get("format", "csv")
        filters = {}
        status_filter = request.GET.get("status")
        if status_filter:
            filters["status"] = status_filter

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
                    "instituicao": a.reviewer.institution or "",
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
                a.reviewer.institution or "",
                a.submission.submission_id,
                a.submission.title,
                a.review.get_recommendation_display() if hasattr(a, "review") else "Pendente",
                a.assigned_at.strftime("%Y-%m-%d %H:%M") if a.assigned_at else "",
                a.review.submitted_at.strftime("%Y-%m-%d %H:%M") if hasattr(a, "review") else "",
            ]
            for a in qs
        ]
        return export_csv(rows, headers, "revisoes_cbnv_2026.csv")


class ProceedingsExportView(AdminOrChairMixin, TemplateView):
    template_name = None

    def get(self, request, *args, **kwargs):
        fmt = request.GET.get("format", "csv")
        from proceedings.models import FinalMaterial

        qs = FinalMaterial.objects.export_queryset()

        if fmt == "json":
            data = [
                {
                    "submissao_id": fm.submission.submission_id,
                    "titulo": fm.submission.title,
                    "modalidade": fm.submission.get_final_modality_display() or "",
                    "status": fm.submission.status_label,
                    "autores": ", ".join(
                        a.full_name for a in fm.submission.authors.all()
                    ),
                    "video_url": fm.video_url or "",
                    "data_recebimento": (
                        fm.received_at.isoformat() if fm.received_at else ""
                    ),
                    "validado": bool(fm.validated_at),
                }
                for fm in qs
            ]
            return export_json(data, "proceedings_cbnv_2026.json")

        headers = [
            "Submissão ID", "Título", "Modalidade", "Status",
            "Autores", "Vídeo URL", "Data recebimento", "Validado",
        ]
        rows = [
            [
                fm.submission.submission_id,
                fm.submission.title,
                fm.submission.get_final_modality_display() or "",
                fm.submission.status_label,
                ", ".join(a.full_name for a in fm.submission.authors.all()),
                fm.video_url or "",
                fm.received_at.strftime("%Y-%m-%d %H:%M") if fm.received_at else "",
                "Sim" if fm.validated_at else "Não",
            ]
            for fm in qs
        ]
        return export_csv(rows, headers, "proceedings_cbnv_2026.csv")


class AuthorsExportView(AdminOrChairMixin, TemplateView):
    template_name = None

    def get(self, request, *args, **kwargs):
        fmt = request.GET.get("format", "csv")
        qs = (
            SubmissionAuthor.objects
            .select_related("submission__thematic_axis")
            .order_by("institution", "last_name")
        )

        if fmt == "json":
            data = [
                {
                    "nome": a.full_name,
                    "email": a.email,
                    "instituicao": a.institution,
                    "correspondente": a.is_corresponding,
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
            "Nome", "E-mail", "Instituição", "Correspondente",
            "Submissão ID", "Título", "Eixo", "Status",
        ]
        rows = [
            [
                a.full_name,
                a.email,
                a.institution,
                "Sim" if a.is_corresponding else "Não",
                a.submission.submission_id,
                a.submission.title,
                a.submission.thematic_axis.name if a.submission.thematic_axis else "",
                a.submission.status_label,
            ]
            for a in qs
        ]
        return export_csv(rows, headers, "autores_cbnv_2026.csv")


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
    response = HttpResponse(content_type="text/csv; charset=utf-8-sig")
    response["Content-Disposition"] = 'attachment; filename="decisoes_cbnv_2026.csv"'
    writer = csv.writer(response)
    writer.writerow(["ID", "Título", "Autor correspondente", "Status", "Modalidade"])
    for sub in submissions:
        corresponding = sub.get_corresponding_author()
        author_name = f"{corresponding.first_name} {corresponding.last_name}" if corresponding else ""
        writer.writerow(
            [
                sub.submission_id,
                sub.title,
                author_name,
                sub.status_label,
                sub.get_final_modality_display() if sub.final_modality else "",
            ]
        )
    return response
