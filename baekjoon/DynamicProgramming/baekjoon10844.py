#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:32:05 2022

@author: sangyoon
"""

N = int(input())

memo = [0,1,1,1,1,1,1,1,1,1]

for i in range(1,N):
    temp = memo.copy()
    for j in range(10):
        if j == 0:
            memo[j] = temp[j+1]
        elif j == 9:
            memo[j] = temp[j-1]
        else:
            memo[j] = temp[j-1] + temp[j+1]
            
print(sum(memo) % 1000000000)