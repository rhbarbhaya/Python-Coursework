# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 19:34:23 2018

@author: rhbar
"""
LCount = 0
DCount = 0
LCount = 0
File_Handle = open('names.txt','r')
for words in File_Handle:
    names = words.split()
    for i in range(len(words)):
        if names == "Lea":
            LCount += 1
        elif names == "Darth":
            DCount += 1
        elif names == "Luke":
            LCount += 1
        else:
            print "Error"
            break