# notifications

## Purpose

Define implementation requirements for correcting low-risk notification copy and trigger inconsistencies found by the audit.

## MODIFIED Requirements

### Requirement: Notification copy aligns with approved terminology

Notification subject and body text MUST use approved terminology.

#### Scenario: Notification copy mismatch exists

Given the notification trigger review identifies a subject or body mismatch  
When this polish change is implemented  
Then notification copy MUST be corrected or explicitly deferred.

### Requirement: Notification fixes preserve privacy

Notification fixes MUST not leak private review notes, reviewer identity or protected file links.

#### Scenario: Decision notification copy is changed

Given decision notification copy is updated  
Then the message MUST not expose private review content to unauthorized recipients.
