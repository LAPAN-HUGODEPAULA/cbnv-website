## Why

Trabalhos aprovados precisam de um fluxo para entrega de materiais finais (versão final do PDF, apresentação, vídeo para apresentações orais), geração dos anais digitais e publicação no site público. Atualmente, os estados `final_materials_pending`, `ready_for_proceedings` e `published_in_proceedings` existem na máquina de estados, mas não há views, modelos ou lógica que os implementem.

## What Changes

- **Fluxo de Material Final**: Authors upload a revised PDF, presentation file, and optionally a YouTube video link. The commission validates and marks materials as received.
- **Anais Digitais**: Commission can mark accepted works as "ready for proceedings" and publish them to the public proceedings page.
- **Vídeos por Trabalho**: Associate YouTube video links with accepted oral/video presentations. No self-hosting.
- **Página Pública de Anais**: Public page listing all published proceedings with metadata, authors, and links.
- **Página Pública de Trabalhos Aprovados**: Public listing of accepted works with abstracts and modality.
- **Notificações**: Alerts for authors when materials are requested, received, validated, and published.

## Capabilities

### New Capabilities
(nenhuma — as capacidades necessárias já possuem specs base)

### Modified Capabilities
- `proceedings`: Extending from historical editions management to full current-edition proceedings workflow (material collection, validation, publication).
- `submissions`: Adding final materials upload flow and "published" state visibility.
- `videos`: Adding association between accepted submissions and YouTube video links.
- `public-site`: Adding proceedings and accepted works public pages.
- `notifications`: Adding email templates for final materials lifecycle events.

## Impact

- **Models**: New `FinalMaterial` model. Update `Submission` for `is_published` flag. Optional FK from accepted submissions to `VideoResource`.
- **Views**: Author materials upload, commission validation dashboard, public proceedings page.
- **State Machine**: Transitions `accepted_* → final_materials_pending → ready_for_proceedings → published_in_proceedings` become functional.
- **Templates**: New templates for materials upload, validation, and public proceedings.
- **Emails**: New notification templates for material request, receipt, validation, and publication.
