# Implantação e Segurança (deployment-security)

## Purpose
Estabelecer diretrizes de segurança, gestão de dados sensíveis e configurações de ambiente para produção.

## Requirements

### Requirement: Environment-based settings
Os settings SHALL ser divididos em `settings/base.py` (configuração comum), `settings/development.py` (DEBUG=True, ferramentas de dev), `settings/test.py` (banco em memória, settings mínimos), `settings/production.py` (DEBUG=False, segurança restritiva). Cada ambiente SHALL poder sobrescrever variáveis do base.

#### Scenario: Development settings activate
- **WHEN** `DJANGO_SETTINGS_MODULE=cbnv.settings.development` está definido
- **THEN** `DEBUG` SHALL ser `True` e `ALLOWED_HOSTS` SHALL incluir `localhost` e `127.0.0.1`

#### Scenario: Test settings use in-memory database
- **WHEN** `DJANGO_SETTINGS_MODULE=cbnv.settings.test` está definido e pytest executa
- **THEN** SHALL usar SQLite em memória (`:memory:`) sem necessidade de PostgreSQL

### Requirement: Security headers
Os settings de produção SHALL configurar `SECURE_SSL_REDIRECT=True`, `SESSION_COOKIE_SECURE=True`, `CSRF_COOKIE_SECURE=True`, `SECURE_HSTS_SECONDS`, `SECURE_BROWSER_XSS_FILTER=True`, `SECURE_CONTENT_TYPE_NOSNIFF=True`, `X_FRAME_OPTIONS='DENY'`. Headers SHALL ser aplicados via `SecurityMiddleware`.

#### Scenario: Security headers present in production
- **WHEN** uma requisição HTTP é feita ao servidor em produção
- **THEN** SHALL incluir headers `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`

### Requirement: Sensitive data via environment
`SECRET_KEY`, `DATABASE_URL`, credenciais de email e outras variáveis sensíveis SHALL ser lidas de variáveis de ambiente. Nenhum segredo SHALL estar hardcoded no código-fonte. O `.env` SHALL estar listado em `.gitignore`.

#### Scenario: Secrets loaded from environment
- **WHEN** o servidor inicia com `SECRET_KEY` definido como variável de ambiente
- **THEN** SHALL usar esse valor sem fallback para string hardcoded

#### Scenario: .env not in git
- **WHEN** `git status` é verificado
- **THEN** `.env` SHALL aparecer em `.gitignore` e não SHALL ser rastreado

### Requirement: Docker secrets support
O `docker-compose.yml` SHALL suportar passagem de variáveis sensíveis via `env_file` ou Docker secrets. O `docker-compose.yml` SHALL referenciar `.env` file para desenvolvimento. Em produção, variáveis sensíveis (SECRET_KEY, DATABASE_URL, SMTP credentials, SSL paths) SHALL ser passadas via `env_file` montado no servidor, nunca hardcoded.

#### Scenario: Docker Compose loads environment
- **WHEN** `docker compose up` é executado com `.env` presente
- **THEN** SHALL carregar variáveis de ambiente para os serviços `web` e `db`

#### Scenario: Production uses external env file
- **WHEN** `docker compose --env-file /etc/cbnv/.env up` é executado em produção
- **THEN** SHALL usar as variáveis do arquivo externo sem fallback para valores padrão inseguros

### Requirement: Nginx reverse proxy
O `docker-compose.yml` SHALL incluir um serviço `nginx` que atua como único ponto de entrada HTTP/HTTPS. O serviço SHALL escutar na porta 80 (HTTP → redirect para HTTPS) e 443 (HTTPS). O Nginx SHALL fazer proxy_pass para o serviço `web` na porta 8000 interna. O serviço `web` SHALL ter `expose: ["8000"]` em vez de `ports` — não SHALL ser acessível diretamente do host em produção.

#### Scenario: HTTPS serve the application
- **WHEN** uma requisição HTTPS é feita na porta 443
- **THEN** o Nginx SHALL fazer proxy_pass para o serviço `web` e retornar a resposta da aplicação

#### Scenario: HTTP redirects to HTTPS
- **WHEN** uma requisição HTTP é feita na porta 80
- **THEN** o Nginx SHALL retornar redirect 301 para a URL equivalente em HTTPS

#### Scenario: Django not exposed directly
- **WHEN** o `docker-compose.yml` de produção é inspecionado
- **THEN** o serviço `web` SHALL usar `expose` em vez de `ports` e SHALL não ser acessível diretamente do host

### Requirement: TLS termination
O Nginx SHALL fazer terminação TLS usando certificados montados em volume. Os caminhos dos certificados SHALL ser configuráveis via variáveis de ambiente `SSL_CERT_PATH` e `SSL_KEY_PATH` com defaults `/etc/nginx/ssl/cert.pem` e `/etc/nginx/ssl/key.pem`. O Nginx SHALL usar protocolo TLS 1.2+ com cipher suite segura.

#### Scenario: Nginx starts with valid certificates
- **WHEN** os certificados estão montados nos paths configurados
- **THEN** o Nginx SHALL iniciar sem erros e servir HTTPS

