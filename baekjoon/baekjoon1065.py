#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 18:30:52 2022

@author: sangyoon
"""

import sys 
num = int(sys.stdin.readline())

if num < 100:
    print(num)
else:
    ans = 99 
    for i in range(100, num + 1):
        if (i // 100 - (i % 100) // 10) == ((i % 100) // 10 - i % 10):
            ans += 1
    print(ans)