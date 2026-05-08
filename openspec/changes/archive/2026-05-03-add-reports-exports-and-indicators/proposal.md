## Why

A comissão organizadora e o admin técnico precisam de indicadores consolidados para prestação de contas, relatório técnico-científico do evento e acompanhamento em tempo real do fluxo de submissões, revisões e materiais finais. Sem isso, a coordenação depende de planilhas manuais e consultas ad-hoc ao banco.

## What Changes

- Novo app `reports` com dashboard de indicadores acessível a chairs e staff/superuser
- Views de agregação: contagens por estado de submissão, eixo temático, modalidade, instituição, revisor
- Exportação em CSV e JSON dos indicadores e das listagens detalhadas (submissões, revisões, autores, proceedings)
- Queries otimizadas com `annotate()`/`values()` do Django ORM para agregações
- Template de dashboard com cards de KPI, tabelas resumo e botões de export
- Testes de permissões (acesso restrito) e consistência dos dados exportados

## Capabilities

### New Capabilities
- `reports`: Dashboard de indicadores, agregações e exportação CSV/JSON para comissão e admin técnico

### Modified Capabilities
- `submissions`: Adicionar manager com métodos de agregação (por estado, eixo, modalidade, instituição) e queryset filtrável para exports
- `reviews`: Adicionar manager com métodos de agregação (por revisor, por status, tempos médios) para dashboard de revisões
- `proceedings`: Adicionar métodos de consulta para materiais entregues vs. pendentes e proceedings publicados

## Impact

- **Novo app**: `reports/` (views, urls, templates, tests)
- **Apps modificados**: `submissions/`, `reviews/`, `proceedings/` (managers, não models)
- **Dependencies**: nenhuma nova dependência externa (usa csv/json nativos)
- **Templates**: novo template base para dashboard admin, sem impacto no site público
- **Permissões**: views protegidas por `@staff_member_required` ou decorador customizado de role
