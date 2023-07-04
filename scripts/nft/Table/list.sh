#!/bin/bash

# Check if the name and family type are provided as arguments
if ! [ $# -ne 2 ]; then

# Assign the arguments to variables
family=$1
name=$2


# Check if the family type is valid
if [ "$family" != "ip" ] && [ "$family" != "ip6" ] && [ "$family" != "inet" ] && [ "$family" != "arp" ] && [ "$family" != "bridge" ]; then
echo "Invalid family type: $family"
exit 2
fi

# listing based on name and family type
nft list table $family $name


else

nft list tables

fi