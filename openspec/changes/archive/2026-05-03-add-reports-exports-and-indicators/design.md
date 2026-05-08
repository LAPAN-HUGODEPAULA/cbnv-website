## Context

O app `reports/` já existe com views e urls básicos. O app precisa ser expandido com dashboard de indicadores, agregações ORM e exportação em CSV/JSON. Os dados vivem em `submissions/`, `reviews/`, `proceedings/` e `accounts/` — o reports app consulta esses modelos sem alterá-los diretamente (managers com métodos de agregação). Acesso restrito a staff/superuser e chairs.

Tech stack: Django ORM `annotate()`/`values()` para agregações, `csv` e `json` stdlib para exports, Tailwind para dashboard templates.

## Goals / Non-Goals

**Goals:**
- Dashboard de KPIs com cards, tabelas resumo e filtros por período/estado
- Exportação CSV e JSON de indicadores agregados e listagens detalhadas
- Queries otimizadas que não degradam com volume crescente de submissões
- Cobertura de testes para permissões e consistência dos dados exportados

**Non-Goals:**
- BI complexo (graficos interativos, drill-down, widgets customizáveis)
- Integração automática com UFMG/FUNDEP/Sympla
- Dashboard público — acesso exclusivo de comissão/admin
- Streaming de exports grandes (batch size fixo é suficiente para escala do evento)
- Cache de agregações (volume do evento (<5k submissões) não justifica)

## Decisions

### 1. Agregações via custom QuerySet Managers nos apps de domínio

**Decisão:** Adicionar métodos de agregação como métodos de custom Manager em `submissions`, `reviews` e `proceedings`, consumidos pelo app `reports`.

**Alternativa:** Queries diretas no app `reports` via `Submissions.objects.annotate(...)`.
**Racional:** Managers encapsulam lógica de agregação perto dos modelos, facilitam reuso e testes unitários. O app `reports` fica como camada de apresentação/orquestração.

### 2. Exportação via Django HttpResponse com stdlib csv/json

**Decisão:** Usar `HttpResponse` com `content_type` apropriado e `csv.writer`/`json.dump` da stdlib.

**Alternativa:** Bibliotecas como `django-import-export` ou `djangorestframework` serializers.
**Racional:** Formatos simples (CSV flat, JSON de agregações), sem necessidade de serialização complexa. Evita dependência adicional.

### 3. Formato dos exports — dois tipos

**Decisão:** Dois tipos de export:
- **Indicadores (agregados):** summary por categoria (estado, eixo, modalidade, instituição)
- **Listagem detalhada:** registros individuais (submissões, revisores, autores, proceedings)

Cada export aceita `format=csv|json` via query parameter.

**Alternativa:** Um único endpoint com tudo misturado.
**Racional:** Separar permite que a comissão baixe resumos executivos (indicadores) ou dados completos para análise externa.

### 4. Permissões via decorator `@admin_or_chair_required`

**Decisão:** Criar decorator em `accounts/decorators.py` (já existe) que verifica `is_staff` OU `is_chair`. Todas as views de reports usam esse decorator.

**Alternativa:** Django Guardian ou per-object permissions.
**Racional:** Modelo simples (editorial = staff, transacional = chair) já definido no spec de accounts. Sem necessidade de RBAC granular para esta change.

### 5. Templates server-side com Tailwind

**Decisão:** Dashboard renderizado server-side com template Django + Tailwind. Sem HTMX para esta change — os dados são read-only e os exports são downloads.

**Alternativa:** HTMX partials para atualizar cards sem reload.
**Racional:** Dashboard consultado poucas vezes ao dia. Sem benefício mensurável de interatividade client-side. Pode evoluir depois se necessário.

### 6. Estrutura de URLs

```
/reports/                          — Dashboard principal (KPIs + tabelas)
/reports/submissions/export/       — Export detalhado de submissões
/reports/reviews/export/           — Export detalhado de revisões
/reports/proceedings/export/       — Export de proceedings/materiais
/reports/indicators/export/        — Export de indicadores agregados
/reports/authors/export/           — Export de autores e instituições
```

### 7. Queries de agregação — estratégia

Submissões por estado:
```python
Submission.objects.values('status').annotate(count=Count('id'))
```

Submissões por eixo + modalidade:
```python
Submission.objects.values('topic', 'modality').annotate(count=Count('id'))
```

Autores por instituição:
```python
SubmissionAuthor.objects.values('institution').annotate(count=Count('id')).order_by('-count')
```

Revisores com métricas:
```python
ReviewAssignment.objects.values('reviewer').annotate(
    assigned=Count('id'),
    completed=Count('id', filter=Q(status='completed'))
)
```

Materiais finais pendentes:
```python
Submission.objects.filter(status__in=['accepted_oral', 'accepted_poster', 'accepted_video']).annotate(
    has_final=Count('finalmaterial')
).filter(has_final=0)
```

Todas as queries usam `select_related`/`prefetch_related` conforme necessário para evitar N+1.

## Risks / Trade-offs

- **[Volume de dados]** → Para <5k submissões (típico de congresso nacional), agregações em tempo real são viáveis. Se crescer, adicionar `date_hierarchy` e filtros obrigatórios de período.
- **[Consistência de exports]** → Testes de snapshot garantem que formato CSV/JSON não muda inesperadamente entre deploys.
- **[N+1 em listagens]** → Queries de export detalhado usam `select_related` para submissão + autores + revisores. Monitorar com `django-silk` ou `django-debug-toolbar` se necessário.
- **[Permissões]** → Decorador único simplifica, mas se futuramente precisar de acesso diferenciado (chair vs. admin), refatorar para mixin ou CBV com `get_queryset()` filtrado por role.
