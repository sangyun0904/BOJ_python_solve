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

for i in xyList:
    rank = 1
    for j in xyList:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")