#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 20:39:25 2022

@author: sangyoon
"""
N, K = map(int, input().split())

stds = list(map(int, input().split()))

ans = stds[-1] - stds[0]

diffs = []

for i in range(len(stds)-1):
    diffs.append(stds[i+1] - stds[i])
    
diffs.sort()

for _ in range(K-1):
    ans -= diffs.pop()
    
print(ans)