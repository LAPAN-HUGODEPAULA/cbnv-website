#!/bin/bash
# scripts/restore_all.sh — Restore database and media from a rebuild backup
set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Usage: $0 <backup-directory>"
    echo "Example: $0 backups/rebuild_20260507_123456"
    exit 1
fi

BACKUP_DIR="$1"

if [ ! -d "$BACKUP_DIR" ]; then
    echo "ERROR: Backup directory not found: $BACKUP_DIR"
    exit 1
fi

echo "================================================================"
echo "XII CBNV 2026 — FULL RESTORE STARTING"
echo "Source: $BACKUP_DIR"
echo "================================================================"

# 1. Restore Database
if [ -f "${BACKUP_DIR}/db_backup.dump.gz" ]; then
    echo "[1/3] Restoring database..."
    # Copy to backup volume first
    docker cp "${BACKUP_DIR}/db_backup.dump.gz" "$(docker compose ps -q backup):/backups/restore_temp.dump.gz"
    # Run existing restore script
    docker compose exec -T backup /scripts/restore.sh /backups/restore_temp.dump.gz
    # Clean up temp file
    docker compose exec -T backup rm /backups/restore_temp.dump.gz
else
    echo "[SKIP] Database backup not found in $BACKUP_DIR"
fi

# 2. Restore Media Files
if [ -f "${BACKUP_DIR}/media_files.tar.gz" ]; then
    echo "[2/3] Restoring media files..."
    docker run --rm -v cbnv-website_media_files:/volume -v "$(pwd)/${BACKUP_DIR}":/backup alpine \
        sh -c "rm -rf /volume/* && tar -xzf /backup/media_files.tar.gz -C /volume"
else
    echo "[SKIP] Media files backup not found in $BACKUP_DIR"
fi

# 3. Restore Protected Media
if [ -f "${BACKUP_DIR}/protected_media.tar.gz" ]; then
    echo "[3/3] Restoring protected media..."
    docker run --rm -v cbnv-website_protected_media:/volume -v "$(pwd)/${BACKUP_DIR}":/backup alpine \
        sh -c "rm -rf /volume/* && tar -xzf /backup/protected_media.tar.gz -C /volume"
else
    echo "[SKIP] Protected media backup not found in $BACKUP_DIR"
fi

echo "================================================================"
echo "RESTORE COMPLETED SUCCESSFULLY"
echo "================================================================"
echo "Next steps:"
echo "1. Restart web container: docker compose restart web"
echo "2. Check site: http://localhost:8001/"
echo "================================================================"
