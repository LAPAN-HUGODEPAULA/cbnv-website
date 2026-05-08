# Relatórios e Indicadores (reports)

## Purpose

Fornecer dashboard de indicadores e exportação de dados para prestação de contas, relatório técnico-científico e acompanhamento da comissão organizadora.

## Requirements

### Requirement: Dashboard de Indicadores Gerais
O sistema SHALL exibir um dashboard com KPIs consolidados acessível apenas a usuários com papel de chair ou staff/superuser. Os KPIs DEVEM incluir:
- Total de submissões recebidas
- Submissões por estado (aceitas, rejeitadas, em avaliação, rascunho)
- Total de autores e instituições distintas
- Total de revisores e revisões concluídas
- Materiais finais entregues vs. pendentes
- Vídeos/links publicados

#### Scenario: Chair acessa dashboard de indicadores
- **WHEN** um usuário com `is_chair=True` ou `is_staff=True` acessa `/reports/`
- **THEN** SHALL visualizar cards com os KPIs principais e tabelas resumo com filtros opcionais

#### Scenario: Autor tenta acessar dashboard
- **WHEN** um usuário sem papel de chair ou staff acessa `/reports/`
- **THEN** SHALL receber resposta HTTP 403 Forbidden

### Requirement: Indicadores por Eixo Temático e Modalidade
O sistema SHALL apresentar tabelas com contagem de submissões agrupadas por eixo temático e por modalidade (oral, pôster, vídeo).

#### Scenario: Chair visualiza submissões por eixo
- **WHEN** o chair acessa a seção de indicadores por eixo
- **THEN** SHALL ver tabela com nome do eixo e contagem de submissões, ordenada por contagem decrescente

#### Scenario: Chair visualiza submissões por modalidade
- **WHEN** o chair acessa a seção de indicadores por modalidade
- **THEN** SHALL ver tabela com nome da modalidade e contagem, incluindo percentual do total

### Requirement: Indicadores de Revisão
O sistema SHALL apresentar métricas de revisão incluindo revisores atribuídos, revisões concluídas, revisões pendentes e tempo médio de avaliação.

#### Scenario: Chair visualiza métricas de revisão
- **WHEN** o chair acessa a seção de indicadores de revisão
- **THEN** SHALL ver total de revisores ativos, revisões concluídas/pendentes e lista dos 10 revisores com mais avaliações

### Requirement: Indicadores de Autores e Instituições
O sistema SHALL apresentar ranking das instituições com mais submissões e contagem de autores únicos.

#### Scenario: Chair visualiza ranking de instituições
- **WHEN** o chair acessa a seção de autores e instituições
- **THEN** SHALL ver tabela com instituição e contagem de submissões, ordenada por contagem decrescente

### Requirement: Indicadores de Materiais Finais e Proceedings
O sistema SHALL apresentar contagem de trabalhos aceitos com materiais finais entregues vs. pendentes, e proceedings publicados.

#### Scenario: Chair visualiza status de materiais
- **WHEN** o chair acessa a seção de materiais finais
- **THEN** SHALL ver contagem de materiais entregues, pendentes e proceedings publicados

### Requirement: Exportação CSV de Indicadores
O sistema SHALL permitir exportação dos indicadores agregados em formato CSV via query parameter `format=csv`.

#### Scenario: Export CSV de indicadores
- **WHEN** o chair acessa `/reports/indicators/export/?format=csv`
- **THEN** SHALL baixar arquivo CSV com header em português contendo indicadores agregados (submissões por estado, eixo, modalidade, revisores, instituições)

### Requirement: Exportação JSON de Indicadores
O sistema SHALL permitir exportação dos indicadores agregados em formato JSON via query parameter `format=json`.

#### Scenario: Export JSON de indicadores
- **WHEN** o chair acessa `/reports/indicators/export/?format=json`
- **THEN** SHALL baixar arquivo JSON estruturado com indicadores agregados

### Requirement: Exportação Detalhada de Submissões
O sistema SHALL permitir exportação da listagem completa de submissões em CSV ou JSON, incluindo título, autores, instituição, eixo, modalidade, estado e data.

#### Scenario: Export CSV de submissões
- **WHEN** o chair acessa `/reports/submissions/export/?format=csv`
- **THEN** SHALL baixar arquivo CSV com todas as submissões e campos detalhados

#### Scenario: Export com filtro de estado
- **WHEN** o chair acessa `/reports/submissions/export/?format=csv&status=accepted_oral`
- **THEN** SHALL baixar arquivo CSV apenas com submissões do estado filtrado

### Requirement: Exportação Detalhada de Revisões
O sistema SHALL permitir exportação da listagem de revisões em CSV ou JSON, incluindo revisor, submissão, status e data de conclusão.

#### Scenario: Export CSV de revisões
- **WHEN** o chair acessa `/reports/reviews/export/?format=csv`
- **THEN** SHALL baixar arquivo CSV com revisor, título da submissão, status e datas

### Requirement: Exportação de Proceedings e Materiais
O sistema SHALL permitir exportação da listagem de proceedings em CSV ou JSON, incluindo título, autores, modalidade, status de materiais e link do vídeo.

#### Scenario: Export CSV de proceedings
- **WHEN** o chair acessa `/reports/proceedings/export/?format=csv`
- **THEN** SHALL baixar arquivo CSV com dados de proceedings e materiais finais

### Requirement: Exportação de Autores e Instituições
O sistema SHALL permitir exportação da listagem de autores e suas instituições em CSV ou JSON.

#### Scenario: Export CSV de autores
- **WHEN** o chair acessa `/reports/authors/export/?format=csv`
- **THEN** SHALL baixar arquivo CSV com nome do autor, instituição, país e submissões associadas

### Requirement: Permissões de Exportação
Todas as views de exportação SHALL usar o decorator `@admin_or_chair_required` e retornar 403 para usuários não autorizados.

#### Scenario: Usuário sem permissão tenta exportar
- **WHEN** um usuário sem papel de chair ou staff acessa qualquer endpoint de export
- **THEN** SHALL receber HTTP 403 Forbidden

### Requirement: Review progress summary
The system SHALL provide a summary view for the commission showing the number of reviews completed vs pending for each submission.

#### Scenario: Viewing progress summary
- **WHEN** a commission member accesses the reports dashboard
- **THEN** they SHALL see a list of works with their current review status and reviewer assignments

### Requirement: Submission status export
The system SHALL allow the commission to export a list of all submissions with their final decisions and assigned modalities in CSV format.

#### Scenario: Exporting decisions
- **WHEN** the commission clicks the "Export Decisions" button
- **THEN** a CSV file with ID, Title, Author, Status, and Modality SHALL be downloaded
