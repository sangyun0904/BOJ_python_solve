#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 17:10:09 2022

@author: sangyoon
"""

import sys 

# num = int(sys.stdin.readline())
num = 26
newNum = num
cnt = 0

while True:
    if newNum < 10:
        newNum = newNum * 11
    else:
        newNum = (newNum % 10) * 10 + ((newNum // 10 + newNum % 10) % 10)
    cnt += 1
    
    if num == newNum:
        break

print(cnt)