# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:17:47 2018

@author: Rushabh Barbhaya
"""

"""
Error Checking Section 2 - Midterm
"""
#Question 6. 
print "Secton 2 -\n\n\n\n"
N = raw_input("Enter your characters: ") #Take input from user
L = '' #Inititate an empty string
for letters in N: #Run a loop for adding characters
    letters.split() #Remove any white spaces
    L = L + letters*2 #Add the string twice
print L #Prining the output

#------------------------------------

#Question 7.

#filename = raw_input('Please enter the name of file: ')
file = open("word_list.csv", 'r') #Reading the input file
freq_list = {} #Creating a dict
length = 0 #Counter for length of word
wordcount = 0 #total word count
maxlength = '' #Inititate an empty string
for line in file: #Passing each variable in loop
    word = line.strip().lower().split(",") #Removing and sepereating from white spaces and breaking at ,
    for alphabets in word: #Passing each word and breaking it to alphabets
        length += len(alphabets) #Length of alphabets
        wordcount += 1 #Alphabet counter
    avg_length = float(length)/wordcount #Counting average
    
print "\n\nAverage word length is:", avg_length #print the average

#-------------------------------------

#Question 8.
while True:
#prompts and receives user input
    char = raw_input('Please enter an alphabetical character: \nOR type done to end   :')
    char = char.lower()
    if char == "done": #Breaking an infinate loop
        break
    elif char.isdigit() == True: #checks if input is numerical
        print 'Invalid input.'
    elif len(char) > 1: #checks if input is more than one character
        print 'Invalid input.'
    elif char in 'aeiou': #checks if input is a vowel
        print 'False'
    elif char in "$&^()*#@!.,?;:": #Added condition for special characters
        print "Invalid Input"
    else:
        print 'True'

print "End of Secton 2 --\n\n"
#-----------------------------------
        
#Question 9.
print "Secton 3 - \n\n\n\n\n"


file1 = open("ai_trends.txt","r")
file2 = open("stopwords_en.txt", "r")
data = []
stopwords = []

for words in file1:
    parts = words.lower().split()
    data.append(parts)

for words in file2:
    parts = words.lower().strip()
    stopwords.append(parts)
    
ai_trends = [item for sublist in data for item in sublist] #Making a list of list of lists
#Source: https://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python

clear_list = [i for i in ai_trends if i not in stopwords]

dic = {}
_length = 0
_wordnumber = 0
_maxlength = ""

for word in clear_list:
    _length += len(word)
    _wordnumber += 1

    try:
        dic[word] += 1
    except:
        dic[word] = 1

    if len(word) > len(_maxlength):
        _maxlength = word

average_word_len = float(_length)/_wordnumber

sort = sorted(dic.values(), reverse = True)

print sort[:10]
print "Average occurances of a word are:"
print "\nLongest word is:", _maxlength
print "\naverage word length =", average_word_len