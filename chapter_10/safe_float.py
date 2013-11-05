#!/usr/bin/env python

def safe_float(obj):
	try:
		retval = float(obj)
	except ValueError:
		retval = 'could not convert non-number to float'
	except TypeError:
		retval = 'object type cannot be converted to float'

	return retval

def safe_float_2(obj):
	try:
		retval = float(obj)
	except (ValueError, TypeError):
		retval = 'argument must be a number or numeric string'
	return retval

print safe_float('12.34')
print safe_float('bad input')
print safe_float(())
