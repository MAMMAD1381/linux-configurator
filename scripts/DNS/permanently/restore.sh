#!/bin/bash

backup=/etc/network/interfaces.bak
if [ -f "$backup" ]; then
    cp /etc/network/interfaces.bak /etc/network/interfaces
    echo setting restored
else 
    echo "backup file not found (you havn't changed the settings maybe)"
fi

# use backup file which we made recently to restore settings
