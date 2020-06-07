# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:01:35 2020

@author: ak792
"""
# Write a program to calculate the bill amount for an item given it's quantity
# sold, value, discount, and tax.
print("Program to calculate the bill amount for an item.\n\n\n")
print("************************BILL************************")
qty = int(input("Enter quantity of object:"))
value = float(input("Enter value of the object:"))
discount = float(input("Enter discount percentage:"))
tax = float(input("Enter tax percentage:"))
amount = (qty * value) 
discount_amount=(discount / 100) * amount
tax_value = (tax / 100) * amount
total = amount + tax - discount
print("Quantity =" + str(qty) + "\nPrice per item = " + str(value) + "\n----------------------------\nDiscount = " + str(discount_amount))
print("Tax = " + str(tax_value) + "\n----------------------------\nTotal = " + str(total))
input()

