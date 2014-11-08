#!/bin/bash

if [ -f $RASPICAM_RAW_MEASUREMENTS ]; then
	echo -ne "Status: 200 OK\nContent-type: text/plain\n\n"
	cat $RASPICAM_RAW_MEASUREMENTS
else
	echo -ne "Status: 404 Not Found\nContent-type: text/html\n\n"
	echo "<h1>Error</h1>"
fi

