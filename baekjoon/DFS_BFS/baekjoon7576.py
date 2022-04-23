#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 20:50:22 2022

@author: sangyoon
"""

import sys 
from collections import deque
input = sys.stdin.readline 

def BFS(start):
    d = 0
    q = deque()
    for i in start:
        q.append((i, 0))
        visited[i[1]][i[0]] = True
    
    while q:
        n, d = q.popleft()
        x, y = n
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < M:
                if graph[yy][xx] == 0:
                    q.append(((xx, yy), d+1))
                    graph[yy][xx] = 1
    return d

            
N, M = map(int, input().split())

graph = []
for _ in range(M):
    graph.append(list(map(int, input().split())))
    
visited = [[False for _ in range(N)] for _ in range(M)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

first = []

for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            first.append((j, i))

day = BFS(first)

isDone = True 

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            isDone = False
            
if isDone:
    print(day)
else:
    print(-1)