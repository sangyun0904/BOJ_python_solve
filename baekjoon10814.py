#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:00:59 2022

@author: sangyoon
"""
import sys

N = int(sys.stdin.readline())

members = []

for i in range(N):
    m = [i]
    m.append(list(sys.stdin.readline().split()))
    members.append(m)
    
members.sort(key = lambda x : (int(x[1][0]), x[0]))

for i in members:
    print(i[1][0], i[1][1])