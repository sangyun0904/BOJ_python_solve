#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 15:31:02 2022

@author: sangyoon
"""

import sys 
from collections import deque
from itertools import combinations
input = sys.stdin.readline 

def BFS(start, g):
    queue = deque()
    queue.append(start)
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= yy < N and 0 <= xx < M:
                if g[yy][xx] == 0:
                    g[yy][xx] = 2
                    queue.append([yy, xx])
                    

graph = []
N, M = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    graph.append(list(map(int, input().split())))
    
blanks = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            blanks.append([i, j])
            
answer = 0
            
for walls in list(combinations(blanks, 3)):
    g = []
    for i in graph:
        g.append(list(i))
    
    for w in walls:
        g[w[0]][w[1]] = 1 
        
    
    for i in range(N):
        for j in range(M):
            if g[i][j] == 2:
                BFS([i, j], g)

    temp = 0
    for i in g:
        for j in i:
            if j == 0:
                temp += 1 
    
    if temp > answer:
        answer = temp
        

print(answer)