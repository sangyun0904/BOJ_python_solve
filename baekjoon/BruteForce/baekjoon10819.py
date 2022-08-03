#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 17:18:41 2022

@author: sangyoon
"""

import sys 
from itertools import permutations

input = sys.stdin.readline 

N = int(input())

nums = list(map(int, input().split()))
nums_permut = permutations(nums)

ans = 0 

for t in nums_permut:   
    temp = 0
    for i in range(N-1):
        temp += abs(t[i] - t[i+1])
        
    if temp > ans:
        ans = temp 
        
print(ans)