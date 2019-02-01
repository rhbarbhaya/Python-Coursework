# Author:  ---

# Exercise 0
# Sample progam

# This program prompts the user for two integers, 
#     then calculates and prints their sum

# The program is written as a loop (using while True), so that the user
#     must enter the word 'done" (without quotes) to signal
#     that they want to end

while True:  
    first_num = raw_input("Enter first integer, or 'done' (no quote) to stop: ")
    if first_num == 'done':
        break
    else:
        #  get numbers from user
        second_num = raw_input("Enter second integer: ")
        
        # calculate and print sum
        # use int() built-in fuction to convert raw input to integer

        print '\nThe sum of', first_num, '+', second_num, 'is equal to ', int(first_num) + int(second_num)

print '\nThanks for using this tool!\n'
