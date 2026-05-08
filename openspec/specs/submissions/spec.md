# Submissões (submissions)

## Purpose
Gerenciar o ciclo de vida de submissões de trabalhos científicos, incluindo listagem para autores e painel de controle para chairs.

## Requirements

### Requirement: Submission List for Authors
The system SHALL display a list of all submissions owned by the authenticated author in their dashboard.

#### Scenario: Author sees empty submission list
- **WHEN** an author with no submissions accesses the submissions list
- **THEN** they see an "Empty State" component with a "New Submission" CTA (even if disabled).

### Requirement: Submission Dashboard for Chairs
The system SHALL provide a view for Chairs to see all submissions in the system, with filtering by status and category. O Manager de Submission SHALL fornecer métodos de agregação para consultas de indicadores: `by_status()`, `by_topic()`, `by_modality()`, `by_institution()` e `summary_stats()`.

#### Scenario: Chair views all submissions
- **WHEN** a user with `is_chair=True` accesses the Chair Dashboard
- **THEN** they see a table with all submitted works and their current status.

#### Scenario: Reports consulta agregações por estado
- **WHEN** o app reports chama `Submission.objects.by_status()`
- **THEN** SHALL retornar queryset com `values('status').annotate(count=Count('id'))` ordenado por contagem decrescente

#### Scenario: Reports consulta agregações por eixo e modalidade
- **WHEN** o app reports chama `Submission.objects.by_topic()` ou `by_modality()`
- **THEN** SHALL retornar queryset com contagens agrupadas pelo campo respectivo

#### Scenario: Reports consulta stats resumidos
- **WHEN** o app reports chama `Submission.objects.summary_stats()`
- **THEN** SHALL retornar dicionário com total, contagem por estado e datas (primeira/última submissão)

### Requirement: Submission status machine
A máquina de estados da submissão SHALL implementar as transições finais:
- `accepted_oral` / `accepted_poster` / `accepted_video` → `final_materials_pending` (quando a comissão solicita materiais finais)
- `final_materials_pending` → `ready_for_proceedings` (quando a comissão valida materiais)
- `ready_for_proceedings` → `published_in_proceedings` (quando a comissão publica nos anais)

#### Scenario: Chair requests final materials
- **WHEN** a comissão solicita materiais finais para um trabalho aprovado
- **THEN** a submissão SHALL transitar para `final_materials_pending` e uma notificação SHALL ser enviada ao autor

#### Scenario: Author uploads materials
- **WHEN** o autor faz upload dos materiais finais para uma submissão em `final_materials_pending`
- **THEN** os materiais SHALL ser armazenados e uma confirmação SHALL ser enviada ao autor

#### Scenario: Author cannot upload for wrong status
- **GIVEN** uma submissão com status diferente de `final_materials_pending`
- **WHEN** o autor tenta acessar a página de upload de materiais
- **THEN** o sistema SHALL exibir uma mensagem informando que materiais não são necessários

### Requirement: Author final materials page
O autor SHALL ter uma página dedicada para upload de materiais finais quando sua submissão está em `final_materials_pending`.

#### Scenario: Author accesses materials page
- **WHEN** o autor acessa a página de materiais finais para sua submissão aprovada
- **THEN** SHALL ver o formulário de upload com campos para PDF final, apresentação e link de vídeo (quando aplicável)

#### Scenario: Author re-uploads materials
- **GIVEN** uma submissão em `final_materials_pending` com materiais já enviados
- **WHEN** o autor faz upload de novos materiais
- **THEN** os materiais anteriores SHALL ser substituídos e `received_at` SHALL ser atualizado

### Requirement: Submission Export QuerySet
O Manager de Submission SHALL fornecer método `export_queryset(filters=None)` que retorna queryset otimizado com `select_related` para exportação detalhada, aceitando filtros opcionais (status, eixo, modalidade).

#### Scenario: Export com filtros
- **WHEN** chamado `Submission.objects.export_queryset(filters={'status': 'accepted_oral'})`
- **THEN** SHALL retornar queryset filtrado com `select_related` aplicado

