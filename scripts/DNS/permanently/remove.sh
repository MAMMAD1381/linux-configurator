#!/bin/bash

# Delete the line with dns-nameservers from the interfaces file
sed -i '/dns-nameservers/d' /etc/network/interfaces

# Print a success message
echo "DNS settings removed successfully"
echo pls restart your network service to see the changes
