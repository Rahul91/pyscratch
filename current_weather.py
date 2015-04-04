import urllib2
from bs4 import BeautifulSoup

url = urllib2.urlopen("https://in.weather.yahoo.com/india/maharashtra/pimpri-chinchwad-2275834/")

soup = BeautifulSoup(url)

var = soup.find("div", {"class" : "day-temp-current temp-c "})
print var.text
