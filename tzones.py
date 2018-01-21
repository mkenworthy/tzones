#!/usr/bin/env python
import os
from datetime import datetime
from astropy.table import Table
import pytz # pip install pytz

# Written by M Kenworthy
# 2018 Jan 21

# Instructions: list the cities you want to get the local time
# If multiple cities found, use geoid code to uniquely identify the
# city instead (see example for Louisville below)
cities = ("Leiden","Phoenix","Baltimore","4299276")
#cities = ("Leiden","Phoenix","Baltimore","Louisville")

### heavily modified from https://stackoverflow.com/questions/16505501/get-timezone-from-city-in-python-django
### by https://stackoverflow.com/users/4279/jfs

# get cities15000.zip from:
# http://download.geonames.org/export/dump/cities15000.zip
# unzip, and recompress with gzip

def get_tzone():
    localfile = 'tzones.csv'
    tzonefile = 'cities15000.txt.gz'
    if not os.path.exists(localfile):
        print('local cache file {} not found - reading in {} and processing'.format(localfile, tzonefile))
        print('first time takes 10 seconds, next time will be much faster')

        # fast_reader=False due to bug in astropy.Table
        t = Table.read(tzonefile, fast_reader=False, format='ascii.no_header', delimiter='\t')

        # column names in geonames database and tzonefile:
        # http://download.geonames.org/export/dump/readme.txt

        ttz = Table([t['col1'],t['col2'],t['col3'],t['col18']],
            names=('geoid','name','asciiname','tz'), dtype=(str,str,str,str))

        ttz.write(localfile)
        print('Wrote local copy {}'.format(localfile))

    else:
        # fast_reader=False due to bug in Table. should be removed
        # sometime.
        ttz = Table.read(localfile, fast_reader=False)

        # making sure geoid column is read as a string for comparison to work
        ttz = Table(ttz, dtype=(str,str,str,str))
    return ttz

fmt = '%Y-%m-%d %H:%M %Z%z'

ttz = get_tzone()

for city in cities:
    # see how many matches there are
    tcity = ttz[(ttz['asciiname'] == city) + (ttz['geoid'] == city)]

    if (len(tcity) < 1):
        print('no city with name {} found'.format(city))
    elif (len(tcity) > 1):
        print('multiple cities with name {} found'.format(city))
        print('use the \'geoid\' number from table below to uniquely identify your city')
        print(tcity)
    else: # unique city found
        cityname = tcity['asciiname'][0]
        citytz = tcity['tz'][0]

        now = datetime.now(pytz.timezone(citytz))
        print("")
        print("Current time in %s is %s" % (cityname, now.strftime(fmt)))
