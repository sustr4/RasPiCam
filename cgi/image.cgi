#!/bin/bash

if [ -e $RASPICAM_VIDEO_DEVICE ]; then

	# Set up temporary directory
	TMPDIR="/tmp/RASPICAM.$RANDOM.tmp"
	mkdir $TMPDIR

	# Run vgrabbj
	COMMAND="vgrabbj -d $RASPICAM_VIDEO_DEVICE -f $TMPDIR/snapshot.jpg"
	vgrabbj -d $RASPICAM_VIDEO_DEVICE -f $TMPDIR/snapshot.jpg 2> $TMPDIR/snapshot.err > /dev/null

	if [ $! == 0 ]; then
		# Return image
		echo -ne "Status: 200 OK\nContent-type: image/jpeg\n\n"
		cat $TMPDIR/snapshot.jpg
	else
		echo -ne "Status: 404 Not Found\nContent-type: text/html\n\n"
		echo "<h1>Error grabbing image</h1>\nCommand was: <pre>$COMMAND</pre>, output was: <pre>"
		cat $TMPDIR/snapshot.err
		echo "</pre>"
	fi

	# Remove temporary files
	rm -rf $TMPDIR
else
	echo -ne "Status: 404 Not Found\nContent-type: text/html\n\n"
	echo "<h1>Error</h1>"
fi

