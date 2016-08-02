#!/bin/bash 

# Description
# Working with special variables.
# Author: remus

echo "Running $0"

echo "Print all arguments using \$@:"
for a in $@; do
	echo $a;
done

echo "Print all arguments using \$*:"
for a in $*; do
	echo $a;
done