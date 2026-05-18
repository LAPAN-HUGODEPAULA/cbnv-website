# dashboards

## Purpose

Define implementation requirements for aligning author, reviewer and chair dashboards with the persona status map, canonical labels and operational destinations.

## MODIFIED Requirements

### Requirement: Dashboard labels align with persona status map

Dashboard status labels MUST align with the persona status map.

#### Scenario: Dashboard status mismatch exists

Given the audit identifies a dashboard status mismatch  
When this polish change is implemented  
Then the dashboard label MUST be corrected or explicitly deferred.

### Requirement: Dashboard states match notification outcomes

Dashboard states MUST not contradict notification outcomes.

#### Scenario: Notification-dashboard drift exists

Given the audit identifies drift between notification copy and dashboard status  
When this polish change is implemented  
Then the dashboard or notification wording MUST be corrected or deferred with rationale.
