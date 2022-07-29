#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 11:26:29 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N = int(input())

line = list(map(int, input().split()))

M = int(input())

memo = [0 for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    
    isPalin = True
    
    for i in range(b-a):
        if line[a+i-1] != line[b-i-1]:
            isPalin = False 
            
    if isPalin:
        print(1)
    else:
        print(0)