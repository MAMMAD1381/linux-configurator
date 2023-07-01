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

# Change the hostname using the hostname command
hostname "$hostname"

# Print a success message
echo "Hostname changed temporarily to $hostname"