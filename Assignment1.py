# -*- coding: utf-8 -*-
"""
Created on Thu Sep 06 14:06:02 2018

@author: Rushabh Barbhaya
"""

print '\n---Convert your currency---'

while True:
    USD = raw_input('--Enter the amount of US$ to be exchanged\nOR\n--Type "done" to end: ')
    if USD == 'done':
        print '\n--- Thank you for using this tool ---'
        break
    
#Error Check
    if USD.isdigit() == False:
        print '\nInvalid character'
        continue
   # print '\nFollowing currencies are available:'
    #print 'Conversion rates as of September 6th, 2018'
    #print '\n1. Custom (Enter Own Conversion Rate)'
    #print '2. Euro'
    #print '3. Japanese Yen'
    #print '4. Indian Rupees'
    #print '5. Chinese Yuan'
    #print '6. Bitcoin'
    currency = raw_input('Enter the number of the desired currency: ')

#Error check
    if currency.isdigit() == False:
        print '\nInvalid character'
        continue
    
#Currency Conversion --> Euro
    if currency == '2':
        euro_ex = 0.86
        Euro = float(USD) * euro_ex
        print '$',USD, 'Equals', Euro, 'Euro(s) with exchange rate of', euro_ex
        continue
#Currency Conversion --> Yen
    if currency == '3':
        yen_ex = 110.8
        Yen = float(USD) * yen_ex
        print '$',USD, 'Equals', Yen, 'Japanese Yen(s) with exchange rate of', yen_ex
        continue
#Currency Conversion --> Rupees
    if currency == '4':
        rupee_ex = 71.93
        Rupees = float(USD) * rupee_ex
        print '$',USD, 'Equals', Rupees, 'Indian Rupee(s) with exchange rate of', rupee_ex
        continue
#Currency Conversion --> Yuan
    if currency == '5':
        yuan_ex = 6.84
        Yuan = float(USD) * yuan_ex
        print '$',USD, 'Equals', Yuan, 'Chinese Yuan(s) with exchange rate of', yuan_ex
        continue
#Currency Conversion --> Bitcoin
    if currency == '6':
        bit_ex = 1/6429.01
        Bit = float(USD) * bit_ex
        print '$',USD, 'Equals', Bit, 'Bitcoin(s) with change rate of', bit_ex
        continue
#Currency Conversion --> Custom
    if currency == '1':
        conversion_rate = raw_input('Enter the conversion rate: ')
        if conversion_rate.isdigit == False:
            continue
        Custom = float(USD) * float(conversion_rate)
        print '$',USD, 'Equals', Custom, 'Units(s) with exchange rate of', conversion_rate
        continue