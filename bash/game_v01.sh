#!/bin/bash

# Description
# Write a simple guessing game, using interactive input and test condition.
# Alos, build the program so that if responds to a command line argument
# and also has a function if no argument is specified. Use a function as well.

randomNumber=5

read -p "Your number is: " number

while [[ -z "$number" ]]; do
	read -p "Please enter a number: " number
done

while [[ ! $number -eq $randomNumber ]]; do
	read -p "Sorry! Please try again: " number
done

echo "Congratulation! You guess the number!"