# Tasks: Add Author Submission Initial Flow

## OpenSpec

- [x] Create `openspec/changes/add-author-submission-initial-flow/`.
- [x] Add `proposal.md`.
- [x] Add `design.md`.
- [x] Add `tasks.md`.
- [x] Add delta spec `specs/submissions/spec.md`.
- [x] Add delta spec `specs/accounts/spec.md`.
- [x] Add delta spec `specs/files/spec.md`.
- [x] Add delta spec `specs/notifications/spec.md`.
- [x] Add delta spec `specs/dashboards/spec.md`.
- [x] Add delta spec `specs/security/spec.md`.
- [x] Add delta spec `specs/qa/spec.md`.
- [x] Run `openspec validate add-author-submission-initial-flow --strict`.

## Pre-implementation audit

- [x] Review `submissions` app current files.
- [x] Review author dashboard implementation.
- [x] Review `UserProfile` role fields.
- [x] Review public Submissions page content.
- [x] Review settings for media/private file storage.
- [x] Decide submission status values.
- [x] Decide max PDF file size.
- [x] Decide thematic axis source/model/choices.
- [x] Decide draft support vs direct submission.

## Models

- [x] Implement `Submission`.
- [x] Add unique submission code.
- [x] Add owner/submitter relation.
- [x] Add title field.
- [x] Add abstract field.
- [x] Add keywords field or related model.
- [x] Add thematic axis/category.
- [x] Add presentation preference if needed.
- [x] Add status field.
- [x] Add created/updated/submitted timestamps.
- [x] Implement `SubmissionAuthor`.
- [x] Add ordered author support.
- [x] Add corresponding author flag.
- [x] Add presenting author flag if needed.
- [x] Implement `SubmissionFile`.
- [x] Add initial PDF file category.
- [x] Store original filename.
- [x] Store size/content type if feasible.
- [x] Add uploaded_by/uploaded_at.
- [x] Generate migrations.

## File handling

- [x] Define private/protected upload path.
- [x] Sanitize stored filenames.
- [x] Validate `.pdf` extension.
- [x] Validate file size.
- [x] Validate content type or PDF signature where practical.
- [x] Prevent video file upload in initial flow.
- [x] Do not expose direct public media URLs.
- [x] Implement protected file download/view if needed.
- [x] Test unauthorized file access.

## Forms

- [x] Implement submission form.
- [x] Implement author form/formset.
- [x] Implement file upload field.
- [x] Add field help texts.
- [x] Add no-video-in-initial-submission notice.
- [x] Add acknowledgement checkbox if needed.
- [x] Add field-level validation errors.
- [x] Ensure CSRF protection.

## Views and routes

- [x] Implement submission list for current user.
- [x] Implement create view.
- [x] Implement draft edit view if draft support exists.
- [x] Implement submit/finalize action.
- [x] Implement detail/status view.
- [x] Implement protected file download if files need direct author access.
- [x] Add URLs.
- [x] Ensure login required on all author submission views.

## Dashboard integration

- [x] Add submissions summary to author dashboard.
- [x] Add create submission CTA if submissions are open.
- [x] Add submissions closed/coming-soon state if not open.
- [x] List user's submissions.
- [x] Link to submission detail.
- [x] Avoid showing other users' submissions.

## Submission window/status

- [x] Determine source of submissions open/closed state.
- [x] Add setting/model/constant if needed.
- [x] Ensure public Submissions page and dashboard states are coherent.
- [x] Do not render broken CTAs when closed.

## Notifications

- [x] Implement confirmation e-mail helper.
- [x] Include submission code/title/timestamp.
- [x] Include no-video-at-initial-stage reminder.
- [x] Use configured default from e-mail.
- [x] Do not lose submission if e-mail fails.
- [x] Add tests with locmem backend.

## Admin

- [x] Register submission models in Django Admin.
- [x] Add list display/search/filter for submissions.
- [x] Add inline authors/files if useful.
- [x] Ensure admin does not expose unsafe file links.

## Security and permissions

- [x] Ensure only authenticated users create submissions.
- [x] Ensure owner-only detail access.
- [x] Ensure owner-only draft edit access.
- [x] Ensure owner-only file access.
- [x] Prevent IDOR through predictable IDs.
- [x] Ensure submitted records are read-only to author unless reopened.
- [x] Ensure role handling is explicit.

## Templates and UX

- [x] Use existing design system.
- [x] Add submission list template.
- [x] Add create/edit form template.
- [x] Add detail/status template.
- [x] Add success confirmation state.
- [x] Add empty state.
- [x] Ensure mobile layout works.
- [x] Ensure form errors are visible.

## Tests

- [x] Test login required for create/list/detail.
- [x] Test valid initial submission.
- [x] Test multiple ordered authors.
- [x] Test valid PDF upload.
- [x] Test non-PDF rejection.
- [x] Test oversized file rejection.
- [x] Test video is not accepted/required.
- [x] Test user cannot view another user's submission.
- [x] Test user cannot download another user's file.
- [x] Test dashboard lists own submissions only.
- [x] Test confirmation e-mail sent.
- [x] Test submitted submission read-only behavior.
- [x] Test admin/model string representations where useful.

## Documentation

- [x] Document submission workflow boundary.
- [x] Document file upload rules.
- [x] Document no-video initial phase rule.
- [x] Document statuses.
- [x] Document future integration points for review/final materials.

## Validation

- [x] Run `openspec validate add-author-submission-initial-flow --strict`.
- [x] Run `uv run python manage.py check`.
- [x] Run `uv run python manage.py makemigrations --check --dry-run`.
- [x] Run `uv run pytest`.
- [x] Run `npm run build` if templates/CSS changed.

## PR checklist

- [ ] Branch is `change/add-author-submission-initial-flow`.
- [ ] PR title starts with `[add-author-submission-initial-flow]`.
- [ ] PR body includes `Closes #12`.
- [ ] PR does not implement review workflow.
- [ ] PR does not collect video.
- [ ] PR protects uploaded files.
- [ ] PR includes tests for permission and file validation.
