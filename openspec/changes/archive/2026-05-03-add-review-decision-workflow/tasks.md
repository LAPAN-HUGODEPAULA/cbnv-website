## 1. Models and Extensions

- [x] 1.1 Create `ReviewerAssignment` model.
- [x] 1.2 Create `Review` model with recommendation and comments.
- [x] 1.3 Add `final_modality` and `decision_notes` fields to `Submission`.
- [x] 1.4 Run migrations.

## 2. Reviewer Portal

- [x] 2.1 Implement `ReviewerMixin`.
- [x] 2.2 Create view for listing assigned submissions.
- [x] 2.3 Implement the review feedback form.

## 3. Commission Dashboard

- [x] 3.1 Implement `CommissionMixin`.
- [x] 3.2 Create assignment interface.
- [x] 3.3 Implement final decision view (Accept/Reject + Modality + decision notes).
- [x] 3.4 Implement "Decision Bundle" aggregation logic (pulling review comments for notifications).

## 4. Notifications

- [x] 4.1 Implement notification for reviewer assignment.
- [x] 4.2 Implement notification for final decision (including the full Decision Bundle: Chair notes + anonymized review feedback).

## 5. Reports and Export

- [x] 5.1 Create review progress summary view.
- [x] 5.2 Implement CSV export of final decisions.

## 6. Verification and Tests

- [x] 6.1 Add tests for reviewer assignment and permission checks.
- [x] 6.2 Add tests for review submission.
- [x] 6.3 Add tests for Chair decision issued (state transition and notification content).
- [x] 6.4 Add tests for Decision Bundle aggregation (ensuring all feedback is included in notification).
- [x] 6.5 Add tests for CSV export content.
