## Context

The platform currently exists as a Wagtail-based informational site with a custom user model already defined but underutilized for scientific workflows. We need to implement the transition from public visitors to authenticated participants with specific roles. The design must leverage the previously implemented `dashboard.html` shell.

The custom `User` model has a redundant `full_name` field alongside Django's inherited `first_name`/`last_name`. This change removes the duplication and adds model-level role enforcement.

## Goals / Non-Goals

**Goals:**
- Remove `full_name` from the `User` model in favor of Django's `first_name`/`last_name` and `get_full_name()`.
- Implement the complete authentication cycle (Login, Logout, Register, Password Reset).
- Establish the Role-Based Access Control (RBAC) logic based on the boolean flags in the `accounts.User` model.
- Enforce at model level that every user has at least one role (`is_author`, `is_reviewer`, `is_chair`) or is staff/superuser.
- Create role-specific dashboard routes and initial "Empty State" views.
- Implement dynamic sidebar navigation that shows only links relevant to the user's roles.
- Add mobile-responsive hamburger menu to the dashboard shell using Alpine.js.
- Ensure all authentication and dashboard views are responsive and accessible.
- Lay the foundation for future submission and review workflows.

**Non-Goals:**
- Implementation of actual submission forms or file processing logic.
- Implementation of the actual peer-review evaluation form.
- Complex multi-level RBAC for the Wagtail CMS (editorial access remains separate/single-admin).
- Payment gateway integration.
- Email verification on registration (auto-login only).

## Decisions

- **Remove `full_name`**: Drop the redundant `full_name` field from `User`. Use Django's `first_name`/`last_name` for input and `get_full_name()` for display. This enables personalized greetings via `first_name` ("Olá, Hugo!") without duplication.
- **Role enforcement at model level**: Every user must have at least one transactional role (`is_author`, `is_reviewer`, or `is_chair`) or be staff/superuser (`is_staff`, `is_superuser`). Enforced via `User.clean()`. Registration always sets `is_author=True`. Admin form validation bubbles up from `clean()`.
- **Authentication Views**: Use Django's built-in `auth` views but with custom templates to ensure full Design System integration.
- **Registration flow**: Auto-login on registration, no email verification. Welcome email sent asynchronously (non-blocking).
- **Access Control Layer**: Use standard Django decorators (`@login_required`) and custom mixins/decorators (`@user_passes_test` or similar) to enforce transactional roles.
- **Dashboard Routing**: A single entry point `/dashboard/` that redirects users to their appropriate role-specific view (e.g., `/dashboard/author/`, `/dashboard/reviewer/`) based on their permissions, following the hierarchy Chair > Reviewer > Author.
- **Dynamic sidebar**: The sidebar in `dashboard.html` will conditionally render navigation links based on the authenticated user's role flags. All users see "Painel"; additional sections (Submissões, Revisões, Indicadores) appear only if the user has the corresponding role.
- **Mobile hamburger**: Add an Alpine.js hamburger menu to the dashboard shell, reusing the same pattern established in `templates/components/header.html` (x-data toggle, x-show, x-transition, escape to close).
- **User Profile Management**: Authors can update their own profile data (first_name, last_name, Institution, Country, Position) via a dedicated dashboard page.
- **Audit Logging Foundation**: Implement a lightweight logging signal that records key events like account creation, login, and role changes for future auditing needs.

## Risks / Trade-offs

- **[Risk] Role overlap** → **[Mitigation]** The system explicitly supports multiple roles per user; the UI will prioritize the "highest" role but allow switching between dashboard contexts if needed.
- **[Risk] Security of personal data** → **[Mitigation]** Strictly enforce HTTPS and follow Django's security best practices for session management and password hashing.
- **[Trade-off] Simple flags vs. Permissions system** → **[Rationale]** For the MVP scale of CBNV, the boolean flags (`is_author`, `is_reviewer`, etc.) are sufficient and much simpler to implement than a full Django Group/Permission matrix.
- **[Trade-off] No email verification** → **[Rationale]** For the MVP, auto-login simplifies the onboarding flow. Email is used only for welcome notifications, not as a verification gate. Can be added later if needed.
