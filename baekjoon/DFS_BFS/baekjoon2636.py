#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 14:30:29 2022

@author: sangyoon
"""

import sys 
from collections import deque
input = sys.stdin.readline 

def findEdge(start):
    melt = []
    queue = deque([start])
    
    isOutside = False
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = dx[i] + x 
            yy = dy[i] + y 
            if 0 <= xx < M and 0 <= yy < N:
                if not visited[yy][xx]:
                    if graph[yy][xx] == 0:
                        visited[yy][xx] = True
                        queue.append([xx, yy])
                    elif graph[yy][xx] == 1:
                        visited[yy][xx] = True
                        melt.append([xx, yy])
                    else:
                        visited[yy][xx] = True
                        isOutside = True
                        queue.append([xx, yy])
    if isOutside:
        return melt 
    else:
        return []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
for i in range(N):
    for j in range(M):
        if i == 0 or i == N-1 or j == 0 or j == M-1:
            graph[i][j] = 2 
            
last = 0
hour = 0 
while True:   
    hour += 1
    melt = [] 
    visited = [[False for _ in range(M)] for _ in range(N)]      
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 1:
                melt.extend(findEdge([j, i]))
    if melt == []:
        break
    last = len(melt)
    for loc in melt:
        graph[loc[1]][loc[0]] = 0 
    
print(hour-1)
print(last)