# Guia de Configuração e Implantação — XII CBNV 2026

Este documento detalha o funcionamento técnico da infraestrutura do projeto, focando em Docker, processos de build, gerenciamento de banco de dados e implantação.

---

## 1. Arquitetura Docker Compose

O projeto utiliza **Docker Compose** para orquestrar o ambiente de desenvolvimento e garantir paridade com a produção. A configuração base está no arquivo `docker-compose.yml`.

> **Regra crítica de dados:** o conteúdo do CMS não fica na imagem Docker nem no container `web`. O CMS fica no PostgreSQL, persistido no volume Docker `postgres_data`. Arquivos enviados pelo CMS ficam nos volumes `media_files` e `protected_media`. Rebuild de imagem e recriação de containers não apagam conteúdo, mas remover esses volumes apaga dados.

### 1.1 Serviços

- **db**: Instância PostgreSQL 18 (Alpine).
    - **Healthcheck**: O serviço `web` só inicia após o banco estar pronto para receber conexões (`pg_isready`).
    - **Persistência**: Dados são salvos no volume `postgres_data`, montado em `/var/lib/postgresql` conforme a estrutura exigida pelas imagens PostgreSQL 18+.
    - **Backups**: Volume `backups` montado em `/backups` para scripts de backup/restore.
- **web**: Aplicação Django 6.0.4 com Gunicorn (produção) ou `runserver` (desenvolvimento).
    - **Porta**: Expõe internamente na 8000. Em produção, acessível apenas via Nginx na rede `cbnv_internal`.
    - **Volumes**: O Compose atual monta o checkout do projeto em `/app`. Portanto, em deploy, o código ativo vem do diretório do servidor; o rebuild da imagem atualiza dependências e ambiente, mas `git pull` é o que atualiza os arquivos montados em `/app`.
- **nginx**: Reverse proxy Nginx Alpine.
    - **Portas**: 80 (HTTP → redirect HTTPS) e 443 (HTTPS).
    - **TLS**: Terminação SSL com certificados montados em volume.
    - **Rate limiting**: `limit_req_zone` por IP com burst configurável.
- **backup**: Serviço PostgreSQL dedicado que executa `scripts/backup.sh` a cada 24h.

### 1.1.1 Volumes persistentes e descartáveis

| Volume | Conteúdo | Pode apagar em deploy normal? | Como recuperar |
|---|---|---:|---|
| `postgres_data` | Banco PostgreSQL: Wagtail/CMS, usuários, páginas, menus, submissões, revisões | **Não** | Restore de backup `pg_dump` |
| `media_files` | Uploads públicos do CMS/Wagtail | **Não** | Restore/cópia de mídia |
| `protected_media` | Arquivos protegidos de submissões | **Não** | Restore/cópia de mídia protegida |
| `backups` | Dumps gerados pelo serviço `backup` | **Não**, a menos que já tenha cópia fora do Docker | Cópia externa/off-server |
| `staticfiles` | Resultado do `collectstatic` | Sim | `collectstatic --noinput` |
| volume anônimo `/app/.venv` | Ambiente Python do container `web` | Sim | Rebuild/restart do container |

Comandos como `docker compose down -v`, `docker volume prune`, `docker system prune --volumes` ou `docker volume rm cbnv-website_postgres_data` destroem o banco e deixam o CMS vazio após a próxima migração.

### 1.2 Comandos Úteis
```bash
# Iniciar em modo foreground (ver logs)
docker compose up

# Iniciar em modo background (detached)
docker compose up -d

# Parar e remover containers
docker compose down

# Ver logs em tempo real
docker compose logs -f web
```

### 1.3 Rede Interna

Todos os serviços (`web`, `db`, `nginx`) comunicam-se via rede Docker `cbnv_internal`. Em produção, o banco de dados não é exposto ao host. O `docker-compose.override.yml` (desenvolvimento) reexpõe as portas `8001` (web) e `5432` (db) para facilitar o desenvolvimento local.

