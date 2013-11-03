#!/usr/bin/env python

def factorial(n):
	if n == 0:
		return 1
	total = 1
	for i in range(1, n):
		total *= i
	return total * n 

for i in range(1, 50):
	print i, ":", factorial(i)
