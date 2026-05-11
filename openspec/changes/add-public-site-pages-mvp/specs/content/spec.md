# Public Content Integration Delta

## ADDED Requirements

### Requirement: Public pages consume CMS-backed global settings

Public pages SHALL use CMS-backed global settings for repeated event facts.

#### Scenario: Page needs event dates

Given a page needs event dates  
When it renders  
Then it SHALL read the dates from global settings or the documented canonical source.

### Requirement: Public pages consume announcements

Public pages SHALL consume published announcement/news content where appropriate.

#### Scenario: Draft announcements are not public

Given an announcement is draft  
When public pages query announcements  
Then the draft announcement SHALL NOT be displayed.

### Requirement: Public pages avoid misleading copy

Public MVP pages SHALL avoid unverified promotional claims.

#### Scenario: Home copy is conservative

Given Home renders MVP copy  
When the content is inspected  
Then it SHALL NOT claim that CBNV is the largest Neurovision event in Latin America or use similarly unverified claims.

### Requirement: Coming-soon states

Public pages SHALL render coming-soon states for unavailable links.

#### Scenario: External link missing

Given a required external URL is unavailable  
When a CTA is rendered  
Then it SHALL show a clear disabled or coming-soon state and SHALL NOT render `#` as a destination.

### Requirement: Static fallback content is temporary

Public MVP pages SHOULD prefer CMS/domain models over static constants for repeated event facts.

#### Scenario: Home renders repeated event facts

Given `CoreSettings` contains event identity, dates, location and links
When Home renders
Then it SHALL use those settings instead of duplicating those facts in hardcoded template copy.