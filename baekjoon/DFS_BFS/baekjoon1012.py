#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 14:49:47 2022

@author: sangyoon
"""

import sys
from collections import deque

def BFS(x, y):
    queue = deque()
    
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        if x > 0:
            if ground[y][x-1] == 1:
                queue.append((x-1, y))
                ground[y][x-1] = 0
        if y > 0:
            if ground[y-1][x] == 1:
                queue.append((x, y-1))
                ground[y-1][x] = 0
        if x < M-1:
            if ground[y][x+1] == 1:
                queue.append((x+1, y))
                ground[y][x+1] = 0
        if y < N-1:
            if ground[y+1][x] == 1:
                queue.append((x, y+1))
                ground[y+1][x] = 0
    return

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    
    ground = [[0 for _ in range(M)] for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        ground[y][x] = 1 
    
    cnt = 0
    
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                BFS(j, i)
                cnt += 1
    
    print(cnt)