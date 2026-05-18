# Proposal: Add Reports, Exports and Indicators

## Change ID

`add-reports-exports-and-indicators`

## Linked issue

GitHub issue: `OpenSpec: add reports, exports and indicators`  
Expected issue number: `#15`

## Problem

The platform now has the major operational workflows for public pages, accounts, submissions, review/decision handling, final materials, proceedings and video links. The scientific committee still needs structured ways to monitor the event workflow, export operational data, prepare technical-scientific reports and generate proceedings-support datasets.

Without reports, exports and indicators, the committee must inspect individual records manually. That creates risk of inconsistent counts, missed submissions, delayed proceedings preparation, poor transparency about workflow status and fragile manual spreadsheets.

## Proposed Change

Implement committee-facing reports, CSV/XLSX exports and indicators for the CBNV platform.

The implementation must provide:

1. dashboard indicators for submissions, authors, institutions, reviews, decisions, final modalities and proceedings readiness;
2. CSV exports for submissions, authors, institutions, review/decision summaries and proceedings-support data;
3. XLSX exports when dependency support exists or can be added safely;
4. role-protected report/export views;
5. privacy-aware export behavior;
6. reusable services/query helpers for indicators and exports;
7. tests for permissions, export structure and indicator counts.

## Goals

1. Allow chair/scientific committee users to export core operational data.
2. Provide indicators by status, thematic axis, modality, institution, geography and workflow stage.
3. Provide review/decision exports according to permissions.
4. Provide proceedings-support exports for accepted/published work.
5. Provide author and institution exports.
6. Add report cards or dashboards for committee monitoring.
7. Keep exports deterministic and documented.
8. Avoid exposing private files or sensitive review details to unauthorized users.
9. Support CSV and XLSX when practical.
10. Prepare structured data for the technical-scientific report after the event.

## Non-goals

This change MUST NOT:

1. implement a business intelligence platform;
2. implement arbitrary custom report builders;
3. implement public analytics dashboards;
4. expose personal data publicly;
5. expose reviewer identities or review content without explicit permission rules;
6. replace the proceedings pages;
7. implement certificates, check-in or QR-code reports;
8. integrate with external registration platforms;
9. export protected files in bulk;
10. implement automated e-mail distribution of reports;
11. implement advanced charts unless low-complexity and already supported by the UI.

## Scope

In scope:

- committee report index;
- dashboard indicators;
- CSV exports;
- XLSX exports if dependency/support exists;
- submissions export;
- authors export;
- institutions export;
- reviews/decisions export with permission controls;
- proceedings-support export;
- final materials readiness export;
- filters for status, thematic axis, modality and date range;
- tests for exports and indicators;
- documentation of fields and privacy behavior.

Out of scope:

- public statistics pages;
- external analytics;
- automatic report submission to funding agencies;
- automatic proceedings PDF generation;
- direct protected-file ZIP exports;
- payment/certificate/check-in exports.

## Report Areas

### Operational overview

The committee dashboard must show counts for:

- total submissions;
- submissions by status;
- submissions by thematic axis;
- submissions by final modality;
- pending reviews;
- completed reviews;
- decisions issued;
- accepted submissions;
- final materials pending;
- final materials received;
- ready for proceedings;
- published in proceedings.

### Author and institution overview

The reports must support indicators for:

- total submitting authors;
- total coauthors if data is available;
- institutions;
- state;
- country;
- thematic axis by institution/geography if feasible.

### Review and decision overview

The reports must support committee-only indicators for:

- assignments by status;
- pending reviews;
- completed reviews;
- decision counts;
- accepted/rejected/revision outcomes;
- reviewer workload if reviewer identity export is permitted.

### Proceedings and final materials overview

The reports must support indicators for:

- accepted works by modality;
- materials requested;
- materials received;
- materials validated;
- missing publication authorization;
- ready for proceedings;
- published in proceedings;
- works with video URL;
- works promoted to public video gallery.

