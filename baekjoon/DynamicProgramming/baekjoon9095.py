# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 13:47:25 2022

@author: USER
"""

T = int(input())

dp = [0 for _ in range(12)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    n = int(input())
    print(dp[n])