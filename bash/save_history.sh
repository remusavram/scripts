#!/bin/bash

# Description
# This script save the result of history cmd in a file with a specific name.
# Author: remus

history > ${HOSTNAME}_root_history_`date +"%Y%m%d"`.txt
