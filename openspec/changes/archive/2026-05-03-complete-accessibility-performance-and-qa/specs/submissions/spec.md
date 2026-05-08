## ADDED Requirements

### Requirement: Accessible Validation Feedback
Form validation errors SHALL be announced by screen readers using `aria-live="polite"` and explicitly linked to input fields via `aria-describedby`.

#### Scenario: Form error announced
- **WHEN** an author submits an invalid form
- **THEN** the error message SHALL be automatically announced by the screen reader
- **AND** focus SHALL be moved to the first invalid field

### Requirement: Protected File Information Accessibility
Submission metadata (titles, authors) SHALL be accessible to screen readers, while file download links SHALL have descriptive `aria-label` attributes (e.g., "Download PDF for [Submission Title]").

#### Scenario: Accessible download links
- **WHEN** a Chair views the list of submissions
- **THEN** each download link SHALL contain an `aria-label` that includes the submission title for context

### Requirement: Submission Progress Indicator
The submission workflow SHALL include a progress indicator that is semantically clear to assistive technologies.

#### Scenario: Progress step identified
- **WHEN** an author is on the second step of submission
- **THEN** the progress bar SHALL use `aria-current="step"` to identify the active phase
