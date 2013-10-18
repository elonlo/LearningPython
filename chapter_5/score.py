#!/usr/bin/env python

def score(num):
	if num >= 90 and num <= 100:
		return 'A'
	elif num >= 80 and num <= 89:
		return 'B'
	elif num >= 70 and num <= 79:
		return 'C'
	elif num >= 60 and num <= 69:
		return 'D'
	elif num >= 0 and num < 60:
		return 'F'


