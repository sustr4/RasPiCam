#!/bin/bash

#Prevent caching
printf "Cache-Control: no-cache, no-store, must-revalidate\nPragma: no-cache\nExpires: 0\n"

#TODO Log levels
#TODO Query strings


#Sensor from Query String
SENSOR=`echo "$QUERY_STRING" | sed 's/sensor=\([^\\?^;]*\).*/\1/'`
SIZE=`echo "$QUERY_STRING" | grep -oE 'size=[0-9x]+' | sed 's/size=\([0-9]*\)x\([0-9]*\)/\1,\2/'`
FONT=`echo "$QUERY_STRING" | grep -oE 'font=[0-9]+' | sed 's/font=\([0-9]*\)/\1/'`
RASPICAM_RAW_MEASUREMENTS="$RASPICAM_RAW_DIR/$SENSOR.csv"

#Use default size if unspecified
if [ "$SIZE" == "" ]; then
	SIZE="800,600"
fi
if [ "$FONT" == "" ]; then
	FONT="14"
fi

if [ -f "$RASPICAM_RAW_MEASUREMENTS" ]; then

	# Set up temporary directory
	TMPDIR="/tmp/RASPICAM.$RANDOM.tmp"
	mkdir $TMPDIR

	# Generate gnuplot input file
cat << EndPlotScript > $TMPDIR/plot.in
set terminal png size $SIZE enhanced font "Helvetica,$FONT"
set datafile separator ","
set xdata time
set timefmt "%Y%m%d_%H%M%S"
set output "$TMPDIR/output.png"
plot "< tail -n 4032 $RASPICAM_RAW_MEASUREMENTS" using 1:2 $RASPICAM_PLOT_STYLE	
EndPlotScript

	# Run gnuplot
	gnuplot $TMPDIR/plot.in > $TMPDIR/gnuplot.err 2>&1

        RETVAL=$?
        if [ $RETVAL == 0 ] && [ -s $TMPDIR/output.png ]; then
                # Return image
		echo -ne "Status: 200 OK\nContent-type: image/png\n\n"
		cat $TMPDIR/output.png
        else
                echo -ne "Status: 404 Not Found\nContent-type: text/html\n\n"
                printf "<h1>Error constructing chart</h1>\nConfig file was: <pre>"
                cat $TMPDIR/plot.in
                printf "</pre>Return value was: <b>$RETVAL</b>.\n<P>\n<code>gnuplot</code> output was:<pre>"
		cat $TMPDIR/gnuplot.err
		printf "</pre>"
        fi


	# Remove temporary files
	rm -rf $TMPDIR
else
	echo -ne "Status: 404 Not Found\nContent-type: text/html\n\n"
	echo "<h1>Error</h1> log file <code>$RASPICAM_RAW_MEASUREMENTS</code> as requested in your query <code>$QUERY_STRING</code> does not exist"
fi

logger RasPiCam: $REMOTE_ADDR getting measurements with query string \"$QUERY_STRING\, requesting sensor $SENSOR. Requested size was $SIZE."

