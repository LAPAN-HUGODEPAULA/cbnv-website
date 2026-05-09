# Accounts Foundation Delta

## MODIFIED Requirements

### Requirement: Authentication model

The platform SHALL use a custom `User` model for authentication.

The platform SHALL define `accounts.User` as custom user model via `AUTH_USER_MODEL = "accounts.User"`. The model SHALL inherit from `AbstractUser` and utilize the native Django `first_name` and `last_name` fields instead of a redundant `full_name` field.

#### Scenario: Custom User model is used

Given Django settings are loaded  
When the authentication user model is inspected  
Then the platform SHALL use the custom `accounts.User` model  
And SHALL require proper configuration via `AUTH_USER_MODEL = "accounts.User"`.

#### Scenario: Standard name fields are used

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