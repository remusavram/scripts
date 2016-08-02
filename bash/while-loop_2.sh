#!/bin/bash

# Description
# Working with while-loop

i=0
while [ $i -le 10 ]; do
	echo i:$i
	((i+=1))
done