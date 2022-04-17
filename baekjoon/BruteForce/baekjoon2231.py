# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 18:05:57 2022

@author: USER
"""

N = int(input())
ans = 0

for i in range(N):
    temp = i
    for j in str(i):
        temp += int(j)
    if temp == N:
        ans = i
        break
    
print(ans)