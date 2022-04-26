# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 18:24:44 2022

@author: USER
"""

import sys 
input = sys.stdin.readline 

N = int(input())
steps = [int(input()) for _ in range(N)]

memo = [(0, 0) for _ in range(N)]
memo[0] = (steps[0], 0)
if N != 1:
    memo[1] = (steps[0] + steps[1], steps[1])

for i in range(2,N):
    memo[i] = (memo[i-1][1] + steps[i], max(memo[i-2]) + steps[i])
    
print(max(memo[N-1]))