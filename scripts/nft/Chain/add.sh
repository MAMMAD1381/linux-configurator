#!/bin/bash

# Check if the family type, table name and chain name are provided as arguments
if [ $# -lt 3 ]; then
echo "Usage: $0 family table chain [type hook priority]"
exit 1
fi

# Assign the arguments to variables
family=$1
table=$2
chain=$3

# Check if the chain type, hook and priority are provided as optional arguments
if [ $# -eq 7 ]; then
type=$4
hook=$5
priority=$6
policy=$7
# Create the chain configuration string with the optional arguments
config="{ type $type hook $hook priority $priority ; policy $policy ; }"
else
# Create an empty chain configuration string
config=""
fi

# Create the chain using nft command
nft add chain $family $table $chain "$config"

# Check if the chain creation was successful
if [ $? -eq 0 ]; then
echo "Chain $chain created successfully in table $table"
else
echo "Chain creation failed"
fi