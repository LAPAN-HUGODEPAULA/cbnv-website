# security

## Purpose

Define implementation requirements ensuring polish fixes do not introduce privacy regressions, protected-file exposure or unauthorized role-data exposure.

## MODIFIED Requirements

### Requirement: Protected files remain protected

Polish fixes MUST not expose protected files.

#### Scenario: Public template is changed

Given a public or report template is modified  
Then the implementation MUST verify protected file URLs are not exposed.

### Requirement: Role boundaries remain intact

Polish fixes MUST preserve role-specific data boundaries.

#### Scenario: Dashboard status fix is applied

Given a dashboard is modified  
Then users MUST not gain access to data outside their role.
