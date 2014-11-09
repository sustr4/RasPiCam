#!/bin/bash

#Prevent caching
printf "Cache-Control: no-cache, no-store, must-revalidate\nPragma: no-cache\nExpires: 0\n"

#TODO Log levels
#TODO Query strings


#Sensor from Query String
SENSOR=`echo "$QUERY_STRING" | sed 's/sensor=\([^\\?^;]*\).*/\1/'`
SIZE=`echo "$QUERY_STRING" | grep -oE 'size=[0-9x]+' | sed 's/size=\([0-9]*\)x\([0-9]*\)/\1,\2/'`
RASPICAM_RAW_MEASUREMENTS="$RASPICAM_RAW_DIR/$SENSOR.csv"

#Use default size if unspecified
if [ "$SIZE" == "" ]; then
	SIZE="800,600"
fi

if [ -f "$RASPICAM_RAW_MEASUREMENTS" ]; then

	# Set up temporary directory
	TMPDIR="/tmp/RASPICAM.$RANDOM.tmp"
	mkdir $TMPDIR

	# Generate gnuplot input file
cat << EndPlotScript > $TMPDIR/plot.in
set terminal png size $SIZE enhanced font "Helvetica,14"
set datafile separator ","
set xdata time
set timefmt "%Y%m%d_%H%M%S"
set output "$TMPDIR/output.png"
plot "$RASPICAM_RAW_MEASUREMENTS" using 1:2 $RASPICAM_PLOT_STYLE	
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
	echo "<h1>Error</h1> log file <code>$RASPICAM_RAW_MEASUREMENTS</code> as requested in your query <code>$QUERY_STRING</code> does not exist"
fi

logger RasPiCam: $REMOTE_ADDR getting measurements with query string \"$QUERY_STRING\, requesting sensor $SENSOR. Requested size was $SIZE."

