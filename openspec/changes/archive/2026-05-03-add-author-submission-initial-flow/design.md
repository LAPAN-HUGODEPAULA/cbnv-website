## Context

The platform currently has a custom user model (`accounts.User`) with role flags (`is_author`, `is_reviewer`, `is_chair`) and auth decorators (`@author_required`, `@reviewer_required`, `@chair_required`). The `submissions` and `notifications` apps exist as scaffolding but have no models or logic. This design establishes the foundations for the scientific workflow, starting with Phase 1 author-facing features.

## Goals / Non-Goals

**Goals:**
- Define the complete submission state machine (13 states) and implement Phase 1 transitions.
- Implement the Phase 1 submission workflow (metadata + PDF) via a 3-step wizard.
- Establish a secure storage mechanism for submission files.
- Create an Author Dashboard.
- Implement automated email notifications for submission receipts.
- Provide admin-editable thematic axes via Wagtail Snippet.

**Non-Goals:**
- Implementation of the peer review process (Proposal 08).
- Final material submission (Proposal 09).
- Payment processing or certificate generation.
- Public display of submitted works.

## Decisions

### 1. Data Model: Submission and Related Entities

We will implement the following models in the `submissions` app:

- **`ThematicAxis`** (Wagtail Snippet): `name` (CharField), `order` (PositiveIntegerField). Admin-editable; no code deploy needed to add/remove/reorder axes.
- **`Submission`**: Main entry representing a scientific work. Fields: `submission_id` (auto-generated, e.g. `CBNV-2026-0001`), `title`, `abstract` (TextField, max 2500 chars), `keywords` (JSONField or comma-separated), `thematic_axis` (FK to `ThematicAxis`), `status` (CharField with 13 choices), `submitter` (FK to `accounts.User`), `created_at`, `updated_at`.
- **`SubmissionAuthor`**: Links authors to a submission. Fields: `first_name`, `last_name`, `email`, `institution`, `order` (PositiveIntegerField), `is_corresponding` (BooleanField). The submitting user is auto-added as the first author with `is_corresponding=True`.
- **`SubmissionFile`**: Represents the uploaded PDF. Fields: `submission` (FK to Submission), `file` (FileField using protected storage), `uploaded_at`. Separate model for future versioning (final materials in Phase 3).

**Rationale:** Separating authors from the Django `User` model allows for co-authors who may not have accounts. `SubmissionFile` as a separate model enables future versioning without schema changes.

### 2. Submission State Machine (Full)

All 13 states are defined now. Phase 1 only exposes `draft → submitted`. Future proposals unlock subsequent transitions.

```
draft
  │
  ▼
submitted
  │
  ▼
admin_screening
  │
  ▼
assigned_to_reviewers
  │
  ▼
under_review
  │
  ▼
reviews_completed
  │
  ▼
decision_pending
  │
  ├──▶ accepted_oral
  ├──▶ accepted_poster
  ├──▶ accepted_video
  └──▶ rejected
        │
        ▼ (accepted branches only)
  final_materials_pending
        │
        ▼
  ready_for_proceedings
        │
        ▼
  published_in_proceedings
```

**Implementation:** Manual state transitions via methods on the `Submission` model (e.g., `submit()`, `withdraw_to_draft()`). Each method validates that the current status allows the transition. No `django-fsm` dependency.

**Rationale:** Defining all states from the start avoids data migrations when future phases insert intermediate states. Manual transitions are transparent and avoid adding `django-fsm` as a dependency for what is ultimately a simple state map.

**Author-facing status labels (simple Portuguese):**

| Internal State | Author Label |
|---|---|
| draft | Rascunho |
| submitted | Enviado |
| admin_screening | Em triagem |
| assigned_to_reviewers | Em avaliação |
| under_review | Em avaliação |
| reviews_completed | Em avaliação |
| decision_pending | Em avaliação |
| accepted_oral | Aprovado — Oral |
| accepted_poster | Aprovado — Pôster |
| accepted_video | Aprovado — Vídeo |
| rejected | Rejeitado |
| final_materials_pending | Materiais finais pendentes |
| ready_for_proceedings | Pronto para anais |
| published_in_proceedings | Publicado nos anais |

### 3. Secure Storage Strategy

Files will be stored using a dedicated `FileSystemStorage` pointing to a directory outside the static/media public serve path (`PROTECTED_MEDIA_ROOT`). Access is mediated by a Django view using `FileResponse` with permission checks (submitter only in Phase 1).

**Rationale:** Direct URL access to sensitive scientific work must be prevented before official publication/proceedings.

### 4. Author Profile Completeness

Before starting a submission, the author's profile must be complete. The check is: `first_name`, `last_name`, `institution`, and `country` must all be non-blank. Implemented as a `has_complete_author_profile()` property on `accounts.User`.

If incomplete, the author is redirected to the profile edit page with a message.

### 5. Submission Wizard (3 Steps)

A 3-step wizard using HTMX for dynamic interactions:

- **Step 1 — Metadata + Authors:** Title, abstract, keywords (3–5), thematic axis. Authors section: submitting author auto-filled, HTMX "Add co-author" button inserts rows inline. Each co-author row: first_name, last_name, email, institution, remove button.
- **Step 2 — Upload PDF:** Drag-and-drop or click to upload. Validation: PDF only, max 10MB. Auto-save draft to database.
- **Step 3 — Review & Confirm:** Read-only summary of all metadata, author list, and PDF filename/size. "Back" and "Submit Work" buttons.

**Rationale:** 3 steps is the minimum that separates concerns without unnecessary page loads. HTMX handles dynamic author rows without full-page reloads. Auto-save on step transitions prevents data loss.

### 6. Thematic Axes as Wagtail Snippet

Admin-editable via Wagtail admin. Default fixture seeds the initial axes:
- Neurociência da Visão
- Oftalmologia Clínica
- Ergonomia Visual
- Tecnologia Assistiva

**Rationale:** Organizers may want to add, remove, or rename axes without a code deploy. A Wagtail Snippet provides this flexibility with minimal effort.

### 7. Automated Notifications

Django's built-in `send_mail` with background task (using `django-q2` or simple threading if volume is low). Templates stored in `notifications/templates/notifications/email/`.

**Rationale:** Providing immediate feedback to authors is critical. Email includes submission title, submission ID, and next steps.

## Risks / Trade-offs

- **[Risk]** Heavy file uploads slowing down the app → **Mitigation**: Client-side validation, 10MB limit, standard SSR upload is sufficient for this volume.
- **[Risk]** Data loss during multi-step submission → **Mitigation**: Auto-save draft to the database after each wizard step.
- **[Trade-off]** Full state machine adds complexity now → **Mitigation**: Phase 1 only exposes `draft → submitted`; remaining transitions are unlocked by future proposals.
- **[Trade-off]** `SubmissionFile` as separate model adds a join → **Mitigation**: Necessary for Phase 3 versioning; minimal overhead with indexed FK.
