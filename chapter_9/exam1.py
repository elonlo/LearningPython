#!/usr/bin/env python

filename = raw_input('Enter a file name: ')
fobj = open(filename, 'r')
for eachLine in fobj:
	npos = eachLine.find('#')
	if npos:
		print eachLine[0:npos]


