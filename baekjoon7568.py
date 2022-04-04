# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 08:59:15 2022

@author: USER
"""
import sys

N = int(sys.stdin.readline())

xyList = []

for _ in range(N):
    xyList.append(list(map(int, sys.stdin.readline().split())))
    
xyList.sort(reverse=True)

print(xyList)