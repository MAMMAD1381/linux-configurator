#! /bin/bash

if [ $# -ne 2 ]; then
echo "Usage: $0 dns1 dns2"
exit 1
fi

# Check if the arguments are valid IP addresses
if ! [[ $1 =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]] || ! [[ $2 =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
echo "Invalid IP address format"
exit 2
fi

dns1=$1
dns2=$2


# Save the original /etc/resolv.conf file
# cp /etc/resolv.conf /etc/resolv.conf.bak

#removing the previous dns
# bash remove.sh


# Append the new nameserver lines to /etc/resolv.conf
echo "nameserver $dns1" >> /etc/resolv.conf
echo "nameserver $dns2" >> /etc/resolv.conf

echo setting $dns1 and $dns2 as primary and secondary dns

# Exit with success
exit 0



