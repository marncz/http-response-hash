import urllib2
import string
import hashlib

def getHeader(url):
	page = urllib2.urlopen(url)
	return page.info()

hashable = [  "Accept",
			  "Accept-Charset",
			  "Accept-Encoding",
			  "Accept-Language",
			  "Cache-Control",
			  "Content-Type",
			  "Vary"          ]	
	
url = "http://www.wykop.pl"

new_header = ""
header = str(getHeader(url))
splitted =  string.split(header, '\n')

	
for line in splitted:
	split = line.split(":")
	if(split[0] in hashable):
		new_header += line 
	else:
		new_header += split[0]

		
new_header.replace(" ", "")
m = hashlib.sha256()	
print hashlib.sha256(new_header).hexdigest()
