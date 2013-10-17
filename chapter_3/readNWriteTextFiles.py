#!/usr/bin/env python

'write and read the file'

import os

flag = True
while flag:
	print 'Select 1 to make a file...'
	print 'Select 2 to read a file...'
	print 'Select q to exit the program...'
	index = raw_input('Enter your select...: ')
	if index == '1':
		ls = os.linesep
		# get filename
		while True:
			fname = raw_input('Enter a file name: ')
			if os.path.exists(fname):
				print "ERROR: '%s' already exists" % fname
			else:
				break
		# get file comtent 
		all = []
		print "\nEnter lines('.' itself to quit).\n"	
		
		# loop until user terminates input .
		while True:
			entry = raw_input('>')
			if entry == '.':
				break
			else:
				all.append(entry)
		#write lines to files with proper line-ending
		try:
			fobj = open(fname, 'w')
		except IOError, e:
			print 'Write file ERROR', e
		else:
			fobj.writelines(['%s%s' %(x, ls) for x in all])
			fobj.close()
			print 'DONE'
	
	elif index == '2':
		# get filename
		fname = raw_input('Enter you will open the file name: ')
		print
		# attempt to open file for reading
		try:
			fobj = open(fname, 'r')
		except IOError, e:
			print "*** file open error:", e	
		else:
			# display contents to the screen
			for eachLine in fobj:
				print str.strip(eachLine)
			fobj.close()

	elif index == 'q':
		break

