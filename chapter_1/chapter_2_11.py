#!/usr/bin/env python 

def sum(numList):
	output = 0
	for i in range(5):
		output += int(numList[i])

	return output

def avg(numList):
	output = sum(numList)
	return float(output) / 5	


flag = True
while flag:
	print 'Select 1 to take the sum of the five numbers'
	print 'Select 2 to take the average of the five numbers'
	print 'Select n to ...'
	print 'Select X to exit the program'
	index = raw_input('Enter your select:')
	if index == '1':
		nums = [0, 0, 0, 0, 0]
		for	 i in range(5):
			nums[i] = int(raw_input('Enter the %d numbers: ' % (i+1))) 
		
		print sum(nums)
	elif index == '2':
		nums = [0, 0, 0, 0, 0]
		for i in range(5):
			nums[i] = int(raw_input('Enter the %d numbers: ' % (i)))

		print avg(nums)
	elif index == 'X':
		print 'Exit the program...'
		flag = False

