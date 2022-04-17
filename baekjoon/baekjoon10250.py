#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 15:27:47 2022

@author: sangyoon
"""

import sys 

T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    if N % H == 0:
        xx = N // H 
        yy = H
    else:
        xx = N // H + 1 
        yy = N % H 
    print(yy * 100 + xx)