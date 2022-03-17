#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:55:21 2022

@author: sangyoon
"""

import sys 

word = sys.stdin.readline().strip()

time = 0

for i in word:
    if i in "ABC":
        time += 3
    elif i in "DEF":
        time += 4
    elif i in "GHI":
        time += 5
    elif i in "JKL":
        time += 6
    elif i in "MNO":
        time += 7
    elif i in "PQRS":
        time += 8
    elif i in "TUV":
        time += 9
    else:
        time += 10
    
print(time)