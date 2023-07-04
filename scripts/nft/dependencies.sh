#!/bin/bash

# Check if the package name is provided as an argument
if [ $# -ne 1 ]; then
echo "Usage: $0 package"
exit 1
fi

# Assign the argument to a variable
package=$1

# Check if the package is installed using dpkg command
dpkg -s $package > /dev/null 2>&1

# If the package is not installed, install it using apt command
if [ $? -ne 0 ]; then
echo "Package $package is not installed"
echo "Installing $package..."
sudo apt update
sudo apt install -y $package
# else
# echo "Package $package is already installed"
fi