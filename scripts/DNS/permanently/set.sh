#!/bin/bash

# Check if two arguments are given
if [ $# -ne 2 ]; then
echo "Usage: $0 ip1 ip2"
exit 1
fi

# Check if the arguments are valid IP addresses
if ! [[ $1 =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]] || ! [[ $2 =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
echo "Invalid IP address format"
exit 2
fi

dns1=$1
dns2=$2

# Backup the original interfaces file
# cp /etc/network/interfaces /etc/network/interfaces.bak

# #removing the previous dns
# bash remove.sh

# Append the DNS settings to the interfaces file
echo "dns-nameservers $dns1 $dns2" >> /etc/network/interfaces

# Print a success message
echo "DNS settings updated successfully: primary DNS: $dns1, secondary DNS: $dns2"
echo pls restart your network service to see the changes