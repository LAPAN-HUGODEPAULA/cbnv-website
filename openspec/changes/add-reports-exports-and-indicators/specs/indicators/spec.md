# indicators

## Purpose

Define aggregate metrics and indicator calculations for submissions, reviews, decisions, authors, institutions, final materials, proceedings, and videos.

## ADDED Requirements

### Requirement: Submission status indicators

The platform MUST calculate submission counts by status.

#### Scenario: Submissions have multiple statuses

Given submissions exist with different statuses  
When indicators are calculated  
Then counts by status MUST be returned.

### Requirement: Thematic axis indicators

The platform MUST calculate submission counts by thematic axis.

#### Scenario: Submissions have thematic axes

Given submissions exist across thematic axes  
When indicators are calculated  
Then counts by thematic axis MUST be returned.

### Requirement: Final modality indicators

The platform MUST calculate counts by final modality.

#### Scenario: Accepted submissions have final modalities

Given accepted submissions have oral, poster or video modalities  
When indicators are calculated  
Then counts by modality MUST be returned.

### Requirement: Review indicators

The platform MUST calculate review and assignment indicators for privileged users.

#### Scenario: Review assignments exist

Given review assignments have pending and completed statuses  
When indicators are calculated for a chair user  
Then pending and completed review counts MUST be returned.

### Requirement: Decision indicators

The platform MUST calculate decision outcome indicators.

#### Scenario: Decisions exist

Given submissions have decision outcomes  
When indicators are calculated  
Then counts by decision outcome MUST be returned.

### Requirement: Final materials indicators

The platform MUST calculate final-material workflow indicators.

#### Scenario: Final materials exist

Given submissions are in final-materials states  
When indicators are calculated  
Then counts for pending, received, validated and ready-for-proceedings states MUST be returned.

### Requirement: Proceedings indicators

The platform MUST calculate proceedings publication indicators.

#### Scenario: Proceedings items exist

Given submissions are ready or published in proceedings  
When indicators are calculated  
Then ready-for-proceedings and published-in-proceedings counts MUST be returned.

### Requirement: Author and institution indicators

The platform MUST calculate author and institution indicators where data exists.

#### Scenario: Author and institution data exist

Given submissions include ordered authors and institutions  
When indicators are calculated  
Then author counts and institution counts MUST be returned.

### Requirement: Geography indicators

The platform MUST calculate state and country indicators where data exists.

#### Scenario: Geographic data exists

Given author or profile data includes state or country  
When indicators are calculated  
Then counts by state or country MUST be returned.
