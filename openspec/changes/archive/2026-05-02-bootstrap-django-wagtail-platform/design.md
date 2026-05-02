## Context

A plataforma digital do XII CBNV 2026 precisa de fundação técnica antes de qualquer funcionalidade de negócio. O projeto é uma aplicação monolítica modular em Django/Wagtail, com PostgreSQL, Tailwind CSS e Docker Compose. Esta é a primeira proposta do plano de implementação e não há código existente — tudo será criado do zero.

O documento de requisitos (`docs/CBNV2026_Requisitos_Arquitetura_v1.md`) define a stack aprovada e a estrutura de apps. Esta change implementa a fundação sobre a qual as propostas 02-12 serão construídas.

## Goals / Non-Goals

**Goals:**

- Projeto Django 5.x funcional com Wagtail integrado
- Custom user model definido antes de qualquer model de domínio (decisão irreversível sem migração complexa)
- PostgreSQL via Docker Compose com healthcheck
- Settings separados por ambiente (development/test/production)
- Tailwind CSS com pipeline de build mínima
- Apps Django vazios por domínio, prontos para crescimento
- pytest configurado com fixtures base
- Healthcheck endpoint para orquestração
- Documentação de desenvolvimento completa

**Non-Goals:**

- Páginas públicas finais (Proposal 05)
- Design system completo (Proposal 02)
- Funcionalidades de negócio (submissões, revisão, etc.)
- Deploy production completo (Proposal 11)
- Redis/Celery (adicionado quando necessário por e-mails assíncronos)
- Reverse proxy (Caddy/Nginx) em produção

## Decisions

### D1: Custom user model no app `accounts`

**Decisão:** Definir `accounts.User` herdando de `AbstractUser` com campos adicionais de perfil e flags de papéis científicos.

**Campos:**
- `full_name`: CharField (verbose_name="Nome completo")
- `institution`: CharField (verbose_name="Instituição", blank=True)
- `country`: CharField (verbose_name="País", blank=True, choices baseados em ISO 3166-1)
- `position`: CharField (verbose_name="Vínculo/Cargo", blank=True)
- `is_author`: BooleanField (default=False, verbose_name="Autor")
- `is_reviewer`: BooleanField (default=False, verbose_name="Revisor")
- `is_chair`: BooleanField (default=False, verbose_name="Comissão Científica")
- `consent_privacy`: BooleanField (default=False)
- `consent_image`: BooleanField (default=False)

**Alternativa considerada:** Usar um campo singular `role` com choices ou uma tabela `Role` (M2M) — rejeitados por complexidade desnecessária e por impedirem que um usuário acumule papéis (ex: autor e revisor) de forma simples e idiomatica no Django.

**Racional:** Flags booleanas são eficientes para filtragem no DB, simples de usar em templates e permitem multiplicidade de papéis sem joins extras. Django recomenda custom user model em todo projeto novo. Uma vez criadas migrations, trocar é complexo. Wagtail suporta custom user via `get_user_model()`.

### D2: Settings como pacote, não módulo único

**Decisão:** Usar `cbnv/settings/` como pacote Python com `base.py`, `development.py`, `test.py`, `production.py`. Cada arquivo importa de `base` e sobrescreve o necessário.

**Alternativa considerada:** Módulo único com `if DEBUG:` — rejeitado por misturar configurações de produção com desenvolvimento e dificultar testes determinísticos.

**Racional:** Separação clara entre ambientes. Settings de teste usam SQLite in-memory para velocidade. Settings de produção são lock-down.

### D3: Tailwind via build standalone, não Django integration package

**Decisão:** Instalar Tailwind CLI via npm. Build manual (ou via npm script) que gera `static/css/output.css`. O Django serve o CSS compilado como arquivo estático.

**Alternativa considerada:** `django-tailwind` — rejeitado por adicionar complexidade e dependência de outro pacote com ciclo de vida incerto. O build standalone é simples, previsível e alinhado com o princípio de simplicidade do projeto.

**Racional:** Menos dependências. O build é determinístico. Fácil de integrar com `collectstatic`.

### D4: Docker Compose com docker-compose.yml + override

**Decisão:** `docker-compose.yml` com serviços `web` e `db` para produção/base. `docker-compose.override.yml` (gitignored opcionalmente) para desenvolvimento com volumes e live reload.

**Alternativa considerada:** Arquivo único — rejeitado por misturar configuração de produção com desenvolvimento.

**Racional:** Compose v2 suporta profiles e overrides. Desenvolvedores podem usar `docker compose up` (carrega override automaticamente) e CI pode usar `docker compose -f docker-compose.yml up`.

### D5: Apps Django vazios com AppConfig

**Decisão:** Cada app (`core`, `pages`, `program`, `submissions`, `reviews`, `proceedings`, `videos`, `sponsors`, `accounts`, `reports`, `notifications`) será criado com `startapp` Django, contendo apenas `apps.py`, `__init__.py`, e `migrations/` com `__init__.py`.

**Racional:** Estrutura definida desde o início evita refactoring. Apps de domínio serão preenchidos pelas propostas subsequentes.

### D6: Teste com SQLite in-memory para velocidade

**Decisão:** `settings/test.py` usa `DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}` (SQLite in-memory é o padrão do pytest-django).

**Alternativa considerada:** PostgreSQL de teste via Docker — rejeitado por adicionar complexidade ao CI local. PostgreSQL será testado via Docker Compose em integração.

**Racional:** Testes unitários precisam ser rápidos. Diferenças SQL entre PostgreSQL e SQLite são mínimas para testes de models básicos.

## Risks / Trade-offs

- **[Custom user irreversível]** → Mitigação: definir User imediatamente como primeira migration. Documentar que troca após domain models requer migração complexa.
- **[Tailwind build manual]** → Mitigação: npm scripts com `build` e `watch`. Documentar no README.
- **[SQLite vs PostgreSQL divergência]** → Mitigação: testes de integração críticos (submissão, upload) serão executados contra PostgreSQL via Docker em CI quando configurado.
- **[Versão Wagtail/Django]** → Mitigação: fixar versões em `requirements.txt` com pinamento exato. Django 5.x LTS e Wagtail 7.x.
- **[Docker volume permissions]** → Mitigação: usar user `1000:1000` no Dockerfile ou configurar `USER` no compose.

## Migration Plan

1. Criar estrutura do projeto Django com `django-admin startproject`
2. Instalar Wagtail e adaptar projeto
3. Criar custom user no app `accounts` e gerar migration inicial
4. Criar apps de domínio vazios
5. Criar settings split
6. Configurar Docker Compose
7. Configurar Tailwind build pipeline
8. Criar templates base
9. Configurar pytest
10. Implementar healthcheck
11. Criar `.env.example` e README
12. Validar com `openspec validate`

**Rollback:** `git revert` do commit da proposal. Como é a primeira proposta, não há dados existentes para migrar.

## Open Questions

1. Versão exata do Django LTS a usar (5.0.x ou 5.1.x) — definida no momento da implementação.
2. Necessidade de `django-extensions` no desenvolvimento — adicionar se útil, não bloquear.
3. Formato do `country` field (ISO 3166-1 alpha-2 codes ou lista livre) — definir com o coordenador.
