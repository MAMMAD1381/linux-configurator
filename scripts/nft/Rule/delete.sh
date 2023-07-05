#!/bin/bash

# Check if the family type, table name, chain name and handle are provided as arguments
if [ $# -lt 4 ]; then
echo "Usage: $0 family table chain handle"
exit 1
fi

# Assign the arguments to variables
family=$1
table=$2
chain=$3
handle=$4

# replacing the rule using nft command
nft delete rule $family $table $chain handle $handle