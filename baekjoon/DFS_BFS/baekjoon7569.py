#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 21:46:44 2022

@author: sangyoon
"""

import sys 
from collections import deque 
input = sys.stdin.readline

def BFS(start):
    d = 0 
    q = deque()
    for i in start:
        q.append((i, d))
    while q:
        node, d = q.popleft()
        m,n,h = node
        for i in range(6):
            mm = m + dm[i]
            nn = n + dn[i]
            hh = h + dh[i]
            if 0 <= mm < M  and 0 <= nn < N and 0 <= hh < H:
                if graph[hh][nn][mm] == 0:
                    q.append(((mm, nn, hh), d+1))
                    graph[hh][nn][mm] = 1 
    return d
        

M, N, H = map(int, input().split())
graph = [[] for _ in range(H)]

for h in range(H):
    for _ in range(N):
        graph[h].append(list(map(int, input().split())))

dm = [1,-1,0,0,0,0]
dn = [0,0,-1,1,0,0]
dh = [0,0,0,0,-1,1]
        
start = []

for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 1:
                start.append((m, n, h))

day = BFS(start)
isDone = True 

for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 0:
                isDone = False 
                
if isDone:
    print(day)
else:
    print(-1)