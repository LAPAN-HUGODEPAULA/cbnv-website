## Why

A aplicação possui os fluxos centrais operacionais (submissões, avaliações, CMS), mas não está endurecida para staging/produção. Arquivos de submissão ficam acessíveis por URL direta, não há reverse proxy, HTTPS, backups automatizados ou rate limiting. Sem essas camadas, a plataforma não pode ser implantada em ambiente público com segurança.

## What Changes

- Adicionar reverse proxy Nginx no Docker Compose com terminação TLS e headers de segurança
- Implementar serving de media protegido (arquivos de submissão inacessíveis por URL direta)
- Configurar backups automatizados do PostgreSQL com restore verificado
- Adicionar rate limiting em endpoints públicos (login, formulário de contato, health check)
- Configurar logging estruturado em JSON para produção (coleta via stdout/stderr)
- Documentar SMTP transacional e variáveis de ambiente adicionais em `.env.example`
- Adicionar playbook de restore e checklist de verificação pós-deploy
- Atualizar `docker-compose.yml` e `docker-compose.override.yml` com rede isolada, health checks e volumes de backup

## Capabilities

### New Capabilities

(nenhuma — todos os requisitos se encaixam em specs existentes)

### Modified Capabilities

- `deployment-security`: adicionar requisitos de reverse proxy/TLS, rate limiting, logging estruturado, backups/restore, media protegido, rede Docker isolada, health check do proxy
- `developer-experience`: atualizar `.env.example` com novas variáveis (SMTP, Nginx, backups), documentar comandos de restore e verificação de saúde
- `submissions`: reforçar que arquivos submetidos NÃO são acessíveis por URL direta — servir via view autorizada com X-Accel-Redirect ou response streaming
- `notifications`: adicionar requisitos de configuração SMTP em produção (host, porta, TLS, credenciais via env vars), fallback gracioso e logging de falhas de envio

## Impact

- `docker-compose.yml` / `docker-compose.override.yml`: novo serviço `nginx`, rede, volumes de backup
- `cbnv/settings/production.py`: novas configurações de segurança, SMTP, logging, rate limiting
- `submissions/views.py` (ou novo `media/views.py`): view de serving de arquivos protegidos
- Novos arquivos: `nginx/default.conf`, `scripts/backup.sh`, `scripts/restore.sh`, `docs/implementation/SETUP_DEPLOY.md` (atualização)
- Dependências: `django-axes` (rate limiting), `gunicorn` (WSGI prod)
- Nenhuma mudança breaking em models, APIs REST ou templates existentes
