#!/bin/bash

# Check if six arguments are given
if [ $# -ne 6 ]; then
echo "Usage: $0 interface ip_address netmask gateway dns1 dns2"
exit 1
fi

interface=$1
ip=$2
mask=$3
gateway=$4
dns1=$5
dns2=$6

# Check if the interface exists
if ! ip link show "$interface" > /dev/null 2>&1; then
echo "Invalid interface name"
exit 2
fi

# Check if the IP address, netmask, gateway, and DNS servers are valid
for arg in {2..6}; do
if ! [[ ${!arg} =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
echo "Invalid IP address format for argument $arg"
exit 3
fi
done

# Backup the original network configuration file
cp /etc/network/interfaces /etc/network/interfaces.bak

# Find the old IP address of the interface
old_ip=$(ip addr show "$interface" | grep -oP '(?<=inet\s)\d+(\.\d+){3}')

# Replace the old IP address with the new one in the network configuration file
sed -i "s/$old_ip/$ip/g" /etc/network/interfaces

# Add or replace the netmask, gateway, and DNS servers in the network configuration file
sed -i "/iface $interface inet static/a\    netmask $mask" /etc/network/interfaces
sed -i "/netmask $mask/a\    gateway $gateway" /etc/network/interfaces
sed -i "/gateway $gateway/a\    dns-nameservers $dns1 $dns2" /etc/network/interfaces

# Restart the network service or reboot the system for the changes to take effect
systemctl restart networking

# Print a success message
echo "Static IP address and other settings configured successfully"
