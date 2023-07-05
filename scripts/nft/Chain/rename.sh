#!/bin/bash

if [ $# -eq 4 ]; then
family_type=$1
table_name=$2
chain_name=$3
new_name=$4

echo nft rename chain $family_type $table_name $chain_name $new_name
nft rename chain $family_type $table_name $chain_name $new_name


else 
echo pls pass the right amount of arguments
fi
