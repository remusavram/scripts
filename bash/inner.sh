#!/bin/bash 

# Description
# Working with export.
# Author: remus

echo "inner before: $var1"
# this export doesn't work because it is set only to this section/process
export var1="inner"
echo "inner after: $var1"