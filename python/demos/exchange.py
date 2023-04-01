""" exchange.py
    basic web scraping for exchange rate """

import urllib2

rateFile = urllib2.urlopen("http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml")
for line in rateFile:
  if "USD" in line:
    rate =float(line[30:35])
    print rate

