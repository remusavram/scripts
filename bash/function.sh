#!/bin/bash

# Description
# Working with function.

function greet {
	# describe what function does.

	echo "Hi $1! What a nice $2"
}

echo "And now, a greeting!"
greet Remus Morining
greet Everybody Evening

echo

function numberthings {
	# print files in folder

	i=1
	for f in $@; do
		echo $i: $f
		((i+=1))
	done
}

numberthings $(ls)
numberthings pine bitch maple spruce