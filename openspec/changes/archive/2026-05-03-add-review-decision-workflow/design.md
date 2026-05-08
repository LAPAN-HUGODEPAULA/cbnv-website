## Context

The submission system exists, but lacks the internal workflow for evaluation. This design introduces the scientific review layer, connecting authors, reviewers, and the scientific commission.

## Goals / Non-Goals

**Goals:**
- Implement a reviewer portal for feedback entry.
- Implement a commission dashboard for assignments and decisions.
- Handle linear state transitions for scientific review (Submitted -> Under Review -> Accepted/Rejected).
- Support "Decision Bundles" (Chair notes + aggregated reviewer feedback).
- Reuse existing 13-state machine.

**Non-Goals:**
- Implementation of automated reviewer matching.
- Complex mid-process revision loops.
- Post-decision workflows like conference program scheduling.

## Decisions

### 1. Model Extensions and New Entities
- `ReviewerAssignment`: Link table between `User` (Reviewer) and `Submission`.
- `Review`: Stores qualitative comments and a `recommendation`.
- `Submission`: Add `final_modality` (ORAL, POSTER) and `decision_notes` (Chair comments).

### 2. State Machine Transitions
We reuse the existing 13-state machine. Transitions:
- `admin_screening` -> `assigned_to_reviewers`
- `assigned_to_reviewers` -> `under_review`
- `under_review` -> `reviews_completed`
- `reviews_completed` -> `decision_pending`
- `decision_pending` -> `accepted_oral` / `accepted_poster` / `rejected`

**Rationale**: Linear flow simplifies the author's experience and reduces maintenance burden.

### 3. Decision Bundle Pattern
When the Chair issues a decision, the system creates a "Decision Bundle":
- Aggregates all `Review` comments (anonymized).
- Combines with the Chair's `decision_notes`.
- Sends this composite package as the notification to the author.

**Rationale**: Minimizes administrative work for the Chair while providing comprehensive feedback to authors.

### 4. Authorization and Views
- `ReviewerMixin`: Access control for reviewers.
- `CommissionMixin`: Access control for Chairs.
- **Reviewer Portal**: Focused dashboard for assigned reviews.