#### Scenario: Export sem filtros
- **WHEN** chamado `Submission.objects.export_queryset()`
- **THEN** SHALL retornar queryset completo com `select_related` aplicado

### Requirement: Final decision and modality
The scientific commission SHALL issue a final decision (Accepted, Rejected, Accepted with Corrections) and assign a presentation modality (Oral, Poster, Video).

#### Scenario: Issuing an acceptance decision
- **WHEN** the commission selects "Accepted" and modality "Oral"
- **THEN** the submission status SHALL transition to "Accepted" and the modality SHALL be recorded

### Requirement: Revision submission for corrections
If a work is "Accepted with Corrections", the author SHALL be allowed to upload a revised PDF file.

#### Scenario: Author uploads revised PDF
- **WHEN** a submission is in "Accepted with Corrections" status and the author uploads a new file
- **THEN** the system SHALL store the revised file and notify the commission

### Requirement: Simplified author status language
The author dashboard SHALL display submission status using user-friendly terms: "In Evaluation" (for Under Review), "Pending Corrections" (for Accepted with Corrections), and "Finalized" (for Accepted/Rejected).

#### Scenario: Author checks dashboard status
- **WHEN** a submission is internally "Under Review"
- **THEN** the author dashboard SHALL display "In Evaluation"

### Requirement: Accessible Validation Feedback
Form validation errors SHALL be announced by screen readers using `aria-live="polite"` and explicitly linked to input fields via `aria-describedby`.

#### Scenario: Form error announced
- **WHEN** an author submits an invalid form
- **THEN** the error message SHALL be automatically announced by the screen reader
- **AND** focus SHALL be moved to the first invalid field

### Requirement: Protected File Information Accessibility
Submission metadata (titles, authors) SHALL be accessible to screen readers, while file download links SHALL have descriptive `aria-label` attributes (e.g., "Download PDF for [Submission Title]").

#### Scenario: Accessible download links
- **WHEN** a Chair views the list of submissions
- **THEN** each download link SHALL contain an `aria-label` that includes the submission title for context

### Requirement: Submission Progress Indicator
The submission workflow SHALL include a progress indicator that is semantically clear to assistive technologies.

#### Scenario: Progress step identified
- **WHEN** an author is on the second step of submission
- **THEN** the progress bar SHALL use `aria-current="step"` to identify the active phase

### Requirement: Protected submission file serving
Arquivos anexados a submissões (PDF, arquivos complementares) SHALL ser servidos exclusivamente via view autorizada do Django. A view SHALL verificar se o usuário autenticado é dono da submissão ou membro da equipe editorial (staff). O serving SHALL usar X-Accel-Redirect para delegar ao Nginx. A URL pública SHALL ser do tipo `/submissions/<id>/download/<file_id>/` e não SHALL expor o caminho real no sistema de arquivos.

#### Scenario: Author downloads own submission file
- **WHEN** o autor autenticado acessa `/submissions/<id>/download/<file_id>/` e é dono da submissão
- **THEN** o Django verifica permissão, retorna header `X-Accel-Redirect` para o Nginx e o arquivo é transmitido ao cliente

#### Scenario: Staff downloads any submission file
- **WHEN** um usuário staff acessa `/submissions/<id>/download/<file_id>/`
- **THEN** o arquivo SHALL ser servido independentemente de ser o dono

#### Scenario: Non-owner gets access denied
- **WHEN** um usuário autenticado que não é dono e não é staff acessa `/submissions/<id>/download/<file_id>/`
- **THEN** SHALL retornar HTTP 403 Forbidden

#### Scenario: Unauthenticated user gets redirected
- **WHEN** um usuário não autenticado acessa `/submissions/<id>/download/<file_id>/`
- **THEN** SHALL retornar HTTP 302 redirect para a página de login

#### Scenario: Direct media URL returns 404
- **WHEN** uma requisição é feita para `/media/submissions/<qualquer-caminho>`
- **THEN** o Nginx SHALL retornar HTTP 404

## Notes

- `SubmissionAuthor.full_name` is intentionally separate from `User.first_name`/`last_name`. Co-authors on a submission may not have user accounts, so their names are stored as plain text on the submission model, not linked to the User model.
