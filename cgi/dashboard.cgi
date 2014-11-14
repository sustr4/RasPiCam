#!/bin/bash

#Prevent caching
printf "Cache-Control: no-cache, no-store, must-revalidate\nPragma: no-cache\nExpires: 0\n"

#Print header
printf "Status: 200 OK\nContent-type: text/html\n\n"

#Construct Dashboard
printf "<!DOCTYPE HTML><HTML>\n<TITLE>RasPiCam Dashboard</TITLE>\n<BODY>\n"

printf "<TABLE>\n"

printf "<TR><TD>System time</TD><TD>$(date)</TD></TR>\n"

for logfile in $RASPICAM_RAW_DIR/*.csv; do
	LF="$(basename $logfile .csv)"
	printf "<TR><TD>History for $LF</TD><TD><IMG src=\"/cgi-bin/measurements.cgi?sensor=$LF?size=352x288?font=6\" alt=\"Sensor data plot\"><br>\n"
	printf "Other sizes: <A HREF=\"/cgi-bin/measurements.cgi?sensor=$LF?size=1024x576\">1024&times;576</a>\n"
	printf "<A HREF=\"/cgi-bin/measurements.cgi?sensor=$LF?size=1280x720\">1280&times;720</a>\n"
	printf "<A HREF=\"/cgi-bin/measurements.cgi?sensor=$LF?size=1600x900\">1600&times;900</a><P>"
	printf "Download <A HREF=\"/cgi-bin/measurements_raw.cgi?sensor=$LF\">raw data</a><P>"
	printf "Last update: $(stat -c%y $logfile)<P>"
	printf "</TD></TR>\n"
done

printf "<TR><TD>Camera view</TD><TD><IMG src=\"/cgi-bin/image.cgi\" alt=\"Current photo\"><BR><A HREF=\"/cgi-bin/image.cgi\">Direct link</A></TD></TR>\n"

printf "</TABLE>\n"
printf "</BODY>\n</HTML>\n"
