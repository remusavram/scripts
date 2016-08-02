#!/bin/bash

# Description
# Getting input during execution.

echo "What is your name?"
read name

echo "What is your password?"
read -s pass

read -p "What's your favorite animal? " animal

echo name: $name, password: $pass, animal: $animal