## Export Requirements

### Submissions export

Must include, subject to permission:

- submission code;
- title;
- thematic axis;
- status;
- final modality;
- submitter;
- corresponding author;
- created/submitted timestamps;
- decision status if available;
- final-material/proceedings status if available.

### Authors export

Must include:

- submission code;
- author order;
- full name;
- e-mail where permitted;
- institution;
- country/state/city if available;
- corresponding author flag;
- presenting author flag.

### Institutions export

Must include:

- institution name;
- count of submissions;
- count of authors;
- state/country if available;
- thematic-axis breakdown if feasible.

### Review/decision export

Must include only data allowed by the current user role.

Potential fields:

- submission code;
- assignment status;
- review status;
- decision status;
- final modality;
- timestamps;
- reviewer identity only when the exporter has chair/scientific committee permission.

### Proceedings export

Must include:

- submission code;
- title;
- authors;
- affiliations;
- abstract;
- keywords;
- thematic axis;
- final modality;
- publication authorization status;
- final material validation status;
- video URL if present and permitted;
- proceedings publication status.

## Format Requirements

CSV exports must use UTF-8 encoding.

XLSX exports must use deterministic sheet names and column order.

Recommended sheet names:

```text
Submissions
Authors
Institutions
Reviews
Proceedings
```

If XLSX implementation is not feasible in this change, CSV must still be implemented and the XLSX limitation must be documented.

## Filters

Report/export views should support practical filters:

- status;
- thematic axis;
- final modality;
- date range;
- institution;
- country/state if available;
- proceedings readiness;
- final material validation status.

Filters must be applied consistently between visible indicators and corresponding exports where practical.

## Access Control

Reports and exports are internal tools.

Default rule:

- chair/scientific committee users can access full reports and exports;
- staff/superusers may access reports if project convention allows;
- authors cannot access global reports;
- reviewers cannot access global exports unless a restricted reviewer-specific export/report is explicitly defined.

Sensitive data must require privileged access.

## Privacy and Data Minimization

The implementation must document and enforce privacy boundaries.

1. Protected files must not be exported.
2. Personal data must only be included in internal privileged exports.
3. Reviewer identities and review text must not be exposed in exports for unauthorized users.
4. Public proceedings data must only include publication-approved content.
5. Exports should include only fields needed for committee operations and reports.

## Implementation Strategy

1. Implement service/query functions for indicators.
2. Implement export builders separate from views.
3. Implement role-protected report views.
4. Add a committee report index/dashboard.
5. Add CSV exports first.
6. Add XLSX exports if dependency/support exists.
7. Add deterministic tests for export columns and counts.
8. Document export fields and permission rules.

Recommended structure:

```text
reports/
  services.py
  exports.py
  views.py
  urls.py
  tests/
templates/
  reports/
    index.html
    indicators.html
```

If the project has another app convention, adapt to that convention while preserving separation between query, export and view logic.

## Acceptance Criteria

1. Chair/scientific committee users can access a reports dashboard.
2. Unauthorized users cannot access reports or exports.
3. Submission indicators are available by status, thematic axis and modality.
4. Review/decision indicators are available to privileged users.
5. Final-material/proceedings indicators are available.
6. CSV exports exist for submissions, authors, institutions and proceedings.
7. Review/decision exports exist with permission controls.
8. XLSX exports exist if dependency support is available, or the limitation is documented.
9. Export columns are deterministic.
10. Exports use UTF-8 for CSV.
11. Exports do not expose protected files.
12. Exports do not expose reviewer identities or review text to unauthorized users.
13. Indicators and exports are covered by tests.
14. The chair dashboard links to reports/exports if appropriate.
15. Validation passes:

```bash
openspec validate add-reports-exports-and-indicators --strict
uv run python manage.py check
uv run python manage.py makemigrations --check --dry-run
uv run pytest
```
