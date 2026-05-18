# translations

## Purpose

Define implementation requirements for applying terminology and translation consistency fixes across Portuguese, English and bilingual surfaces.

## MODIFIED Requirements

### Requirement: Preferred terminology is applied

Preferred terminology from the consistency audit MUST be applied to implemented fixes.

#### Scenario: Portuguese term mismatch exists

Given the audit identifies a Portuguese terminology mismatch  
When this polish change touches that surface  
Then the term MUST be corrected or explicitly deferred.

### Requirement: Bilingual labels remain semantically aligned

Portuguese and English labels MUST remain semantically aligned where both exist.

#### Scenario: English label conflicts with Portuguese label

Given the audit identifies a bilingual terminology conflict  
When this polish change is implemented  
Then labels MUST be aligned or the difference MUST be documented.
