## 1. Setup and Apps

- [x] 1.1 Create `submissions` and `notifications` Django apps (scaffolding exists — populate models, views, templates).
- [x] 1.2 Register apps in `settings/base.py` (already registered).

## 2. Models and Migrations

- [x] 2.1 Implement `ThematicAxis` Wagtail Snippet with `name` and `order` fields.
- [x] 2.2 Implement `Submission` model with full 13-state state machine, `submission_id` auto-generation, and manual transition methods.
- [x] 2.3 Implement `SubmissionAuthor` model with `first_name`, `last_name`, `email`, `institution`, `order`, `is_corresponding`.
- [x] 2.4 Implement `SubmissionFile` model with protected storage FileField.
- [x] 2.5 Create and run migrations for the new models.
- [x] 2.6 Create default fixture for ThematicAxis (Neurociência da Visão, Oftalmologia Clínica, Ergonomia Visual, Tecnologia Assistiva).

## 3. Secure Storage Configuration

- [x] 3.1 Configure `PROTECTED_MEDIA_ROOT` and `PROTECTED_MEDIA_STORAGE` in settings.
- [x] 3.2 Update `SubmissionFile` to use the protected storage backend.
- [x] 3.3 Create a Django view to serve files securely with permission checks (submitter only in Phase 1).
- [x] 3.4 Configure URL routes for the secure file download.

## 4. Author Dashboard and Permissions

- [x] 4.1 Add `has_complete_author_profile()` property to `accounts.User` checking `first_name`, `last_name`, `institution`, `country`.
- [x] 4.2 Implement the Author Dashboard view listing user's submissions with Portuguese status labels.
- [x] 4.3 Create the dashboard template using the project's layout shell.
- [x] 4.4 Add permission decorators/mixins to restrict submission views to authors with complete profiles.

## 5. Submission Wizard (3 Steps)

- [x] 5.1 Create forms for Step 1 (metadata + authors), Step 2 (PDF upload), Step 3 (review & confirm).
- [x] 5.2 Implement the 3-step wizard with HTMX for dynamic author row addition/removal.
- [x] 5.3 Add validation for keywords count (3–5) and abstract length (max 2500 chars).
- [x] 5.4 Implement the PDF upload field with file type (.pdf only) and size (max 10MB) validation.
- [x] 5.5 Implement auto-save draft to database on step transitions.
- [x] 5.6 Implement the final submit action (draft → submitted transition) and trigger confirmation email.

## 6. Notifications and Emails

- [x] 6.1 Implement the notification service to send emails (Portuguese Brazilian).
- [x] 6.2 Create the submission confirmation email template with title, submission ID, and next steps.
- [x] 6.3 Trigger the confirmation email on submission status transition to `SUBMITTED`.

## 7. Verification and Tests

- [x] 7.1 Add tests for submission draft creation and status transitions (including invalid transition rejection).
- [x] 7.2 Add tests for metadata validation (keywords 3–5, abstract max 2500).
- [x] 7.3 Add tests for secure file storage (verify direct URL access fails, permission-gated download works).
- [x] 7.4 Add tests for author permissions and dashboard access (including incomplete profile redirect).
- [x] 7.5 Add tests for automated email notification triggering.
- [x] 7.6 Add tests for ThematicAxis snippet creation and ordering.
