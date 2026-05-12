# Design: Add Author Submission Initial Flow

## Overview

This change implements the first real scientific workflow in the platform: the initial author submission phase.

It should be narrow, secure and operational. It creates the submission data foundation that later review and final-materials proposals will consume.

## Workflow Boundaries

### Initial submission phase

Included here:

- submission metadata;
- authors and affiliations;
- initial PDF upload;
- author dashboard listing;
- submission confirmation.

Not included here:

- reviewer assignment;
- review forms;
- acceptance/rejection decisions;
- final PDF/poster/video materials;
- proceedings publication.

### Video rule

Video is explicitly out of scope for this phase.

The UI, validation and models must not require or collect video in initial submission.

## Model Design

### Submission

Recommended fields:

```text
id
code
owner
title
abstract
keywords
thematic_axis
presentation_preference
status
created_at
updated_at
submitted_at
```

`code` should be human-readable enough for confirmation e-mails and support, for example:

```text
CBNV2026-0001
```

The exact format can be implementation-defined but must be stable and unique.

### Status design

Keep status minimal:

```text
draft
submitted
withdrawn
```

Avoid adding review statuses such as accepted/rejected in this proposal. Review statuses belong later.

If administrative check status is necessary, document why.

### SubmissionAuthor

Use an ordered child model. Do not store all authors in a single text field.

Recommended fields:

```text
submission
full_name
email
institution
country
orcid
order
is_corresponding
is_presenting
linked_user
```

At least one corresponding author should exist if feasible.

### SubmissionFile

Recommended fields:

```text
submission
file
file_type = initial_pdf
original_filename
size_bytes
content_type
checksum
uploaded_by
uploaded_at
is_current
```

If checksum is too much for MVP, it may be deferred. File size and original filename are useful for audit and support.

## File Storage Design

The storage path should be private or protected.

Recommended path pattern:

```text
submissions/{submission_code}/initial/{uuid}.pdf
```

Avoid:

- user names in file path;
- original filenames as only stored names;
- public `/media/` direct access for protected files.

If the project uses local media in development, protect download access through authenticated views instead of linking directly to `file.url`.

## Form Design

Recommended form sections:

1. Work identification
   - title
   - abstract
   - keywords
   - thematic axis
   - presentation preference if applicable

2. Authors
   - ordered author list
   - corresponding author
   - presenting author

3. File
   - PDF upload
   - accepted format and size note

4. Confirmation
   - rules acknowledgement
   - no-video-in-initial-submission notice

Use formsets for authors if practical. If formsets are too complex for this iteration, use a minimal first version that supports multiple authors without blocking later extension.

## Views and Routes

Recommended route names:

```text
/submissions/dashboard/
/submissions/new/
/submissions/<code>/
/submissions/<code>/edit/
/submissions/<code>/submit/
/submissions/<code>/download/<file_id>/
```

Actual routes may follow project conventions.

Essential views:

- list own submissions;
- create submission;
- edit draft;
- submit final initial submission;
- view detail/status;
- protected file download.

## Author Dashboard Integration

The existing author dashboard should link to submission list/create views.

Recommended dashboard states:

- no submissions yet;
- draft submissions;
- submitted submissions;
- submissions closed;
- profile incomplete.

## Validation Design

### File validation

Validate:

- extension `.pdf`;
- size;
- content type where reliable;
- optionally PDF magic bytes (`%PDF`) if easy.

Do not rely only on browser MIME type.

### Required fields

On final submit:

- title required;
- abstract required;
- thematic axis required if defined by project;
- at least one keyword required if required by rules;
- at least one author required;
- PDF required;
- consent/acknowledgement required if implemented.

### Draft validation

If draft mode exists, allow partial data but do not allow transition to submitted until all required data passes validation.

## Notification Design

Use a service/helper function, for example:

```python
send_submission_confirmation(submission)
```

This keeps e-mail logic out of views.

Failure policy:

- submission should not be lost if e-mail fails;
- failure should be logged;
- user should still see confirmation or a warning depending on implementation.

## Permissions Design

Use object-level checks in views:

```text
request.user == submission.owner
```

For future chair/staff access, add explicit helpers later.

Do not expose file download without checking object ownership.

## Testing Strategy

Minimum tests:

1. login required for create/list/detail;
2. author can create draft/submission;
3. profile author flag is set or required;
4. submission with valid PDF succeeds;
5. non-PDF upload fails;
6. oversized upload fails;
7. video upload or video URL is not accepted/available;
8. other user cannot view submission;
9. other user cannot download file;
10. dashboard lists only current user's submissions;
11. confirmation e-mail is sent with locmem backend;
12. submitted submission is read-only to author.

## Future Integration

`add-review-decision-workflow` will build on:

- `Submission`;
- `SubmissionAuthor`;
- `SubmissionFile`;
- submitted status;
- author dashboard list/detail.

`add-final-materials-proceedings-videos` will later add final files and video links for accepted works.
