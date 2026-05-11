## Why

The public Programacao, Palestrantes and venue sections need canonical domain data before the public-site MVP can render them reliably. Without program, speaker and venue models, the site would depend on ad hoc page copy for official schedules, pending names, address details and map links.

This change prepares the structured event data layer needed by later public pages while keeping editorial copy and final page polish in their own proposals.

## What Changes

- Add or refine CMS/admin-managed models for program days, sessions, activities/talks and speakers/participants.
- Add status and visibility rules for confirmed, pending and hidden speakers or activities.
- Add canonical activity/session types for talks, plenaries, round tables, posters, oral sessions, breaks and institutional moments.
- Add a canonical venue model or settings-backed venue structure covering official venue name, address, map URL and access instructions.
- Add ordering/query behavior so public pages can render program data chronologically without template-specific hardcoding.
- Add seed/data-loading support for the preliminary official program when canonical source data is available.
- Add focused tests for visibility, ordering, relationship integrity and venue data behavior.
- Do not implement the final public Programacao/Palestrantes pages, final editorial copy, registration, submissions, payments, certificates or external API integrations.

## Capabilities

### New Capabilities

- `venue`: Canonical venue and access information for the event, including official location data, map links and public visibility rules.

### Modified Capabilities

- `program`: Refine the existing programming and speaker requirements so program days, sessions, activities, speakers, statuses and venue references can support the public-site MVP without ad hoc text.

## Impact

- Affected Django/Wagtail apps are expected to include the program domain app and whichever app owns global event settings or venue content.
- Database migrations will be required for new or refined program, speaker and venue models.
- Wagtail admin/snippet configuration will be affected for single-admin data entry.
- Later public-site templates will consume these models but are not delivered by this change.
- Test coverage should include model validation, query helpers, publication/visibility behavior and canonical seed behavior where implemented.
