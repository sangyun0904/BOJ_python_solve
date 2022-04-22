#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:04:28 2022

@author: sangyoon
"""

import sys 

input = sys.stdin.readline 

dest = [(0, -1), (1, 0), (0, 1), (-1, 0)]
memo = []

def lookLeft(d):
    if d == 0:
        d = 3
    else:
        d -= 1
    return d

def moveForward(r, c, d):
    r += dest[d][0]
    c += dest[d][1]
    memo.append((r,c))
    return r, c

def moveBackward(r, c, d):
    r -= dest[d][0]
    c -= dest[d][1]
    memo.append((r,c))
    return r, c

def move(r, c, d):
    memo.append((r,c))
    room[c][r] = 2
    clean = 1
    count = 0
    while True:
        d = lookLeft(d)
        if room[c+dest[d][1]][r+dest[d][0]] == 0:
            r, c = moveForward(r, c, d)
            room[c][r] = 2
            clean += 1
            count = 0
        else:
            count += 1
            
        if count == 4:
            if room[c-dest[d][1]][r-dest[d][0]] == 1:
                return clean 
            else:
                r, c = moveBackward(r, c, d)
                count = 0
            
N, M = map(int, input().split())
c, r, d = map(int, input().split())

room = []

for _ in range(N):
    room.append(list(map(int, input().split())))

print(move(r, c, d))
