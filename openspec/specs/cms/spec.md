# cms Specification

## Purpose
TBD - created by archiving change produce-public-site-content-round-1. Update Purpose after archive.
## Requirements
### Requirement: Content is mapped to CMS or implementation targets

Every produced content block SHALL identify whether it belongs in CMS, seed data, page fields, templates or a later proposal.

#### Scenario: Content target is clear

Given a copy-map row exists  
When an implementer reads it  
Then they SHALL know whether the content should be stored in a CMS field, seed command, Wagtail page body, template placeholder or deferred.

### Requirement: Avoid schema expansion during content production

The content-production change SHALL avoid adding new CMS fields unless separately justified.

#### Scenario: Missing field is discovered

Given the content producer finds no appropriate target field  
When documenting the copy map  
Then they SHOULD mark the block as `needs-field` or `defer` rather than adding unapproved schema.

### Requirement: Safe content implementation

If content is applied to seed data or editable page fields, it SHALL not overwrite human-edited content without an explicit documented reason.

#### Scenario: Seed content update

Given a seed command is updated with round-1 copy  
When the command is run on a database with existing manually edited content  
Then overwrite behavior SHALL follow the documented seed policy.

