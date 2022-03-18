# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:27:24 2022

@author: USER
"""

import sys 

A, B, C = map(int, sys.stdin.readline().split())

if C <= B:
    ans = -1
else:
    ans = A // (C - B) + 1
    
print(ans)