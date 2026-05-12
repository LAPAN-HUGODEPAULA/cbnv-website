# Tasks: Add Accounts, Profiles and Dashboards

## OpenSpec

- [x] Create `openspec/changes/add-accounts-profiles-and-dashboards/`.
- [x] Add `proposal.md`.
- [x] Add `design.md`.
- [x] Add `tasks.md`.
- [x] Add delta spec `specs/accounts/spec.md`.
- [x] Add delta spec `specs/dashboards/spec.md`.
- [x] Add delta spec `specs/security/spec.md`.
- [x] Add delta spec `specs/public-site/spec.md`.
- [x] Add delta spec `specs/submissions/spec.md`.
- [x] Add delta spec `specs/reviews/spec.md`.
- [x] Add delta spec `specs/qa/spec.md`.
- [x] Run `openspec validate add-accounts-profiles-and-dashboards --strict`.

## Pre-implementation audit

- [x] Confirm the project uses Django default `User`.
- [x] Review current `accounts.models`.
- [x] Review current `accounts.admin`.
- [x] Review current account-related URLs/views/forms/templates if any.
- [x] Confirm whether `UserProfile` already exists.
- [x] Confirm current profile fields.
- [x] Confirm current design-system form components.
- [x] Confirm `django-axes` login compatibility.

## UserProfile

- [x] Ensure `UserProfile` is linked one-to-one to Django default `User`.
- [x] Add or confirm institution field.
- [x] Add or confirm country field.
- [x] Add or confirm position/role field.
- [x] Add or confirm author flag.
- [x] Add or confirm reviewer flag.
- [x] Add or confirm chair/scientific committee flag.
- [x] Add or confirm privacy consent field if required.
- [x] Add or confirm image consent field if required.
- [x] Add timestamps if project convention uses them.
- [x] Register profile in Django Admin.
- [x] Add migrations if model changes are required.

## Registration

- [x] Implement registration form.
- [x] Collect first name.
- [x] Collect last name.
- [x] Collect e-mail.
- [x] Collect password using Django-safe password handling.
- [x] Collect profile metadata.
- [x] Create user.
- [x] Create/update profile.
- [x] Set author flag if public registration should create author accounts.
- [x] Prevent chair self-assignment.
- [x] Prevent unrestricted reviewer self-assignment unless deliberately approved.
- [x] Add success/error messages.
- [x] Add registration template.

## Authentication

- [x] Implement or wire login view.
- [x] Implement or wire logout view.
- [x] Add safe redirect handling.
- [x] Ensure CSRF protection.
- [x] Ensure login integrates with `django-axes`.
- [x] Consider password reset using Django defaults if feasible.
- [x] Add templates for auth views.

## Profile

- [x] Implement profile detail view.
- [x] Implement profile edit view.
- [x] Add profile form.
- [x] Prevent editing privileged flags through public profile form.
- [x] Show role status.
- [x] Show profile completion status if useful.
- [x] Add profile templates.

## Dashboard index

- [x] Implement `/dashboard/` or equivalent.
- [x] Require authentication.
- [x] Show available role dashboard cards.
- [x] Show no-role state if user has no role.
- [x] Show multiple roles if applicable.
- [x] Link to profile edit.
- [x] Use design-system components.

## Author dashboard shell

- [x] Implement author dashboard route/view.
- [x] Require author role.
- [x] Show future submissions placeholder.
- [x] Show submission workflow not yet implemented message.
- [x] Link to public Submissions page.
- [x] Do not implement submission creation.

## Reviewer dashboard shell

- [x] Implement reviewer dashboard route/view.
- [x] Require reviewer role.
- [x] Show future assigned reviews placeholder.
- [x] Show review workflow not yet implemented message.
- [x] Do not implement review assignments or forms.

## Chair dashboard shell

- [x] Implement chair dashboard route/view.
- [x] Require chair/scientific committee role.
- [x] Show future committee tools placeholder.
- [x] Do not implement decisions/review management.
- [x] Ensure public users cannot self-assign chair access.

## Authorization helpers

- [x] Implement helper/decorator/mixin for author access.
- [x] Implement helper/decorator/mixin for reviewer access.
- [x] Implement helper/decorator/mixin for chair access.
- [x] Handle missing profile safely.
- [x] Decide whether staff/superuser bypasses role checks and document it.

## Templates and UX

- [x] Use existing layout/design-system.
- [x] Ensure forms have labels.
- [x] Ensure errors are visible.
- [x] Ensure dashboard cards are responsive.
- [x] Use text-bearing role badges.
- [x] Use clear future-state/empty-state language.
- [x] Ensure keyboard navigation works.

## Tests

- [x] Test registration creates User.
- [x] Test registration creates UserProfile.
- [x] Test registration does not allow chair self-assignment.
- [x] Test login.
- [x] Test logout.
- [x] Test profile edit.
- [x] Test dashboard requires login.
- [x] Test author dashboard requires author role.
- [x] Test reviewer dashboard requires reviewer role.
- [x] Test chair dashboard requires chair role.
- [x] Test no-role dashboard state.
- [x] Test multi-role dashboard state if implemented.
- [x] Test missing profile handling.

## Documentation

- [x] Document account/profile behavior if needed.
- [x] Document role flags.
- [x] Document what this proposal intentionally does not implement.
- [x] Document integration points for submissions/reviews.

## Validation

- [x] Run `openspec validate add-accounts-profiles-and-dashboards --strict`.
- [x] Run `uv run python manage.py check`.
- [x] Run `uv run python manage.py makemigrations --check --dry-run`.
- [x] Run `uv run pytest`.
- [x] Run `npm run build` if templates/CSS changed.

## PR checklist

- [x] Branch is `change/add-accounts-profiles-and-dashboards`.
- [ ] PR title starts with `[add-accounts-profiles-and-dashboards]`.
- [ ] PR body includes `Closes #11`.
- [x] PR does not implement submissions.
- [x] PR does not implement review assignments/forms.
- [x] PR does not introduce custom user model.
- [x] PR includes authorization tests.
