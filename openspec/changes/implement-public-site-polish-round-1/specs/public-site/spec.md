# public-site

## Purpose

Define implementation requirements for correcting public-page inconsistencies found by the cross-page consistency audit.

## MODIFIED Requirements

### Requirement: Public pages use canonical event facts

Public pages MUST use canonical event facts consistently.

#### Scenario: Canonical event fact finding exists

Given the consistency backlog identifies a public-page mismatch for event name, dates, venue, theme or contact information  
When this polish change is implemented  
Then the page MUST be corrected or the finding MUST be explicitly deferred with rationale.

### Requirement: Public CTAs respect configured status

Public CTAs MUST respect configured registration, submission and livestream status.

#### Scenario: Registration is unavailable

Given registration status is coming soon or unavailable  
When public pages render registration CTAs  
Then the CTA MUST not act as an available registration link.

### Requirement: Current pages exclude forbidden legacy facts

Current-event public pages MUST exclude forbidden legacy facts.

#### Scenario: Legacy venue appears in current context

Given the legacy ghost facts inventory flags an old venue on a current-event page  
When this polish change is implemented  
Then the old venue MUST be removed, corrected or explicitly deferred with rationale.
