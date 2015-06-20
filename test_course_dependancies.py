from bs4 import BeautifulSoup
import re, urllib

# debug logger: terminal can't handle some characters
log = open('log2.txt', 'w')

# turn webpage into beautiful soup object
def url_to_beautifulsoup(url):
	response = urllib.urlopen(url, data=None)
	html = response.read()
	soup = BeautifulSoup(html)
	return soup

catalog = url_to_beautifulsoup('http://www.washington.edu/students/crscat/info.html')
classes = catalog.find_all('p')

regex_c_num = re.compile('\d{2,}')

for course in classes:
	print(course.string)
	course_num = regex_c_num.match(course.a['name'])
	print(course_num)
