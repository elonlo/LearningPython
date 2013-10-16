#!/usr/bin/env python

inputList = [1, 2, 3, 4]
for i in range(4):
	inputList[i] = raw_input('Enter the %d value' % (i))

i = 1
output = int(inputList[0])
while i < 4:
	output += int(inputList[i])
	i += 1

print output

output = int(inputList[0])
for i in range(3):
	output += int(inputList[i+1])

print output
	
