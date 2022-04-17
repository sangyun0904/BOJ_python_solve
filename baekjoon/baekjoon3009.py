#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 17:55:16 2022

@author: sangyoon
"""

import sys 

x = []
y = []

for _ in range(3):
    a, b = map(int, sys.stdin.readline().split())
    if a in x:
        x.remove(a)
    else:
        x.append(a)
    if b in y:
        y.remove(b)
    else:
        y.append(b)
        
print(x[0], y[0])