#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 12:40:56 2022

@author: sangyoon
"""

import sys 
from collections import deque 

input = sys.stdin.readline 

def bfs(start):
    q = deque([start])
    
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[start[0]][start[1]] = True
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            
            if 0 <= xx < R and 0 <= yy < C:
                if not visited[xx][yy] and graph[xx][yy] != 'X':
                    if graph[xx][yy] == 'L':
                        return True
                    q.append([xx, yy])
                    visited[xx][yy] = True
                    
    return False

                    

R, C = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []

for _ in range(R):
    graph.append(input().strip())
    
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'L':
            swan = [i, j]
    
time = 0

melt = []

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'X':
            for k in range(4):
                xx = i + dx[k]
                yy = j + dy[k]
                
                if 0 <= xx < R and 0 <= yy < C:
                    if graph[xx][yy] == '.':
                        melt.append([i,j])
                        break
    
while True:
    if bfs(swan):
        print(time)
        break 
    
                        
    for i, j in melt:
        graph[i] = graph[i][:j] + '.' + graph[i][j+1:]
        
    melt_next = []
    
    for _ in range(len(melt)):
        i, j = melt.pop()
        for k in range(4):
            xx = i + dx[k]
            yy = j + dy[k]
            
            if 0 <= xx < R and 0 <= yy < C:
                if graph[xx][yy] == 'X':
                    melt_next.append([xx, yy])
    
    melt = melt_next
                
    for i in graph:
        print(i)
    print()
                
    time += 1