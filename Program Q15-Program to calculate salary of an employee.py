# -*- coding: utf-8 -*-
"""
Created on Mon May 18 08:42:02 2020

@author: ak792
"""
# WAP to calculate salary of an employee given his basic pay (to be entered by
# the user). HRA = 10% of basic pay, TA = 5% of basic pay. Define HRA and TA as
# constants and use them to calculate salary of the employee.
print("Program to calculate salary of an employee.\n\n\n")
HRA=0.1
TA=0.05
basic_pay=int(input("Enter your basic pay : "))
print("At HRA = 10% and TA = 5%\nSalary = ",(basic_pay + (basic_pay * HRA) + (basic_pay * TA)))
input()
