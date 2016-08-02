#!/bin/bash

# Description
# Working wiht arguments.

echo $1
echo $2
echo

for i in $@
do
	echo $i
done

echo "There were $# arguments."