# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 10:51:11 2022

@author: USER
"""

import sys 
input = sys.stdin.readline 

s1 = input().strip()
s2 = input().strip()

memo = [["" for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]

for i in range(len(s2)):
    for j in range(len(s1)):
        if s2[i] == s1[j]:
            memo[i+1][j+1] = memo[i][j] + s2[i]
        else:
            if len(memo[i+1][j]) > len(memo[i][j+1]):
                memo[i+1][j+1] = memo[i+1][j]
            else:
                memo[i+1][j+1] = memo[i][j+1]
            
if len(memo[-1][-1]) == 0:
    print(0)
else:
    print(len(memo[-1][-1]))
    print(memo[-1][-1])
