# videos

## Purpose

Define implementation requirements for aligning video terminology, final-material YouTube links and public gallery visibility.

## MODIFIED Requirements

### Requirement: Video terminology is consistent

Video-related labels MUST use approved terminology.

#### Scenario: YouTube terminology mismatch exists

Given the consistency audit identifies inconsistent YouTube or video-gallery terms  
When this polish change is implemented  
Then terminology MUST be corrected or explicitly deferred.

### Requirement: Non-promoted videos remain non-public

Final-material video URLs MUST not appear as public gallery items unless explicitly promoted.

#### Scenario: Non-promoted video appears publicly

Given the audit identifies a non-promoted final-material video in the public gallery  
When this polish change is implemented  
Then the video MUST be removed from public gallery display or the finding MUST be escalated.
