#!/bin/bash 

# Description
# Working with function.
# Author: remus

sum () {
	return $(( $1 + $2 ))
}

sum 4 5
echo $?