#!/usr/bin/env python

filename = raw_input('Enter a file name: ')
fobj = open(filename)
print len([line for line in fobj])
fobj.close()
