# videos

## Purpose

Define verification requirements for YouTube link terminology, public gallery visibility, explicit video promotion and video-resource consistency.

## ADDED Requirements

### Requirement: Video link terminology consistency

The audit MUST verify consistent terminology for YouTube links and video resources.

#### Scenario: YouTube URL displayed

Given a final material includes a YouTube URL
When public, chair and report surfaces are reviewed
Then video terminology MUST be consistent.

### Requirement: No automatic gallery publication consistency

The audit MUST verify that final-material video URLs are not represented as public gallery items unless explicitly promoted.

#### Scenario: Final material video exists

Given a final material has a YouTube URL but no public video resource association
When the public video gallery is reviewed
Then the video MUST not appear as public gallery content.
