#!/bin/bash

if [ -f $RASPICAM_VIDEO_DEVICE ]; then

	# Set up temporary directory
	TMPDIR="/tmp/RASPICAM.$RANDOM.tmp"
	mkdir $TMPDIR

	# Run vgrabbj
	vgrabbj -d $RASPICAM_VIDEO_DEVICE -f $TMPDIR/snapshot.jpg 2> $TMPDIR/snapshot.err > /dev/null

	# Return image
	echo -ne "Status: 200 OK\nContent-type: image/jpeg\n\n"
	cat $TMPDIR/snapshot.jpg

	# Remove temporary files
	rm -rf $TMPDIR
else
	echo -ne "Status: 404 Not Found\nContent-type: text/html\n\n"
	echo "<h1>Error</h1>"
fi
