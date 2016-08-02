#!/bin/bash

# Description
# Working with data.

today=$(date +"%d-%m-%Y")
time=$(date +"%H:%M:%S")

printf -v d "Current User:\t%s\nDate:\t\t%s @ %s\n" $USER $today $time
echo "$d"













