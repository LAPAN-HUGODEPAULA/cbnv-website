# Proposal: Add Author Submission Initial Flow

## Change ID

`add-author-submission-initial-flow`

## Linked issue

GitHub issue: `OpenSpec: add author submission initial flow`  
Expected issue number: `#12`

## Problem

The platform now has public pages, account/profile infrastructure and dashboard shells. The next workflow boundary is the initial author submission flow.

CBNV 2026 uses a two-phase submission process. The first phase collects scientific submission metadata and the initial manuscript/abstract file. Video is not required in this first phase. Video links or final materials are only relevant after approval, in a later final-materials/proceedings workflow.

Without this proposal, authors can authenticate but cannot submit work, track initial submission status, or receive confirmation. Later review and decision workflows also need a stable submission data model and state machine to build on.

## Proposed Change

Implement the first phase of the scientific submission workflow for authenticated authors.

This change creates submission models, author/affiliation metadata, secure initial PDF upload, submission form views, status tracking and confirmation notification. It integrates with the existing author dashboard but does not implement review assignments, decisions, final materials, proceedings or video submission.

## Goals

1. Allow authenticated authors to create an initial scientific submission.
2. Store submission metadata, authors and affiliations.
3. Allow upload of the initial PDF file.
4. Validate uploaded file type and size.
5. Keep uploaded files private and protected from direct public access.
6. Implement initial submission states.
7. Allow authors to view their own submissions and status.
8. Send confirmation e-mail after successful submission when e-mail is configured.
9. Provide clear operational copy that video is not required in the initial phase.
10. Prepare a stable foundation for `add-review-decision-workflow`.

## Non-goals

This change SHALL NOT:

1. implement reviewer assignment;
2. implement review forms;
3. implement decision workflow;
4. implement final PDF/poster/video material submission;
5. collect video files or video links;
6. publish proceedings;
7. implement payment, certificates or QR/check-in;
8. implement anonymous peer review unless separately specified;
9. implement advanced conflict-of-interest logic;
10. implement full chair management beyond basic visibility/status support needed for submissions.

## Prerequisites

This change assumes the following proposals are complete:

1. `stabilize-platform-foundation`
2. `add-accounts-profiles-and-dashboards`
3. relevant public-site/content proposals for submission information pages

The implementation should integrate with the existing author dashboard from `add-accounts-profiles-and-dashboards`.

## Data Model Scope

### Submission

The `Submission` model SHOULD include:

- owner/submitter user;
- title;
- abstract;
- keywords;
- thematic axis/category;
- presentation preference if applicable;
- status;
- created timestamp;
- updated timestamp;
- submitted timestamp;
- unique public/internal code;
- optional notes to authors or admin-only notes if already needed.

Recommended status values:

- `draft`
- `submitted`
- `withdrawn`

Optionally, include early administrative statuses only if needed for immediate operation:

- `under_admin_check`
- `requires_correction`

Review/decision statuses such as accepted/rejected belong to the later review workflow.

### SubmissionAuthor

The `SubmissionAuthor` model SHOULD include:

- submission relation;
- full name;
- e-mail;
- institution;
- department/program if needed;
- city/state/country if needed;
- ORCID if useful;
- order;
- corresponding author flag;
- presenting author flag;
- relation to registered user if applicable.

At minimum, the submission must support multiple authors and ordered display.

### SubmissionFile

The `SubmissionFile` model SHOULD include:

- submission relation;
- file;
- file type/category;
- original filename;
- content type if captured;
- file size;
- checksum if feasible;
- uploaded by;
- uploaded timestamp;
- active/current flag if multiple uploads are allowed.

Initial allowed file category:

- `initial_pdf`

This proposal SHALL NOT add video file or video link category.

## Workflow

### Create draft

An authenticated author opens the submission form and creates or saves a draft if draft support is implemented.

Draft support is recommended but not mandatory if the form is simple. If draft support is implemented, validation may be less strict until final submit.

### Submit

On final submission:

1. user must be authenticated;
2. user must have or receive author role/profile flag;
3. required metadata must be present;
4. at least one author must be present;
5. initial PDF must be uploaded;
6. file validation must pass;
7. status becomes `submitted`;
8. submitted timestamp is set;
9. confirmation message is shown;
10. confirmation e-mail is sent if configured.

