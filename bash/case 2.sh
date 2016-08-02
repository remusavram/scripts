#!/bin/bash 

# Description
# Working with 'case'.
# Author: remus

case $1 in
	cat)
		echo "meow";;
	dog|wolf)
		echo "woof";;
	cow)
		echo "mmoooo";;
	*)
		echo "unknown animal"
esac