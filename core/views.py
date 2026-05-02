from django.http import JsonResponse
from django.db import connection


def healthcheck(request):
    try:
        connection.ensure_connection()
        return JsonResponse({"status": "ok"})
    except Exception:
        return JsonResponse({"status": "unavailable"}, status=503)
