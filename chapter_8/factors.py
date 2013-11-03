#!/usr/bin/env python

def getfactors(num):
	temp = num
	if num > 0:
		temp += 1
		return [x for x in range(1, temp) if num % x == 0]
	elif num < 0:
		return [x for x in range(temp, 2) if x != 0 and num % x == 0]
	else:
		print "Cann't Zero"

for i in range(20, 50):
	print i, ":", getfactors(i)

for i in range(-50, -20):
	print i, ":", getfactors(i)
