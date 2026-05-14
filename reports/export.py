import csv
import json

from django.http import HttpResponse


def export_csv(rows, headers, filename):
    """
    Exports a list of rows to a CSV file.
    """
    response = HttpResponse(content_type="text/csv; charset=utf-8-sig")
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    writer = csv.writer(response)
    writer.writerow(headers)

    for row in rows:
        writer.writerow(row)
    return response


def export_json(data, filename):
    """
    Exports a data structure to a JSON file.
    """
    response = HttpResponse(content_type="application/json; charset=utf-8")
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    json.dump(data, response, ensure_ascii=False, indent=2)
    return response


def export_xlsx(rows, headers, filename, sheet_name="Dados"):
    """
    Exports a list of rows to an XLSX file using openpyxl.
    """
    from openpyxl import Workbook
    
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    
    wb = Workbook()
    ws = wb.active
    ws.title = sheet_name[:31]  # Excel sheet name limit
    
    ws.append(headers)
    for row in rows:
        ws.append(row)
        
    wb.save(response)
    return response
