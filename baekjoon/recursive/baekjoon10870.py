# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 21:23:38 2022

@author: USER
"""

def fibo(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
N = int(input())

print(fibo(N))