#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 15:03:01 2022

@author: sangyoon
"""

N = int(input())

dp = [0 for _ in range(N+1)]

dp[1] = 1 

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]
    
print(dp[-1])