#### Scenario: Nginx refuses to start without certificates
- **WHEN** os arquivos de certificado não existem
- **THEN** o Nginx SHALL falhar com erro de configuração logged

### Requirement: Gunicorn WSGI server
Em produção, o serviço `web` SHALL usar Gunicorn como WSGI server em vez de `runserver`. O comando SHALL ser `gunicorn cbnv.wsgi:application --bind 0.0.0.0:8000 --workers 4 --timeout 120`. O número de workers SHALL ser configurável via variável `GUNICORN_WORKERS`.

#### Scenario: Production uses Gunicorn
- **WHEN** `DJANGO_SETTINGS_MODULE=cbnv.settings.production`
- **THEN** o comando do serviço `web` SHALL ser `gunicorn` e não `runserver`

#### Scenario: Development keeps runserver
- **WHEN** `DJANGO_SETTINGS_MODULE=cbnv.settings.development`
- **THEN** o comando do serviço `web` SHALL ser `python manage.py runserver`

### Requirement: Protected media serving via X-Accel-Redirect
Arquivos de submissão SHALL ser servidos exclusivamente por views autorizadas do Django que delegam ao Nginx via header `X-Accel-Redirect`. O diretório `MEDIA_ROOT/submissions/` SHALL ser um `internal location` no Nginx — não acessível por URL pública. Outros arquivos de media (publicidade, imagens de sponsors) podem continuar sendo servidos diretamente.

#### Scenario: Authorized author downloads submission file
- **WHEN** o autor dono da submissão acessa a view de download
- **THEN** o Django verifica permissão, retorna header `X-Accel-Redirect` e o Nginx serve o arquivo

#### Scenario: Unauthorized user cannot access submission file
- **WHEN** um usuário sem permissão tenta acessar a view de download
- **THEN** o Django retorna HTTP 403 sem expor o caminho do arquivo

#### Scenario: Direct URL to submission file is blocked
- **WHEN** uma requisição direta é feita para `/media/submissions/arquivo.pdf`
- **THEN** o Nginx SHALL retornar HTTP 404

### Requirement: Rate limiting
O Nginx SHALL aplicar rate limiting genérico via `limit_req_zone` (padrão: 10 req/s por IP com burst de 20). O `django-axes` SHALL proteger endpoints de login contra brute-force (5 tentativas falhas → lockout de 15 minutos por username+IP). Os limites SHALL ser configuráveis via variáveis de ambiente.

#### Scenario: Rate limit exceeded returns 503
- **WHEN** um IP excede o limite de requisições configurado
- **THEN** o Nginx SHALL retornar HTTP 503 com `Retry-After` header

#### Scenario: Login brute-force blocked
- **WHEN** 5 tentativas de login falham para o mesmo username
- **THEN** o sistema SHALL bloquear novas tentativas por 15 minutos e logar o evento

### Requirement: PostgreSQL automated backups
O projeto SHALL fornecer script `scripts/backup.sh` que faz backup do PostgreSQL via `pg_dump --format=custom`, comprime com gzip e salva em volume `backups` com timestamp. O script SHALL manter retenção de 7 dias (excluir backups mais antigos). O projeto SHALL fornecer script `scripts/restore.sh` que restaura um backup específico em um banco limpo.

#### Scenario: Daily backup runs successfully
- **WHEN** o script de backup é executado
- **THEN** SHALL criar arquivo `.dump` comprimido no diretório de backups com timestamp

#### Scenario: Old backups are pruned
- **WHEN** existem mais de 7 backups no diretório
- **THEN** o script SHALL remover os mais antigos mantendo apenas os 7 mais recentes

#### Scenario: Restore from backup succeeds
- **WHEN** `scripts/restore.sh <backup-file>` é executado contra um banco limpo
- **THEN** o banco SHALL conter os dados do backup e o script SHALL retornar exit code 0

### Requirement: Structured JSON logging
Em produção, o Django SHALL configurar logging para emitir JSON estruturado em stdout/stderr via `python-json-logger`. O formato SHALL incluir campos `timestamp`, `level`, `logger`, `message`, `request_id` (quando disponível). Logs de segurança (login falho, acesso negado) SHALL usar nível `WARNING` ou superior.

#### Scenario: Production logs are JSON
- **WHEN** o Django está em modo produção e um log é emitido
- **THEN** a saída SHALL ser um único JSON object por linha em stdout/stderr

#### Scenario: Failed login is logged with warning level
- **WHEN** uma tentativa de login falha
- **THEN** SHALL ser emitido log com nível `WARNING` incluindo username e IP

### Requirement: Isolated Docker network
O `docker-compose.yml` SHALL definir uma rede interna `cbnv_internal` onde apenas `nginx` e `web` se comunicam. O serviço `db` SHALL estar nesta rede mas não SHALL ser acessível do host (remover mapeamento de ports). Apenas o `nginx` SHALL expor portas ao host (80, 443).

#### Scenario: Database not accessible from host
- **WHEN** o docker-compose de produção está ativo
- **THEN** a porta 5432 SHALL não estar mapeada no host

#### Scenario: Web communicates with database internally
- **WHEN** o serviço `web` se conecta ao banco
- **THEN** SHALL usar o hostname interno `db` na rede `cbnv_internal`
