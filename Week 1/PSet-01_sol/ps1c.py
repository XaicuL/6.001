#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 18:19:40 2025

@author: jeonhyunjun
"""
r = 0.04
portion_down_payment = 0.25

annual_salary = int(input("Enter your starting annual salary: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

down_payment = total_cost * portion_down_payment
months = 36

def simulate_savings(rate):
    current_savings = 0
    local_annual_salary = annual_salary
    monthly_salary = local_annual_salary / 12
    m = 0

    while m < months:
        current_savings += current_savings * r/12
        current_savings += monthly_salary * rate
        m += 1
        if m % 6 == 0:
            local_annual_salary = local_annual_salary * (1 + semi_annual_raise)
            monthly_salary = local_annual_salary / 12

    return current_savings


if simulate_savings(1.0) < down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    left = 0.0
    right = 1.0
    epsilon = 100
    steps = 0

    while True:
        mid = (left + right) / 2
        saved = simulate_savings(mid)
        steps += 1

        if abs(saved - down_payment) < epsilon:
            break

        if saved < down_payment:
            left = mid
        else:
            right = mid

    print("Best savings rate:", round(mid, 4))
    print("Steps in bisection search:", steps)