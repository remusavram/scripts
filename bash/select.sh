#!/bin/bash

# Description
# Working with select.

select animal in "cat" "dog" "bird" "fish"
do
	echo "You selected $animal!"
	break
done


select option in "cat" "dog" "bird" "fish" "quit"
do
	case $option in
		cat) echo "Cats like to sleep!";;
		dog) echo "Dogs like to play catch.";;
		bird) echo "Birds like to sing.";;
		fish) echo "Fishs are interesting.";;
		quit) break;;
		*) echo "I'm not sure what that is.";;
	esac
done
