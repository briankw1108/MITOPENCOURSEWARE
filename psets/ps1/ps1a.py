# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:18:30 2018

@author: bw033154
"""

# Problem Set 1 A

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentage of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream house: "))

current_savings = 0
r = 0.04
portion_down_payment = 0.25
goal = total_cost * portion_down_payment
number_of_months = 0

while current_savings < goal:
    current_savings = current_savings*(1+r/12) + ((annual_salary/12)*portion_saved)
    number_of_months += 1
    
print("Number of months:", number_of_months)
    








