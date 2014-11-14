RasPiCam
========

Casual scripts to collect measurements and WebCam photos from Raspberry PI.

Motivation
----------

I could not find anything lightweight enough for PI to allow downloading current snapshots from a webcam and get recent GPIO sensor measurements at the same tome, so I started this. I try to make the scripts secure against code injection, but I do not have any plans to include authentication. It is intended to run either in private environment precluding outside access, or as a completely public resource.

I don't have any ambition to make this a multi-user project, but I'll be of course happy to accept pull request namely to support additional sensor types, or to improve security and fix bugs.

Dependencies
------------

These packages must be installed for all features to work properly:

`apt-get install -y apache2 gnuplot vgrabbj build-essential python-dev`

It also uses [DHT scripts from Adafruit](https://github.com/adafruit/Adafruit_Python_DHT). Install as follows:

```git clone https://github.com/adafruit/Adafruit_Python_DHT
cd Adafruit_Python_DHT
sudo python setup.py install
```

Important notes
---------------

user `www-data` must be member of groups `video` if you wish to download pictures from your WebCam, and group `kmem` if you need to use Adafruit DHT:

```sudo usermod -a -G video www-data
sudo usermod -a -G kmem www-data
sudo service apache2 restart```

