#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 15:35:46 2022

@author: sangyoon
"""

maxInt = 30

dp = [[0 for _ in range(maxInt + 1)] for _ in range(maxInt + 1)]

for i in range(1, maxInt):
    for j in range(1, maxInt):
        if i == 1:
            dp[i][j] = j 
        elif i == j:
            dp[i][j] = 1 
        elif i < j:
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

print(dp[13][29])