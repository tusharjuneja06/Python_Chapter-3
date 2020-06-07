# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:13:18 2020

@author: ak792
"""
# WAP that prompts the user to enter the first name and last name. Then display
# the following message.
# Hello firstname lastname
# Welcome to Python!
print("Program to display a message using sting concatenation")
firstname=str(input("Enter your first name : "))
lastname=str(input("Enter your last name : "))
print("\nHello " + firstname + " " + lastname + "\nWelcome to Python!")
input()
