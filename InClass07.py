# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 20:01:01 2018

@author: rhbar
"""

import wordcloud
import nltk
#Russian_Agents = []
#StopWords = []
#Cleared_data = []
file_handle = open("Russian_agents.txt", "r")
#file_handle2 = open("stopwords_en.txt", "r")
#for i in file_handle.read().lower().split():
#    Russian_Agents.append(i)
#    
#for i in file_handle2.read().lower().split():
#    StopWords.append(i)
#    
#if StopWords not in Russian_Agents:
#    Cleared_data.append(Russian_Agents)
wordcloud(file_handle)