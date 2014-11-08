all:
	echo All scripts, no build. Run 'make install' to install into Raspbian
install:
	install -o www-data -g www-data -m 775 cgi/measurements_raw.cgi /usr/lib/cgi-bin/measurements_raw.cgi
	install -o www-data -g www-data -m 775 cgi/measurements.cgi /usr/lib/cgi-bin/measurements.cgi
	install -o www-data -g www-data -m 775 cgi/image.cgi /usr/lib/cgi-bin/image.cgi
	install -o www-data -g www-data -m 775 cgi/dashboard.cgi /usr/lib/cgi-bin/dashboard.cgi
	install config/RasPiCam.conf /etc/apache2/conf.d/RasPiCam.conf
