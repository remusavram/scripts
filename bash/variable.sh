#!/bin/bash

# Description
# In this script will describe the variable type.

# variable
a=Hello
b="Good morning"
c=16


echo $a
echo $b
echo $c
echo
echo "$a! I have $c apples!"
echo "$b! Nice!"


# Adding attributes to variables

declare -i d=123            # d is an integer
declare -r e=456            # e is read-only
declare -l f="LOLCates"     # f is lolcats
declare -i g="LOLCates"     # g is LOLCATS


# Build-in variables

echo $HOME            # home directory
echo $PWD             # curent directory
echo $MACHTYPE        # returns the machine type
echo $HOSTNAME        # returns the system name
echo $BASH_VERSION    # returns version of Bash
echo $SECONDS         # returns the number of seconds the BASH session has run
echo $0               # returns the name of the script
