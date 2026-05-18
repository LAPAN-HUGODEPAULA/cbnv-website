# Design: Add Reports, Exports and Indicators

## Overview

This change adds the internal reporting layer for CBNV operations. It turns submission, review, decision, final material and proceedings data into committee-facing indicators and deterministic exports.

The design must remain pragmatic. The goal is not a generic BI platform; the goal is committee oversight, exportable data and technical-scientific reporting support.

## Design Principles

### 1. Committee utility first

Reports must answer operational questions the committee actually has: how many submissions exist, what stage they are in, what reviews are pending, what decisions were made, and which works are ready for proceedings.

### 2. Deterministic exports

Exports must have stable column order, stable sheet names and predictable filtering. This is essential for reproducible reporting.

### 3. Privacy by default

Reports and exports are internal. Personal data and review data must not leak to unauthorized users.

### 4. Services before templates

Indicator calculations and export generation should live in service functions or export builders, not in templates.

### 5. No protected-file bulk export

Reports may expose metadata and status. They must not leak protected file URLs or bulk-download private files.

## Data Sources

The reports may aggregate from:

- submissions;
- submission authors;
- accounts/profiles;
- review assignments;
- reviews;
- decisions;
- final materials;
- proceedings/editions;
- video resources.

The implementation should tolerate missing optional data. If a workflow has not produced data yet, indicators should show zero or an empty state.

## Report Dashboard Design

The reports dashboard should use summary cards and simple tables.

Suggested sections:

1. Submissions overview
2. Review status
3. Decision outcomes
4. Final materials and proceedings
5. Authors and institutions
6. Export actions

Charts are optional. Counts and tables are sufficient for MVP.

## Indicator Design

Indicator service functions should return simple data structures, for example:

```python
{
    "total_submissions": 120,
    "by_status": {"submitted": 40, "accepted_oral": 12},
    "by_axis": {"Retina": 20},
}
```

Avoid embedding queryset logic directly in templates.

## Export Design

Export builders should define columns explicitly.

Recommended builder pattern:

```python
class SubmissionsExport:
    columns = [...]
    def rows(self, queryset): ...
```

or function-based equivalent.

CSV should be implemented with standard library support.

XLSX can use the project's available spreadsheet dependency if already present. If no dependency exists, either add a lightweight dependency with justification or document CSV-only for this stage.

## Permission Design

Use explicit permission helpers.

Recommended access levels:

- `can_view_reports(user)`
- `can_export_submissions(user)`
- `can_export_reviews(user)`
- `can_export_proceedings(user)`

Chair/scientific committee should have full access. Staff/superuser access may follow project convention.

Authors must not access global reports. Reviewers must not access global exports unless a reviewer-specific report is explicitly implemented.

## Privacy Design

Fields should be classified:

### Low sensitivity

- aggregate counts;
- status counts;
- thematic axis counts;
- final modality counts.

### Moderate sensitivity

- submission title;
- author names;
- institutions;
- country/state.

### High sensitivity

- e-mails;
- reviewer names;
- review text;
- decision notes;
- internal committee notes.

High-sensitivity fields require privileged access and must be excluded from public or broad exports.

## Export Field Documentation

Create or update documentation such as:

```text
docs/reports-exports-and-indicators.md
```

It should list:

- available report pages;
- available exports;
- field definitions;
- permission rules;
- privacy notes;
- known limitations.

## Filtering Design

Filters should be simple and query-backed.

Recommended filters:

- status;
- thematic axis;
- modality;
- date range;
- institution;
- country/state;
- final-material status;
- proceedings status.

Exported data should reflect active filters where practical.

## Testing Strategy

Minimum tests:

1. reports dashboard requires authorization;
2. unauthorized users cannot download exports;
3. submission indicators count statuses correctly;
4. modality indicators count correctly;
5. proceedings readiness indicators count correctly;
6. CSV export has expected headers;
7. CSV export has expected rows;
8. XLSX export has expected sheets if implemented;
9. reviewer data is hidden from unauthorized roles;
10. protected file URLs are not present in exports.

## Future Integration

This change prepares data for:

- technical-scientific final report;
- post-event indicators;
- proceedings preparation;
- funding-agency reporting;
- internal committee monitoring.

It does not generate the final report document automatically.
