# proceedings

## Purpose

Define proceedings and final-material export and indicator behavior for accepted, validated and published works.

## ADDED Requirements

### Requirement: Proceedings readiness indicators

The platform MUST report counts for works ready for proceedings and published in proceedings.

#### Scenario: Proceedings statuses exist

Given submissions have ready-for-proceedings and published-in-proceedings statuses  
When indicators are calculated  
Then counts for both statuses MUST be returned.

### Requirement: Final material indicators

The platform MUST report final material workflow status.

#### Scenario: Final materials exist

Given final material records exist  
When proceedings indicators are calculated  
Then counts for pending, received, validated and missing authorization states MUST be returned.

### Requirement: Proceedings support export

The platform MUST provide an export suitable for proceedings preparation.

#### Scenario: Chair exports proceedings data

Given proceedings-eligible submissions exist  
When a chair user downloads proceedings export  
Then the export MUST include publication-relevant metadata and MUST identify publication authorization status.

### Requirement: Video link indicator

The platform MUST report counts for final materials with video URLs and videos promoted to gallery if that association exists.

#### Scenario: Final materials have video URLs

Given final materials include YouTube URLs  
When proceedings/video indicators are calculated  
Then the count of works with video URLs MUST be returned.
