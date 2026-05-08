## 1. Custom Managers — Agregações nos apps de domínio

- [x] 1.1 Criar custom Manager em `submissions/managers.py` com métodos `by_status()`, `by_topic()`, `by_modality()`, `by_institution()`, `summary_stats()` e `export_queryset(filters=None)`
- [x] 1.2 Criar custom Manager em `reviews/managers.py` com métodos `by_reviewer()`, `by_status()`, `completion_stats()`, `top_reviewers(limit=10)` e `export_queryset()`
- [x] 1.3 Criar custom Manager em `proceedings/managers.py` com métodos `materials_status()` e `export_queryset()`
- [x] 1.4 Registrar custom managers nos modelos respectivos (`objects = SubmissionManager()`, etc.)
- [x] 1.5 Escrever testes unitários para cada método de agregação (verificar contagens, ordenação, filtros)

## 2. App Reports — Views e URLs

- [x] 2.1 Criar view `ReportsDashboardView` (CBV) com contexto de KPIs gerais
- [x] 2.2 Criar view `SubmissionIndicatorsView` — tabela de submissões por estado, eixo e modalidade
- [x] 2.3 Criar view `ReviewIndicatorsView` — métricas de revisão, top revisores
- [x] 2.4 Criar view `AuthorIndicatorsView` — ranking de instituições, contagem de autores
- [x] 2.5 Criar view `MaterialsIndicatorsView` — materiais entregues vs. pendentes, proceedings publicados
- [x] 2.6 Configurar URLs em `reports/urls.py` com as rotas do design
- [x] 2.7 Garantir que todas as views usam `@admin_or_chair_required` (verificar `accounts/decorators.py`)

## 3. Exportação — CSV e JSON

- [x] 3.1 Criar utilitário `reports/export.py` com funções `export_csv(queryset, headers, filename)` e `export_json(data, filename)`
- [x] 3.2 Criar view `IndicatorsExportView` — export agregados em CSV/JSON via `?format=csv|json`
- [x] 3.3 Criar view `SubmissionsExportView` — export detalhado com filtro opcional de status
- [x] 3.4 Criar view `ReviewsExportView` — export detalhado de revisões
- [x] 3.5 Criar view `ProceedingsExportView` — export de proceedings e materiais
- [x] 3.6 Criar view `AuthorsExportView` — export de autores e instituições
- [x] 3.7 Registrar URLs de export em `reports/urls.py`

## 4. Templates — Dashboard

- [x] 4.1 Criar template base `reports/base.html` (estende `base.html` do projeto)
- [x] 4.2 Criar template `reports/dashboard.html` com cards de KPI (Tailwind dark-mode)
- [x] 4.3 Criar partials para cada seção: `_kpi_cards.html`, `_submissions_table.html`, `_reviews_table.html`, `_authors_table.html`, `_materials_table.html`
- [x] 4.4 Adicionar botões de export em cada seção (links com `?format=csv` e `?format=json`)
- [x] 4.5 Garantir responsividade mobile (Tailwind responsive breakpoints)

## 5. Navegação — Links no admin/chair dashboard

- [x] 5.1 Adicionar link "Relatórios e Indicadores" na sidebar/navegação do chair dashboard
- [x] 5.2 Verificar que `accounts/urls.py` inclui as URLs de reports quando usuário é chair/staff

## 6. Testes — Permissões e Consistência

- [x] 6.1 Testar que usuários sem permissão recebem 403 em todas as views de reports
- [x] 6.2 Testar que chairs e staff conseguem acessar dashboard e exports
- [x] 6.3 Testar snapshot de CSV — header, encoding UTF-8, separador vírgula, BOM opcional
- [x] 6.4 Testar snapshot de JSON — estrutura, tipos de dados, campos obrigatórios
- [x] 6.5 Testar filtros de export (status, formato)
- [x] 6.6 Testar que exports com queryset vazio retornam header CSV ou JSON vazio (não 500)
- [x] 6.7 Testar que aggregate counts conferem com contagem manual de objetos no banco

## 7. Integração e Verificação Final

- [x] 7.1 Rodar `uv run pytest` e garantir todos os testes passam
- [x] 7.2 Verificar `openspec validate add-reports-exports-and-indicators --strict`
- [x] 7.3 Testar manualmente o dashboard com dados de fixture (submissões, revisões, proceedings)
