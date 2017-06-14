import urllib,urllib2,re,httplib
import traceback
from urllib2 import HTTPError

phones = []
emails = []


with open("emails.csv", "r") as f:
	content = f.readlines()

content = [x.strip() for x in content]

print content

for singleitem in content:
	try:
		f = urllib2.urlopen(singleitem)
		s = f.read()
		phone = re.findall(r"\+\d{2}\s?0?\d{10}",s)
		email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
		phone = str(phone)
		phone = phone.translate(None, '[]\'')
		email = str(email)
		email = email.translate(None, '[]\'')
		phones.append(phone)
		emails.append(email)
	except urllib2.HTTPError:
		print ""
	except httplib.BadStatusLine:
		print ""
	except urllib2.URLError:
		print ""

output = open("urls.csv", "a")
output.write( "\"Name\";\"Phone\";\"Email\"\n" )
	
n = 0

for single_email in emails:
	output.write( "\"" + content[n] + "\";\"" + phones[n] + "\";\"" + emails[n] + "\"\n" )
	n = n + 1

f.close()
output.close()
