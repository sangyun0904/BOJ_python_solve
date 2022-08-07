#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 14:54:59 2022

@author: sangyoon
"""

A, B = input().strip().split()

diff = len(B) - len(A)

ans = 50

for i in range(diff+1):
    temp = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            temp += 1 
    if temp < ans:
        ans = temp 
        
print(ans)