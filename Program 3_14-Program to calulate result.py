# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:20:18 2020

@author: ak792
"""
# Write a program to calculate a student's result based on two examinations, 1
# sport event, and 3 activities conducted. The weightage of activities = 30 per
# cent, sports = 20 per cent, and examination = 50 per cent.
print("Calculations of marks of a student.\n\n\n")
exam1 = int(input("Enter marks in first examination:"))
exam2 = int(input("Enter marks in second examination:"))
sport_event = int(input("Enter marks in sport event:"))
activity1 = int(input("Enter marks in activity 1:"))
activity2 = int(input("Enter marks in activity 2:"))
activity3 = int(input("Enter marks in activity 3:"))
exam_total = exam1 + exam2
activity_total = activity1 + activity2 + activity3
activity_percentage = (activity_total / 300) * 30
sports_percentage = (sport_event / 100) * 20
exam_percentage = (exam_total/200)*50
print("**********************RESULT**********************")
print("Marks(%) in examinations = " + str(exam_percentage))
print("Marks(%) in sports = " + str(sports_percentage))
print("Marks(%) in activities = " + str(activity_percentage))
print("--------------------------------------------------")
print("Total marks = " + str(exam_percentage + sports_percentage + activity_percentage))
input()