# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 20:18:30 2018
@author: Rushabh Barbhaya
Subject:
Problem Statement:
"""

import pandas as pd

file_handle = pd.read_csv("hoboken_tweets.csv")
file_handle2 = open("stopwords_en.txt", "r")
stopwords = []
for word in file_handle2:
    stopwords.append(word)

text = list(file_handle["text"])
cleaned_text = []

for lines in text:
    for words in lines:
        cleaned_text.append(words)

#file_handle["text"].apply(f)