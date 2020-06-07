# -*- coding: utf-8 -*-
"""
Created on Wed May 13 07:57:02 2020

@author: ak792
"""
#Program to read and print values of variable of different data types
print("Program to read and print values of variable of different data types\n\n\n")
name=str(input("Enter your name:"))
age=int(input("Enter your age:"))
savings=int(input("Enter your savings:"))
interest=0.02*savings
print("Hello " + name + " !\nYour age is " + str(age) + "\nYour savings=" + str(savings) + "\nInterest You will get yearly at 2% per annum=" +str(interest))
input()
