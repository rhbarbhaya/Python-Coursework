# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 19:15:51 2018

@author: rhbar
"""

import csv
import pandas as pd

csvfile = pd.read_csv("US_Baby_Names_right.csv")
sumfile = csvfile.groupby(["Gender"]).size()

females = csvfile.loc[csvfile["Gender"] == "F"].count()
males = csvfile.loc[csvfile["Gender"] == "M"].count()

if len(males) > len(females):
    print "Higher number of males"
else:
    print "Higher number of females"
    
topfive = csvfile.groupby(["Name"]).size().nlargest(5)