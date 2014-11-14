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
	TEMPERATURE="$(tail -n 1 "$sensor/w1_slave" | grep -o '[0-9]*$' | sed 's/\([0-9][0-9][0-9]$\)/.\1/')"
	printf "$TIMESTAMP,$TEMPERATURE\n" >> "$MDIR/$SN.csv"
done


# -------------------------------
# DHT modules, read with AdaFruit
# -------------------------------

#for port in $(grep RASPICAM_DHT11_GPIO /etc/apache2/conf.d/RasPiCam.conf | awk '{ print $3 }'); do
#	HUMIDITY=printf "import Adafruit_DHT\nprint Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, $port)[0]" | python
#	printf "$TIMESTAMP,$HUMIDITY\n" >> "$MDIR/DHT_GPIO$port.csv"
#done

## Currently AdaFruid sadly requires root privileges. As a dirty hack, values are collected by a separate cron script

