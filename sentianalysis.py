# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 18:38:29 2018

@author: rhbar
"""
'''Short sample on using sentiwordnet to calculate thesentiment for a given list of words'''
# importing the library
from nltk.corpus import sentiwordnet as swn
# defining the list of words to be evaluated
#   (please note: they are all the same part-of-speech)
words = ['good', 'great', 'bad', 'terrible', 'happy', 'cruel']
# looping into the list of words and printing the sentiment
for elem in words:
    print '\nfor word', elem, 'sentiment is', swn.senti_synset(elem + '.a.02')