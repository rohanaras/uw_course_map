from bs4 import BeautifulSoup
import re, urllib

# JSON file to store course info
f = open('course_info.json', 'w')

# turn webpage into beautiful soup object
def url_to_beautifulsoup(url):
	response = urllib.urlopen(url, data=None)
	html = response.read()
	soup = BeautifulSoup(html)
	return soup

f.write('{\n\t"Informatics":{\n')

# get list of couse elements
catalog = url_to_beautifulsoup('http://www.washington.edu/students/crscat/info.html')
classes = catalog.find_all('p')
classes.pop(0)

# regular expressions
regex_c_name = re.compile('\D*\d*')
# regex_c_num = re.compile('\d{2,}')

# get course name, description, prereqs, andd area of knowldege information for each 
# course
for course in classes:
	# print(course.prettify()) # debug
	print(course.b.string) # debug
	
	course_name = regex_c_name.search(course.b.string).group(0)
	# course_num = re.findall('\d*', course.b.string, flags=0)[0] <-alternate version
	print(course_name) # debug

	course_header = course.b.string.split(') ')
	if len(course_header) > 1:
		aok = course_header[1] 
	else:
		aok = ''
	print(aok) # debug

	# gets any crosslisted classes. still needs work (doesn't work when there is one)
	course_desc = course.contents[2].split('Offered: jointly')
	if len(course_desc) > 1:
		crosslist = course_desc[1]
	else:
		crosslist = 'none'
	print(crosslist) # debug
	course_desc = course_desc[0]

	# gets any prerequisites. still needs work (doesn't handle more than one, crosslisted
	# classes, or multiple options)
	course_desc = course_desc.split('Prerequisite: ')
	if len(course_desc) > 1:
		prerequisites = course_desc[1]
	else:
		prerequisites = ''
	print(prerequisites) # debug
	course_desc = course_desc[0]
	# print(course_desc) # debug

	# gets any corequisites. still needs work (doesn't handle more than one, crosslisted
	# classes, or multiple options) could potentially just handle as a prereq
	course_desc = course_desc.split('Corequisite: ')
	if len(course_desc) > 1:
		corequisites = course_desc[1]
	else:
		corequisites = ''
	print(corequisites) # debug
	course_desc = course_desc[0]
	
	print(course_desc) # debug

	print('\n') # debug

	f.write('\t\t"' + course_name + '":{\n\t\t\t"crosslist":"' + crosslist + 
		'",\n\t\t\t"courseDescription":"' + course_desc + 
		'",\n\t\t\t"aok":[\n\t\t\t\t"placeholder",\n\t\t\t],\n\t\t\t"prerequisites":[\n\t\t\t\t"placeholder",\n\t\t\t],\n\t\t},\n')

f.write('\t},\n}')