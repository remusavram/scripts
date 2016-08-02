#!/bin/bash 

# Description
# Working with patterns.
# Author: remus

i="/Users/reindert/demo.txt"

echo "Our string is: " $i
echo ${i#*/}
echo ${i##*/}
echo ${i%.*}
echo ${i%/*}