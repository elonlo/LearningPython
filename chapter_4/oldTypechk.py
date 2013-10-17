#!/usr/bin/env python

import types
from types import IntType

def displayNumType(num):
	print num, 'is ',
	if type(num) == IntType:
		print 'an integer'
	elif type(num) == type(0L):
		print 'a long'
	elif type(num) == type(0.0):
		print 'a float'
	elif type(num) == type(0+oj):
		print 'a complex number'
	else:
		print 'not a number at all!!'

