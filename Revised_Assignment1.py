# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 12:55:00 2018

@author: rushabh barbhaya
"""

print "---Currency Conversion---"

def exchange():
    global usd
    global conversion_rate
    change = float(usd) * float(conversion_rate)
    print '------------------------------------------------'
    print '$', usd, 'equals', change, currency, 'with conversion rate of', conversion_rate    
    print '------------------------------------------------'

while True:
    usd = raw_input('-- Enter the amount of $ to be converted: \n OR \n-- Type "done" to end: ')
    if usd == 'done':
        break
    if usd.isdigit() == False:
        print 'Invalid Character'
        continue
    
    currency = raw_input('--Enter the name of the currency: ')
    conversion_rate = raw_input('Enter the conversion rate: ')
    if conversion_rate.isdigit() == False:
        print 'Invalid Character'
        continue
    exchange()