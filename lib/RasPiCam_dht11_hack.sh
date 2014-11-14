#!/bin/bash
printf "$(date +%Y%m%d_%H%M%S),$(printf "import Adafruit_DHT\nprint Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 18)[0]" | python)%%\n" >> "/var/lib/RasPiCam/DHT_GPIO18.csv"
