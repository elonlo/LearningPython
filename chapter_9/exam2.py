#!/usr/bin/env python

F = raw_input('Enter F: ')
N = raw_input('Enter N: ')

i = 0
n = int(N)
fobj = open(F, 'r')
for eachLine in fobj:
	if i >= n:
		break
	else:
		print eachLine
		i += 1
		
