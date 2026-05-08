## 1. Infraestrutura Docker — Nginx e Rede

- [x] 1.1 Criar `nginx/default.conf` com server block HTTPS (listen 443 ssl), HTTP→HTTPS redirect (listen 80), proxy_pass para `web:8000`, headers de segurança (HSTS, X-Content-Type-Options, X-Frame-Options, CSP básica)
- [x] 1.2 Adicionar serviço `nginx` ao `docker-compose.yml`: imagem `nginx:alpine`, volumes para config e certificados SSL, ports 80 e 443, depends_on web com healthcheck
- [x] 1.3 Criar rede interna `cbnv_internal` no `docker-compose.yml` e atribuir aos serviços `web`, `db` e `nginx`
- [x] 1.4 Remover mapeamento de ports do serviço `db` em produção (usar apenas rede interna)
- [x] 1.5 Alterar serviço `web` para usar `expose: ["8000"]` em vez de `ports` no compose de produção

## 2. Gunicorn — WSGI de Produção

- [x] 2.1 Adicionar `gunicorn` às dependências do projeto via `uv add gunicorn`
- [x] 2.2 Criar `gunicorn.conf.py` com workers, timeout, bind e logging configuráveis via env vars
- [x] 2.3 Atualizar `docker-compose.override.yml` (dev) para manter `runserver` e `docker-compose.yml` (prod) para usar Gunicorn

## 3. TLS e Headers de Segurança

- [x] 3.1 Configurar paths de certificados SSL via env vars `SSL_CERT_PATH` e `SSL_KEY_PATH` no serviço nginx
- [x] 3.2 Adicionar volume para certificados SSL no serviço nginx (`./ssl:/etc/nginx/ssl:ro`)
- [x] 3.3 Verificar que `cbnv/settings/production.py` já inclui `SECURE_SSL_REDIRECT`, `SECURE_HSTS_SECONDS`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE` — ajustar se necessário

## 4. Media Protegido — X-Accel-Redirect

- [x] 4.1 Adicionar `internal location /protected-media/` no `nginx/default.conf` apontando para o volume de media
- [x] 4.2 Criar view `SubmissionFileDownloadView` em `submissions/views.py` que verifica permissão (dono ou staff) e retorna `X-Accel-Redirect`
- [x] 4.3 Adicionar URL pattern `/submissions/<int:pk>/download/<int:file_id>/` em `submissions/urls.py`
- [x] 4.4 Remover acesso público ao diretório `/media/submissions/` no Nginx (retornar 404)
- [x] 4.5 Atualizar templates de detalhes da submissão para usar a nova URL protegida

## 5. Rate Limiting

- [x] 5.1 Adicionar `limit_req_zone` no `nginx/default.conf` (zona `$binary_remote_addr`, rate configurável via env, burst 20, nodelay)
- [x] 5.2 Aplicar `limit_req` nos location blocks públicos (login, formulário de contato)
- [x] 5.3 Adicionar `django-axes` via `uv add django-axes`
- [x] 5.4 Configurar `django-axes` em `settings/base.py`: backend, failure limit (5), cooldown (15min), lockout parameters via env vars
- [x] 5.5 Adicionar `axes.backends.AxesStandaloneBackend` ao `AUTHENTICATION_BACKENDS` em produção

## 6. Backups e Restore

- [x] 6.1 Criar `scripts/backup.sh`: pg_dump custom format, gzip, timestamp, salvar em volume `backups`
- [x] 6.2 Implementar retenção de 7 dias no `scripts/backup.sh` (excluir backups mais antigos)
- [x] 6.3 Criar `scripts/restore.sh`: receber path do backup, drop/create db, restore, verificar exit code
- [x] 6.4 Adicionar volume `backups` ao serviço `db` no `docker-compose.yml`
- [x] 6.5 Criar serviço `backup` no `docker-compose.yml` com cron diário (ou documentar cron no host)
- [x] 6.6 Testar restore completo: backup → drop db → restore → verificar dados → exit code 0

## 7. Logging Estruturado

- [x] 7.1 Adicionar `python-json-logger` via `uv add --group dev python-json-logger`
- [x] 7.2 Configurar logging em `cbnv/settings/production.py`: formatter JSON para stdout, logger raiz, loggers específicos (django.request=WARNING, axes=WARNING)
- [x] 7.3 Garantir que requests tenham ID único para correlação (middleware ou Gunicorn config)

## 8. SMTP Transacional

- [x] 8.1 Configurar `EMAIL_BACKEND` condicional: `console` em dev, `smtp` em produção em `settings/production.py`
- [x] 8.2 Ler `SMTP_HOST`, `SMTP_PORT`, `SMTP_USE_TLS`, `SMTP_USER`, `SMTP_PASSWORD`, `DEFAULT_FROM_EMAIL` de env vars
- [x] 8.3 Criar wrapper `core/email.py` com try/except que loga falhas em ERROR sem interromper o fluxo principal
- [x] 8.4 Adicionar notificação de mudança de status de submissão nos signals/views de decisão (accepted/rejected → email ao autor)

## 9. Documentação e .env.example

- [x] 9.1 Atualizar `.env.example` com todas as novas variáveis organizadas por seção (Geral, BD, SMTP, SSL, Rate Limiting, Backups)
- [x] 9.2 Atualizar `docs/implementation/SETUP_DEPLOY.md` com seção de restore, health checks, e troubleshooting de produção
- [x] 9.3 Adicionar checklist de verificação pós-deploy em `SETUP_DEPLOY.md` (HTTPS, headers, health check, backup recente, media protegido)
- [x] 9.4 Adicionar instrução para `docker compose --env-file /etc/cbnv/.env up -d` no guia de deploy

## 10. Health Checks e Validação

- [x] 10.1 Adicionar healthcheck ao serviço `nginx` (curl HTTPS localhost/health/)
- [x] 10.2 Verificar healthcheck do serviço `web` usa `/health/` endpoint existente
- [x] 10.3 Adicionar página de erro 503 customizada para rate limiting no Nginx
- [x] 10.4 Executar checklist de validação final: HTTPS funcional, headers presentes, media protegido, backup/restore testado, rate limiting ativo, logs JSON
