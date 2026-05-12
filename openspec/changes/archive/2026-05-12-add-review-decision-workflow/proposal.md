# Proposal: Add Review and Decision Workflow

## Why

The platform currently has the author submission flow implemented, but it lacks the scientific evaluation workflow. To complete the congress cycle, we need to implement the reviewer assignment, evaluation forms, and the final decision process by the scientific committee (chair).

## What Changes

- **Reviewer Assignment**: Implementation of the interface for Chairs to assign reviewers to submissions.
- **Reviewer Dashboard**: Actual listing of assigned reviews for reviewers.
- **Evaluation Form**: The form for reviewers to submit their scores, recommendations, and comments.
- **Decision Interface**: Interface for Chairs to review all evaluations and issue a final decision (Accept, Reject, etc.) and assign the final presentation modality.
- **Automated Notifications**: E-mail notifications for reviewers (when assigned) and authors (when a decision is made).
- **Status Transitions**: Moving submissions from `submitted` through `under_review` to final states like `accepted_oral`, `rejected`, etc.

## Capabilities

### New Capabilities
- None (Using existing capabilities).

### Modified Capabilities
- `reviews`: Implement the core reviewer assignment and evaluation requirements.
- `submissions`: Add status transition logic and decision metadata handling.
- `notifications`: Implement reviewer assignment and decision notification e-mails.
- `dashboards`: Populate reviewer and chair dashboards with real scientific workflow actions.
- `security`: Enforce object-level permissions for review assignments and evaluations.
- `qa`: Define tests for the review cycle and decision-making process.

## Impact

- **reviews app**: Major updates to views, forms, and templates.
- **submissions app**: Updates to status machine and manager methods.
- **notifications app**: Addition of new e-mail templates and service methods.
- **accounts app**: Use of `is_reviewer` and `is_chair` roles in dashboards.
- **Database**: New records in `ReviewerAssignment` and `Review` models.
