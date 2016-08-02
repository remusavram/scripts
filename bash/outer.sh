#!/bin/bash 

# Description
# Working with export.
# Author: remus

declare -x var1="outer"
echo "outer before: $var1"
inner.sh
echo "oute after: $var1"