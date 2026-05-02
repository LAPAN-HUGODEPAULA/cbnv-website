# CBNV 2026

Website e plataforma digital do **XII Congresso Brasileiro de Neurociências da Visão** — "Neurovisão na Era da Inteligência Artificial", 11–13 de novembro de 2026, CAD-1 UFMG, Belo Horizonte, MG.

## Stack

Django 5.x + Wagtail 7.x + PostgreSQL 16 + Tailwind CSS 4 + Docker Compose

## Pré-requisitos

- Python 3.10+
- Node.js 18+
- Docker e Docker Compose (opcional, para ambiente containerizado)

## Setup Local

```bash
# Clonar repositório
git clone <repo-url>
cd cbnv-website

# Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependências Python
pip install -r requirements.txt

# Instalar dependências frontend
npm install

# Copiar variáveis de ambiente
cp .env.example .env

# Build do CSS
npm run build

# Criar banco (requer PostgreSQL rodando)
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Servidor de desenvolvimento
python manage.py runserver
```

## Docker

```bash
# Iniciar serviços (web + PostgreSQL)
docker compose up

# Criar superusuário (em outro terminal)
docker compose exec web python manage.py createsuperuser
```

## Tailwind CSS

```bash
# Build único (produção)
npm run build

# Watch mode (desenvolvimento)
npm run watch
```

## Testes

```bash
# Executar testes (usa SQLite in-memory)
pytest

# Com verbose
pytest -v
```

## Estrutura de Apps

| App | Finalidade |
|---|---|
| `core` | Configurações globais, utilitários, healthcheck |
| `pages` | Tipos de páginas Wagtail |
| `program` | Programação, sessões, palestrantes |
| `submissions` | Submissões, autores, arquivos |
| `reviews` | Revisões, pareceres, decisões |
| `proceedings` | Anais, exportações |
| `videos` | Links YouTube e acervo |
| `sponsors` | Patrocinadores |
| `accounts` | Usuários, autenticação, papéis |
| `reports` | Indicadores e exports |
| `notifications` | E-mails transacionais |

## Ambiente

O projeto usa settings divididos:

- `cbnv/settings/development.py` — desenvolvimento local (padrão)
- `cbnv/settings/test.py` — testes (SQLite in-memory)
- `cbnv/settings/production.py` — produção (security headers, HTTPS)

Defina `DJANGO_SETTINGS_MODULE` para alterar.

## Documentação

- [Requisitos e Arquitetura](docs/CBNV2026_Requisitos_Arquitetura_v1.md)
- [OpenSpec](openspec/) — propostas de mudança e implementação
