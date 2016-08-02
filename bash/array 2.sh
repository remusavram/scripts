#!/bin/bash -x

# Description
# Working with array.
# Author: remus

ar=(this is an array)

ar[15]=30

declare -p ar

echo "Length of arry is: " ${#ar[@]}
echo "Pring used position: " ${!ar[@]}
