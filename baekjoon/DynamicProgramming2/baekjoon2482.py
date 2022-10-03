#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 10:12:13 2022

@author: sangyoon
"""

N = int(input())
K = int(input())

dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

for i in range(N+1):
    dp[0][i] = 1

for i in range(1, K+1):
    for j in range(1, N+1):
        if j >= 2:
            dp[i][j] = dp[i][j-1] + dp[i-1][j-2]
        else:
            if i == 1:
                dp[i][j] = 1
        
print((dp[K][N-1] + dp[K-1][N-3]) % 1000000003)