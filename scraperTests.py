__author__ = 'kylechamplin'

import requests
from BeautifulSoup import BeautifulSoup




r = requests.get("http://seattle.craigslist.org/search/sss?excats=7-13-22-2-24-1-4-19-1-1-1-1-1-1-3-6-10-1-1-1-2-2-8-1-2-2-4-1-3-1-3-1-1-1-1-7-1-1-1-1-1-1-1-1-1-1-1-1-1-2-1-1-1-2-1-1-2-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1&sort=rel&query=cabinets")
soup = BeautifulSoup(r.text)
results = soup.findAll("a", {"class" :"hdrlnk"})
prices = soup.findAll("span", {"class" : "price"})
for x, y in zip(results, prices):
    print x.text.strip() + " : " + y.text.strip()
