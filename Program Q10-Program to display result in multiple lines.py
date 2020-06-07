# -*- coding: utf-8 -*-
"""
Created on Mon May 18 07:54:37 2020

@author: ak792
"""
# WAP to read the address of a user. Display the result by breaking it in
# multiple lines.
print("Program to read the address of a user and display the result by breaking it in multiple lines.\n\n\n")
string=str(input("Enter your address : "))
part=string.split()
for i in part:
    print(i)
input()
