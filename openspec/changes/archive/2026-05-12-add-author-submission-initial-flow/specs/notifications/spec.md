# notifications

## Purpose

Define confirmation behavior for successful initial submissions, including e-mail behavior when an e-mail backend is configured.

## ADDED Requirements

### Requirement: Submission confirmation

The platform SHALL provide confirmation after successful initial submission and SHALL send a confirmation e-mail when e-mail is configured.

#### Scenario: Confirmation e-mail sent

Given e-mail backend is configured  
When an author successfully submits an initial submission  
Then a confirmation e-mail SHALL be sent to the corresponding author or submitter.

#### Scenario: E-mail failure does not lose submission

Given the submission was saved successfully  
When confirmation e-mail fails  
Then the submission SHALL remain saved and the failure SHALL be handled without corrupting submission data.

### Requirement: Confirmation content

The confirmation message SHALL include key submission information.

#### Scenario: Confirmation message content

Given a confirmation e-mail is generated  
Then it SHALL include submission code, title, submitted timestamp and a reminder that video is not required at the initial stage.
