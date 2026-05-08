## Context

A plataforma CBNV 2026 possui fluxos centrais (CMS Wagtail, submissões, avaliações, contas) operando em Docker Compose com PostgreSQL 18 e Django 6.0.4. O `docker-compose.yml` expõe o app Django diretamente via `runserver` e o volume `media_files` serve arquivos sem controle de acesso. Não há reverse proxy, TLS, rate limiting, backups automatizados ou logging estruturado. A implantação em produção exige todas essas camadas.

## Goals / Non-Goals

**Goals:**
- Terminação TLS e headers de segurança via Nginx reverse proxy
- Serving de arquivos de submissão exclusivamente via views autorizadas (X-Accel-Redirect)
- Backups automatizados do PostgreSQL com verificação de restore
- Rate limiting em endpoints públicos sensíveis (login, submissão)
- Logging estruturado (JSON) em produção para coleta centralizada
- Configuração SMTP transacional com fallback e logging de falhas
- Documentação completa de setup, deploy e restore

**Non-Goals:**
- Kubernetes, Helm charts ou orquestração complexa
- CDN ou cache de borda
- Certificados automáticos (Let's Encrypt automatizado — usar certificados pré-existentes)
- Monitoramento com Prometheus/Grafana (pode ser adicionado futuramente)
- Alterações em models, templates de produto ou fluxos de negócio

## Decisions

### D1: Nginx como reverse proxy

**Decisão:** Serviço Nginx no Docker Compose como único ponto de entrada, com terminação TLS e proxy_pass para o app Django (Gunicorn).

**Alternativas:**
- Caddy: auto-TLS, mas menos controle granular de headers e rate limiting
- Traefik: overkill para stack simples

**Racional:** Nginx é padrão de mercado, configuração declarativa em arquivo estático, suporta X-Accel-Redirect nativo para serving de media protegido, e rate limiting robusto via `limit_req_zone`. A imagem `nginx:alpine` é leve (~10MB).

### D2: Gunicorn como WSGI server em produção

**Decisão:** Substituir `runserver` por Gunicorn (workers=4, gthread) em produção.

**Racional:** `runserver` não é seguro nem eficiente para produção. Gunicorn é o WSGI server recomendado pelo Django. Configuração mínima via `gunicorn cbnv.wsgi:application --bind 0.0.0.0:8000 --workers 4 --timeout 120`.

### D3: Media protegido via X-Accel-Redirect

**Decisão:** Arquivos de submissão servidos por uma view Django que verifica permissão e delega o streaming ao Nginx via header `X-Accel-Redirect`. O diretório `MEDIA_ROOT/submissions/` não é mapeado no Nginx — apenas acessível internamente via X-Accel.

**Alternativas:**
- Django `FileResponse` direto: consome workers do Gunicorn para streaming de arquivos grandes
- Signed URLs com expiração: complexidade adicional sem ganho significativo para este caso

**Racional:** X-Accel-Redirect é o padrão para Django+Nginx. O processo Django verifica permissão (autor = dono ou staff) e devolve um header que faz o Nginx servir o arquivo diretamente, sem consumir workers.

### D4: Backups via pg_dump + cron no container

**Decisão:** Script `scripts/backup.sh` executado via cron diário no host ou container dedicado. Faz `pg_dump` custom format, comprime com gzip e salva em volume `backups` com retenção de 7 dias. Script `scripts/restore.sh` para restore verificado.

**Alternativas:**
- WAL archiving / PITR: complexidade desnecessária para evento de 3 dias
- Barman: overkill

**Racional:** `pg_dump` custom format suporta restore seletivo e é verificável. Retenção de 7 dias cobre o período do evento com margem. Restore pode ser testado em container isolado.

### D5: Rate limiting com django-axes + Nginx limit_req

**Decisão:** Dupla camada: Nginx `limit_req_zone` para limitação genérica por IP (global) e `django-axes` para proteção de login (contagem de tentativas por username/IP, lockout temporário).

**Racional:** Nginx ataca antes de chegar ao Django, protegendo contra flood genérico. `django-axes` protege especificamente contra brute-force de login com blocklist persistente no banco.

### D6: Logging estruturado JSON via python-json-logger

**Decisão:** Em produção, configurar `logging` do Django para emitir JSON em stdout/stderr via `python-json-logger`. Docker coleta e envia para o sistema de logs do host.

**Alternativas:**
- Structlog: mais poderoso, mas maior complexidade
- Sentry: é um serviço externo, foge do escopo desta change

**Racional:** JSON em stdout é o padrão para containers Docker. Pode ser consumido por qualquer sistema de agregação (CloudWatch, Loki, ELK) sem configuração adicional.

### D7: SMTP transacional com fallback silencioso

**Decisão:** Configurar `EMAIL_BACKEND` para usar SMTP com TLS (`django.core.mail.backends.smtp.EmailBackend`). Em staging/produção, usar host/porta/credenciais via env vars. Falhas de envio SHALL ser logadas em `ERROR` mas NÃO SHALL levantar exceção que quebre o fluxo principal.

**Racional:** O evento precisa de emails transacionais (confirmação de conta, notificação de role, status de submissão). Fallback para console em desenvolvimento é padrão Django. Em produção, SMTP com TLS é suficiente.

## Risks / Trade-offs

- **[Certificados TLS manuais]** → O deploy exige certificados `.crt`/`.key` montados no volume do Nginx. Documentar o caminho e formato esperado. No futuro, Let's Encrypt pode automatizar isso.
- **[Restore sem PITR]** → Backups diários via pg_dump não permitem restore point-in-time. Para um evento de 3 dias, isso é aceitável. Caso haja perda de dados entre backups, o RPO é de até 24h.
- **[Rate limiting pode bloquear usuários legítimos]** → Configurar limites conservadores (ex: 10 req/s por IP) e documentar como ajustar. Nginx retorna 503 quando limitado — incluir página de erro amigável.
- **[X-Accel-Redirect requer header interno]** → Se o Nginx não estiver configurado corretamente, o Django pode expor o header ou o arquivo pode não ser servido. Testar com cenário de arquivo inexistente e usuário sem permissão.
- **[Cron de backup depende do host]** → Se o host reiniciar, o cron precisa ser reiniciado. Alternativa: usar `restart: unless-stopped` no serviço de backup ou agendar via systemd timer no host.
