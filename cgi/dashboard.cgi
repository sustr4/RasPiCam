#!/bin/bash

# Load Human Readable names

IDS=$(grep -vE "^\s*#" /etc/apache2/conf.d/RasPiCam.conf | grep -w RASPICAM_SENSOR_IDS | awk '{ print $3 }' | tr ";" "\n")
NAMES=$(grep -vE "^\s*#" /etc/apache2/conf.d/RasPiCam.conf | grep -w RASPICAM_SENSOR_NAMES | awk '{ print $3 }' | tr ";" "\n")
COLORS=$(grep -vE "^\s*#" /etc/apache2/conf.d/RasPiCam.conf | grep -w RASPICAM_SENSOR_COLORS | awk '{ print $3 }' | tr ";" "\n")

#Prevent caching
printf "Cache-Control: no-cache, no-store, must-revalidate\nPragma: no-cache\nExpires: 0\n"

#Print header
printf "Status: 200 OK\nContent-type: text/html\n\n"

#Construct Dashboard
printf "<!DOCTYPE HTML><HTML>\n<TITLE>RasPiCam Dashboard</TITLE>\n<BODY>\n"

printf "System time: $(date)\n<HR>\n<div>\n"

for i in $IDS; do
	printf "ID: $i\n"
done


for logfile in $RASPICAM_RAW_DIR/*.csv; do
	LF="$(basename $logfile .csv)"
	printf "<TABLE style=\"float: left; margin:20px; align:center;\">\n"
	printf "<TR><TD align=\"center\">Last two weeks at $LF<P><IMG src=\"/cgi-bin/measurements.cgi?sensor=$LF?size=352x288?font=6\" alt=\"Sensor data plot\"><br>\n"
	printf "Other sizes: <A HREF=\"/cgi-bin/measurements.cgi?sensor=$LF?size=1024x576\">1024&times;576</a>\n"
	printf "<A HREF=\"/cgi-bin/measurements.cgi?sensor=$LF?size=1280x720\">1280&times;720</a>\n"
	printf "<A HREF=\"/cgi-bin/measurements.cgi?sensor=$LF?size=1600x900\">1600&times;900</a><P>"
	printf "Download <A HREF=\"/cgi-bin/measurements_raw.cgi?sensor=$LF\">raw data</a><P>"
	printf "Last update:<BR>$(stat -c%y $logfile)<P>\n<font size=\"+3\">$(tail -n 1 $logfile | awk -F "\"*,\"*" '{print $2}')</font>"
	printf "</TD></TR>\n"
	printf "</TABLE>\n"
done

printf "<TABLE style=\"float: left; margin:20px;\">\n<TR><TD align=\"center\">Camera view<P><IMG src=\"/cgi-bin/image.cgi\" alt=\"Current photo\"><BR><A HREF=\"/cgi-bin/image.cgi\">Direct link</A></TD></TR>\n</TABLE>\n"

printf "</div>\n<div style=\"clear: both;\"><HR>\nGenerated by <A HREF=\"https://github.com/sustr4/RasPiCam\">RasPiCam</A>\n</div></BODY>\n</HTML>\n"
