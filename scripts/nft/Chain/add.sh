#!/bin/bash

# Check if the table_name and family_type type are provided as arguments
if [ $# -ne 6 ]; then
echo "Usage: $0 table_name family_type"
exit 1
fi

# Assign the arguments to variables
family_type=$1
table_name=$2
chain_name=$3
chain_type=$4
hook=$5
priority=$6

# Check if the family_type type is valid
if [ "$family_type" != "ip" ] && [ "$family_type" != "ip6" ] && [ "$family_type" != "inet" ] && [ "$family_type" != "arp" ] && [ "$family_type" != "bridge" ]; then
echo "Invalid family_type type: $family_type"
exit 2
fi

# check if the chain type is valid
if [ "$chain_type" != "filter" ] && [ "$chain_type" != "route" ] && [ "$chain_type" != "nat" ]; then
echo "Invalid chain_type type: $chain_type"
exit 3
fi

# Check if the hook type is valid
if [ "$hook" != "prerouting" ] && [ "$hook" != "input" ] && [ "$hook" != "forward" ] && [ "$hook" != "output" ] && [ "$hook" != "postrouting" ] && [ "$hook" != "ingress" ] && [ "$hook" != "egress" ]; then
echo "Invalid hook type: $hook"
exit 4
fi

# checking the foramt of priority
if ! [[ "$priority" =~ ^[0-9]+$ ]]
    then
        echo "pls enter a number as priority"
        exit 5
fi


nft add chain $family_type $table_name $chain_name '{ type $chain_type hook $hook priority $priority ; }'

