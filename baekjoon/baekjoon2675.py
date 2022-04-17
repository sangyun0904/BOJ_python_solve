#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:44:34 2022

@author: sangyoon
"""

import sys 

N = int(sys.stdin.readline())
for _ in range(N):
    r, s = sys.stdin.readline().split()
    for i in s:
        print(i * int(r), end="")
    print()
        