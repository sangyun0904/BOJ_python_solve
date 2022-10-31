# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 13:08:41 2022

@author: USER
"""

N, K = map(int, input().split())
p = 1000000007

def factorial(n):
    res = 1
    for i in range(2, n+1):
        res = res * i 
    return res 

ans = factorial(N) / (factorial(K) * factorial(N-K))
print(ans)