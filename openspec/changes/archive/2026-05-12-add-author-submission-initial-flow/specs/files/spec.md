# files

## Purpose

Define protected handling, validation, and access rules for initial submission PDF files.

## ADDED Requirements

### Requirement: Initial PDF upload

The initial submission flow SHALL accept a PDF file as the initial submission document.

#### Scenario: Valid PDF uploaded

Given an author uploads a valid PDF within the configured size limit  
When the submission is finalized  
Then the PDF SHALL be stored as the initial submission file.

### Requirement: Non-PDF files rejected

The initial submission flow SHALL reject non-PDF files.

#### Scenario: Non-PDF uploaded

Given an author uploads a file that is not a PDF  
When validation runs  
Then the form SHALL reject the file with a clear error message.

### Requirement: Oversized files rejected

The initial submission flow SHALL enforce a maximum file size.

#### Scenario: Oversized PDF uploaded

Given an author uploads a PDF larger than the configured maximum size  
When validation runs  
Then the form SHALL reject the file with a clear error message.

### Requirement: Uploaded files are protected

Initial submission files SHALL NOT be publicly accessible by direct public URL.

#### Scenario: Another user requests file

Given a submission file belongs to another author  
When an authenticated user requests the file  
Then access SHALL be denied.

#### Scenario: Anonymous visitor requests file

Given a submission file exists  
When an anonymous visitor requests the file  
Then access SHALL be denied or redirected to login.
