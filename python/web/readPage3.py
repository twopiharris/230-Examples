""" readPage with requests 
    note this requires the requests module
    which may not be on all python installations """

import requests
url = "http://www.cs.iupui.edu/~aharris/230"
r = requests.get(url)

for line in r:
  print(line)

