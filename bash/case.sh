#!/bin/bash

# Description.

a="dog"
case $a in
	cat) echo "Feline";;
	dog|puppy) echo "Canine";;
	*) echo "No match!";;
esac

