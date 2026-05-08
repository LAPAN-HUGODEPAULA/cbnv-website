from django.http import JsonResponse
from django.db import connection
from django.shortcuts import render


def healthcheck(request):
    try:
        connection.ensure_connection()
        return JsonResponse({"status": "ok"})
    except Exception:
        return JsonResponse({"status": "unavailable"}, status=503)


def design_system(request):
    timeline_items = [
        {
            "time": "08:00",
            "title": "Recepção e Credenciamento",
            "description": "Registro dos participantes.",
            "badge": {"label": "Credenciamento", "variant": "info"},
        },
        {
            "time": "09:00",
            "title": "Conferência Plenária de Abertura",
            "description": "Neurociência da Visão e Inteligência Artificial.",
            "speaker": "Dr. Nome do Palestrante — UFMG",
            "badge": {"label": "Confirmado", "variant": "confirmed"},
        },
        {
            "time": "11:00",
            "title": "Sessão de Pôsteres",
            "description": "Apresentação de trabalhos selecionados.",
            "badge": {"label": "Pendente", "variant": "pending"},
        },
    ]
    choices = [
        ("author", "Autor"),
        ("reviewer", "Revisor"),
        ("chair", "Comissão Científica"),
    ]
    return render(
        request,
        "core/design_system.html",
        {"timeline_items": timeline_items, "choices": choices},
    )
