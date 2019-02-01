# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 23:05:56 2018

@author: Rushabh Barbhaya
CWID: 10427219
"""

#Part 1 of assignment 3
print "\nAssignment 3 - Part 1"
file_handle = open('marketingdata.txt','rU')
marketingData = file_handle.readlines()

lineCount1 = 0
lineCount2 = 0

for line1 in marketingData:
    lineCount1 += 1
    if lineCount1 == 11:
        break
    print lineCount1, "--\t", line1
    
for i in marketingData:
    lineCount2 += 1
print "Line Count of MarketingData =", lineCount2
#End of Part 1

print "---------------------------------------------"
    
#Part 2 of assignment 3
print "\nAssignment 3 - Part 2"
#File_Handle
CitiBike = open('NYC-CitiBike-2016.csv','r')
bike = CitiBike.readlines()

lineCount3 = 0
lineCount4 = 0

for lines_bike in bike:
    lineCount3 += 1
    if '9/29/16' in lines_bike.strip().split(","):        
        lineCount4 += 1
print 'The citibike file contains', lineCount3, 'lines, of which', lineCount4, 'are from 9/29/16'