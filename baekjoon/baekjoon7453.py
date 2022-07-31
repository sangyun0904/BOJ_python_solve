#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 16:50:39 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

n = int(input())

A, B, C, D = [[] for _ in range(4)]

for _ in range(n):
    nums = list(map(int, input().split()))
    A.append(nums[0])
    B.append(nums[1])
    C.append(nums[2])
    D.append(nums[3])
    
A_B = {}

for i in A:
    for j in B:
        if i+j in A_B.keys():
            A_B[i+j] += 1 
            
        else:
            A_B[i+j] = 1 

ans = 0
            
for i in C:
    for j in D:
        if -(i + j) in A_B.keys():
            ans += A_B[-i-j]
            
print(ans)