#!/bin/bash

if [ $# -eq 3 ]; then
family_type=$1
table_name=$2
chain_name=$3

nft delete chain $family_type $table_name $chain_name

else 
echo pls pass right amount of arguments
fi
