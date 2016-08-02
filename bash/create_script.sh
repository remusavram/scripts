#!/bin/bash

# Description
# this script creates a new bash script, sets permissinos and more
# Author: remus

# Is there an argument?
if [[ ! $1 ]]; then
	echo "Missing argument!"
	exit 1
fi

scriptname="$1"

bindir="${HOME}/bin"
filename="${bindir}/$scriptname"

if [[ -e $filename ]]; then
	echo "File ${filename} already exists!"
	exit 1
fi

if type "$scriptname" > /dev/null 2>&1; then
	echo "There is already a command wiht name ${scriptname}"
	exit 1
fi

# chenck bin directory exists
if [[ ! -d $bindir ]]; then
	# if not: create bin directory
	if mkdir "$bindir"; then
		echo "created ${bindir}"
	else
		echo "Could not create ${bindir}."
		exit 1
	fi
fi 

# create a script with a single line
echo '#!/bin/bash' > "$filename"
# add executable permissinos
chmod u+x "$filename"
# open with editor
if [[ $EDITOR ]]; then
	$EDITOR "$filename"
else
	echo "Script created; not starting editor because \$EDITOR is not set."
fi


#echo "End of code reached!"
#exit 0