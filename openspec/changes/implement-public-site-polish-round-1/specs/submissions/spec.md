# submissions

## Purpose

Define implementation requirements for aligning submission rules, author-facing labels, dashboard states and initial-submission messaging with the consistency audit.

## MODIFIED Requirements

### Requirement: Submission persona labels align with status map

Submission status labels MUST align with the persona status map.

#### Scenario: Author-facing label mismatch exists

Given the persona status map identifies an author-facing submission label mismatch  
When this polish change is implemented  
Then the label MUST be corrected or explicitly deferred.

### Requirement: Initial video rule remains consistent

Initial submission surfaces MUST consistently state that video is not required initially.

#### Scenario: Initial video inconsistency exists

Given the consistency audit finds a surface implying video is required initially  
When this polish change is implemented  
Then the wording MUST be corrected or explicitly deferred.
