#!/bin/bash
# Backs up the OpenShift PostgreSQL database for this application
# by Skye Book <skye.book@gmail.com>
 
NOW="$(date +"%Y-%m-%d")"
FILENAME="$OPENSHIFT_DATA_DIR/db_backups/$OPENSHIFT_APP_NAME.$NOW.backup.sql.gz"
/opt/rh/postgresql92/root/usr/bin/pg_dump -h $OPENSHIFT_POSTGRESQL_DB_HOST -p $OPENSHIFT_POSTGRESQL_DB_PORT -F c $OPENSHIFT_APP_NAME > $FILENAME