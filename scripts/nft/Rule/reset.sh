#!/bin/bash

family_type=$1
table_name=$2
chain_name=$3


# if all arguments are passed: deleting rules of chain
if [[ $family_type != '' ]] && [[ $table_name != '' ]] && [[ $chain_name != '' ]]; then
nft reset rules chain $family_type $table_name $chain_name

# if family type and table is passed: deleting rules of table
elif [[ $family_type != '' ]] && [[ $table_name != '' ]]; then
nft reset rules table $family_type $table_name

# hust family type passed: deleting all rules of that type
elif [[ $family_type != '' ]] && [[ $table_name != '' ]]; then
nft reset rules $family_type

else
echo pls enter at least on argument
exit 1

fi