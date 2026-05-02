# Experiência do Desenvolvedor (developer-experience)

## Requirements

### Requirement: Tailwind CSS build pipeline
O projeto SHALL integrar Tailwind CSS via pipeline de build com `tailwindcss` npm package. SHALL existir `tailwind.config.js` com content paths apontando para templates Django. O build SHALL gerar CSS compilado em `static/css/output.css`. O `manage.py collectstatic` SHALL incluir o CSS compilado.

#### Scenario: Tailwind CSS builds successfully
- **WHEN** `npx tailwindcss --input src/input.css --output static/css/output.css --minify` é executado
- **THEN** SHALL gerar `static/css/output.css` com classes Tailwind compiladas

#### Scenario: Tailwind classes available in templates
- **WHEN** um template Django usa classes utilitárias do Tailwind como `bg-blue-600` e `text-white`
- **THEN** os estilos SHALL ser aplicados corretamente no HTML renderizado

### Requirement: pytest configuration
O projeto SHALL usar pytest como framework de testes. SHALL existir `pytest.ini` ou `pyproject.toml` com configuração `DJANGO_SETTINGS_MODULE = cbnv.settings.test` e `django_db` habilitado. SHALL existir arquivo `conftest.py` global com fixtures para `db` e `client`.

#### Scenario: Tests run with pytest
- **WHEN** `pytest` é executado no diretório raiz do projeto
- **THEN** SHALL descobrir e executar testes sem erros de configuração

#### Scenario: Database fixture available
- **WHEN** um teste usa a fixture `db` do pytest-django
- **THEN** SHALL ter acesso a um banco de dados de teste limpo

### Requirement: Base templates
O projeto SHALL fornecer templates base mínimos: `base.html` (layout HTML5 com `<head>`, `<body>`, blocos `{% block title %}`, `{% block content %}`, `{% block scripts %}`) e `base_admin.html` (herda de `base.html` com navegação admin). Os templates SHALL carregar Tailwind CSS.

#### Scenario: Base template renders
- **WHEN** uma view renderiza usando `base.html`
- **THEN** SHALL produzir HTML válido com Tailwind CSS carregado e blocos substituíveis

### Requirement: Healthcheck endpoint
O sistema SHALL fornecer endpoint `/health/` que retorne HTTP 200 com JSON `{"status": "ok"}` quando o banco de dados está acessível. SHALL retornar HTTP 503 quando o banco está indisponível.

#### Scenario: Healthcheck with database available
- **WHEN** `GET /health/` é chamado e PostgreSQL está acessível
- **THEN** SHALL retornar HTTP 200 com `{"status": "ok"}`

#### Scenario: Healthcheck with database unavailable
- **WHEN** `GET /health/` é chamado e PostgreSQL não está acessível
- **THEN** SHALL retornar HTTP 503

### Requirement: Environment variables documentation
O projeto SHALL fornecer `.env.example` com todas as variáveis de ambiente necessárias documentadas. SHALL fornecer `README.md` com instruções de setup, desenvolvimento e testes.

#### Scenario: Developer can set up environment
- **WHEN** um desenvolvedor copia `.env.example` para `.env` e preenche os valores
- **THEN** SHALL poder iniciar o projeto com `docker compose up` ou `python manage.py runserver`
