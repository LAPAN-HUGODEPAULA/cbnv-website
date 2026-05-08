#!/bin/bash
# scripts/rebuild.sh — Full rebuild with data safety for XII CBNV 2026
set -euo pipefail

# 1. Configuration & Setup
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="backups/rebuild_${TIMESTAMP}"
mkdir -p "$BACKUP_DIR"

echo "================================================================"
echo "XII CBNV 2026 — FULL REBUILD STARTING"
echo "Timestamp: $TIMESTAMP"
echo "Backup Directory: $BACKUP_DIR"
echo "================================================================"

# 2. Backup Phase
echo "[1/4] Starting full data backup..."

# 2.1 Database Backup
echo "  -> Backing up database..."
docker compose exec -T backup /scripts/backup.sh
LATEST_DB_BACKUP=$(docker compose exec -T backup sh -c 'ls -t /backups/cbnv_*.dump.gz | head -n 1')
docker cp "$(docker compose ps -q backup):${LATEST_DB_BACKUP}" "${BACKUP_DIR}/db_backup.dump.gz"

# 2.2 Media Files Backup
echo "  -> Backing up media files..."
docker run --rm -v cbnv-website_media_files:/volume -v "$(pwd)/${BACKUP_DIR}":/backup alpine \
    tar -czf /backup/media_files.tar.gz -C /volume .

# 2.3 Protected Media Backup
echo "  -> Backing up protected media..."
docker run --rm -v cbnv-website_protected_media:/volume -v "$(pwd)/${BACKUP_DIR}":/backup alpine \
    tar -czf /backup/protected_media.tar.gz -C /volume .

echo "[OK] Backup completed successfully in $BACKUP_DIR"

# 3. Rebuild Phase
echo "[2/4] Rebuilding web container..."

# We build before stopping to minimize downtime
docker compose build --no-cache web

# 4. Deployment Phase
echo "[3/4] Deploying updated containers..."

# Stop and remove only the web container as requested
echo "  -> Deleting existing web container..."
docker compose stop web
docker compose rm -f web

# Re-deploy
echo "  -> Starting containers..."
docker compose up -d web nginx

# 5. Initialization Phase
echo "[4/4] Finalizing deployment..."

echo "  -> Running migrations..."
docker compose exec web uv run python manage.py migrate --noinput

echo "  -> Collecting static files..."
docker compose exec web uv run python manage.py collectstatic --noinput

echo "  -> Cleaning up old images..."
docker image prune -f

echo "================================================================"
echo "REBUILD COMPLETED SUCCESSFULLY"
echo "================================================================"
echo "Verification Checklist:"
echo "1. Check logs: docker compose logs -f web"
echo "2. Check health: curl -I http://localhost:8001/health/"
echo "3. Backups preserved in: $BACKUP_DIR"
echo "================================================================"
