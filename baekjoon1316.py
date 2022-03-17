#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:17:49 2022

@author: sangyoon
"""

import sys 

n = int(sys.stdin.readline())

cnt = 0 

for _ in range(n):
    word = sys.stdin.readline()[0:-1]
    isGroup = True
    for i in word:
        r = word.count(i)
        if i * r not in word:
            isGroup = False 
    if isGroup:
        cnt += 1
        
print(cnt)