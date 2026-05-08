## 1. User Model Refactor

- [x] 1.1 Create migration to remove `full_name` field from `accounts.User`.
- [x] 1.2 Update `User.__str__` to use `get_full_name()` with `username` fallback.
- [x] 1.3 Add `User.clean()` validation enforcing at least one role (`is_author`, `is_reviewer`, `is_chair`) or staff/superuser (`is_staff`, `is_superuser`).
- [x] 1.4 Update `accounts/admin.py` — replace `full_name` with `first_name`/`last_name` in fieldsets and list_display.
- [x] 1.5 Update existing tests in `accounts/tests/test_models.py` to use `first_name`/`last_name` instead of `full_name`.

## 2. Authentication & Registration

- [x] 2.1 Implement registration form and view in `accounts/` to create users with `is_author=True`, collecting `first_name` and `last_name` separately.
- [x] 2.2 Set up Django standard authentication URLs (login, logout, password reset).
- [x] 2.3 Create styled templates for all authentication views using the Design System components.
- [x] 2.4 Add validation for mandatory profile fields and privacy/image consents in the registration flow.
- [x] 2.5 Configure `LOGIN_URL`, `LOGIN_REDIRECT_URL`, and `LOGOUT_REDIRECT_URL` in settings.

## 3. Dashboard Routing & Logic

- [x] 3.1 Implement the `/dashboard/` entry view with redirect logic based on user roles (Chair > Reviewer > Author).
- [x] 3.2 Create Author Dashboard view and template (extending `dashboard.html`) with an empty state for submissions.
- [x] 3.3 Create Reviewer Dashboard view and template with an empty state for assigned reviews.
- [x] 3.4 Create Chair Dashboard view and template with a summary of system-wide submissions.
- [x] 3.5 Implement dynamic sidebar navigation in `dashboard.html` — conditionally render links based on user role flags.

## 4. Access Control & Security

- [x] 4.1 Create custom decorators/mixins to protect views based on `is_author`, `is_reviewer`, and `is_chair` flags.
- [x] 4.2 Apply `@login_required` and role-specific decorators to all dashboard routes.
- [x] 4.3 Implement a basic profile edit view for authors to update their profile data (first_name, last_name, institution, country, position).
- [x] 4.4 Ensure the Wagtail admin remains restricted to superusers only.

## 5. Mobile Responsiveness

- [x] 5.1 Add Alpine.js hamburger menu to `templates/layouts/dashboard.html`, following the pattern from `templates/components/header.html`.
- [x] 5.2 Ensure sidebar slides in/out with transitions, closes on Escape and on link click.
- [x] 5.3 Verify responsive behavior of all dashboard pages and auth templates at mobile, tablet, and desktop breakpoints.

## 6. Notifications (Email Foundation)

- [x] 6.1 Configure basic email settings for local development (console backend).
- [x] 6.2 Create a signal to send a welcome email upon successful user registration (async, non-blocking).
- [x] 6.3 Implement a placeholder function for role-assignment notifications.

## 7. Verification

- [x] 7.1 Write unit tests for the registration flow, data validation, and role enforcement.
- [x] 7.2 Write integration tests for dashboard access control (verify 403/redirects for unauthorized roles).
- [x] 7.3 Manually verify the responsive behavior of the dashboard shell with different sidebar configurations. (Manual — requires visual check in browser)
