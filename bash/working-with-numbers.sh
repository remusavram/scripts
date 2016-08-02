#!/bin/bash

# Description
# In this script is presented some operation
# which can be done with variables.

# variables
d=2
e=$((d+2))

echo 'The sum is: '$e

((e++))
echo $e

((e--))
echo $e

echo
((e+=5))
echo $e

((e*=3))
echo $e

((e/=3))
echo $e

((e-=5))
echo $e


echo 
f=$((1/3))
echo $f

g=$(echo 1/3 | bc -l)
echo $g


