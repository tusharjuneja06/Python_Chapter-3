# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:51:26 2020

@author: ak792
"""
# Write a program to calculate average of two numbers.
# Also print deviation
print("Write a program to calculate average of two numbers.Also print deviation\n\n\n")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("Average value = " + str((num1+num2)/2))
print("Deviation from " + str(num1) + " = " + str(num1-((num1+num2)/2)))
print("Deviation from " + str(num2) + " = " + str(num2-((num1+num2)/2)))
input()