#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 21:00:11 2022

@author: sangyoon
"""

import sys
K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(lan) 

while start <= end: 
    mid = (start + end) // 2 
    lines = 0 
    for i in lan:
        lines += i // mid 
        
    if lines >= N: 
        start = mid + 1
    else:
        end = mid - 1
print(end)