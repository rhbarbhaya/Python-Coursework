'''
Author: Rushabh Barbhaya
Date: 09/12/2018

Assignment 02
EM 624
'''

print '\n\n--- Welcome! ---'

def Cancel():
	print '\n\nThank you for using this program!'

while True:
	Input = raw_input('--- Enter the amount (in cents) which are multiple of 5\n--- OR \n--- type "done" to end: ')
	if Input == 'done':
		Cancel()
		break

	IntInput = int(Input)
	if IntInput%5 == 0:
		print '\n--->you entered', IntInput,'cents'
		continue
	else:
		print '\n--->Invalid Number'
		continue