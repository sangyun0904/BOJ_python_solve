#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 18:38:25 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N, K = map(int, input().split())
vals = []
for _ in range(N):
    vals.append(int(input()))
    
cnt = 0

for i in range(-1, -N-1, -1):
    cnt += K // vals[i]
    K = K % vals[i]
    
print(cnt)