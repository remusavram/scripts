#!/bin/bash

# Description
# Ensuring is a response is ok.

echo; echo

if [ $# -lt 3 ]; then
	cat <<- EOM
	This command requires three arguments:
	username, userid, and favorite number.
	EOM
else
	# the program goes here
	echo "Username: $1"
	echo "UserID: $2"
	echo "favorite number: $3"
fi

echo; echo

read -p "Favorite animal? " a
while [[ -z "$a" ]]; do
	read -p "I need an answer!" a
done
echo "$a was selected."

echo; echo

read -p "Favorite animal? [cat] " a
while [[ -z "$a" ]]; do
	a="cat"
done
echo "$a was selected."

echo; echo

read -p "What year? [nnnn]: " a
while [[ ! $a =~ [0-9]{4} ]]; do
	read -p "A year, please! [nnnn]: " a
done
echo "Selected year: $a"

