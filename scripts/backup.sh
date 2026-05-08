#!/bin/sh
set -eu

POSTGRES_HOST="${POSTGRES_HOST:-db}"
POSTGRES_DB="${POSTGRES_DB:-cbnv}"
POSTGRES_USER="${POSTGRES_USER:-cbnv}"
POSTGRES_PASSWORD="${POSTGRES_PASSWORD:-cbnv}"
BACKUP_DIR="/backups"
RETENTION_DAYS="${BACKUP_RETENTION_DAYS:-7}"

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="${BACKUP_DIR}/cbnv_${TIMESTAMP}.dump"

export PGPASSWORD="$POSTGRES_PASSWORD"

echo "[backup] Starting backup of ${POSTGRES_DB} at $(date)"

pg_dump \
    -h "$POSTGRES_HOST" \
    -U "$POSTGRES_USER" \
    -d "$POSTGRES_DB" \
    --format=custom \
    > "$BACKUP_FILE"

gzip "$BACKUP_FILE"

echo "[backup] Backup created: ${BACKUP_FILE}.gz ($(du -h "${BACKUP_FILE}.gz" | cut -f1))"

echo "[backup] Pruning backups older than ${RETENTION_DAYS} days..."
find "$BACKUP_DIR" -name "cbnv_*.dump.gz" -type f -mtime +"$RETENTION_DAYS" -delete

REMAINING=$(find "$BACKUP_DIR" -name "cbnv_*.dump.gz" -type f | wc -l)
echo "[backup] Backup complete. ${REMAINING} backup(s) retained."

unset PGPASSWORD
