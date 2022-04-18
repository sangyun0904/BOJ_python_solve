#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 15:35:22 2022

@author: sangyoon
"""
import sys 

T = int(sys.stdin.readline())

fibo = [[-1,-1] for _ in range(41)]
fibo[0] = [1,0]
fibo[1] = [0,1]

def fibonacci(n):
    
    if fibo[n] != [-1,-1]:
        return fibo[n]
    
    else:
        l1 = fibonacci(n-2)
        l2 = fibonacci(n-1)
        fibo[n] = [l1[0] + l2[0], l1[1] + l2[1]]
        return fibo[n]

for _ in range(T):
    N = int(sys.stdin.readline())
    ans = fibonacci(N)
    print(ans[0], ans[1])
