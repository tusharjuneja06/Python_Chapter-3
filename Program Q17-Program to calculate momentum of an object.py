# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:50:14 2020

@author: ak792
"""
# Momentum is calculated as, e = mc^2, hwere m is the mass of the object and
# c is it's velocity. WAP that accepts an object's mass (in kg) and velocity
# (in m/s) and displays it's momentum.
print("Program to display momentum of an object.\n\n\n")
mass = float(input("Enter mass of object (in kg) : "))
velocity = float(input("Enter velocity of object (in m/s) : "))
print("\nMomentum of object = " , mass*(velocity**2))
input()

