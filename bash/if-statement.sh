#!/bin/bash

# Description
# Working with if statement

a=2
if [ $a -gt 4 ]; then
	echo $a is greater then 4!
else
	echo $a is not greater then 4!
fi

b="This is a string 12 !"
if [[ $b =~ [0-9]+ ]]; then
	echo "There are numbers in the string: $b"
else
	echo "There are nu numbers in the string: $b"
fi

c=1
if [ $c -gt 4 ]
	then
		echo $c is greater then 4!
else
		echo $c is not greater then 4!
fi