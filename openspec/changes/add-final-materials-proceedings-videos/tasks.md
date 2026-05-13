# Tasks: Add Final Materials, Proceedings and Videos

## OpenSpec hygiene

- [x] Create `openspec/changes/add-final-materials-proceedings-videos/`.
- [x] Add `proposal.md`.
- [x] Add `design.md`.
- [x] Add `tasks.md`.
- [x] Add delta spec `specs/proceedings/spec.md`.
- [x] Add delta spec `specs/videos/spec.md`.
- [x] Add delta spec `specs/submissions/spec.md`.
- [x] Add delta spec `specs/notifications/spec.md`.
- [x] Add delta spec `specs/dashboards/spec.md`.
- [x] Add delta spec `specs/security/spec.md`.
- [x] Add delta spec `specs/qa/spec.md`.
- [x] Ensure every delta spec starts with `# <capability-name>`.
- [x] Ensure every delta spec includes `## Purpose`.
- [x] Ensure every requirement uses `MUST`.
- [x] Ensure every requirement has at least one `#### Scenario:` block.
- [x] Run `openspec validate add-final-materials-proceedings-videos --strict`.

## FinalMaterial model

- [x] Implement or update `FinalMaterial`.
- [x] Add relation to `Submission`.
- [x] Add final PDF field using protected storage.
- [x] Add optional presentation file field using protected storage.
- [x] Add optional YouTube URL field.
- [x] Add `publication_authorized` boolean field with default `False`.
- [x] Add received timestamp.
- [x] Add validated timestamp.
- [x] Add validator user relation.
- [x] Add internal notes field.
- [x] Add optional `video_resource` relation or equivalent explicit association mechanism.
- [x] Add migrations.

## Publication authorization

- [x] Add publication authorization checkbox to `FinalMaterialForm`.
- [x] Make the checkbox required before final material is considered complete.
- [x] Add clear authorization text in Brazilian Portuguese.
- [x] Prevent ready-for-proceedings transition without authorization.
- [x] Add tests for missing authorization.
- [x] Add tests for accepted authorization.

## File validation

- [x] Validate final PDF extension and size.
- [x] Validate presentation file extension and size.
- [x] Accept presentation formats PDF and PPTX.
- [x] Keep protected/private media storage.
- [x] Avoid direct public protected file URLs.
- [x] Add unauthorized file access tests.

## YouTube and video handling

- [x] Implement or verify YouTube URL parser.
- [x] Validate submitted YouTube URLs.
- [x] Ensure no full video file upload is supported.
- [x] Ensure submitted YouTube URL does not automatically publish to public gallery.
- [x] Add optional `VideoResource` association or explicit promotion action.
- [x] Add tests for invalid YouTube URLs.
- [x] Add tests that submitted video URL alone does not create public gallery item.
- [x] Add tests for explicit promotion/association if implemented.

## Submission status integration

- [x] Add or verify accepted statuses: `accepted_oral`, `accepted_poster`, `accepted_video`.
- [x] Add or verify final-material statuses: `final_materials_pending`, `ready_for_proceedings`, `published_in_proceedings`.
- [x] Implement safe status transition for requesting final materials.
- [x] Implement safe status transition after final-material validation.
- [x] Add transition tests.

## Committee workflow

- [x] Add `Solicitar materiais` action to the submissions management page.
- [x] Show action only for accepted submissions.
- [x] Implement request-materials view/service.
- [x] Restrict action to chair/scientific committee users.
- [x] Add success/error messages.
- [x] Add tests for allowed and denied access.

## Author workflow

- [x] Add author final-material upload view.
- [x] Restrict upload to submission owner.
- [x] Allow upload only after materials have been requested.
- [x] Add final-material detail/status view for author if needed.
- [x] Integrate with author dashboard.
- [x] Add tests for owner access and unauthorized access.

## Committee validation workflow

- [x] Add final-material management list.
- [x] Add final-material validation view.
- [x] Restrict validation to chair/scientific committee users.
- [x] Record `validated_at`.
- [x] Record `validated_by`.
- [x] Move submission to ready-for-proceedings state when valid.
- [x] Add validation tests.

## Chair dashboard integration

- [x] Update `dashboard/chair.html`.
- [x] Add link/card to `Gerenciar submissões`.
- [x] Add link/card to `Gerenciar materiais finais`.
- [x] Add link/card to `Ver anais`.
- [x] Add link/card to `Galeria de vídeos`.
- [x] Reduce placeholder-only copy.
- [x] Add smoke test if dashboard tests exist.

## Proceedings and editions

- [x] Implement or verify `Edition` snippet/model.
- [x] Support previous edition metadata.
- [x] Implement or verify public proceedings list page.
- [x] Implement or verify public proceedings detail page.
- [x] Display only ready/published proceedings items.
- [x] Ensure previous editions are framed as archive/history.

## Notifications

- [x] Implement notification for materials requested.
- [x] Implement notification for materials received.
- [x] Implement notification for materials validated.
- [x] Ensure notification failure does not corrupt workflow state.
- [x] Add e-mail tests if notification service exists.

## Admin

- [x] Register `FinalMaterial` in admin if needed.
- [x] Configure list display/search/filter.
- [x] Avoid unsafe direct protected file links.
- [x] Register or verify `Edition` snippet/admin.

## Security

- [x] Require login for author upload.
- [x] Require owner permission for author upload/detail.
- [x] Require chair/scientific committee permission for request/validation.
- [x] Protect files.
- [x] Avoid IDOR in final-material routes.
- [x] Verify public proceedings pages do not expose private files improperly.

## Tests

- [x] Test accepted submission can receive materials request.
- [x] Test non-accepted submission cannot receive materials request.
- [x] Test final-material upload with authorization.
- [x] Test final-material upload without authorization fails or remains incomplete.
- [x] Test PDF validation.
- [x] Test presentation validation.
- [x] Test YouTube URL validation.
- [x] Test author ownership checks.
- [x] Test committee validation permissions.
- [x] Test validation timestamp and validator recording.
- [x] Test video URL does not auto-publish to gallery.
- [x] Test explicit video promotion/association if implemented.
- [x] Test chair dashboard links render.

## Validation

- [x] Run `openspec validate add-final-materials-proceedings-videos --strict`.
- [x] Run `uv run python manage.py check`.
- [x] Run `uv run python manage.py makemigrations --check --dry-run`.
- [x] Run `uv run pytest`.
- [x] Run `npm run build` if templates/CSS changed.

## PR checklist

- [x] Branch is `change/add-final-materials-proceedings-videos`.
- [ ] PR title starts with `[add-final-materials-proceedings-videos]`.
- [ ] PR body includes `Closes #14` or the current issue number.
- [x] PR includes `proposal.md`, `design.md`, and `tasks.md`.
- [x] PR does not implement automatic public video publication.
- [x] PR does not implement payment/certificates/QR/external registration.
- [x] PR includes tests for publication authorization and permissions.
