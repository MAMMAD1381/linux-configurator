#!/bin/bash

# Check if the family type, table name, chain name, handle and statement are provided as arguments
if [ $# -lt 5 ]; then
echo "Usage: $0 family table chain handle statement"
exit 1
fi

# Assign the arguments to variables
family=$1
table=$2
chain=$3
handle=$4
statement=$5

# Create the rule using nft command
nft add rule $family $table $chain handle $handle "$statement"

# Check if the rule creation was successful
if [ $? -eq 0 ]; then
echo "Rule created successfully in chain $chain of table $table with handle $handle"
else
echo "Rule creation failed"
fi