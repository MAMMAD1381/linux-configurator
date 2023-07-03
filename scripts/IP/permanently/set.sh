#!/bin/bash

# Check if the interface name is given as an argument
if [ $# -eq 0 ]; then
echo "Usage: $0 interface_name [options]"
exit 1
fi

# Assign the interface name to a variable
interface=$1

# Shift the positional parameters
shift

# Assign the remaining arguments to variables
address=$1
netmask=$2
gateway=$3
dns1=$4
dns2=$5
# Check if the interface exists in /etc/network/interfaces
if grep -q "^auto $interface" /etc/network/interfaces; then
# Replace the existing interface with the new one
echo "Replacing the existing interface $interface with the new one"
# Delete all the lines between auto $interface and next auto or end of file
sudo sed -i "/^auto $interface/,/^auto\|\$/d" /etc/network/interfaces
# Insert the new interface and options at the end of file
sudo echo -e "\nauto $interface\niface $interface inet static\naddress $address\nnetmask $netmask\ngateway $gateway\ndns-nameservers $dns1 $dns2" >> /etc/network/interfaces
else
# Create a new interface
echo "Creating a new interface $interface"
sudo echo -e "\nauto $interface\niface $interface inet static\naddress $address\nnetmask $netmask\ngateway $gateway\ndns-nameservers $dns1 $dns2" >> /etc/network/interfaces
fi

# # Restart the networking service
# sudo service networking restart