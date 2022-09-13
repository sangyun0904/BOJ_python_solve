#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:17:03 2022

@author: sangyoon
"""

A, B, C, N = map(int, input().split())

ans = 1

for i in range(N // A):
    for j in range(N - (i * A) // B):
        if (N - (i * A) - (j * B)) % C == 0:
            ans = 0
            
print(ans)