## ADDED Requirements

### Requirement: Submission model and metadata
The system SHALL provide a model for scientific submissions including a human-readable submission ID (auto-generated, e.g. `CBNV-2026-0001`), title, abstract (max 2500 characters), keywords (3 to 5), and thematic axis (FK to admin-editable ThematicAxis Snippet).

#### Scenario: Metadata validation
- **WHEN** an author submits a work with less than 3 keywords
- **THEN** the system SHALL return a validation error

#### Scenario: Submission ID generation
- **WHEN** a new submission is created
- **THEN** the system SHALL assign a unique submission ID in the format `CBNV-2026-NNNN`

### Requirement: Author and affiliation tracking
The system SHALL allow adding multiple authors to a submission, each with their `first_name`, `last_name`, `email`, and `institution`. The submitting user SHALL be automatically added as the first author with `is_corresponding=True`.

#### Scenario: Adding multiple authors
- **WHEN** an author adds a second author to the submission
- **THEN** both authors SHALL be persisted and associated with the work

#### Scenario: Submitting author auto-populated
- **WHEN** a logged-in author starts a new submission
- **THEN** their first name, last name, email, and institution SHALL be pre-filled as the first (corresponding) author

### Requirement: Thematic axis selection (admin-editable)
Thematic axes SHALL be managed as a Wagtail Snippet (`ThematicAxis`) with `name` and `order` fields, editable by admin users without code deployment. The system SHALL ship with a default fixture: "Neurociência da Visão", "Oftalmologia Clínica", "Ergonomia Visual", "Tecnologia Assistiva".

#### Scenario: Admin adds a new thematic axis
- **WHEN** an admin user creates a new ThematicAxis via the Wagtail admin
- **THEN** that axis SHALL be available in the submission form without any code changes or server restart

#### Scenario: Axis ordering
- **WHEN** thematic axes are displayed in the submission form
- **THEN** they SHALL appear in the order defined by the `order` field

### Requirement: Phase 1 PDF upload
Phase 1 of the submission process SHALL require a single PDF file containing the work for evaluation. Video links SHALL NOT be required at this stage.

#### Scenario: PDF upload in Phase 1
- **WHEN** an author uploads a valid PDF file during Phase 1
- **THEN** the file SHALL be stored securely and associated with the submission

#### Scenario: File validation
- **WHEN** an author attempts to upload a non-PDF file or a file exceeding 10MB
- **THEN** the system SHALL return a validation error

### Requirement: SubmissionFile model
The system SHALL use a separate `SubmissionFile` model linked to `Submission` via ForeignKey, storing the uploaded PDF. This separation supports future versioning (e.g., final materials in Phase 3).

#### Scenario: File association
- **WHEN** an author uploads a PDF
- **THEN** a `SubmissionFile` record SHALL be created linking the file to the submission

### Requirement: Full submission state machine
The system SHALL define all 13 submission states: `draft`, `submitted`, `admin_screening`, `assigned_to_reviewers`, `under_review`, `reviews_completed`, `decision_pending`, `accepted_oral`, `accepted_poster`, `accepted_video`, `rejected`, `final_materials_pending`, `ready_for_proceedings`, `published_in_proceedings`. State transitions SHALL be enforced via methods on the `Submission` model that validate the current status before allowing a transition. No external FSM library SHALL be used.

#### Scenario: Phase 1 transition only
- **WHEN** an author is working on a submission during Phase 1
- **THEN** the only available transitions SHALL be `draft → submitted` and `submitted → draft` (withdrawal)

#### Scenario: Invalid transition blocked
- **WHEN** code attempts to transition a submission from `draft` directly to `admin_screening`
- **THEN** the transition method SHALL raise an `IllegalStateTransition` error or similar

### Requirement: Author Dashboard
Authors SHALL have a dedicated dashboard to view their submissions, check their status, and edit drafts. Status labels SHALL be displayed in simple Portuguese (e.g., "Rascunho", "Enviado", "Em avaliação", "Aprovado — Oral", "Rejeitado").

#### Scenario: Viewing submissions
- **WHEN** a logged-in author accesses the dashboard
- **THEN** they SHALL see a list of all their works with current status label and submission ID

#### Scenario: Edit draft
- **WHEN** an author clicks "Edit" on a submission with status `draft`
- **THEN** they SHALL be taken to the submission wizard pre-filled with their data

#### Scenario: Cannot edit submitted
- **WHEN** an author views a submission with status other than `draft`
- **THEN** no "Edit" action SHALL be available

### Requirement: Submission wizard (3 steps)
The submission process SHALL use a 3-step wizard:

- **Step 1 — Metadata + Authors:** Title, abstract, keywords, thematic axis. Authors section with submitting author auto-filled and HTMX-powered "Add co-author" button for inline row insertion.
- **Step 2 — Upload PDF:** Drag-and-drop or click upload. PDF only, max 10MB. Draft is auto-saved to the database.
- **Step 3 — Review & Confirm:** Read-only summary of metadata, author list, PDF filename/size. "Back" and "Submit Work" buttons.

#### Scenario: Dynamic author addition
- **WHEN** an author clicks "Add co-author" in Step 1
- **THEN** a new author row SHALL appear inline via HTMX without a full page reload

#### Scenario: Auto-save between steps
- **WHEN** an author navigates from Step 1 to Step 2
- **THEN** the submission draft SHALL be saved to the database automatically

### Requirement: Author-facing status labels
The system SHALL map internal state machine states to simple Portuguese labels for display to authors. Authors SHALL NOT see internal state names.

| Internal State | Display Label |
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
