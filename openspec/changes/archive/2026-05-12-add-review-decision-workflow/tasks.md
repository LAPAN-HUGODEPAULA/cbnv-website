# Tasks: Add Review and Decision Workflow

## 1. Submissions App Enhancements

- [x] 1.1 Update `Submission` model with `final_modality` and `decision_notes` fields.
- [x] 1.2 Update `Submission.transition_to` to handle review-related and decision-related statuses.
- [x] 1.3 Add helper methods to `Submission` to retrieve public review feedback (anonymized).

## 2. Reviews App Views and Templates

- [x] 2.1 Refine `assign_reviewers` view to ensure correct status transitions.
- [x] 2.2 Implement `assign_reviewers.html` template with reviewer selection.
- [x] 2.3 Refine `reviewer_submissions` view for listing assigned reviews.
- [x] 2.4 Implement `reviewer_submissions.html` template.
- [x] 2.5 Refine `review_detail` view and `ReviewForm` for evaluation submission.
- [x] 2.6 Implement `review_detail.html` template with evaluation form.
- [x] 2.7 Refine `manage_submissions` (Chair Dashboard) to list all submissions and their review progress.
- [x] 2.8 Implement `manage_submissions.html` template.
- [x] 2.9 Refine `issue_decision` view to record final modality and notes.
- [x] 2.10 Implement `issue_decision.html` template.

## 3. Notifications and E-mails

- [x] 3.1 Verify/Implement `send_reviewer_assigned_email` in `notifications/services.py`.
- [x] 3.2 Verify/Implement `send_decision_notification_email` in `notifications/services.py`.
- [x] 3.3 Create/Update e-mail templates for reviewer assignment.
- [x] 3.4 Create/Update e-mail templates for author decision notification.

## 4. Dashboard Integration

- [x] 4.1 Update Reviewer Dashboard shell to link to `reviews:reviewer_submissions`.
- [x] 4.2 Update Chair Dashboard shell to link to `reviews:manage_submissions`.
- [x] 4.3 Update Author Dashboard to show anonymized feedback when decision is made.

## 5. Security and QA

- [x] 5.1 Apply `reviewer_required` and `chair_required` decorators to all review views.
- [x] 5.2 Add object-level permission checks to ensure reviewers only see their assignments.
- [x] 5.3 Write unit tests for reviewer assignment and evaluation flow.
- [x] 5.4 Write unit tests for decision issuance and notification.
- [x] 5.5 Verify all tests pass with `uv run pytest`.

## 6. OpenSpec and Cleanup

- [x] 6.1 Run `openspec validate add-review-decision-workflow --strict`.
- [x] 6.2 Run `uv run python manage.py check`.
- [x] 6.3 Run `uv run python manage.py makemigrations --check --dry-run`.
- [x] 6.4 Prepare for archiving.
