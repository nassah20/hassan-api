#!/bin/bash

LOG="/home/ubuntu/hassan-api/bash_scripts/update.log"
cd /home/ubuntu/hassan-api || exit 1

echo "[$(date)] Updating packages..." >> $LOG
sudo apt update && sudo apt upgrade -y >> $LOG

echo "[$(date)] Pulling latest code..." >> $LOG
git pull origin main >> $LOG 2>&1
if [ $? -ne 0 ]; then
  echo "Git pull failed. Exiting..." >> $LOG
  exit 1
fi

echo "Restarting web server..." >> $LOG
echo "No web server to restart.">> $LOG
echo "Update complete." >> $LOG
