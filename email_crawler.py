import urllib,re

fot = open("emails.csv", "a+")

filepath = 'urls.csv'
with open(filepath) as fp:  
	line = fp.readline()
	cnt = 1
	while line:
		print("Line {}: {}".format(cnt, line.strip()))
		line = fp.readline()
		site = line
		f = urllib.urlopen(line)
		s = f.read()
		re.findall(r"\+\d{2}\s?0?\d{10}",s)
		email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
		email = str(email)
		email = email.translate(None, '\'[]')
		if email == "":
			email = "NA"
		print site + " = " + email + "\n"
		fot.write("\""+site+"\""+",\""+email+"\"\n")
		cnt += 1

fot.close()
fp.close()
