#!/bin/bash

if [ $# -eq 3 ]; then
family_type=$1
table_name=$2
chain_name=$3

nft list chain $family_type $table_name $chain_name

elif [ $# -eq 1 ]; then
family_type=$1
nft list chains $family_type
fi
