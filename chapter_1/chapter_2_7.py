#!/usr/bin/env python

str = raw_input('Enter a string: ')
i = 0
while i < len(str):
	print str[i]
	i += 1

for i in range(len(str)):
	print str[i]

for i, val in enumerate(str):
	print val
