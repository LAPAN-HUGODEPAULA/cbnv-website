import csv
import json

from django.http import HttpResponse


def export_csv(queryset_or_rows, headers, filename, row_mapping=None):
    response = HttpResponse(content_type="text/csv; charset=utf-8-sig")
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    writer = csv.writer(response)
    writer.writerow(headers)

    for item in queryset_or_rows:
        if row_mapping:
            row = [row_mapping(item, h) for h in headers]
        else:
            row = [getattr(item, h, "") for h in headers]
        writer.writerow(row)
    return response


def export_json(data, filename):
    response = HttpResponse(content_type="application/json; charset=utf-8")
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    json.dump(data, response, ensure_ascii=False, indent=2)
    return response
