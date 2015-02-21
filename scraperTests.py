__author__ = 'kylechamplin'

import requests
from BeautifulSoup import BeautifulSoup

r = requests.get("http://seattle.craigslist.org/search/sss?query=cabinet%2030%20inches&sort=rel")
soup = BeautifulSoup(r.text)
results = soup.findAll("a", {"class" :"hdrlnk"})
prices = soup.findAll("span", {"class" : "price"})
for x, y in zip(results, prices):
    print x.text.strip() + " : " + y.text.strip()
