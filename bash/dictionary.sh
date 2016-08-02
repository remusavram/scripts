#!/bin/bash

# Description
# Working with dictionary.

declare -A mydictionary

mydictionary[color]=blue
mydictionary["office building"]="HQ West"

echo ${mydictionary["office building"]} is ${mydictionary[color]}




