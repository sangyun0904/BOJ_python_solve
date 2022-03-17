#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 17:10:09 2022

@author: sangyoon
"""

import sys 

line = sys.stdin.readline()

for i in range(ord('a'), ord('z') + 1):
    if chr(i) in line:
        print(line.index(chr(i)), end=" ")
    else:
        print(-1, end=" ")