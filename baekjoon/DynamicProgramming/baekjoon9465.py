#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 21:25:26 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

T = int(input())

for _ in range(T):
    n = int(input())
    memo = [[0 for _ in range(n)] for _ in range(2)]
    
    scores = []
    for _ in range(2):
        scores.append(list(map(int, input().split())))
        
    if n == 1:
        print(max(scores[0][0], scores[1][0]))
        break
    
    memo[0][0] = scores[0][0]
    memo[1][0] = scores[1][0]
    
    memo[0][1] = scores[1][0] + scores[0][1]
    memo[1][1] = scores[0][0] + scores[1][1]
    
    for i in range(2, n):
        memo[0][i] = max(memo[1][i-2], memo[1][i-1]) + scores[0][i]
        memo[1][i] = max(memo[0][i-2], memo[0][i-1]) + scores[1][i]
        
    print(max(memo[0][n-1], memo[1][n-1]))