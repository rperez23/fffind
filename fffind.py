#! /usr/bin/python3

import re

inf = 'episodes.txt'

db = open (inf,'r')

for l in db.readlines():
	l = l.strip()
	#print(l)

	m = re.search('FF(\d+)-(\d+)',l)

	if m:
		#print(l)
		yrtmp  = int(m.group(1))
		eptmp  = int(m.group(2))
		yr     = str(yrtmp + 2)
		ep     = str(eptmp)

		#print(l,yr,ep)
		cmd = 'echo "' + l + '"'
		print(cmd) 
		cmd = 'cat s3.txt | grep -i family | grep -i feud | grep -i s' + yr + ' grep -i ' + ep
		print(cmd)
		print('echo ""')





db.close()