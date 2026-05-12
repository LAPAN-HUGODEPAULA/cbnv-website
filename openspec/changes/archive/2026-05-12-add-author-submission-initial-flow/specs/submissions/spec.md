# submissions

## Purpose

Define the initial author submission workflow, data model expectations, pre-review status behavior, and explicit exclusion of video from the initial phase.

## ADDED Requirements

### Requirement: Initial submission creation

Authenticated authors SHALL be able to create an initial scientific submission.

#### Scenario: Authenticated author creates submission

Given an authenticated user with author role  
When they submit valid metadata, author information and initial PDF  
Then a `Submission` SHALL be created or finalized with submitted status.

#### Scenario: Unauthenticated user cannot create submission

Given an unauthenticated visitor  
When they request the submission creation view  
Then they SHALL be redirected to login.

### Requirement: Submission metadata

The initial submission SHALL store core scientific metadata.

#### Scenario: Submission metadata is saved

Given an author submits title, abstract, keywords and thematic axis  
When the submission is saved  
Then those values SHALL be stored with the submission.

### Requirement: Ordered submission authors

The initial submission SHALL support multiple ordered authors.

#### Scenario: Multiple authors are saved

Given an author enters multiple contributors  
When the submission is saved  
Then the contributors SHALL be stored in an explicit order.

### Requirement: Initial submission status

The initial submission SHALL have a status suitable for the pre-review phase.

#### Scenario: Submission is finalized

Given a valid submission is finalized  
When it is saved  
Then the status SHALL indicate it has been submitted and is ready for later workflow steps.

### Requirement: Video is not required initially

The initial submission flow SHALL NOT require video.

#### Scenario: Author submits without video

Given an author completes all required initial submission fields and uploads the required PDF  
When they submit without a video file or video link  
Then the submission SHALL be accepted if all other validation passes.

#### Scenario: Initial form has no video requirement

Given the initial submission form is displayed  
When the author reviews required fields  
Then video SHALL NOT appear as a required field.
