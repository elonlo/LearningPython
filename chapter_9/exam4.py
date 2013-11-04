#!/usr/bin/env python 

filename = raw_input('Enter a file name: ')
fobj = open(filename, 'r')
i = 0
for line in fobj:
	print line,
	i += 1
	if i % 25 == 0:
		print 'please hit any key to be continue...'
		raw_input()
fobj.close()
	
		


			
