# Accounts Foundation Delta

## MODIFIED Requirements

### Requirement: Authentication model

The platform SHALL use Django's default User model for authentication.

Congress-specific user metadata SHALL be stored in a `UserProfile` model linked one-to-one to Django's default User model.

#### Scenario: Default Django User is used

Given Django settings are loaded  
When the authentication user model is inspected  
Then the platform SHALL use Django's default User model  
And SHALL NOT require a custom `accounts.User` model.

#### Scenario: Default name fields are used

Given a user account is created  
When the user's name is stored  
Then Django's standard `first_name` and `last_name` fields SHALL be used  
And a custom `full_name` field SHALL NOT be required.

#### Scenario: Congress metadata is stored in profile

Given a user exists  
When institution, country, scientific role flags, or consent fields are required  
Then these values SHALL be stored in the user's `UserProfile`.

#### Scenario: Scientific roles are independent profile flags

Given a user can be both author and reviewer  
When their profile is updated  
Then `is_author`, `is_reviewer`, and `is_chair` MAY be independently true or false.