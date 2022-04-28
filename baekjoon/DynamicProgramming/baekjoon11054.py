#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:44:29 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N = int(input())
A = list(map(int, input().split()))

asc = [1 for i in range(N)]
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            asc[i] = max(asc[i], asc[j]+1)
            
desc = [1 for i in range(N)]
for i in range(N-1, -1, -1):
    for j in range(N-1, i-1, -1):
        if A[i] > A[j]:
            desc[i] = max(desc[i], desc[j]+1)
            
ans = [0 for i in range(N)]

for i in range(N):
    ans[i] = asc[i] + desc[i] -1 
print(max(ans))