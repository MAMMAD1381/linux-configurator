#!/bin/bash

if [[ $1 == "temporary" ]]; then
    cp /etc/resolv.conf /etc/resolv.conf.bak
    echo succesfull backup for temporary dns-settings
elif [[ $1 == "permanently" ]]; then 
    cp /etc/network/interfaces /etc/network/interfaces.bak
    echo succesfull backup for permanently dns-settings
else
    echo type parameter is wrong
fi