#!/bin/bash

# Check if three arguments are given
if [ $# -ne 3 ]; then
echo "Usage: $0 interface new_ip_address new_netmask"
exit 1
fi

interface=$1
new_ip=$2
new_mask=$3

# Check if the interface exists
if ! ip link show "$interface" > /dev/null 2>&1; then
echo "Invalid interface name"
exit 2
fi

# Check if the new IP address and netmask are valid
for arg in {2..2}; do
if ! [[ ${!arg} =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
echo "Invalid IP address format for argument $arg"
exit 3
fi
done

# Find the old IP address and netmask of the interface
old_ip=$(ip addr show "$interface" | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
old_mask=$(ip addr show "$interface" | grep -oP '(?<=inet\s)\d+(\.\d+){3}/\d+')
echo old ip and mask: $old_mask $new_mask
# Change the IP address and netmask using the ip command
ip addr add "$new_mask" dev "$interface"
ip addr del "$old_mask" dev "$interface"

# Print a success message
echo "IP address and netmask changed temporarily"