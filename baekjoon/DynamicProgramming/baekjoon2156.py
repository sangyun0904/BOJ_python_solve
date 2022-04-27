#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:23:08 2022

@author: sangyoon
"""
import sys
input = sys.stdin.readline

n = int(input())
wines = [int(input()) for _ in range(n)]

memo = [[0,0] for _ in range(n)]

memo[0] = [wines[0]]
if n != 1:
    memo[1] = [wines[0] + wines[1], wines[1]]

for i in range(2, n):
    memo[i][0] = memo[i-1][1]+wines[i]
    temp = 0
    for j in range(i-1):
        if max(memo[j]) + wines[i] > temp:
            temp = max(memo[j]) + wines[i]
    memo[i][1] = temp
ans = 0 
for i in memo:
    if max(i) > ans:
        ans = max(i)
        
print(ans)