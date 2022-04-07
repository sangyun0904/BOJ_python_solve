#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 16:41:21 2022

@author: sangyoon
"""

import sys 

N = int(sys.stdin.readline())

xy_list = []

for _ in range(N):
    xy_list.append(tuple(map(int, sys.stdin.readline().split())))
    
xy_list.sort(key = lambda x : (x[0], x[1]))

for i in xy_list:
    print(i[0], i[1])