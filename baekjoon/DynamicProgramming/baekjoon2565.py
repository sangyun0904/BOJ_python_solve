# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:29:29 2022

@author: USER
"""
import sys

input = sys.stdin.readline

N = int(input())

lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort(key=lambda x:x[0])
memo = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            memo[i] = max(memo[i], memo[j]+1)
            
print(N - max(memo))

a = "sdgsad"
a.cou