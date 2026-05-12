# Acessibilidade (accessibility)

## Purpose
Garantir que a plataforma seja utilizável por todos os participantes, seguindo as diretrizes WCAG 2.2 AA.

## Requirements

### Requirement: Semantic page structure
Public pages SHALL preserve semantic page structure.

#### Scenario: Page has one primary heading
Given a public page renders  
When the document outline is inspected  
Then the page SHOULD have one clear `h1` representing the page topic.

#### Scenario: Landmarks are preserved
Given a public page renders  
When assistive technology inspects the page  
Then header, navigation, main content and footer landmarks SHALL remain available.

### Requirement: Accessible navigation and CTAs
Public navigation and CTAs SHALL be keyboard and screen-reader accessible.

#### Scenario: Keyboard user uses navigation
Given a keyboard user opens the site  
When they tab through the header/navigation  
Then every interactive item SHALL be reachable and visibly focused.

### Requirement: Accessible schedule rendering
The public program schedule SHALL be readable on small screens and by assistive technologies.

#### Scenario: Program viewed on mobile
Given a visitor opens Program on a narrow viewport  
When sessions are displayed  
Then the schedule SHALL remain readable without horizontal scrolling.

#### Scenario: Program status badge is read
Given a status or activity badge is displayed  
When the badge is read without color information  
Then the text SHALL still convey the meaning.

### Requirement: Accessibility baseline review
The UI/UX review SHALL include a baseline accessibility assessment.

#### Scenario: Keyboard navigation is considered
- **GIVEN** the review report exists
- **WHEN** accessibility observations are inspected
- **THEN** keyboard navigation and focus visibility SHALL be addressed.

#### Scenario: Heading structure is considered
- **GIVEN** the review report exists
- **WHEN** accessibility observations are inspected
- **THEN** heading structure SHALL be addressed.

#### Scenario: Icon-only labels are considered
- **GIVEN** the review report exists
- **WHEN** accessibility observations are inspected
- **THEN** icon-only links or buttons SHALL be checked for accessible labels.

### Requirement: Schedule accessibility review
The review SHALL assess public program schedule readability.

#### Scenario: Program accessibility is reviewed
- **GIVEN** the Program page exists
- **WHEN** the accessibility observations are inspected
- **THEN** the review SHALL address whether the schedule is readable on mobile and understandable without relying on color alone.