---

## 2. Processo de Build

O build do projeto ocorre em duas camadas: a imagem do container e os ativos de frontend.

### 2.1 Build da Imagem (Dockerfile)
A imagem utiliza `python:3.13-slim` e o gerenciador de pacotes **uv**. O processo de build:
1. Instala o `uv` no container.
2. Sincroniza dependências via `pyproject.toml` e `uv.lock`.
3. Copia o código para o container.
4. Executa `collectstatic` para pré-compilar assets.

Para reconstruir a imagem após mudar dependências:
```bash
docker compose build
```

Para adicionar uma nova dependência Python:
```bash
uv add <nome-do-pacote>
docker compose build
```

### 2.2 Build do Frontend (Tailwind CSS)
O projeto usa Tailwind CSS 4. O build é gerenciado via npm.
- **Desenvolvimento**: O comando `npm run watch` monitora mudanças nos templates HTML e recompila o CSS automaticamente.
- **Produção**: O comando `npm run build` gera o CSS minificado em `static/css/output.css`.

No Docker, o CSS compilado é servido como um arquivo estático padrão do Django.

---

## 3. Gerenciamento de Banco de Dados e Migrações

O Django utiliza o sistema de migrações para sincronizar o modelo de dados Python com o schema do PostgreSQL.

Migrações **não criam conteúdo editorial do CMS**. Elas criam/alteram tabelas e colunas. Páginas Wagtail, menu do site, imagens, notícias, configurações do congresso e usuários precisam vir de um banco já existente ou de um restore de backup. Em um banco novo, após `migrate`, o admin e as tabelas existem, mas o CMS fica sem conteúdo até alguém cadastrar páginas ou rodar um comando de seed inicial.

### 3.1 Aplicando Migrações
```bash
docker compose exec web uv run python manage.py migrate
```

### 3.2 Criando Novas Migrações
```bash
docker compose exec web uv run python manage.py makemigrations
```

### 3.3 Inicialização (Superusuário)
```bash
docker compose exec web uv run python manage.py createsuperuser
```

### 3.4 Inicialização de ambiente vazio, sem dados reais

Use somente em desenvolvimento, staging descartável ou primeira instalação sem backup. Este comando cria conteúdo inicial de demonstração; ele **não restaura** o conteúdo real editado no CMS.

```bash
docker compose exec web uv run python manage.py populate_cbnv
docker compose exec web uv run python manage.py createsuperuser
```

Em produção com conteúdo existente, a sequência correta é restore de backup, depois migrações.

---

## 4. Backups e Restore

### 4.1 Backup Automatizado

O serviço `backup` executa `scripts/backup.sh` a cada 24h. O script:
- Faz `pg_dump --format=custom` do banco `cbnv`
- Comprime com `gzip`
- Salva em `/backups` (volume Docker) com timestamp: `cbnv_YYYYMMDD_HHMMSS.dump.gz`
- Mantém apenas os últimos `BACKUP_RETENTION_DAYS` backups (padrão: 7)

Para executar backup manualmente:
```bash
docker compose exec backup /scripts/backup.sh
```

Após qualquer backup importante, copie o arquivo para fora do volume Docker. O volume `backups` também é removido por `docker compose down -v` ou `docker system prune --volumes`.

```bash
mkdir -p backups
BACKUP_FILE=$(docker compose exec -T backup sh -c 'ls -t /backups/cbnv_*.dump.gz | head -n 1')
docker cp "$(docker compose ps -q backup):${BACKUP_FILE}" "backups/$(basename "${BACKUP_FILE}")"
ls -lh backups/
```

### 4.2 Restore (Apenas Banco)

```bash
# Listar backups disponíveis
docker compose exec backup ls -lh /backups/

# Restaurar backup específico (ATENÇÃO: destrói dados atuais)
docker compose exec backup /scripts/restore.sh /backups/cbnv_20260501_030000.dump.gz
```

