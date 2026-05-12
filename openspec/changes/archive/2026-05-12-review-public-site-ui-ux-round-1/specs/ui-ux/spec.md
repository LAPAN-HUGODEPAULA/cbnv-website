# UI/UX Review Round 1 Delta

## ADDED Requirements

### Requirement: Public MVP UI/UX review report

The platform SHALL include a versioned UI/UX review report for the public-site MVP.

#### Scenario: Review report exists

Given the review change is completed
When the repository is inspected
Then `docs/reviews/public-site-ui-ux-round-1.md` SHALL exist.

#### Scenario: Review records evidence

Given the review report exists
When it is read
Then it SHALL include reviewed branch or commit, environment, viewport matrix and review date.

### Requirement: User journey assessment

The UI/UX review SHALL assess core public user journeys.

#### Scenario: General visitor journey is reviewed

Given the review report exists
When the user journey section is inspected
Then it SHALL evaluate whether a general visitor can understand what the event is, when and where it happens, and what action to take next.

#### Scenario: Author journey is reviewed

Given the review report exists
When the user journey section is inspected
Then it SHALL evaluate whether a potential author can understand submission status and initial submission expectations.

### Requirement: Section-level decisions

The UI/UX review SHALL make explicit decisions for ambiguous or redundant sections.

#### Scenario: Ambiguous section has decision

Given a section such as latest news placement, “Híbrido” card, “O que esperar?”, partner grids or footer text is reviewed
When the report is inspected
Then the section SHALL have a decision such as keep, remove, merge, move, rewrite, defer or needs-data.

### Requirement: Prioritized UI/UX backlog

The review SHALL produce a prioritized backlog.

#### Scenario: Backlog exists

Given the review change is completed
When the repository is inspected
Then `docs/reviews/public-site-ui-ux-round-1-backlog.md` SHALL exist.

#### Scenario: Finding has actionable metadata

Given a backlog finding exists
When the finding is inspected
Then it SHALL include severity, category, page/section, rationale, recommendation and target proposal.
