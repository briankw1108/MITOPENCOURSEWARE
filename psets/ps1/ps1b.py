# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:27:38 2018

@author: bw033154
"""

# Problem Set 1 B

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentage of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream house: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

current_savings = 0
r = 0.04
portion_down_payment = 0.25
goal = total_cost * portion_down_payment
number_of_months = 0

while current_savings < goal:
    current_savings = current_savings*(1+r/12) + ((annual_salary/12)*portion_saved)
    number_of_months += 1
    if (number_of_months % 6) == 0:
        annual_salary = annual_salary*(1+semi_annual_raise)
    
print("Number of months:", number_of_months)
    








