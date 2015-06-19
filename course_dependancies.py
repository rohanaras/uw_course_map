from bs4 import BeautifulSoup
import urllib.request

# debug logger: terminal can't handle some characters
log = open('log2.txt', 'w')

# list of all catalogue urls
urls = open('department_urls.txt', 'r')

# turn webpage into beautiful soup object
def url_to_beautifulsoup(url):
	response = urllib.request.urlopen(url, data=None)
	html = response.read()
	soup = BeautifulSoup(html)
	return soup

for url in urls:
	print(url)