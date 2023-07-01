#!/bin/bash

# Remove all the nameserver lines from /etc/resolv.conf
sed -i "/nameserver/d" /etc/resolv.conf

echo dns servers removed succesfully

# Exit with success
exit 0