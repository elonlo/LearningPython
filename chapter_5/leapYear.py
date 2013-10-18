#!/usr/bin/env python

def isLeapYear(year):
	if year % 4 == 0 and year % 100 != 0:
		return True
	elif year % 4 == 0 and year % 100 == 0:
		return True
	else:
		return False

print isLeapYear(1992)
print isLeapYear(1996)
print isLeapYear(2000)
print isLeapYear(1967)
