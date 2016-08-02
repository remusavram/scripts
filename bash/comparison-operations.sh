#!/bin/bash

# Description
# In this script 
# [[ expresion ]]
# 1 - failed
# 0 - succed

[[ "cat" == "cat" ]]
echo $?

[[ "cat" = "dog" ]]
echo $?

[[ 20 -gt 100 ]]  # greater then
echo $?

a=""
b="cat"

[[ -z $a && -n $b ]]  # -z is null?; -n Is not null?
echo $?





























