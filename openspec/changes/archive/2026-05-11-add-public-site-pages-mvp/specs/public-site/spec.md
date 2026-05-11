# Public Site MVP Delta

## Purpose

Define the core set of public pages and navigation for the XII CBNV 2026 website MVP.

## ADDED Requirements

### Requirement: Public page set

The platform SHALL provide the public MVP page set: Home, About, Program, Speakers, Submissions, Registration, Sponsorship, Previous Editions and Contact.

#### Scenario: Visitor navigates public site

Given the public site is configured with required pages  
When a visitor uses the main navigation  
Then they SHALL be able to reach Home, About, Program, Speakers, Submissions, Registration, Sponsorship, Previous Editions and Contact.

### Requirement: Home page MVP

The Home page SHALL communicate core event identity and primary actions.

#### Scenario: Home renders event basics

Given global settings are configured  
When a visitor opens Home  
Then the page SHALL render event name or short name, theme, dates, venue/location and format.

#### Scenario: Home renders announcements

Given published announcements exist  
When Home renders  
Then it SHALL show featured or recent announcements.

### Requirement: About page MVP

The About page SHALL provide institutional and scientific context for CBNV 2026.

#### Scenario: About renders event context

Given the About page is live  
When a visitor opens it  
Then it SHALL present the event purpose, 2026 theme context and institutional framing.

### Requirement: Program page MVP

The Program page SHALL render day-based schedule data from program models.

#### Scenario: Program renders published sessions

Given program days and published sessions exist  
When a visitor opens Program  
Then sessions SHALL be grouped by day and displayed with time ranges and activity labels.

#### Scenario: Program excludes unpublished sessions

Given a session is draft, pending or cancelled  
When public program data is rendered  
Then that session SHALL NOT be shown as a published current program item.

### Requirement: Speakers page MVP

The Speakers page SHALL render public speaker data.

#### Scenario: Speakers page hides hidden speakers

Given a speaker has hidden status  
When a visitor opens Speakers  
Then that speaker SHALL NOT be displayed as a public confirmed speaker.

### Requirement: Speakers page type

The platform SHALL provide a public Speakers page type or equivalent Wagtail page.

#### Scenario: Speakers page is navigable

Given the public site is configured
When a visitor uses the main navigation
Then they SHALL be able to access a public speakers page.

### Requirement: Submissions page MVP

The Submissions page SHALL explain the public submission process without implementing the workflow.

#### Scenario: Initial submission video rule is visible

Given a visitor opens Submissions  
When they read submission requirements  
Then they SHALL see that video is not required in the initial submission phase.

### Requirement: Registration page MVP

The Registration page SHALL represent external registration status.

#### Scenario: Registration is coming soon

Given registration status is coming soon or no registration URL exists  
When a visitor opens Registration  
Then the page SHALL show a clear coming-soon state rather than a broken link.

### Requirement: Sponsorship page MVP

The Sponsorship page SHALL show support/sponsorship information and active supporting entities.

#### Scenario: Sponsorship page renders active sponsors

Given active sponsors/supporting entities exist  
When a visitor opens Sponsorship  
Then active entities marked for sponsorship display SHALL be shown.

### Requirement: Previous editions page MVP

The Previous Editions page SHALL present archive/history content without overriding current event facts.

#### Scenario: Previous edition content is archival

Given previous edition records or fallback archive data exist  
When a visitor opens Previous Editions  
Then content SHALL be presented as historical/archive material.

### Requirement: Contact page MVP

The Contact page SHALL provide public contact and current venue information.

#### Scenario: Contact shows current venue

Given canonical venue settings are configured  
When a visitor opens Contact  
Then the page SHALL show the CAD-1/UFMG venue/address or link to current venue information.

### Requirement: Contact page type

The platform SHALL provide a public Contact page type.

#### Scenario: Contact page is navigable

Given the public site is configured
When a visitor uses the main navigation
Then they SHALL be able to access a public contact page.