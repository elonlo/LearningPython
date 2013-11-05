#!/usr/bin/env python

import os

#filename = raw_input("Enter a file name: ")
filename = "/etc/services"
fobj = open(filename, 'r')
allText = fobj.readlines()
fobj.close()

for line in allText:
	if line == os.linesep:
		continue
	npos = line.find("#")
	if npos == 0:
		continue
	print line[0:npos]
