#!/usr/bin/env python 

num1 = int(raw_input('Enter the first numbers: '))
num2 = int(raw_input('Enter the second numbers: '))
num3 = int(raw_input('Enter the third numbers: '))

def order(num1, num2, num3):
	output = [0, 0, 0]
	if num1 < num2 and num1 < num3:
		output[0] = num1	
		if num2 < num3:
			output[1] = num2
			output[2] = num3
		else:
			output[1] = num3
			output[2] = num2
	elif num2 < num1 and num2 < num3:
		output[0] = num2
		if num1 < num3:
			output[1] = num1
			output[2] = num3
		else:
			output[1]= num3
			output[2] = num1
	elif num3 < num1 and num3 < num2:
		output[0] = num3
		if num1 < num2:
			output[1] = num1
			output[2] = num2
		else:
			output[1] = num2
			output[2] = num1
	return output

print order(num1, num2, num3)
