# Guia de Configuração e Implantação — XII CBNV 2026

Este documento detalha o funcionamento técnico da infraestrutura do projeto, focando em Docker, processos de build, gerenciamento de banco de dados e implantação.

---

## 1. Arquitetura Docker Compose

O projeto utiliza **Docker Compose** para orquestrar o ambiente de desenvolvimento e garantir paridade com a produção. A configuração base está no arquivo `docker-compose.yml`.

### 1.1 Serviços
- **db**: Instância PostgreSQL 18 (Alpine).
    - **Healthcheck**: O serviço `web` só inicia após o banco estar pronto para receber conexões (`pg_isready`).
    - **Persistência**: Dados são salvos no volume `postgres_data`.
- **web**: Aplicação Django 6.0.4.
    - **Porta**: Mapeada internamente na 8000. Por padrão, exposta na porta **8001** do host para evitar conflitos com outros serviços locais.
    - **Volumes**: O código fonte é montado em `/app` para permitir *live reload* durante o desenvolvimento.

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

---

## 2. Processo de Build

O build do projeto ocorre em duas camadas: a imagem do container e os ativos de frontend.

### 2.1 Build da Imagem (Dockerfile)
A imagem utiliza `python:3.13-slim` e o gerenciador de pacotes **uv**. O processo de build:
1. Instala o `uv` no container.
2. Sincroniza dependências via `pyproject.toml` e `uv.lock`.
3. Copia o código para o container.

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

### 3.1 Aplicando Migrações
Sempre que iniciar o ambiente pela primeira vez ou baixar mudanças de código que alterem modelos:
```bash
docker compose exec web uv run python manage.py migrate
```

### 3.2 Criando Novas Migrações
Se você alterar um arquivo `models.py`:
```bash
docker compose exec web uv run python manage.py makemigrations
```
As migrações geradas aparecerão na sua pasta local (devido ao volume montado) e devem ser commitadas no repositório.

### 3.3 Inicialização (Superusuário)
Para acessar o admin (`/admin/`), você precisa de um usuário administrador:
```bash
docker compose exec web uv run python manage.py createsuperuser
```

---

## 5. Solução de Problemas (Troubleshooting)

### 5.1 Erro: `relation "wagtailcore_userprofile" does not exist`
Se ao acessar o `/admin/` você encontrar um erro de banco de dados mencionando `wagtailcore_userprofile`, é provável que as migrações internas do Wagtail não tenham sido totalmente detectadas.

**Solução:** Force a criação e aplicação da migração específica:
```bash
docker compose exec web uv run python manage.py makemigrations wagtailcore
docker compose exec web uv run python manage.py migrate
```

---

## 6. Checklist de Deploy
1. Configurar `.env` com `DEBUG=False` e `ALLOWED_HOSTS`.
2. Build da imagem Docker.
3. Executar `migrate`.
4. Executar `collectstatic`.
5. Garantir que o volume de `media` tenha as permissões corretas.
