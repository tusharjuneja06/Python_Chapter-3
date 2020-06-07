# -*- coding: utf-8 -*-
"""
Created on Sun May 17 08:37:43 2020

@author: ak792
"""
# WAP to to swap two numbers using a temporary variable.
print("Program to swap two numbers using temporary variable.\n\n\n")
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
print("a = " + str(a) + "\nb = " + str(b))
temp=a
a=b
b=temp
del(temp)
print("After swapping :")
print("a = " + str(a) + "\nb = " + str(b))
input()