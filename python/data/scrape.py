""" scrape.py
    load a file with requests object and pass it through
    beautiful soup

    Download and display the list of allowed URLs on the
    pythonanywhere white list
    
    expects requests and bs4 modules to be loaded
    (works fine on pythonanywhere)
    
    """

import requests
from bs4 import BeautifulSoup

url = "http://pythonanywhere.com/whitelist"
r = requests.get(url)
print

soup = BeautifulSoup(r.text, "html.parser")
cells = soup.find_all("td")
for item in cells:
    print (item.text)

orgs = [x for x in cells if x.text.endswith(".org")]
for item in orgs:
    print(item.text)

