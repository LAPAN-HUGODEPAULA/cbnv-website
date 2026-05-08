## Why

To support the scientific workflow of XII CBNV 2026, the platform must transition from a purely informational site to an interactive system where participants can register, submit work, and conduct peer reviews. This requires a robust authentication system, clear transactional roles (Author, Reviewer, Chair), and personalized dashboards.

## What Changes

- **User Model Refactor**: Remove redundant `full_name` field in favor of Django's built-in `first_name`/`last_name` fields, with `get_full_name()` for display. Enables personalized greetings using `first_name`.
- **Authentication System**: Implementation of login, registration (auto-login, no email verification), and password recovery for general users (participants).
- **Transactional Roles**: Role-based access control using boolean flags (`is_author`, `is_reviewer`, `is_chair`). Every user must have at least one role or be staff/superuser — enforced at model level.
- **User Dashboards**: Role-specific dashboard views with dynamic sidebar navigation that shows only links relevant to the user's roles.
- **Account Management**: Self-service profile updates and role-specific registration flows.
- **Access Control Foundation**: Decorators/mixins to protect scientific workflow views based on user roles.
- **Mobile Responsiveness**: Hamburger menu on dashboard shell using Alpine.js, following the pattern established in the public header.

## Capabilities

### New Capabilities
- `submissions`: Requirements for managing work submissions, including initial metadata and file uploads.
- `reviews`: Requirements for the peer-review process, including assignment and evaluation criteria.
- `notifications`: Requirements for system-triggered communications (emails, on-site alerts) related to user actions and status changes.

### Modified Capabilities
- `accounts-auth`: Remove `full_name`, enforce at least one role per user, add mobile-responsive dashboard, dynamic sidebar navigation.

## Impact

- **Apps**: `accounts`, `submissions`, `reviews`, `notifications`.
- **UI**: Login/registration forms, role-specific dashboard views, mobile hamburger menu on dashboard shell, dynamic sidebar.
- **Data**: Migration to remove `full_name` from `User` model; model-level validation enforcing at least one role.
- **Middleware**: Authorization decorators/mixins for role-based view protection.
