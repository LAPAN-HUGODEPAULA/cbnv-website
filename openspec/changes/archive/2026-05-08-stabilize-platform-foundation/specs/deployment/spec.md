# Deployment Foundation Delta

## ADDED Requirements

### Requirement: Docker Compose development environment

The platform SHALL run locally through Docker Compose without requiring manual correction of database host settings.

#### Scenario: Web container connects to database service

Given `docker compose up` is executed  
When the web container starts  
Then it SHALL connect to PostgreSQL using the Docker Compose service hostname `db`.

#### Scenario: PostgreSQL version is aligned

Given Docker Compose defines the database service  
When the service image is inspected  
Then it SHALL use the approved PostgreSQL 18.3 image.

### Requirement: Environment file safety

The platform SHALL keep real environment files out of version control.

#### Scenario: Local env file is untracked

Given a developer creates a local `.env` file  
When Git status is inspected  
Then `.env` SHALL remain untracked.

#### Scenario: Example env file is safe

Given `.env.example` is committed  
When it is inspected  
Then it SHALL contain placeholders or safe development defaults  
And SHALL NOT contain real secrets.

### Requirement: Docker build errors are visible

The Docker build SHALL NOT suppress critical build errors.

#### Scenario: Static collection fails

Given static collection fails during a production-oriented build  
When the Docker image is built  
Then the build SHALL fail visibly instead of suppressing the error.