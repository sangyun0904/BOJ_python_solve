#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:09:23 2022

@author: sangyoon
"""

import sys 
from collections import Counter

N = int(sys.stdin.readline())

n_list = []

for _ in range(N):
    num = int(sys.stdin.readline())
    n_list.append(num)
    
n_list.sort()

n_count = sorted((Counter(n_list).items()), key = lambda x: (-x[1], x[0]))
print(round(sum(n_list) / len(n_list)))
print(n_list[len(n_list) // 2])
if (len(n_count) == 1):
    print(n_count[0][0])
else:
    if n_count[0][1] == n_count[1][1]:
        print(n_count[1][0])
    else:
        print(n_count[0][0])
print(n_list[-1] - n_list[0])
