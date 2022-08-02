#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 12:53:00 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N = int(input())

ropes = []

for _ in range(N):
    ropes.append(int(input())) 
    
ropes.sort() 

ans = 0

for i in range(N):
    lift = ropes[i] * (N-i)
    if ans < lift:
        ans = lift 
        
print(ans)