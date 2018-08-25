# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:40:55 2018

@author: bw033154
"""

# Problem Set 1 C

def calculate_diff(annual_salary, saving_percent, goal):
    saving = 0
    for i in range(1, 37):
        saving = saving*(1+0.04/12) + (annual_salary/12)*saving_percent
        if i % 6 == 0:
            annual_salary = annual_salary*(1+0.07)
    return(saving - goal)
    
goal = 1000000*0.25
annual_salary = int(input("Enter your starting annual salary: "))
step = 0
a = 0
b = 1

while True:
    if calculate_diff(annual_salary, b, goal) > 0.0: 
        c = (a+b)/2
        diff = calculate_diff(annual_salary, c, goal)
        step += 1
        if (diff > 0.0) & (diff > 10.0):
            b = c
        elif (diff < 0.0) & (diff < -10.0):
            a = c
        elif (diff > 0.0) & (diff < 10.0):
            print("Best savings rate:", round(c, 4))
            print("Step in bisection search:", step)
            break
    elif calculate_diff(annual_salary, b, goal) == 0.0:
        run = False
        print("Best savings rate:", b)
        print("Step in bisection search:", step)
        break
    else:
        print("It is not possible to pay the down payment in three years.")
        break



