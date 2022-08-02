#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 12:39:20 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort() 
B.sort(reverse=True) 

ans = 0

for i in range(N):
    ans += A[i] * B[i]
    
print(ans)