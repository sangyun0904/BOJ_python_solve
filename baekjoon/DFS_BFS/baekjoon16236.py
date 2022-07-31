#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 14:16:25 2022

@author: sangyoon
"""
import sys
from collections import deque

input = sys.stdin.readline

babySize = 2 
eat = 0

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))
    
momShark = False
ans = 0

def findFish(start):
    visited = [[False for _ in range(N)] for _ in range(N)]
    
    queue = deque([[start, 0]])
    visited[start[0]][start[1]] = True
    locs = []
    dist = 999
    
    while queue:
        yx, d = queue.popleft()
        y, x = yx
        
        if d+1 > dist:
            continue
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            
            if 0 <= xx < N and 0 <= yy < N and not visited[yy][xx]:
                
                if graph[yy][xx] == 0 or graph[yy][xx] == babySize:
                    visited[yy][xx] = True
                    queue.append([(yy,xx), d+1])
                elif graph[yy][xx] < babySize:
                    locs.append((xx,yy))
                    dist = d+1
                
    locs.sort(key=lambda x: (x[1], x[0]))
    
    if dist == 999:
        return True, [0,0], 0
    else:
        return False, locs[0], dist
    
while momShark == False:
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                momShark, newLoc, dist = findFish([i, j])
                if momShark == False:
                    eat += 1
                    if eat == babySize:
                        eat = 0 
                        babySize += 1
                    graph[i][j] = 0
                    x, y = newLoc 
                    graph[y][x] = 9
                    ans += dist
                    
print(ans)            
                    
            