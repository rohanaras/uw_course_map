from bs4 import BeautifulSoup
import urllib

# debug logger: terminal can't handle some characters
log = open('log.txt', 'w')

# list of all catalogue urls
urls = open('department_urls.txt', 'w')

# turn webpage into beautiful soup object
def url_to_beautifulsoup(url):
	response = urllib.urlopen(url, data=None)
	html = response.read()
	soup = BeautifulSoup(html)
	return soup

# gets every college/school section in a list
crscat = url_to_beautifulsoup('http://www.washington.edu/students/crscat/')
colleges = crscat.find_all('ul') 
colleges.pop()

for college in colleges:
	departments = college.find_all('li')

	# gets the url for each department
	for department in departments:
		department_url = 'http://www.washington.edu/students/crscat/'
		#log.write(str(department.string) + '\n') # debug
		if  department.string != None:
			if '--' not in department.string:
				try:
					department_url = department_url + department.a['href']
					log.write(department_url + '\n')
					urls.write(department_url + '\n')
				except TypeError:
					log.write('is not a department' + '\n')
				except KeyError:
					log.write('is not a department \n')
		log.write('\n')
