# Program Public Rendering Delta

## ADDED Requirements

### Requirement: Public program rendering

The public site SHALL render program data from program models.

#### Scenario: Program days are displayed

Given `ProgramDay` records exist with published sessions  
When the Program page renders  
Then the days SHALL be displayed in configured order.

#### Scenario: Session time range is displayed

Given a published session has start and end times  
When the Program page renders  
Then the session time range SHALL be visible.

#### Scenario: Activity type is displayed

Given a published session has an activity type  
When the Program page renders  
Then the activity type SHALL be shown as a text-bearing label or badge.

### Requirement: Public speaker rendering

The public site SHALL respect speaker/talk visibility states.

#### Scenario: Hidden or pending speaker is not misrepresented

Given a speaker or talk is pending or hidden  
When public pages render  
Then the UI SHALL NOT present that participant as confirmed.
