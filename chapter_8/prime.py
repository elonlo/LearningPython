#!/usr/bin/env python

def isprime(num):
	result = True
	for i in range(2, num):
		if num % i == 0:
			result = False
			break
	return result

for i in range(20):
	print i, ':', isprime(i)


