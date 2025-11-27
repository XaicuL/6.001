#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 18:19:27 2025

@author: jeonhyunjun
"""

annual_salary = 0
portion_saved = 0
total_cost = 0

current_savings = 0
portion_down_payment = 0.25 #flaot
r = 0.04

annual_salary = int(input("Enter your annual salary: ")) # 연봉
portion_saved = float(input("Enter the portion of your salary to save, as a decimal: ")) # 월별 저축 비율
total_cost = int(input("Enter the cost of your dream home: ")) # 원하는 집 가격

salary = annual_salary / 12 # 월급
down_payment = total_cost * portion_down_payment
monthlty_saving = salary * portion_saved
months = 0

while current_savings< down_payment:
    current_savings += current_savings * r / 12
    current_savings += monthlty_saving
    months += 1

print("Number of months: ", months)






