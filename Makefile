all:
	echo All scripts, no build. Run 'make install' to install into Raspbian
install:
	install -u www-data -g www-data -m 775 cgi/measurements_raw.cgi /usr/lib/cgi-bin/measurements_raw.cgi

