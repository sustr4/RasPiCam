#!/bin/bash

if [ -f $RASPICAM_RAW_MEASUREMENTS ]; then

	# Set up temporary directory
	TMPDIR="/tmp/RASPICAM.$RANDOM.tmp"
	mkdir $TMPDIR

	# Generate gnuplot input file
cat << EndPlotScript > $TMPDIR/plot.in
set terminal png size 800,600 enhanced font "Helvetica,14"
set output "$TMPDIR/output.png"
plot "$RASPICAM_RAW_MEASUREMENTS"	
EndPlotScript

	# Run gnuplot
	gnuplot $TMPDIR/plot.in

	# Return image
	echo -ne "Status: 200 OK\nContent-type: image/png\n\n"
	cat $TMPDIR/output.png

	# Remove temporary files
	rm -rf $TMPDIR
else
	echo -ne "Status: 404 Not Found\nContent-type: text/html\n\n"
	echo "<h1>Error</h1>"
fi