O script de restore (`scripts/restore.sh`):
1. Encerra conexões ativas ao banco
2. Dropa e recria o banco
3. Restaura via `pg_restore --no-owner --no-acl`
4. Verifica contagem de tabelas restauradas

### 4.3 Scripts Automatizados de Rebuild e Restore Total

Para simplificar operações complexas e garantir a segurança dos dados (banco + mídias), utilize os scripts automatizados:

#### 4.3.1 Rebuild Total com Backup Automático
O script `scripts/rebuild.sh` realiza o backup completo (DB, media, protected_media), reconstrói a imagem e reinicia os serviços.

```bash
# Executa backup completo, rebuild e deploy
./scripts/rebuild.sh
```

#### 4.3.2 Restore Total (Disaster Recovery)
O script `scripts/restore_all.sh` restaura tanto o banco de dados quanto os volumes de mídia a partir de um diretório gerado pelo `rebuild.sh`.

```bash
# Restaura tudo a partir de um backup específico
./scripts/restore_all.sh backups/rebuild_YYYYMMDD_HHMMSS
```

### 4.4 Checklist de Validação Pós-Restore

Após executar o restore, verificar:

- [ ] O site carrega em HTTPS sem erros
- [ ] Login funciona com credenciais existentes
- [ ] Submissões são visíveis no painel
- [ ] Arquivos de submissão podem ser baixados (como dono/staff)
- [ ] `/health/` retorna `{"status": "ok"}`

---

## 5. Segurança

### 5.1 Headers de Segurança

Em produção, os seguintes headers são aplicados (via Nginx e Django):

| Header | Valor |
|---|---|
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains; preload` |
| `X-Content-Type-Options` | `nosniff` |
| `X-Frame-Options` | `DENY` |
| `Referrer-Policy` | `same-origin` |
| `Content-Security-Policy` | Restrito (ver `nginx/default.conf.template`) |

### 5.2 Rate Limiting

- **Nginx**: 10 req/s por IP (configurável via `NGINX_RATE_LIMIT`), burst de 20
- **django-axes**: 5 tentativas de login falhas → lockout de 15 minutos (configurável via env vars)

### 5.3 Media Protegido

Arquivos de submissão são servidos via view autorizada (`SubmissionFileDownloadView`) com delegação ao Nginx via `X-Accel-Redirect`. A URL `/media/submissions/` retorna 404 diretamente. O diretório `/protected-media/` é `internal` no Nginx.

### 5.4 SSL/TLS

O Nginx exige certificados montados em `./ssl/` (ou path configurado via `SSL_CERT_PATH`/`SSL_KEY_PATH`). Protocolos suportados: TLS 1.2 e TLS 1.3.

---

## 6. SSL/TLS

### 6.1 Preparar Certificados

Monte os certificados no diretório `ssl/` do projeto:

```
ssl/
├── cert.pem    # Certificado SSL (chain completo)
└── key.pem     # Chave privada
```

Em produção, use certificados válidos emitidos por uma CA confiável. Certificados self-signed podem ser usados em staging para testes.

---

## 7. Solução de Problemas (Troubleshooting)

### 7.1 Erro: `relation "wagtailcore_userprofile" does not exist`
Force a criação e aplicação da migração específica:
```bash
docker compose exec web uv run python manage.py makemigrations wagtailcore
docker compose exec web uv run python manage.py migrate
```

### 7.2 Erro: `nginx: [emerg] cannot load certificate`
Verifique se os certificados estão montados corretamente:
```bash
ls -la ssl/
docker compose exec nginx ls -la /etc/nginx/ssl/
```

### 7.3 Rate limiting bloqueando requisições legítimas
Ajuste as variáveis de ambiente:
```bash
NGINX_RATE_LIMIT=20r/s
NGINX_BURST=40
```

### 7.4 Email não chega em produção
Verifique as configurações SMTP no `.env`:
```bash
docker compose exec web python -c "
import django; django.setup()
from django.core.mail import send_mail
send_mail('Test', 'Test body', 'from@example.com', ['to@example.com'])
print('Email sent')
"
```

### 7.5 Health check falhando
```bash
docker compose exec web curl -f http://localhost:8000/health/
docker compose exec nginx wget -q -O- http://localhost/health/
```

### 7.6 Arquivos estáticos novos não aparecem no site
Se você adicionou arquivos em `static/` mas eles retornam 404 no navegador, é necessário sincronizá-los com o volume de estáticos que o Nginx consome:
```bash
docker compose exec web uv run python manage.py collectstatic --noinput
```
Isso ocorre porque o Nginx serve arquivos a partir do volume compartilhado `staticfiles`, que é preenchido durante o build da imagem ou manualmente via comando. O diretório `static/` (fonte) não é servido diretamente pelo Nginx em produção.

---

## 8. Implantação em Produção

### 8.1 Antes de qualquer deploy

Em produção, use explicitamente o arquivo base para não carregar `docker-compose.override.yml` por acidente:

```bash
COMPOSE="docker compose -f docker-compose.yml --env-file /etc/cbnv/.env"
```

O `docker-compose.override.yml` é para desenvolvimento local. Ele troca o comando do `web` para `runserver`, monta o código fonte e expõe portas de desenvolvimento.

### 8.2 Deploy normal preservando dados

Use esta sequência para atualizar código/imagem sem perder conteúdo CMS:

```bash
# 1. Entrar no diretório do projeto no servidor
cd /srv/cbnv-website

