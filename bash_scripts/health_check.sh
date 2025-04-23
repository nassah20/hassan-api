#!/bin/bash

LOG_FILE="/home/ubuntu/hassan-api/bash_scripts/server_health.log"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

echo "[$TIMESTAMP] Starting health check..." >> $LOG_FILE

CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
MEMORY=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
DISK=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')

API1=$(curl -s -o /dev/null -w "%{http_code}" http://13.60.254.240/students)
API2=$(curl -s -o /dev/null -w "%{http_code}" http://13.60.254.240/subjects)

echo "CPU: $CPU%, MEM: $MEMORY%, DISK: $DISK%" >> $LOG_FILE
echo "API /students: $API1, /subjects: $API2" >> $LOG_FILE

[[ "$DISK" -lt 10 ]] && echo "WARNING: Disk space < 10%" >> $LOG_FILE
[[ "$API1" -ne 200 ]] && echo "WARNING: /students endpoint down!" >> $LOG_FILE
[[ "$API2" -ne 200 ]] && echo "WARNING: /subjects endpoint down!" >> $LOG_FILE

echo "Done." >> $LOG_FILE
echo "-----------------------------" >> $LOG_FILE
