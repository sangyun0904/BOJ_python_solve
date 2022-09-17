#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 10:57:27 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N, M = map(int, input().split())

memory = list(map(int, input().split()))
costs = list(map(int , input().split()))

answer = sum(costs)
    
dp = [[0 for _ in range(sum(costs)+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(0, sum(costs)+1):
        if j >= costs[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-costs[i-1]] + memory[i-1])
            
        else:
            dp[i][j] = dp[i-1][j]
            
        if dp[i][j] >= M and j < answer:
            answer = j
            
for i in dp:
    print(i)
            
print(answer)