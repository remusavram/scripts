#!/bin/bash

# Description
# Working with strings.

a="hello"
b="world"
c=$a$b

echo $c

echo "Length of string a is: ${#a}"
echo "Length of string c is: "${#c}

# substrings
d=${c:3}
echo $d

e=${c:3:4}
echo $e

echo ${c: -4}
echo ${c: -4:3}

# replace text in a string with other text
fruit="apple banana banana banana cherry"
echo ${fruit/banana/durian} # replace the first aparition
echo ${fruit//banana/durian} # replace all appears in the string
echo ${fruit/#apple/durian} # with # only if it's the very begining of the string
echo ${fruit/%cherry/durian} # only if it's at the end of the string
echo ${fruit/c*/durian} # replace everything wich start with "c"









