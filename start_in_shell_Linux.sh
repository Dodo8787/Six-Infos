#!/bin/sh

CURRENTDATE=`date +"%Y-%m-%d %T"`

SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH

echo '_______________________________' >> $SCRIPTPATH/log_error.txt
echo '(Linux) Started: ' >> $SCRIPTPATH/log_error.txt
echo  Current Date and Time is: ${CURRENTDATE} >> $SCRIPTPATH/log_error.txt
$SCRIPTPATH/main.py 2>> $SCRIPTPATH/log_error.txt
