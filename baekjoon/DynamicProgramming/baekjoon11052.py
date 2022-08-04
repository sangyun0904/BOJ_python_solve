#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 21:18:39 2022

@author: sangyoon
"""

N = int(input())
price = [0] + list(map(int, input().split()))
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    for  k in range(1, i+1):
        dp[i] = max(dp[i], dp[i-k] + price[k]) 
        
print(dp[-1])        