# 2. Garantir que o .env de produção existe e usa settings de produção
grep -E 'DJANGO_SETTINGS_MODULE|POSTGRES_DB|POSTGRES_USER|DB_HOST' /etc/cbnv/.env

# 3. Definir comando Compose de produção
COMPOSE="docker compose -f docker-compose.yml --env-file /etc/cbnv/.env"

# 4. Ver estado atual
$COMPOSE ps
docker volume ls | grep cbnv

# 5. Fazer backup antes de alterar containers ou schema
$COMPOSE up -d db backup
$COMPOSE exec backup /scripts/backup.sh
mkdir -p backups
BACKUP_FILE=$($COMPOSE exec -T backup sh -c 'ls -t /backups/cbnv_*.dump.gz | head -n 1')
docker cp "$($COMPOSE ps -q backup):${BACKUP_FILE}" "backups/$(basename "${BACKUP_FILE}")"
ls -lh "backups/$(basename "${BACKUP_FILE}")"

# 6. Atualizar código
git pull --ff-only

# 7. Se houve alteração de Tailwind/CSS, recompilar o CSS fonte
npm ci
npm run build

# 8. Rebuild da imagem e recriação dos containers, mantendo volumes persistentes
$COMPOSE build web
$COMPOSE up -d --remove-orphans db web nginx backup

# 9. Aplicar migrações e estáticos
$COMPOSE exec web uv run python manage.py migrate --noinput
$COMPOSE exec web uv run python manage.py collectstatic --noinput

# 10. Validar
$COMPOSE ps
curl -I https://<domain>/health/
curl -I https://<domain>/
```

Não rode `docker compose down -v` nesse fluxo. `docker compose down` sem `-v` é aceitável quando você precisa parar tudo, porque preserva volumes nomeados.

### 8.3 Full rebuild sem perder dados

Use quando quiser recriar todos os containers e reconstruir a imagem, mas manter banco, CMS e uploads:

```bash
cd /srv/cbnv-website
COMPOSE="docker compose -f docker-compose.yml --env-file /etc/cbnv/.env"

# Backup obrigatório antes do rebuild
$COMPOSE up -d db backup
$COMPOSE exec backup /scripts/backup.sh
mkdir -p backups
BACKUP_FILE=$($COMPOSE exec -T backup sh -c 'ls -t /backups/cbnv_*.dump.gz | head -n 1')
docker cp "$($COMPOSE ps -q backup):${BACKUP_FILE}" "backups/$(basename "${BACKUP_FILE}")"

