RasPiCam
========

Casual scripts to collect measurements and WebCam photos from Raspberry PI

Dependencies
------------

These packages must be installed for all features to work properly:

`apt-get install -y apache2 gnuplot vgrabbj`


Important notes
---------------

user www-data must be member of group video if you wish to donwload pictires from WebCam:

`sudo usermod -a -G video www-data`

`sudo service apache2 restart`

