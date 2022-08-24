# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 20:32:33 2022

@author: USER
"""

import sys 
from collections import deque
input = sys.stdin.readline 

N, K = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))
    
virus = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            virus.append([graph[i][j], i, j, 0])
            
virus.sort()
q = deque(virus)
    
S, X, Y = map(int, input().split())

while q:
    v, x, y, t = q.popleft()
    
    if t == S:
        break
    
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        
        if 0 <= xx < N and 0 <= yy < N:
            if graph[xx][yy] == 0:
                graph[xx][yy] = v 
                q.append([v, xx, yy, t+1])
                
                    
print(graph[X-1][Y-1])                        