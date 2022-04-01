# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 20:01:08 2022

@author: USER
"""
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


N = int(input())

print(factorial(N))