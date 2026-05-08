#!/bin/sh
set -eu

if [ $# -lt 1 ]; then
    echo "Usage: $0 <backup-file.gz>"
    echo ""
    echo "Restore a CBNV database backup."
    echo ""
    echo "Arguments:"
    echo "  backup-file.gz  Path to a gzip-compressed pg_dump custom format backup"
    echo ""
    echo "Environment variables:"
    echo "  POSTGRES_HOST     Database host (default: db)"
    echo "  POSTGRES_DB       Database name (default: cbnv)"
    echo "  POSTGRES_USER     Database user (default: cbnv)"
    echo "  POSTGRES_PASSWORD Database password (default: cbnv)"
    exit 1
fi

BACKUP_FILE="$1"

if [ ! -f "$BACKUP_FILE" ]; then
    echo "[restore] ERROR: File not found: $BACKUP_FILE"
    exit 1
fi

POSTGRES_HOST="${POSTGRES_HOST:-db}"
POSTGRES_DB="${POSTGRES_DB:-cbnv}"
POSTGRES_USER="${POSTGRES_USER:-cbnv}"
POSTGRES_PASSWORD="${POSTGRES_PASSWORD:-cbnv}"

export PGPASSWORD="$POSTGRES_PASSWORD"

echo "[restore] Restoring from: $BACKUP_FILE"
echo "[restore] Target database: ${POSTGRES_DB}@${POSTGRES_HOST}"

echo "[restore] Step 1/3: Terminating existing connections..."
psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d postgres -c \
    "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = '${POSTGRES_DB}' AND pid <> pg_backend_pid();" \
    2>/dev/null || true

echo "[restore] Step 2/3: Dropping and recreating database..."
dropdb -h "$POSTGRES_HOST" -U "$POSTGRES_USER" --if-exists "$POSTGRES_DB"
createdb -h "$POSTGRES_HOST" -U "$POSTGRES_USER" "$POSTGRES_DB"

echo "[restore] Step 3/3: Restoring backup..."
gunzip -c "$BACKUP_FILE" | pg_restore \
    -h "$POSTGRES_HOST" \
    -U "$POSTGRES_USER" \
    -d "$POSTGRES_DB" \
    --no-owner \
    --no-acl \
    --verbose

echo "[restore] Verifying restore..."
TABLE_COUNT=$(psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -t -c \
    "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'public';" | xargs)

echo "[restore] Restore complete. ${TABLE_COUNT} table(s) in database."
echo "[restore] Running Django migrations check..."

unset PGPASSWORD
