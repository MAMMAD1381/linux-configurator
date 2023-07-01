#!/bin/bash

# Check if one argument is given
if [ $# -ne 1 ]; then
echo "Usage: $0 hostname"
exit 1
fi
hostname=$1
# Check if the hostname is valid
if ! [[ $hostname =~ ^[a-zA-Z0-9.-]+$ ]]; then
echo "Invalid hostname format"
exit 2
fi

# Backup the original hostname file
cp /etc/hostname /etc/hostname.bak

# Write the new hostname to the hostname file
echo "$hostname" > /etc/hostname

# Update the hosts file with the new hostname
sed -i "s/$(hostname)/$hostname/g" /etc/hosts

# Print a success message
echo "Hostname changed permanently to $hostname"