#!/bin/bash


#@brief			Test linear rsync.
#@author		Remus
#@email			remusvrm@yahoo.com
#@date			2014.11


# FIND ALL FILES AND PASS THEM TO MULTIPLE RSYNC PROCESSES
pathSource='/'
pathDestination='/'
args='-a'

# record tipe before transaction
currentMinute=`date +"%M"`
currentSecond=`date +"%S"`


rsync $args $pathSource $pathDestination 
#sleep 1

# record time after transaction
endMinute=`date +"%M"`
endSecond=`date +"%S"`

# caluclate transaction
durationMinute=$((10#$endMinute-10#$currentMinute))
durationSecond=$((10#$endSecond-10#$currentSecond))

echo 'Transfer Duration: '$durationMinute'min '$durationSecond'sec'