# Parar/remover containers e rede, preservando volumes
$COMPOSE down --remove-orphans

# Opcional: remover apenas volume descartável de staticfiles
docker volume rm cbnv-website_staticfiles 2>/dev/null || true

# Nunca remova estes volumes em deploy normal:
# cbnv-website_postgres_data
# cbnv-website_media_files
# cbnv-website_protected_media
# cbnv-website_backups

# Rebuild e subida
$COMPOSE build --no-cache web
$COMPOSE up -d db web nginx backup

# Schema e assets
$COMPOSE exec web uv run python manage.py migrate --noinput
$COMPOSE exec web uv run python manage.py collectstatic --noinput

# Validação do CMS
$COMPOSE exec web uv run python manage.py shell -c "from wagtail.models import Page; from core.models import SiteMenu; print('pages=', Page.objects.count()); print('menus=', SiteMenu.objects.count())"
curl -I https://<domain>/
```

### 8.4 Recuperação se o CMS ficou vazio

Se após `migrate` o CMS apareceu vazio, provavelmente o banco PostgreSQL foi recriado ou o volume `postgres_data` foi removido. Migrações não recuperam conteúdo.

Restaure um backup:

```bash
cd /srv/cbnv-website
COMPOSE="docker compose -f docker-compose.yml --env-file /etc/cbnv/.env"

$COMPOSE up -d db backup
$COMPOSE exec backup ls -lh /backups/

# Escolha o arquivo correto:
$COMPOSE exec backup /scripts/restore.sh /backups/cbnv_YYYYMMDD_HHMMSS.dump.gz

$COMPOSE up -d web nginx
$COMPOSE exec web uv run python manage.py migrate --noinput
$COMPOSE exec web uv run python manage.py collectstatic --noinput
```

Se o backup estava fora do Docker, copie-o para o container/volume antes:

```bash
docker cp backups/cbnv_YYYYMMDD_HHMMSS.dump.gz "$($COMPOSE ps -q backup):/backups/cbnv_YYYYMMDD_HHMMSS.dump.gz"
$COMPOSE exec backup /scripts/restore.sh /backups/cbnv_YYYYMMDD_HHMMSS.dump.gz
```

### 8.5 Primeira instalação sem backup

Use somente quando não existe conteúdo real para preservar:

```bash
cd /srv/cbnv-website
COMPOSE="docker compose -f docker-compose.yml --env-file /etc/cbnv/.env"

$COMPOSE up -d --build db web nginx backup
$COMPOSE exec web uv run python manage.py migrate --noinput
$COMPOSE exec web uv run python manage.py populate_cbnv
$COMPOSE exec web uv run python manage.py createsuperuser
$COMPOSE exec web uv run python manage.py collectstatic --noinput
```

Depois disso, qualquer conteúdo editado no Wagtail passa a depender do banco `postgres_data` e dos volumes de mídia. Preserve-os ou faça restore.

### 8.6 Checklist de Verificação Pós-Deploy

- [ ] HTTPS funcional (sem aviso de certificado)
- [ ] Headers de segurança presentes (verificar com `curl -I https://<domain>/`)
- [ ] `/health/` retorna HTTP 200 com `{"status": "ok"}`
- [ ] Login funciona
- [ ] Admin Wagtail acessível em `/admin/`
- [ ] Home, Sobre, Programação e Edições Anteriores aparecem e navegam pelo menu superior
- [ ] O menu do CMS em Wagtail possui itens, ou o fallback público está renderizando links básicos
- [ ] Arquivos de submissão não são acessíveis por URL direta
- [ ] Rate limiting ativo (verificar com múltiplas requisições rápidas)
- [ ] Logs JSON visíveis em `docker compose logs web`
- [ ] Backup diário configurado (verificar em `docker compose logs backup`)
- [ ] Restore testado com sucesso
