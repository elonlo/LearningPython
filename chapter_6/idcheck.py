#!/usr/bin/env python

import string

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'

myInput = raw_input('Identifier to test?')

if len(myInput) > 1:
	if myInput[0] not in alphas:
		print '''invalid first symbol must be alphabetic'''
	else:
		inputLen = myInput[1:]
		newAlphas = alphas + nums
		for otherChar in inputLen:
			if otherChar not in newAlphas:
				print ''' invalid: remaining
					symbols must be alphanumeric'''
				break
		else:
			print "okay as an identifier"
