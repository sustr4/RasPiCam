#!/bin/bash

#Prevent caching
printf "Cache-Control: no-cache, no-store, must-revalidate\nPragma: no-cache\nExpires: 0\n"

#Print header
printf "Status: 200 OK\nContent-type: text/html\n\n"

#Construct Dashboard
printf "<HTML>\n<TITLE>RasPiCam Dashboard</TITLE>\n<BODY>\n"

printf "<TABLE>\n"

printf "<TR><TD>System time</TD><TD>$(date)</TD></TR>\n"

for logfile in $RASPICAM_RAW_DIR/*.csv; do
	LF="$(basename $logfile .csv)"
	printf "<TR><TD>Measurement history for $LF</TD><TD><IMG src=\"/cgi-bin/measurements.cgi?sensor=$LF\"></TD></TR>\n"
done

printf "<TR><TD>Camera view</TD><TD><IMG src=\"/cgi-bin/image.cgi\"></TD></TR>\n"

printf "</TABLE>\n"
printf "</BODY>\n</HTML>\n"
