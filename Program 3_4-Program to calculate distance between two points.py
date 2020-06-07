# -*- coding: utf-8 -*-
"""
Created on Wed May 13 08:07:49 2020

@author: ak792
"""
#Write a program to calculate the distance between two points
print("Program to calculate distance between two points\n\n\n")
x1=float(input("Enter the value of x1:"))
y1=float(input("Enter the value of y1:"))
x2=float(input("Enter the value of x2:"))
y2=float(input("Enter the value of y2:"))
distance=(((x2-x1)**2)+((y2-y1)**2))**(0.5)
print("First point is (x1,y1)= (" + str(x1) + "," + str(y1) + ")")
print("Second point is (x2,y2)= (" + str(x2) + "," + str(y2) + ")")
print("Distance between the two points=" + str(distance))
input()