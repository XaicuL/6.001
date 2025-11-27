#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 18:19:27 2025

@author: jeonhyunjun
"""
annual_salary = 0
portion_saved = 0
total_cost = 0
semi_annual_raise = 0
current_savings = 0
r = 0.04
portion_down_payment = 0.25 #flaot
months = 0

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the portion of salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

salary = annual_salary / 12
down_payment = total_cost * portion_down_payment

while current_savings < down_payment:
    monthly_rate = current_savings * r/12
    monthly_savings = salary * portion_saved
    current_savings = current_savings  + (current_savings * r/12)  + (salary * portion_saved)
    months += 1 

    if months % 6==0:
        annual_salary = annual_salary * (1 + semi_annual_raise) 
        salary = annual_salary / 12
        monthly_savings = salary * portion_saved

print("Number of months:", months)