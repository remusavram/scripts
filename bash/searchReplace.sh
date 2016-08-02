#!/bin/bash 

# Description
# Searching and replacing parts of the string.
# Author: remus

i="mytxt.txt"

echo "Our string is: " $i

echo "Replace first 'txt' with 'jpg':	 " ${i/txt/jpg}
echo "Replace last 'txt' with 'jpg':	 " ${i/%txt/jpg}
echo "Replace all 'txt' with 'jpg':		" ${i//txt/jpg}
echo "Replace first 'x' or 'y' with 'a': " ${i/[xy]/a}
echo "Replace all 'x' and 'y' with 'a':  " ${i//[xy]/a}