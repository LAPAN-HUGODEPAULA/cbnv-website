# automation

## Purpose

Define implementation requirements for selected automated consistency checks derived from the audit's automation candidate matrix.

## ADDED Requirements

### Requirement: Automation candidates are evaluated

Automation candidates from the audit MUST be evaluated for implementation.

#### Scenario: Automation candidate exists

Given the automation candidate matrix lists a high-priority check  
When this polish change is implemented  
Then the check MUST be implemented or explicitly deferred.

### Requirement: Protected URL checks

Protected-file URL exposure checks MUST be automated when feasible.

#### Scenario: Export includes final material metadata

Given export tests can inspect generated content  
Then tests MUST verify protected direct file URLs are absent or record deferral.
