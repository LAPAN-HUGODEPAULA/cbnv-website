# Public CMS Page Delta

## ADDED Requirements

### Requirement: Wagtail public page types

The public site SHALL use Wagtail page types for public pages.

#### Scenario: Public page can be managed in Wagtail

Given a public page type exists  
When the admin edits it in Wagtail  
Then the page SHALL support title and basic editable content appropriate to its role.

### Requirement: Public pages reuse CMS/domain models

Public page templates SHALL reuse CMS/domain models rather than duplicating content sources.

#### Scenario: Sponsors display comes from sponsor model

Given active sponsor/supporting entities exist  
When a public page needs supporting entities  
Then it SHALL query the sponsor/supporting-entity model.

#### Scenario: Announcements display comes from announcement model

Given public announcements exist  
When a public page needs recent or featured news  
Then it SHALL query the announcement/news model.
