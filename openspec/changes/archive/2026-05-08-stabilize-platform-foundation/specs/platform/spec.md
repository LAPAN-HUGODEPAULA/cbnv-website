# Platform Foundation Delta

## ADDED Requirements

### Requirement: Current stable runtime baseline

The platform SHALL use the latest stable compatible runtime baseline approved at the time of this proposal.

The approved baseline is:

- Python 3.14.x
- Django 6.0.x
- Wagtail 7.4.x LTS
- PostgreSQL 18.3
- Tailwind CSS 4.x
- Node.js 24 LTS when Node is required for frontend tooling

#### Scenario: Runtime baseline is consistent across the repository

Given the repository contains dependency files, Docker files, README, OpenSpec project context, and architecture documentation  
When a developer inspects the runtime versions  
Then all files SHALL describe the same approved baseline.

#### Scenario: Python version is compatible with Django and Wagtail

Given the project runs on Python 3.14.x  
When Django and Wagtail dependencies are installed  
Then the selected Django and Wagtail versions SHALL support Python 3.14.

#### Scenario: Dependency versions are reproducible

Given the project uses `uv` for Python dependency management  
When dependencies are installed in a clean environment  
Then installed Python packages SHALL match the committed `uv.lock`.

### Requirement: No floating production runtime tags

Production and development containers SHALL avoid unconstrained `latest` tags.

#### Scenario: Database image is pinned

Given Docker Compose defines the PostgreSQL service  
When the database image is inspected  
Then it SHALL use a pinned PostgreSQL 18.3 image tag.

#### Scenario: Python image is pinned to the approved series

Given the Dockerfile defines the Python base image  
When the image tag is inspected  
Then it SHALL use Python 3.14.x.