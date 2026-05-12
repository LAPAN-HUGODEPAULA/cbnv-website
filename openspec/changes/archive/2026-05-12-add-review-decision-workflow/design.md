# Design: Add Review and Decision Workflow

## Context

The `reviews` app already contains models (`ReviewerAssignment`, `Review`) and basic views. This design focuses on integrating these components into the dashboard shells, ensuring proper status transitions in the `submissions` app, and implementing the notification logic.

## Goals / Non-Goals

**Goals:**
- Enable Chairs to assign reviewers via a dedicated interface.
- Enable Reviewers to list their assignments and submit evaluations.
- Enable Chairs to issue final decisions based on collected reviews.
- Automate e-mail notifications for assignment and decision events.
- Enforce single-blind anonymity in the author-facing views.

**Non-Goals:**
- Re-opening submissions for revisions (this will be handled in a later proposal).
- Double-blind review (authors and reviewers can see each other's names per requirement).
- Complex automated distribution of reviews (assignment is manual by the chair).

## Decisions

### 1. Status Machine Transitions
The `Submission` model's `transition_to` method will be updated to handle the following flow:
- `submitted` → `admin_screening` (optional manual step)
- `admin_screening`/`submitted` → `assigned_to_reviewers` (when first reviewer is assigned)
- `assigned_to_reviewers` → `under_review` (when all assigned reviewers have submitted their evaluations - automated or manual trigger)
- `under_review`/`reviews_completed` → `accepted_oral`, `accepted_poster`, `accepted_video`, or `rejected`.

*Alternative considered:* Fully automated transitions. *Decision:* Keep some manual control for the Chair to oversee the process.

### 2. Integration with Dashboard Shells
- **Reviewer Dashboard**: Will use the `reviewer_submissions` view to list `ReviewerAssignment` objects for the logged-in user.
- **Chair Dashboard**: Will use the `manage_submissions` view to provide a central control panel for the scientific committee.

### 3. Notification Service
New methods in `notifications.services`:
- `notify_reviewer_assigned(submission, reviewer)`
- `notify_decision(submission)`

These will use the existing `send_transactional_email` helper.

### 4. Anonymous Feedback
In the author-facing submission detail view (or dashboard), only the `recommendation` and `comments` from the `Review` objects will be shown, explicitly excluding the `assignment.reviewer` identity.

## Risks / Trade-offs

- **[Risk]** Authors might find a way to see reviewer names if templates are not carefully crafted. → **Mitigation**: Use a specific context processor or clean context dictionaries in views to only pass needed fields.
- **[Risk]** Reviewers might accidentally submit incomplete forms. → **Mitigation**: Standard Django form validation for required fields (score, recommendation).
