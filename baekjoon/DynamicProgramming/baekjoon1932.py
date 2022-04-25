#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 18:05:43 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N = int(input())

tri = [list(map(int, input().split())) for i in range(N)]
ans = [0 for i in range(N)]

for i in range(N):
    temp = ans.copy()
    for j in range(i+1):
        if j == 0:
            ans[0] = temp[0] + tri[i][j]
        elif j == i:
            ans[j] = temp[j-1] + tri[i][j]
        else:
            ans[j] = max(temp[j-1], temp[j]) + tri[i][j]
    print(ans)
            
print(ans)