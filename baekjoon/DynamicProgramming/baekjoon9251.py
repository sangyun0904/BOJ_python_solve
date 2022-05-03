#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:44:41 2022

@author: sangyoon
"""
import sys 
input = sys.stdin.readline

A = input()
B = input()

memo = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            memo[i][j] = memo[i-1][j-1]+1
        else:
            memo[i][j] = max(memo[i-1][j], memo[i][j-1])
print(memo[len(A)][len(B)])