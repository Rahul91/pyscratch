import urllib2
from bs4 import BeautifulSoup

url = urllib2.urlopen("https://in.finance.yahoo.com/")
soup = BeautifulSoup(url)

sol = soup.find_all("dl", {"class": "first"})

for x in sol:
	print x.content
