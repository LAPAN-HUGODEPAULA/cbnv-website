# Revisões (reviews)

## Purpose
Gerenciar a atribuição de revisões e o acompanhamento do status de avaliações por revisores e chairs.
## Requirements
### Requirement: Nenhum fluxo de revisão na base de contas
A base de contas/dashboard SHALL NOT implementar atribuição de revisão, formulários de revisão ou fluxo de trabalho de decisão.

#### Scenario: Dashboard de revisor existe antes do fluxo de revisão
- **GIVEN** que o dashboard de revisor está implementado
- **WHEN** um revisor o abre
- **THEN** ele PODE exibir um placeholder de revisões atribuídas futuras
- **AND** SHALL NOT criar atribuições de revisão ou formulários de revisão.

### Requirement: Ponto de integração futuro para revisões
Os dashboards de revisor e chair SHALL fornecer pontos de integração claros para a implementação posterior do fluxo de trabalho de revisão.

#### Scenario: Proposta de revisão posterior inicia
- **GIVEN** que os shells de dashboard de revisor e chair existem
- **WHEN** o fluxo de trabalho de revisão for implementado posteriormente
- **THEN** ele SHALL ser capaz de anexar comportamento de atribuição de revisão e decisão sem substituir a base de autenticação.

### Requirement: Review Assignment List for Reviewers
The system SHALL display a list of all submissions assigned to the authenticated reviewer for evaluation.

#### Scenario: Reviewer sees assigned tasks
- **WHEN** a reviewer accesses their dashboard
- **THEN** they see a list of works they are assigned to review, with clear "Evaluation Pending" status.

### Requirement: Review Status for Chairs
The system SHALL allow Chairs to track the progress of all reviews in the system. O Manager de Review (ou ReviewAssignment) SHALL fornecer métodos de agregação: `by_reviewer()`, `by_status()`, `completion_stats()` e `top_reviewers(limit=10)`.

#### Scenario: Chair monitors reviews
- **WHEN** a Chair accesses the review management view
- **THEN** they can see which submissions have completed reviews and which are still pending.

#### Scenario: Reports consulta métricas de revisão
- **WHEN** o app reports chama métodos de agregação do manager de revisão
- **THEN** SHALL retornar contagens por status, por revisor e tempo médio de conclusão

#### Scenario: Reports consulta top revisores
- **WHEN** o app reports chama `top_reviewers(limit=10)`
- **THEN** SHALL retornar os N revisores com mais revisões concluídas, ordenados por contagem decrescente

### Requirement: Review Export QuerySet
O Manager de Review SHALL fornecer método `export_queryset()` que retorna queryset otimizado com `select_related` para submissão e revisor, para exportação detalhada.

#### Scenario: Export de revisões
- **WHEN** chamado o método de export do manager
- **THEN** SHALL retornar queryset com revisor, submissão, status e datas, com joins otimizados

### Requirement: Reviewer assignment
The scientific commission SHALL be able to assign one or more reviewers to a submission that is in the "Submitted" status.

#### Scenario: Assigning a reviewer
- **WHEN** a commission member selects a reviewer for a specific work
- **THEN** an assignment record SHALL be created and the submission status SHALL transition to "Under Review"

### Requirement: Reviewer feedback form
Reviewers SHALL provide feedback through a standardized form including a recommendation (Accept, Reject, Corrections) and qualitative comments.

#### Scenario: Submitting a review
- **WHEN** a reviewer completes the feedback form and submits
- **THEN** the review SHALL be saved and the commission SHALL be notified

### Requirement: Single-blind review
The system SHALL support single-blind review where reviewers can see author names but authors CANNOT see reviewer names.

#### Scenario: Author viewing review
- **WHEN** an author views their work's feedback
- **THEN** the reviewer's identity SHALL be hidden, showing only the comments and recommendations

### Requirement: Accessible Review Forms
Review forms SHALL use standard `<label>` elements for all inputs and ensure that instructions (e.g., scoring rubrics) are associated with fields via `aria-describedby`.

#### Scenario: Review input has label
- **WHEN** a reviewer accesses the evaluation form
- **THEN** every numeric input and text area SHALL have a programmatically associated label

### Requirement: Keyboard-Friendly Rating Scales
Numeric rating scales (e.g., 1-5) SHALL be implemented using accessible radio groups or dropdowns that support standard keyboard interactions (arrow keys, space).

#### Scenario: Rating via keyboard
- **WHEN** a reviewer uses arrow keys to navigate a rating scale
- **THEN** the selection SHALL update and be announced by the screen reader


