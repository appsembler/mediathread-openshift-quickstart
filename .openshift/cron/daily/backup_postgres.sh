#!/bin/bash
# Backs up the OpenShift PostgreSQL database for this application
# by Skye Book <skye.book@gmail.com>
 
NOW="$(date +"%Y-%m-%d")"
FILENAME="$OPENSHIFT_DATA_DIR/$OPENSHIFT_APP_NAME.$NOW.backup.sql.gz"
pg_dump -h $OPENSHIFT_POSTGRESQL_DB_HOST -p $OPENSHIFT_POSTGRESQL_DB_PORT -F c $OPENSHIFT_APP_NAME | gzip -c -9 > $FILENAME