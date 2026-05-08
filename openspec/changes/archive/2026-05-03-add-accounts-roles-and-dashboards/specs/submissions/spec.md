## ADDED Requirements

### Requirement: Submission List for Authors
The system SHALL display a list of all submissions owned by the authenticated author in their dashboard.

#### Scenario: Author sees empty submission list
- **WHEN** an author with no submissions accesses the submissions list
- **THEN** they see an "Empty State" component with a "New Submission" CTA (even if disabled).

### Requirement: Submission Dashboard for Chairs
The system SHALL provide a view for Chairs to see all submissions in the system, with filtering by status and category.

#### Scenario: Chair views all submissions
- **WHEN** a user with `is_chair=True` accesses the Chair Dashboard
- **THEN** they see a table with all submitted works and their current status.

## Notes

- `SubmissionAuthor.full_name` is intentionally separate from `User.first_name`/`last_name`. Co-authors on a submission may not have user accounts, so their names are stored as plain text on the submission model, not linked to the User model.
