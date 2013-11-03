#!/usr/bin/env python

def isperfect(num):
	lt = [x for x in range(1, num) if num % x == 0]
	print lt
	if sum(lt) == num:
		return True
	return False

for i in range(1, 20):
	print i, ":", isperfect(i)
