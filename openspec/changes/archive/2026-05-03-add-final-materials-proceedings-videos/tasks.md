## 1. Model and Extensions

- [x] 1.1 Create `FinalMaterial` model in `proceedings/models.py` with fields: submission (OneToOne), final_pdf, presentation_file, video_url, received_at, validated_at, validated_by, notes.
- [x] 1.2 Add file validation logic (PDF only for final_pdf, PDF/PPTX for presentation_file, max sizes).
- [x] 1.3 Add `video_url` validation using `parse_youtube_url` from `videos/models.py`.
- [x] 1.4 Run migrations.

## 2. Commission: Materials Management

- [x] 2.1 Create view for requesting final materials (transitions submission to `final_materials_pending`).
- [x] 2.2 Create view for listing submissions with pending/ready materials (commission view).
- [x] 2.3 Create view for validating materials (sets `validated_at`/`validated_by`, transitions to `ready_for_proceedings`).
- [x] 2.4 Create view for publishing to proceedings (transitions to `published_in_proceedings`).
- [x] 2.5 Add commission templates (materials management list, validation form, publish button).

## 3. Author: Materials Upload

- [x] 3.1 Create view for author materials upload page (only for `final_materials_pending` status).
- [x] 3.2 Implement file upload form with validation (FinalMaterialForm).
- [x] 3.3 Handle re-upload scenario (replace existing materials, update `received_at`).
- [x] 3.4 Create author materials upload template.
- [x] 3.5 Update author dashboard to show link to materials upload when applicable.

## 4. Notifications

- [x] 4.1 Implement notification for materials requested (email to author with instructions).
- [x] 4.2 Implement notification for materials received (confirmation to author).
- [x] 4.3 Implement notification for materials validated (acceptance to author).
- [x] 4.4 Implement notification for proceedings publication (email with link to public proceedings).
- [x] 4.5 Create email templates (HTML + text) for all 4 notifications.

## 5. Public Proceedings Page

- [x] 5.1 Create public proceedings listing view (filtered by `published_in_proceedings`).
- [x] 5.2 Add filtering by modality and thematic axis.
- [x] 5.3 Create public proceedings template with metadata, abstract, and download link.
- [x] 5.4 Add embedded YouTube player for works with `video_url`.
- [x] 5.5 Create public PDF download view (only for published works).
- [x] 5.6 Wire up public URL (`/anais/`).

## 6. Commission Dashboard Integration

- [x] 6.1 Update commission dashboard to show proceedings progress (pending materials, validated, published).
- [x] 6.2 Add proceedings management links to commission sidebar navigation.

## 7. Verification and Tests

- [x] 7.1 Add tests for FinalMaterial model creation and validation.
- [x] 7.2 Add tests for author materials upload flow (valid files, invalid files, re-upload).
- [x] 7.3 Add tests for commission validation and publication flow (state transitions).
- [x] 7.4 Add tests for public proceedings page (published visible, unpublished hidden).
- [x] 7.5 Add tests for PDF download permissions (published = allowed, unpublished = forbidden).
- [x] 7.6 Add tests for all 4 notification events.
- [x] 7.7 Add tests for video URL validation in FinalMaterial.
