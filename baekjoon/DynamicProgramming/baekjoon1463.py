# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:24:16 2022

@author: USER
"""
#import sys
#input = sys.stdin.readline
N = int(input())

memo = [0 for _ in range(N)]
memo[0] = 0
if N != 1:
    memo[1] = 1

for i in range(2,N):
    if (i+1) % 3 == 0 and (i+1) % 2 == 0:
        memo[i] = min(memo[i//3], memo[i//2], memo[i-1]) + 1
    elif (i+1) % 3 == 0:
        memo[i] = min(memo[i//3], memo[i-1]) + 1 
    elif (i+1) % 2 == 0:
        memo[i] = min(memo[i//2], memo[i-1]) + 1
    else:
        memo[i] = memo[i-1] + 1 
        
print(memo[N-1])