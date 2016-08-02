#!/bin/bash

# Description
# Debug.

# get the date
date=$(date)

# get the topic
topic="$1"



# start debugging
set -x

# filename to write to
filename="${HOME}/workspace/${topic}note.txt"

# stop debugging
set +x



# Ask user for imput
read -p "Your notes: " note

echo "$date: $note" >> "$filename"
echo "Note '$note' saved to $filename!" 
