#!/bin/bash

# Description
# Working with for-loop.

for i in {1..100}
do
	echo $i
done

for i in {1..100..2}
do
	echo $i
done


for (( i=1; i<=10; i++ ))
do
	echo $i
done

arr=("apple" "banana" "cherry")
for i in ${arr[@]}
do
	echo $i
done


declare -A arr2
arr2["name"]="Scott"
arr2["id"]="1234"
for i in "${!arr2[@]}"
do
	echo "$i: ${arr2[$i]}"
done

for i in $(ls)
do
	echo $i
done