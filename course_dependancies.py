from bs4 import BeautifulSoup
import urllib

# debug logger: terminal can't handle some characters
log = open('log2.txt', 'w')

# list of all catalog urls
urls = open('department_urls.txt', 'r')

# turn webpage into beautiful soup object
def url_to_beautifulsoup(url):
	response = urllib.urlopen(url, data=None)
	html = response.read()
	soup = BeautifulSoup(html)
	return soup

for url in urls:
	catalog = url_to_beautifulsoup(url)
	classes = catalog.find_all('p')

