#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 16:08:58 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N = int(input())

data = []

for _ in range(N):
    data.append(input().strip().split()[1:])
    
data.sort()

for i in range(len(data)):
    tmp = -1
    for j in range(len(data[i])):
        tmp += 1
        if i != 0 and len(data[i-1]) > j:
            if data[i-1][:j+1] == data[i][:j+1]:
                continue
        print("--" * tmp + data[i][j])
        