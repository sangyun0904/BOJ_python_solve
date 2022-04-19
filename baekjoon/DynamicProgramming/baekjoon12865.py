#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:42:42 2022

@author: sangyoon
"""

import sys 

N, K = map(int, sys.stdin.readline().split())

goods = [[0,0]]
memo = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    goods.append([W, V])


for i in range(1, N+1):
    for j in range(1, K+1):
        weight = goods[i][0]
        value = goods[i][1]
        
        if j < weight:
            memo[i][j] = memo[i-1][j]
        else:
            memo[i][j] = max(value + memo[i][j-weight], memo[i-1][j])
            
print(memo)