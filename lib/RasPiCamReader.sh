#!/bin/bash

TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# ----------------------------------------
# Read measurements dir from Apache Config
# ----------------------------------------

MDIR="$(grep -vE "^\s*#" /etc/apache2/conf.d/RasPiCam.conf | grep -w RASPICAM_RAW_DIR | awk '{ print $3 }')"


# ----------------------------------------
# W1 modules (one wire bus, input provided
# by w1-gpio and w1-therm kernel modules
# ----------------------------------------

for sensor in /sys/bus/w1/devices/[0-9]*; do
	SN="$(basename $sensor)"
	tail -n 1 "$sensor/w1_slave" | grep -o '[0-9]*$' | sed 's/\([0-9][0-9][0-9]$\)/.\1/' > "$MDIR/$SN.cvs"
done

