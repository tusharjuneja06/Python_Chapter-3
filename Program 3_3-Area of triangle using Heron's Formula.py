# -*- coding: utf-8 -*-
"""
Created on Wed May 13 07:38:07 2020

@author: ak792
"""
#Area of triangle using Heron's Formula
print("Area of triangle using Heron's Formula\n\n\n")
a=int(input("Enter the value of first side:"))
b=int(input("Enter the value of second side:"))
c=int(input("Enter the value of third side:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**(1/2)
print("a=" + str(a) + "\n"+ "b=" + str(b) + "\n" + "c=" + str(c))
print("Area=" + str(area))
input()