#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 15:02:30 2022

@author: sangyoon
"""

T = int(input())

if T % 10 != 0:
    print(-1)
else:
    A = T // 300 
    B = (T - A*300) // 60 
    C = (T - A * 300 - B * 60) // 10 
    
    print(A, B, C)