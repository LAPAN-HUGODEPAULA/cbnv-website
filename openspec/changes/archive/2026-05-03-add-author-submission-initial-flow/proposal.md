## Why

The XII CBNV 2026 congress requires a digital platform to manage the scientific submission process. Implementing the initial submission flow is critical to allow authors to submit their work for evaluation, following a two-phase process where Phase 1 focuses on metadata and assessment materials without requiring video links.

## What Changes

- Define the complete submission state machine (all 13 states) and implement Phase 1 transitions (draft, submit).
- Create an Author Dashboard for managing drafts, submissions, and status tracking.
- Introduce secure, non-publicly accessible file storage for submission PDFs.
- Implement automated email confirmations for successful submissions.
- Establish admin-editable thematic axes (Wagtail Snippet) and metadata requirements for scientific works.
- Implement a 3-step submission wizard (metadata + authors, PDF upload, review & confirm) using HTMX for dynamic author row management.

## Capabilities

### New Capabilities
- `submissions`: Core logic for scientific work submissions, metadata management (authors, affiliations, abstract, keywords), thematic axis selection (Wagtail Snippet), and the full state machine.
- `notifications`: System-wide notification service, starting with automated email confirmations for authors.

### Modified Capabilities
- `accounts-auth`: Extend user roles and dashboard access specifically for scientific authors. Profile completeness check uses `first_name`, `last_name`, `institution`, `country`.
- `deployment-security`: Define and implement security protocols for protected media storage, ensuring submission PDFs are not accessible via direct public URLs.

## Impact

- **Models**: New models for Submissions, SubmissionAuthors, SubmissionFiles, ThematicAxis (Snippet). Full state machine with 13 statuses.
- **Views**: New views for the Author Dashboard and 3-step Submission Wizard.
- **Storage**: Configuration of protected storage backends (e.g., internal-only media folder).
- **Email**: Integration with an email service provider or local SMTP for confirmations.
