# reviews

## Purpose

Define implementation requirements for aligning reviewer, chair and author review/decision labels with the persona status map and privacy boundaries.

## MODIFIED Requirements

### Requirement: Review labels align with persona status map

Review and decision labels MUST align with the persona status map.

#### Scenario: Chair and author decision labels conflict

Given the consistency audit identifies conflicting decision labels  
When this polish change is implemented  
Then labels MUST be corrected or the intentional asymmetry MUST be documented.

### Requirement: Reviewer privacy is preserved during fixes

Review-related polish MUST preserve reviewer privacy.

#### Scenario: Review label fix touches author surface

Given a review-related label is corrected on an author-facing surface  
Then the implementation MUST not expose reviewer identity or private review text.
