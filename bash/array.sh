#!/bin/bash

# Description
# Working with array.

a=()
b=("apple" "banana" "cherry")

echo "The third element is: "${b[2]}

b[5]="kiwi"

# add at the end of the array
b+=("mango")

# print all array
echo "The list is:" ${b[@]}

# grep the last element
echo "The last element is: ${b[@]: -1}"
