## ADDED Requirements

### Requirement: Automated Accessibility Auditing
The project SHALL integrate `axe-core` or a similar tool for automated accessibility auditing in the CI/CD pipeline or local test suite.

#### Scenario: Running accessibility tests
- **WHEN** the test suite is executed
- **THEN** it SHALL include automated checks for ARIA compliance, contrast, and labels

### Requirement: Performance Budgeting
The project SHALL define and enforce a performance budget for the public site, targeting a Lighthouse Performance score of 90+ and LCP under 2.5s.

#### Scenario: Performance audit passes
- **WHEN** a production build is audited with Lighthouse
- **THEN** it SHALL meet the performance budget criteria for Largest Contentful Paint (LCP) and Total Blocking Time (TBT)

### Requirement: E2E QA Coverage for User Journeys
The project SHALL include End-to-End (E2E) tests covering the primary journeys for all user roles (Visitor, Author, Reviewer, Chair).

#### Scenario: Visitor journey E2E
- **WHEN** the visitor E2E test runs
- **THEN** it SHALL verify navigation from Home to Program to Submissions rules without errors

#### Scenario: Author journey E2E
- **WHEN** the author E2E test runs
- **THEN** it SHALL verify login, submission creation, and dashboard status updates
