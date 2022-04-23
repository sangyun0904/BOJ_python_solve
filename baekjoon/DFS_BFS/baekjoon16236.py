#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 14:16:25 2022

@author: sangyoon
"""
import sys
from collections import deque

input = sys.stdin.readline

size = 2

def eatFish(start, size, visited):
    eatables = []
    stop = 999
    q = deque([[start, 0]])
    while q:
        n, d = q.popleft()
        if d == stop:
            break
        x, y = n
        for i in range(4):
            hh = y + dh[i]
            ww = x + dw[i]
            if (0 <= ww < N) and (0 <= hh < N):
                if not visited[hh][ww]:
                    fish = graph[hh][ww]
                    visited[hh][ww] = True
                    if fish <=  size:
                        d += 1
                        q.append(((ww, hh), d))
                        if 0 < fish < size:
                            eatables.append(((ww, hh), d))
                            stop = d
                        d -= 1
    if eatables:
        return min(eatables, key=lambda x:x[0][1])
    else:
        return start, -1
                

def answer(start):
    size = 2
    grow = 0
    dist = 0 
    while True:
        visited = [[False for _ in range(N)] for _ in range(N)]
        n, d = eatFish(start, size, visited)
        if d == -1:
            return dist 
        else:
            graph[start[1]][start[0]] = 0
            graph[n[1]][n[0]] = 9 
            start = n
            dist += d
            grow += 1 
            if grow == size:
                size += 1
                grow = 0

dw = [0, -1, 1, 0]
dh = [-1, 0, 0, 1]

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    
start = (0,0) 
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            start = (j, i)
            
print(answer(start))