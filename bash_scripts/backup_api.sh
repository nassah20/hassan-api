#!/bin/bash

LOG_FILE="/var/log/backup.log"
BACKUP_DIR="/home/ubuntu/backups"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
DATE=$(date +%F)

API_DIR="/var/https://github.com/nassah20/hassan-api"  
DB_NAME=" "
DB_USER=" "    

echo "[$TIMESTAMP] Starting backup..." >> $LOG_FILE

mkdir -p $BACKUP_DIR


# Backup API files
API_BACKUP="$BACKUP_DIR/api_backup_$DATE.tar.gz"
tar -czf $API_BACKUP $API_DIR 2>> $LOG_FILE

# Backup MySQL database
DB_BACKUP="$BACKUP_DIR/db_backup_$DATE.sql"
mysqldump -u $DB_USER -p $DB_NAME > $DB_BACKUP 2>> $LOG_FILE

# Delete backups older than 7 days
find $BACKUP_DIR -type f -mtime +7 -exec rm {} \;

if [[ -f $API_BACKUP && -f $DB_BACKUP ]]; then
    echo "[$TIMESTAMP] Backup successful." >> $LOG_FILE
else
    echo "[$TIMESTAMP] Backup failed!" >> $LOG_FILE
fi

echo "-----------------------------" >> $LOG_FILE

