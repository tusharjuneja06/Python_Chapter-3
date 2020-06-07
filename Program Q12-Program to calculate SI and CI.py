# -*- coding: utf-8 -*-
"""
Created on Mon May 18 08:09:04 2020

@author: ak792
"""
# WAP to calculate simple interest and compound interest.
print("Program to calculate\n(i) Simple Interest\n(ii) Compound Interest\n\n\n")
print("------------------------Simple Interest--------------------------")
principal = float(input("Enter principal amount : "))
roi = float(input("Enter rate of interest(per year) : "))
time = float(input("Enter time(in years) : "))
SI = (principal * roi * time)/100
print("\nSimple interest = ", SI)
print("\n------------------------Compound Interest------------------------")
principal = float(input("Enter principal amount : "))
roi = float(input("Enter rate of interest(per year) : "))
time = float(input("Enter time(in years) : "))
no = float(input("No of time interest applied per time period : "))
CI = principal * ((1 + (roi / no)) ** (no * time))
print("\nCompound interest = ", round(CI,2))
input()
