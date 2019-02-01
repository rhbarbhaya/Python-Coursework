# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 19:09:26 2018

@author: rhbar
"""
a = 1
b = 1

print "Welcome to the program?"

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def linear(a = -1.0,b = 1.0):
    x = -b/a
    print "Linear equation =", a,"*x +", b, "= 0"
    print "Solution to the linear equation(x) =",float(x)
    
while True:
    num1 = raw_input("Enter 1st no: Or type 'done' to end:  ")
    if num1 == "done":
        break
    else:
        n = int(num1)
        print "Factorial of the number: ", factorial(n)

        num2 = raw_input("Enter 2nd No: ")
        a = float(num2)
        print "The number you entered is: ", num2

        num3 = raw_input("Enter 3rd No: ")
        b = float(num3)
        print "The number you entered is: ", num3
        linear(a, b)