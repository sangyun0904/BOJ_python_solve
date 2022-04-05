#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 17:01:14 2022

@author: sangyoon
"""

N = int(input())

cnt = 0
num = 665

while cnt != N:
    num += 1
    if '666' in str(num):
        cnt += 1
        
print(num)