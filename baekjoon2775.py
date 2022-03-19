#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 15:42:30 2022

@author: sangyoon
"""

import sys 

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    
    apt = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
    
    for i in range(k + 1):
        for j in range(1, n + 1):
            if i == 0:
                apt[i][j] = j
            else:
                apt[i][j] = apt[i-1][j] + apt[i][j-1]
                
                
    print(apt[k][n])
    