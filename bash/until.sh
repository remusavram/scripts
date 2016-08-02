#!/bin/bash 

# Description
# Working with until.
# Author: remus

# Get a random number < 100
target=$(($RANDOM % 100))

# Initialize the user's guess
guess=

until [[ $guess -eq $target ]]; do
	read -p "Teke a guess: " guess
	if [[ $guess -lt $target ]]; then
		echo "higher!"
	elif [[ $guess -gt $target ]]; then
		echo "Lower!"
	else 
		echo "You fount it!"
	fi
done

exit 0