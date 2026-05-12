# Proposal: Add Accounts, Profiles and Dashboards

## Change ID

`add-accounts-profiles-and-dashboards`

## Linked issue

GitHub issue: `OpenSpec: add accounts, profiles and dashboards`
Expected issue number: `#11`

## Problem

The public website now has a coherent public-facing layer. The next major system boundary is authentication and role-aware internal areas for authors, reviewers and the scientific committee/chair.

The project needs account creation, login/logout, profile metadata and dashboard shells before implementing the actual submission and review workflows. Without this foundation, subsequent changes such as `add-author-submission-initial-flow` and `add-review-decision-workflow` would either duplicate access logic or mix workflow implementation with authentication concerns.

This proposal implements the account/profile/dashboard foundation only. It must not implement the full submission or review workflows.

## Proposed Change

Implement authentication and base internal dashboard areas using Django's default `User` model plus the project `UserProfile` model.

The change should provide:

1. public registration and authentication views;
2. profile creation/editing;
3. congress-specific profile metadata;
4. role flags for author, reviewer and chair/scientific committee;
5. simple role-aware dashboard routing;
6. dashboard shell pages for author, reviewer and chair;
7. authorization tests.

This change prepares the platform for scientific workflows but does not implement those workflows.

## Architectural Decision

The platform SHALL continue using Django's default `User` model for authentication.

This change SHALL NOT introduce a custom user model.

Congress-specific metadata SHALL live in `accounts.UserProfile` or equivalent profile model linked one-to-one to Django's default `User`.

The system MAY present e-mail as the public-facing login identifier if already implemented or chosen, but it must not require a custom `AUTH_USER_MODEL`.

## Goals

1. Allow users to register, authenticate and log out.
2. Allow users to view and edit profile metadata.
3. Store congress-specific metadata in profile fields.
4. Support independent scientific role flags:
   - author;
   - reviewer;
   - chair/scientific committee.
5. Provide a role-aware dashboard entry point.
6. Provide dashboard shells for each role.
7. Prevent users from accessing dashboards they are not authorized to access.
8. Keep implementation simple and compatible with later submission/review changes.
9. Avoid complex RBAC/editorial permission systems.

## Non-goals

This change SHALL NOT:

1. implement the submission form workflow;
2. implement file uploads for submissions;
3. implement review assignments;
4. implement review forms;
5. implement scientific decisions;
6. implement final materials/proceedings;
7. implement payment, certificates or QR-code functionality;
8. implement complex RBAC;
9. implement organization-level permissions;
10. implement social login;
11. implement external identity provider integration;
12. implement staff/Wagtail editorial workflows beyond the existing admin.

## Scope

In scope:

- registration form;
- login/logout views if not already provided;
- password reset integration if feasible using Django defaults;
- profile view/edit form;
- profile metadata fields already approved by foundation;
- simple dashboard landing page;
- author dashboard shell;
- reviewer dashboard shell;
- chair/scientific committee dashboard shell;
- access decorators/mixins/helpers;
- tests for authentication and authorization;
- templates using existing design system.

Out of scope:

- actual submission creation;
- review/decision domain workflows;
- export/reporting;
- external registration platform integration;
- granular permission matrix;
- Wagtail editorial permissions.

## Profile Model Requirements

The profile model SHOULD support, at minimum:

- user one-to-one relation;
- institution;
- country;
- position/role;
- optional ORCID or academic identifier if already planned;
- consent/privacy fields if already present or required;
- author flag;
- reviewer flag;
- chair/scientific committee flag;
- timestamps if project conventions support them.

If the existing `UserProfile` model already differs slightly, this proposal should adapt to the implemented foundation rather than introduce unnecessary churn.

## Role Model

Roles are profile flags, not a complex permission system.

A user MAY have more than one role. Examples:

- author only;
- reviewer only;
- author and reviewer;
- chair and reviewer;
- chair, reviewer and author.

Dashboard access rules should use these flags.

## Dashboard Requirements

### Dashboard index

The main dashboard entry point SHOULD route the user to available role areas or show a role selector when multiple roles are active.

### Author dashboard shell

The author dashboard shell SHOULD show:

- profile completion status;
- future submissions area placeholder;
- submission status placeholder;
- link to Submissions public page;
- clear message when submission workflow is not yet implemented.

It SHALL NOT implement actual submission creation in this change.

### Reviewer dashboard shell

The reviewer dashboard shell SHOULD show:

- reviewer status;
- future assigned reviews placeholder;
- conflict-of-interest placeholder if useful;
- clear message when review workflow is not yet implemented.

It SHALL NOT implement review assignments or review forms.

### Chair/scientific committee dashboard shell

The chair dashboard shell SHOULD show:

- committee role status;
- future administrative/scientific workflow placeholder;
- links to public program/submissions/admin resources if appropriate;
- clear message that full review workflow comes later.

It SHALL NOT implement decision workflows in this change.

## Public Registration Requirements

Registration should collect only data needed for the profile foundation and later scientific workflows.

Recommended fields:

- first name;
- last name;
- e-mail;
- password;
- institution;
- country;
- position/role;
- intent/role selection if appropriate:
  - author;
  - reviewer;
  - chair only via admin/manual assignment unless explicitly allowed.

Reviewer and chair flags should be controlled carefully. Public users should not self-assign chair privileges.

Recommended policy:

- public users may register as author;
- reviewer role may require admin approval or invitation;
- chair role must not be self-assignable from public registration.

If reviewer self-declaration is allowed, it should be stored as a request/pending state only, not automatically as full reviewer permission, unless a deliberate decision is documented.

## Security Requirements

1. Use Django authentication primitives.
2. Use CSRF protection.
3. Do not store passwords manually.
4. Do not expose profile data publicly by default.
5. Require login for dashboards.
6. Require appropriate role flags for role-specific dashboards.
7. Prevent chair role self-escalation.
8. Use safe redirects after login/logout.
9. Avoid leaking whether privileged accounts exist.
10. Keep `django-axes` behavior compatible with login views.

## UX Requirements

1. Forms should use the design system.
2. Errors should be clear and field-specific where possible.
3. Dashboard pages should clearly distinguish “available now” vs “coming in later workflow”.
4. Role unavailable states should be explicit.
5. Internal pages should remain simple and not look like unfinished broken pages.
6. Mobile layout must remain usable.

## Acceptance Criteria

1. Users can register with required profile metadata.
2. Users can log in and log out.
3. Users can view and edit their profile.
4. A `UserProfile` or equivalent profile exists for registered users.
5. Author/reviewer/chair flags exist and are used for access control.
6. Role-specific dashboard shells exist.
7. Unauthenticated users are redirected to login when accessing dashboards.
8. Users without a role cannot access role-specific dashboards.
9. Chair role cannot be self-assigned from public registration.
10. Dashboard pages clearly state that submission/review workflows come in later proposals.
11. The change passes:
    - `openspec validate add-accounts-profiles-and-dashboards --strict`
    - `uv run python manage.py check`
    - `uv run python manage.py makemigrations --check --dry-run`
    - `uv run pytest`
12. No actual submission/review workflow is implemented.
