# Delta: Submissões (submissions)

## MODIFIED Requirements

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

## ADDED Requirements

### Requirement: Submission Export QuerySet
O Manager de Submission SHALL fornecer método `export_queryset(filters=None)` que retorna queryset otimizado com `select_related` para exportação detalhada, aceitando filtros opcionais (status, eixo, modalidade).

#### Scenario: Export com filtros
- **WHEN** chamado `Submission.objects.export_queryset(filters={'status': 'accepted_oral'})`
- **THEN** SHALL retornar queryset filtrado com `select_related` aplicado

#### Scenario: Export sem filtros
- **WHEN** chamado `Submission.objects.export_queryset()`
- **THEN** SHALL retornar queryset completo com `select_related` aplicado
