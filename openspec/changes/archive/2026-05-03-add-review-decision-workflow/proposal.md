## Why

The XII CBNV 2026 congress needs a structured process for scientific evaluation. This change implements the review workflow, allowing the scientific commission to assign reviewers, collect feedback, and issue final decisions (Accept, Reject, or Corrections) with specific presentation modalities.

## What Changes

- **Scientific Review Workflow**: Implementation of reviewer assignment by the commission.
- **Reviewer Feedback**: Forms for reviewers to provide qualitative and quantitative feedback.
- **Decision Engine**: Commission can issue decisions: "Accepted", "Rejected", or "Accepted with Corrections".
- **Modality Assignment**: Commission defines the final presentation format (Oral, Poster, or Video).
- **Revision Loop**: Authors can upload a revised PDF when corrections are requested.
- **Simple Status Tracking**: Author dashboard displays internal states using simplified language (e.g., "In Evaluation" instead of "Sent to Reviewer 2").
- **Reporting**: Basic export and summary views for the commission to track review progress and final decisions.

## Capabilities

### New Capabilities
- `reviews`: Management of reviewer assignments, feedback forms, and individual assessments.
- `reports`: Export and summary views for review progress, decision status, and work distribution.

### Modified Capabilities
- `submissions`: Extension of the submission state machine to handle review phases, modality assignment, and revised PDF uploads.
- `notifications`: Alerts for reviewers on assignment and authors on final decisions or correction requests.

## Impact

- **Models**: New `Review`, `ReviewerAssignment`, and `Decision` models. Updates to `Submission` for modality and revised files.
- **Views**: Reviewer portal and Commission management interface.
- **State Machine**: Significant transitions added to the `Submission` status flow.
- **Emails**: New templates for review-related alerts.
