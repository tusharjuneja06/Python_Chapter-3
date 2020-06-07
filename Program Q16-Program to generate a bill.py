# -*- coding: utf-8 -*-
"""
Created on Mon May 18 08:49:37 2020

@author: ak792
"""
# WAP to prepare a grocery bill. For that enter the name of the items purchased
# , quantity in which it is purchased, and it's price per unit. Then display 
# the bill in following format.
# ************************************BILL************************************
# Item Name                     Item Quantity                      Item Price
# 
# ****************************************************************************
# Total Amount To Be Paid
# ****************************************************************************
print("Program to generate a bill.\n\n\n")
item_name = str(input("Enter item name : "))
quantity = int(input("Enter quantity of item : "))
price = float(input("Enter price per unit : "))
print("\n****************************BILL****************************")
print("Item Name               Item Quantity             Item Price")
print(item_name, "                      " , quantity , "                  " , price)
print("************************************************************")
print("Total amount to be paid                                " + str(quantity*price))
print("************************************************************")
input()
