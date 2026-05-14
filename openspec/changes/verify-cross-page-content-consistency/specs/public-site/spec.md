# public-site

## Purpose

Define verification requirements for public pages, CTA states, archive separation, footer content and SEO metadata.

## ADDED Requirements

### Requirement: Public page coverage

The audit MUST cover every implemented public MVP page and current public extension page.

#### Scenario: Public page review completed

Given public pages exist
When the audit is performed
Then Home, About, Program, Speakers, Submissions, Registration, Sponsorship, Previous Editions, Contact and Video Gallery MUST be checked.

### Requirement: Public CTA consistency

The audit MUST verify that public CTAs match configured workflow and link states.

#### Scenario: Registration unavailable

Given registration status is not available
When public registration CTAs are reviewed
Then they MUST not appear as active broken links.
