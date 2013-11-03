#!/usr/bin/env python

def fibonacci(n):
	if n == 1 or n == 2:
		return 1
	result = 2
	first = 1
	second = 1
	count = 3
	while count < n:
		first = second
		second = result
		result = first + second
		count += 1
	return result

for i in range(1, 20):
	print i, ":", fibonacci(i)
