#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 17:31:19 2022

@author: sangyoon
"""

M = int(input())
N = int(input())

i = 1

ans1 = 0 
ans2 = 0 

while i*i <= N:
    if i*i >= M:
        ans1 += i*i 
        if ans2 == 0:
            ans2 = i*i
    i += 1
    
print(ans1)
print(ans2)