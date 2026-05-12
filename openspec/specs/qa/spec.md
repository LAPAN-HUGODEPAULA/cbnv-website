# Review QA (qa)

## Purpose
Define quality gates for diagnostic review changes, including scope control, finding routing and severity classification.
## Requirements
### Requirement: Review-only change boundary
The review change SHALL not implement UI/layout/content fixes.

#### Scenario: Review PR contains diagnostics only
- **GIVEN** the PR for this change is inspected
- **WHEN** changed files are reviewed
- **THEN** changes SHALL be limited to OpenSpec files and review documentation unless a minor documentation-only supporting file is justified.

### Requirement: Follow-up routing
Every actionable finding SHALL be routed to an appropriate follow-up proposal.

#### Scenario: Finding has target proposal
- **GIVEN** a backlog finding exists
- **WHEN** its metadata is inspected
- **THEN** it SHALL include a target proposal such as `produce-public-site-content-round-1`, `verify-cross-page-content-consistency`, `implement-public-site-polish-round-1` or a named future proposal.

### Requirement: Severity classification
Every actionable finding SHALL have a severity classification.

#### Scenario: Finding has severity
- **GIVEN** a backlog finding exists
- **WHEN** it is inspected
- **THEN** it SHALL have severity P0, P1, P2 or P3.

### Requirement: Content-only change boundary

This change SHALL not implement layout redesign or unrelated feature work.

#### Scenario: PR is inspected

Given the PR for this change is reviewed  
When changed files are inspected  
Then changes SHALL be limited to OpenSpec files, content documentation, and safe content data/template text updates.

### Requirement: Content quality checklist

The content-production output SHALL include or apply a content quality checklist.

#### Scenario: Content block is reviewed

Given a content block is produced  
When it is checked  
Then it SHOULD be evaluated for truth, necessity, specificity, placement, duplication, overclaiming risk and pending/confirmed status.

### Requirement: Consistency handoff

This change SHALL prepare inputs for cross-page consistency verification.

#### Scenario: Consistency handoff exists

Given the content-production documents exist  
When they are inspected  
Then they SHALL identify repeated facts, standardized terms, open questions and provisional content requiring verification.

