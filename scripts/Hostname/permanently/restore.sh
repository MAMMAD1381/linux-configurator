#!/bin/bash

backup=/etc/hostname.bak

if [ -f "$backup" ]; then
    cp /etc/hostname.bak /etc/hostname
    echo setting restored
else 
    echo "backup file not found (you havn't changed the settings maybe)"
fi

# use backup file which we made recently to restore settings