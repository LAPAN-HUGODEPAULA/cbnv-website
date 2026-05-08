# Infraestrutura e Deploy (deployment-security)

## Purpose
Definir configurações de produção, segurança, Docker e ambiente operacional.

## Requirements

### Requirement: Runtime baseline consistency

Production and development environments SHALL use the approved baseline:

- Python 3.14.x
- Django 6.0.x
- Wagtail 7.4.x LTS
- PostgreSQL 18.3
- Tailwind CSS 4.x
- Node.js 24 LTS when frontend tooling is required

#### Scenario: All dependency files match baseline
- **WHEN** developers inspect `pyproject.toml`, `Dockerfile`, README
- **THEN** all SHALL reference the same approved Python and Django versions

#### Scenario: Container images are pinned
- **WHEN** `docker-compose.yml` is inspected
- **THEN** PostgreSQL SHALL use `postgres:18.3-alpine`
- **THEN** Python SHALL use `python:3.14-alpine`

### Requirement: Production security hardening

The platform SHALL enforce production security practices:

- SHALL use environment variables for all secrets
- SHALL enforce HTTPS in production
- SHALL use CSRF protection for all forms
- SHALL use secure cookies with SameSite=Lax
- SHALL have security middleware enabled

#### Scenario: Production settings enforce security
- **WHEN** `settings/production.py` is loaded
- **THEN** `DEBUG=False` and `SECURE_SSL_REDIRECT=True`
- **THEN** CSRF cookies SHALL have `SameSite=Lax`

#### Scenario: Secrets management
- **WHEN** the application runs
- **THEN** no SHALL hardcode secrets in code or config files
- **THEN** SHALL read `SECRET_KEY`, `DATABASE_URL` from environment

### Requirement: Docker production setup

Docker Compose SHALL provide a production-ready setup:

- SHALL use non-root user in web container
- SHALL mount `.env` file for environment variables
- SHALL expose port 8000 with health checks
- SHALL have proper restart policies

#### Scenario: Docker security
- **WHEN** Dockerfile is inspected
- **THEN** SHALL create non-root user `appuser`
- **THEN** SHALL copy files as root then switch to `appuser`

#### Scenario: Production orchestration
- **WHEN** `docker-compose -f docker-compose.prod.yml up` is run
- **THEN** SHALL start web and db services with proper dependencies
- **THEN** SHALL have health checks and auto-restart policies

### Requirement: File upload security

Submission files SHALL be protected from direct public access:

- SHALL use Django's `FileSystemStorage` with non-public paths
- SHALL generate secure download URLs with permission checks
- SHALL NOT serve files via static files or media root

#### Scenario: Protected file access
- **WHEN** an author tries to download their submission
- **THEN** SHALL verify ownership via database query
- **THEN** SHALL generate temporary signed URL

#### Scenario: Public access prevention
- **WHEN** direct URL to submission file is accessed
- **THEN** SHALL return 403 Forbidden for unauthorized requests
- **THEN** SHALL not serve files from static media directories

### Requirement: Backup and recovery

The platform SHALL provide automated backups:

- PostgreSQL dumps SHALL be created daily
- Backups SHALL be encrypted and stored externally
- Restore SHALL be documented and tested

#### Scenario: Backup execution
- **WHEN** the backup service runs
- **THEN** SHALL create compressed PostgreSQL dump
- **THEN** SHALL upload to cloud storage with timestamp

### Requirement: Monitoring and logging

Production SHALL include:

- Application logs with correlation IDs
- Error tracking and alerting
- Performance metrics collection

#### Scenario: Error tracking
- **WHEN** an error occurs
- **THEN** SHALL send error to monitoring service with request context
- **THEN** SHALL alert on-call engineer for critical errors