import sys
import requests
from lxml import html
from bs4 import BeautifulSoup

# Usage
if len(sys.argv) == 1:
	print("Please input a URL in the format of: http://www.your_url_here.com")
	sys.exit(2)

# Globals
link_list = []
bad_links = []
base_url = str(sys.argv[1])

# Print executing info
print("This is the name of the script: ", sys.argv[0])
print("The website to test is: " , base_url)

# Prepare request
r = requests.get(str(base_url))
soup = BeautifulSoup(r.content, "html.parser")

# Iterate through Monetate HTML to get link_list of all valid hyperlinks
# *** NOTE: only checks links that have href attributes ***
for a in soup.findAll("a", href=True):
	link_list.append(a['href'])

# Iterate through link_list
for link in link_list:
	# Scrub URLs
	if link[:4] == 'http':
		#print(link)
		link_request = requests.get(link)
		if str(link_request.status_code)[0] == '2':
			bad_links.append(link)

# Print output to console
print(bad_links)