#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:49:35 2022

@author: sangyoon
"""

import sys 

MAX_N = 123456

prime_nums = [False] * 2 + [True] * (2 * MAX_N - 1)

for i in range(2 * MAX_N + 1):
    if prime_nums[i]:
        j = 2
        while True: 
            if i * j > MAX_N * 2:
                break 
            prime_nums[i * j] = False 
            j += 1 
            
while True:
    N = int(sys.stdin.readline())
    
    if N == 0:
        break 
    
    cnt = 0 
    
    for i in range(N + 1, 2 * N + 1):
        if prime_nums[i]:
            cnt += 1 
    
    print(cnt)