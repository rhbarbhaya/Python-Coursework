# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:03:27 2018

@author: rhbar
"""
from datetime import *

Name = raw_input('Please enter your name: ')
age = raw_input('Please enter your age: ')

year = 2018
yearCent = (int(year) - int(age)) + 100
today = date(year, 9, 11)
future = date(yearCent, 1, 1)

daysBetween = future - today
print Name+'.', 'There are', daysBetween.days, 'days between now 1st day of your 100th year.'
print "You'll be 100 years old at the year", yearCent