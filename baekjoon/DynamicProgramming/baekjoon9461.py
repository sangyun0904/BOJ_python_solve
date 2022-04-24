#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:37:25 2022

@author: sangyoon
"""

T = int(input())
for _ in range(T):
    N = int(input())
    memo = [0 for _ in range(max(6,N+1))]
    memo[1] = 1
    memo[2] = 1
    memo[3] = 1
    memo[4] = 2
    memo[5] = 2
    for i in range(6, N+1):
        memo[i] = memo[i-1] + memo[i-5]
    print(memo[N])