### Edit after submission

Default rule:

- submitted records are read-only to authors unless reopened by later workflow/admin.

If editing after submission is allowed, it must be explicitly documented. For MVP, prefer read-only after submission.

### Withdraw

This proposal MAY implement withdrawal if simple. If implemented:

- only submitter/owner can withdraw;
- withdrawn submissions are not available for review later;
- withdrawal is timestamped or logged if possible.

If not implemented, mark as future.

## File Upload Requirements

1. Only PDF files are accepted for initial submission.
2. Video files are not accepted.
3. Video links are not collected in this phase.
4. Max file size must be configured.
5. File name should be sanitized.
6. Uploaded files must not be served as public media URLs.
7. File storage path should avoid exposing user names or predictable sensitive information where practical.
8. Authors should only access files belonging to their own submissions.
9. Staff/chair access can be deferred or implemented minimally if required for admin.

## Dashboard Integration

The author dashboard SHOULD show:

- create new submission link if submissions are open;
- list of the user's submissions;
- submission code/title/status/submitted date;
- link to detail page;
- clear message if submissions are not open;
- clear statement that video is not part of initial submission.

The account dashboard should not duplicate full submission logic. Submission list/detail should live in submissions views or templates.

## Access Control

Rules:

1. only authenticated users can create submissions;
2. only submission owner can edit draft;
3. only submission owner can view their submission detail;
4. users cannot access other authors' uploaded files;
5. users without author role should either be granted author role on first submission or redirected to complete profile/role selection;
6. chair/staff access to all submissions can be deferred unless needed for basic admin.

## Submission Window

The system SHOULD support an open/closed submission state.

Implementation options:

1. settings-based submission status in CMS/global settings;
2. submissions app setting/model;
3. environment or configuration flag for MVP.

The public Submissions page and author dashboard should agree on status. If no formal submission window model exists yet, implement a simple setting or documented placeholder without overengineering.

## Notifications

On successful submission, the system SHOULD send confirmation e-mail if e-mail backend is configured.

E-mail should include:

- submission code;
- title;
- submitted timestamp;
- confirmation that initial submission was received;
- reminder that video is not required at this stage;
- next-step language that review/decision will be communicated later.

If e-mail is not configured, the system must still show in-app success confirmation and not fail the submission transaction.

## Admin

Use Django Admin and/or Wagtail admin snippets if appropriate.

Minimum admin needs:

- list submissions;
- search title/code/author;
- filter by status;
- inspect metadata;
- inspect author list;
- inspect uploaded file reference safely.

Full chair review workflow belongs later.

## UX Requirements

1. Form labels must be clear.
2. Required fields must be indicated.
3. Errors must be field-specific where possible.
4. File-upload errors must explain accepted format and size.
5. The workflow must clearly state that video is not required initially.
6. Users should be able to return to dashboard after submission.
7. Empty states must be clear.
8. Mobile layout must be usable.

## Security and Privacy

1. Use CSRF protection.
2. Require login for all author submission views.
3. Protect uploaded files.
4. Validate file extension and content type as far as practical.
5. Avoid trusting client-provided content type alone.
6. Do not expose uploaded files in public pages.
7. Avoid leaking other authors' submissions through predictable IDs.
8. Use permission checks on detail/download views.
9. Keep personal data handling aligned with profile privacy consent.

## Acceptance Criteria

1. Authenticated authors can create an initial submission.
2. Submission stores title, abstract, keywords, thematic axis/category and status.
3. Submission supports multiple ordered authors.
4. Author can upload an initial PDF file.
5. Non-PDF uploads are rejected.
6. Oversized files are rejected according to configured limit.
7. Video files and video links are not part of the initial flow.
8. Uploaded files are not publicly accessible by direct public media URLs.
9. Author dashboard lists the user's submissions.
10. Authors cannot view or modify other users' submissions.
11. Successful submission shows confirmation and sends e-mail if configured.
12. Submitted records are read-only to authors unless explicitly reopened.
13. The change passes:
    - `openspec validate add-author-submission-initial-flow --strict`
    - `uv run python manage.py check`
    - `uv run python manage.py makemigrations --check --dry-run`
    - `uv run pytest`
14. No review/decision/final-materials workflow is implemented.
