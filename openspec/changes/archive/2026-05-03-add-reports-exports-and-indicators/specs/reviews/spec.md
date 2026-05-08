# Delta: Revisões (reviews)

## MODIFIED Requirements

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

## ADDED Requirements

### Requirement: Review Export QuerySet
O Manager de Review SHALL fornecer método `export_queryset()` que retorna queryset otimizado com `select_related` para submissão e revisor, para exportação detalhada.

#### Scenario: Export de revisões
- **WHEN** chamado o método de export do manager
- **THEN** SHALL retornar queryset com revisor, submissão, status e datas, com joins otimizados
