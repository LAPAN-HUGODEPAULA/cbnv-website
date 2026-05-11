# Public Site Accessibility Delta

## ADDED Requirements

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
