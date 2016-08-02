#!/bin/bash 

# Description
# Working with declare variables.
# Author: remus

# Get a random number < 100
# -r means read-only
# -i means integer
declare -ir target=$(( ($RANDOM % 100) + 1 ))

# Initialize the user's guess
declare -i guess=0

until [[ $guess == $target ]]; do
	read -p "Teke a guess: " guess

	# if guess is 0, it was not a number
	(( guess )) || continue

	if [[ $guess -lt $target ]]; then
		echo "higher!"
	elif [[ $guess -gt $target ]]; then
		echo "Lower!"
	else 
		echo "You fount it!"
	fi
done

exit 0