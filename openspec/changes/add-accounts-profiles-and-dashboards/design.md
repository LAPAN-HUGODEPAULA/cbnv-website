# Design: Add Accounts, Profiles and Dashboards

## Overview

This change creates the authentication and role-aware internal-area foundation for the CBNV 2026 platform.

The guiding principle is simple: use Django defaults where possible, keep congress-specific information in `UserProfile`, and expose only the dashboard shells required for later scientific workflows.

## Design Principles

### 1. Django defaults before custom authentication

Use Django's default `User`, authentication views, password hashing, sessions and CSRF protections. Avoid custom authentication architecture unless absolutely required.

### 2. Profile metadata belongs outside `User`

Congress-specific metadata belongs in `UserProfile`.

### 3. Role flags are enough for this phase

Do not introduce a complex RBAC system. Author/reviewer/chair flags are sufficient for current workflow boundaries.

### 4. Dashboard shells should be honest

A dashboard shell should not pretend that submissions or reviews already exist. Use clear future-state placeholders.

### 5. Security over convenience

Public users should not be able to grant themselves privileged reviewer/chair access unless explicitly approved by later workflow design.

## Model Strategy

### User

Use Django default `User`.

Fields used:

- `username`;
- `first_name`;
- `last_name`;
- `email`;
- password fields managed by Django.

If the public registration UX uses e-mail as identity, the implementation may set `username=email` internally, but must document this behavior.

### UserProfile

Recommended fields:

```text
user
institution
country
position
orcid optional
is_author
is_reviewer
is_chair
consent_privacy
consent_image
created_at
updated_at
```

Adapt to existing model fields. Do not introduce churn if the current model already covers these needs.

## Profile Creation Strategy

Choose one and document it:

1. signal-based automatic creation on user creation; or
2. explicit creation in registration flow.

For predictability in tests and registration, explicit creation in the registration service/form is often easier to reason about. Signals are acceptable if already used.

## Registration Flow

Recommended flow:

1. visitor opens registration page for account creation;
2. fills name, e-mail, password and profile metadata;
3. selects author intent if appropriate;
4. account is created;
5. profile is created;
6. user is logged in or sent to login depending on policy;
7. user lands on dashboard index or profile completion page.

Chair role must not be exposed as a self-service option.

Reviewer role should be either omitted from public self-registration or stored as a pending request if that concept exists. Since pending reviewer requests are not in current scope, prefer admin/manual reviewer assignment.

## Login/Logout Flow

Use Django auth views or thin wrappers.

Requirements:

- CSRF enabled;
- safe next redirect;
- clear login errors;
- `django-axes` compatibility;
- redirect authenticated users away from login if appropriate.

## Dashboard Routing

Recommended routes:

```text
/accounts/login/
/accounts/logout/
/accounts/register/
/accounts/profile/
/dashboard/
/dashboard/author/
/dashboard/reviewer/
/dashboard/chair/
```

Actual route names may follow existing project conventions.

### Dashboard index behavior

- no roles: show profile and “no dashboard role assigned” message;
- one role: show direct card/link for that role;
- multiple roles: show role cards.

### Author dashboard shell

Do not create submissions here. Show future submission state.

### Reviewer dashboard shell

Do not create review assignments here. Show future assigned reviews placeholder.

### Chair dashboard shell

Do not implement review decisions. Show future committee tools placeholder.

## Authorization Strategy

Use simple helpers:

```python
def is_author(user): ...
def is_reviewer(user): ...
def is_chair(user): ...
```

or equivalent decorators/mixins.

Rules:

- all dashboards require authentication;
- author dashboard requires `profile.is_author`;
- reviewer dashboard requires `profile.is_reviewer`;
- chair dashboard requires `profile.is_chair`;
- staff/superuser do not bypass the user-facing author/reviewer/chair dashboard checks in this foundation; privileged admin/committee tools use separate admin-or-chair helpers where needed;
- missing profile should not crash; it should be created or handled safely.

## Template Strategy

Use existing public/internal layout components where practical.

Required template concerns:

- accessible form labels and errors;
- concise dashboard cards;
- role badges with text;
- clear empty/future-state components;
- mobile-friendly layouts.

## Messages and States

Recommended states:

- profile incomplete;
- no role assigned;
- author dashboard available;
- reviewer role pending/not assigned;
- chair access restricted;
- submissions not yet open;
- review workflow not yet available.

## Security Notes

### Prevent privilege escalation

Public forms must not allow setting:

- `is_staff`;
- `is_superuser`;
- `is_chair`;
- unrestricted `is_reviewer` unless deliberately approved.

### Protect redirects

Only allow safe internal redirects from `next`.

### Profile privacy

Profile views are private to the authenticated user. Public speaker/team pages should not depend on account profiles.

## Testing Strategy

Minimum tests:

1. registration creates user and profile;
2. login works;
3. logout works;
4. profile edit works;
5. unauthenticated dashboard access redirects;
6. author dashboard requires author flag;
7. reviewer dashboard requires reviewer flag;
8. chair dashboard requires chair flag;
9. public registration cannot self-assign chair;
10. users with multiple roles see multiple dashboard options.

## Future Integration

This change creates integration points for:

- `add-author-submission-initial-flow`;
- `add-review-decision-workflow`;
- notifications;
- reports;
- final materials/proceedings.

Those proposals will add real dashboard data.
