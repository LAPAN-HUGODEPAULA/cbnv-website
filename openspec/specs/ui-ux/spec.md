# UI/UX Review (ui-ux)

## Purpose
Define expectations for versioned public-site UI/UX review reports, user journey assessment, section decisions and prioritized backlogs.

## Requirements

### Requirement: Public MVP UI/UX review report
The platform SHALL include a versioned UI/UX review report for the public-site MVP.

#### Scenario: Review report exists
- **GIVEN** the review change is completed
- **WHEN** the repository is inspected
- **THEN** `docs/reviews/public-site-ui-ux-round-1.md` SHALL exist.

#### Scenario: Review records evidence
- **GIVEN** the review report exists
- **WHEN** it is read
- **THEN** it SHALL include reviewed branch or commit, environment, viewport matrix and review date.

### Requirement: User journey assessment
The UI/UX review SHALL assess core public user journeys.

#### Scenario: General visitor journey is reviewed
- **GIVEN** the review report exists
- **WHEN** the user journey section is inspected
- **THEN** it SHALL evaluate whether a general visitor can understand what the event is, when and where it happens, and what action to take next.

#### Scenario: Author journey is reviewed
- **GIVEN** the review report exists
- **WHEN** the user journey section is inspected
- **THEN** it SHALL evaluate whether a potential author can understand submission status and initial submission expectations.

### Requirement: Section-level decisions
The UI/UX review SHALL make explicit decisions for ambiguous or redundant sections.

#### Scenario: Ambiguous section has decision
- **GIVEN** a section such as latest news placement, "Hibrido" card, "O que esperar?", partner grids or footer text is reviewed
- **WHEN** the report is inspected
- **THEN** the section SHALL have a decision such as keep, remove, merge, move, rewrite, defer or needs-data.

### Requirement: Prioritized UI/UX backlog
The review SHALL produce a prioritized backlog.

#### Scenario: Backlog exists
- **GIVEN** the review change is completed
- **WHEN** the repository is inspected
- **THEN** `docs/reviews/public-site-ui-ux-round-1-backlog.md` SHALL exist.

#### Scenario: Finding has actionable metadata
- **GIVEN** a backlog finding exists
- **WHEN** the finding is inspected
- **THEN** it SHALL include severity, category, page/section, rationale, recommendation and target proposal.
