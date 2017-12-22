import sys
import requests
from lxml import html
from bs4 import BeautifulSoup

# Globals
link_list = []
bad_links = []
r = requests.get("http://www.monetate.com/")
soup = BeautifulSoup(r.content, "html.parser")

# Iterate through Monetate HTML to get link_list of all valid hyperlinks
# *** NOTE: only checks links that have href attributes ***
for a in soup.findAll("a", href=True):
	link_list.append(a['href'])

# Iterate through link_list
for link in link_list:
	# Scrub URLs
	if link[0] == '/' or link[0] == '#':
		link = 'https://www.monetate.com' + link
	if link[:3] == 'tel':
		continue
	
	link_request = requests.get(link)
	if str(link_request.status_code)[0] == '4':
		bad_links.append(link)

# Print output to console
print(bad_links)