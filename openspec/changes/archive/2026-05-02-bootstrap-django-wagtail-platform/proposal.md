## Why

A plataforma digital do XII CBNV 2026 não possui fundação técnica. É necessário criar o projeto Django/Wagtail com custom user, PostgreSQL, Docker Compose, pipeline Tailwind e estrutura modular de apps antes de qualquer funcionalidade de negócio. Sem essa base, propostas subsequentes (design system, CMS, submissões, revisão) não podem ser implementadas.

## What Changes

- Criar projeto Django 5.x com Wagtail integrado e custom user model (`accounts.User`) definido antes de qualquer app de domínio.
- O modelo `User` deve incluir flags booleanas para papéis científicos (`is_author`, `is_reviewer`, `is_chair`) e campos de perfil (`full_name`, `institution`, `country`, `position`).
- Configurar PostgreSQL via Docker Compose com healthcheck automático.
- Estruturar apps Django vazios por domínio: `core`, `pages`, `program`, `submissions`, `reviews`, `proceedings`, `videos`, `sponsors`, `accounts`, `reports`, `notifications`.
- Separar settings Django em `settings/` com módulos base, development, test e production.
- Configurar pipeline Tailwind CSS com build mínimo e integração com `collectstatic`.
- Criar templates base mínimos (shell HTML com Tailwind carregado).
- Configurar pytest com fixtures base para banco de dados e cliente Django.
- Implementar endpoint de healthcheck (`/health/`) para Docker e monitoramento.
- Criar `.env.example` com todas as variáveis de ambiente necessárias.
- Adicionar `README.md` de desenvolvimento com instruções completas.
- Adicionar `.gitignore` adequado para Django/Python.

## Capabilities

### New Capabilities

- `architecture`: Estrutura monolítica modular do projeto Django/Wagtail — apps, settings, custom user, Docker Compose, dependências.
- `developer-experience`: Ambiente de desenvolvimento — Tailwind build pipeline, pytest, templates base, healthcheck, README, `.env.example`.
- `accounts-auth`: Custom user model `accounts.User` com campos mínimos (`full_name`, `institution`, `country`, `position`, `consent_privacy`, `consent_image`) e flags de papéis científicos (`is_author`, `is_reviewer`, `is_chair`). Gestão de autenticação Wagtail/Django integrada.
- `deployment-security`: Configuração de segurança base — headers, variáveis sensíveis via `.env`, Docker secrets, settings production restritivos.

### Modified Capabilities

_Nenhuma — esta é a primeira proposta e não há specs existentes._

## Impact

- **Código**: Cria toda a estrutura do projeto Django; migrações iniciais geradas.
- **Dependências**: Django, Wagtail, PostgreSQL (via Docker), Tailwind CSS (via npm/build), pytest, pytest-django.
- **Infraestrutura**: Docker Compose com serviços `web` e `db`.
- **Desenvolvedores**: Novo clone do repositório requer `docker compose up` ou instalação local conforme README.
- **Segurança**: Custom user model definido antes de migrations de domínio — decisão irreversível sem migração complexa.
