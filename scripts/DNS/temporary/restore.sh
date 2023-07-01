#!/bin/bash

backup=/etc/resolv.conf.bak
if [ -f "$backup" ]; then
    cp /etc/resolv.conf.bak /etc/resolv.conf
    echo setting restored
else 
    echo "backup file not found (you havn't changed the settings maybe)"
fi

# use backup file which we made recently to restore settings
