#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:08:41 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

T = int(input())

for _ in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    
    memo = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(1, N):
        for j in range(N-i):
            memo[j][j+i] = min([memo[j][j+k] + memo[j+k+1][j+i] for k in range(i)]) + sum(data[j:j+i+1])
            
    print(memo[0][-1])