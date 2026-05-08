## ADDED Requirements

### Requirement: Production environment variables documentation
O `.env.example` SHALL documentar todas as variáveis de ambiente necessárias para produção, incluindo: `SMTP_HOST`, `SMTP_PORT`, `SMTP_USE_TLS`, `SMTP_USER`, `SMTP_PASSWORD`, `DEFAULT_FROM_EMAIL`, `SSL_CERT_PATH`, `SSL_KEY_PATH`, `GUNICORN_WORKERS`, `AXES_FAILURE_LIMIT`, `AXES_COOLOFF_TIME`, `AXES_LOCKOUT_PARAMETERS`, `NGINX_RATE_LIMIT`, `NGINX_BURST`, `BACKUP_RETENTION_DAYS`.

#### Scenario: Developer configures production environment
- **WHEN** um desenvolvedor copia `.env.example` para `.env` e preenche os valores de produção
- **THEN** SHALL ter todas as variáveis necessárias documentadas com valores de exemplo seguros

### Requirement: Restore playbook
O documento `docs/implementation/SETUP_DEPLOY.md` SHALL incluir seção de restore com passos para: (1) identificar o backup mais recente, (2) executar `scripts/restore.sh`, (3) verificar integridade dos dados restaurados, (4) checklist de validação pós-restore.

#### Scenario: Operator restores from backup
- **WHEN** um operador segue o playbook de restore em `SETUP_DEPLOY.md`
- **THEN** SHALL conseguir restaurar o banco e verificar integridade usando apenas os comandos documentados

### Requirement: Health check for all services
O `docker-compose.yml` SHALL incluir `healthcheck` para todos os serviços (`db`, `web`, `nginx`). O health check do `web` SHALL usar `curl` para `/health/`. O health check do `nginx` SHALL verificar que a porta 443 está respondendo.

#### Scenario: Nginx health check passes
- **WHEN** o serviço `nginx` está ativo e respondendo HTTPS
- **THEN** o healthcheck SHALL retornar sucesso

#### Scenario: Unhealthy service stops dependents
- **WHEN** o serviço `web` falha o healthcheck
- **THEN** o Docker SHALL marcar o serviço como unhealthy e dependências SHALL parar de enviar tráfego

## MODIFIED Requirements

### Requirement: Environment variables documentation
O projeto SHALL fornecer `.env.example` com todas as variáveis de ambiente necessárias documentadas. SHALL fornecer `README.md` com instruções de setup, desenvolvimento e testes. O `.env.example` SHALL ser organizado em seções: Geral, Banco de Dados, SMTP/Email, SSL/TLS, Rate Limiting, Backups. Cada variável SHALL ter comentário com descrição, valor de exemplo e indicação se é obrigatória ou opcional.

#### Scenario: Developer can set up environment
- **WHEN** um desenvolvedor copia `.env.example` para `.env` e preenche os valores
- **THEN** SHALL poder iniciar o projeto com `docker compose up` ou `python manage.py runserver`

#### Scenario: Variable categories are clear
- **WHEN** um desenvolvedor abre `.env.example`
- **THEN** SHALL encontrar variáveis agrupadas por categoria com comentários explicativos
