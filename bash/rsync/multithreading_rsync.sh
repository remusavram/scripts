#!/bin/bash


#@brief			Test multithreading rsync.
#@author		Remus
#@email			remusvrm@yahoo.com
#@date			2014.11


# SETUP OPTIONS
pathSource='/'
pathDestination='/'
args='-zd'
THREADS="8"

# record tipe before transaction
currentMinute=`date +"%M"`
currentSecond=`date +"%S"`

# RSYNC TOP LEVEL FILES AND DIRECTORY STRUCTURE
rsync $args $pathSource $pathDestination 

# RSYNC DIRECTORY STRUCTURE
cd $pathSource; find . -type d | xargs -n1 -I% rsync $args % $pathDestination%

# FIND ALL FILES AND PASS THEM TO MULTIPLE RSYNC PROCESSES
cd $pathSource; find . -type f | xargs -n1 -P$THREADS -I% rsync -az % $pathDestination%

# record time after transaction
endMinute=`date +"%M"`
endSecond=`date +"%S"`

# caluclate transaction
durationMinute=$((10#$endMinute-10#$currentMinute))
durationSecond=$((10#$endSecond-10#$currentSecond))

echo 'Transfer Duration: '$durationMinute'min '$durationSecond'sec'