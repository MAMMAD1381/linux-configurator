#!/bin/bash

# Check if the name and family type are provided as arguments
if [ $# -ne 2 ]; then
echo "Usage: $0 name family"
exit 1
fi

# Assign the arguments to variables
family=$1
name=$2

# Check if the family type is valid
if [ "$family" != "ip" ] && [ "$family" != "ip6" ] && [ "$family" != "inet" ] && [ "$family" != "arp" ] && [ "$family" != "bridge" ]; then
echo "Invalid family type: $family"
exit 2
fi

# Create the table using nft command
nft add table $family $name

# Check if the table creation was successful
if [ $? -eq 0 ]; then
echo "Table $name created successfully"
else
echo "Table creation failed"
fi