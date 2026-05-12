# Accessibility Review Delta

## ADDED Requirements

### Requirement: Accessibility baseline review

The UI/UX review SHALL include a baseline accessibility assessment.

#### Scenario: Keyboard navigation is considered

Given the review report exists
When accessibility observations are inspected
Then keyboard navigation and focus visibility SHALL be addressed.

#### Scenario: Heading structure is considered

Given the review report exists
When accessibility observations are inspected
Then heading structure SHALL be addressed.

#### Scenario: Icon-only labels are considered

Given the review report exists
When accessibility observations are inspected
Then icon-only links or buttons SHALL be checked for accessible labels.

### Requirement: Schedule accessibility review

The review SHALL assess public program schedule readability.

#### Scenario: Program accessibility is reviewed

Given the Program page exists
When the accessibility observations are inspected
Then the review SHALL address whether the schedule is readable on mobile and understandable without relying on color alone.
