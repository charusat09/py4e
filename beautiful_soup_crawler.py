import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = "https://mayurkumar.info"

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
a_tags = soup("a")

for a in a_tags:
    print(a.get("href", None))
