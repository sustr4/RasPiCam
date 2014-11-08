all:
	echo All scripts, no build. Run 'make install' to install into Raspbian
install:
	-mkdir -p /var/lib/RasPiCam
	-chown www-data:www-data /var/lib/RasPiCam
	-mkdir -p /usr/lib/cgi-bin
	-chown www-data:www-data /usr/lib/cgi-bin
	install -o www-data -g www-data -m 775 cgi/measurements_raw.cgi /usr/lib/cgi-bin/measurements_raw.cgi
	install -o www-data -g www-data -m 775 cgi/measurements.cgi /usr/lib/cgi-bin/measurements.cgi
	install -o www-data -g www-data -m 775 cgi/image.cgi /usr/lib/cgi-bin/image.cgi
	install -o www-data -g www-data -m 775 cgi/dashboard.cgi /usr/lib/cgi-bin/dashboard.cgi
	install -o www-data -g www-data -m 544 cron/RasPiCam.cron /etc/cron.d/RasPiCam
	-mkdir -p /usr/lib/RasPiCam
	-chown root:root /usr/lib/RasPiCam
	install -o root -g root -m 775 lib/RasPiCamReader.sh /usr/lib/RasPiCam/RasPiCamReader.sh
	install config/RasPiCam.conf /etc/apache2/conf.d/RasPiCam
	service cron reload
