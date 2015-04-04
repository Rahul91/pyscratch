import urllib2
from bs4 import BeautifulSoup

url = urllib2.urlopen("https://in.weather.yahoo.com/india/maharashtra/pimpri-chinchwad-2275834/")

soup = BeautifulSoup(url)

var1 = soup.find("div", {"class" : "day-temp-current temp-c "})
var2 = soup.find("div", {"class" : "current-weather-city"})

print type (var1.get_text)
print var1.get_text()
#print ("Current temperature is : %s", %var1)
print var2.text
