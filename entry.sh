#!/bin/sh

# Add Docker compose env to local env folder
if ! grep -q DB_HOST "/etc/environment"; then
  printenv | grep 'DB_HOST' >> /etc/environment
fi

# start cron
/usr/sbin/cron -f -l 8