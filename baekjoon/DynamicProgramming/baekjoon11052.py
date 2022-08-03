#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 21:18:39 2022

@author: sangyoon
"""

N = int(input())
price = list(map(int, input().split()))

memo = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i > j:
            memo[i][j] = memo[i-1][j]
        else:
            if j % i == 0:
                cost = (j // i) * price[i-1]
            else:
                cost = max((j // i) * price[i-1] + memo[i][j % i], (j // i -1) * price[i-1] + memo[i][j % i + i])
            if cost > memo[i-1][j]:
                memo[i][j] = cost 
            else:
                memo[i][j] = memo[i-1][j]
                
print(memo[-1][-1])