#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:11:32 2022

@author: sangyoon
"""

from collections import deque
import sys 
input = sys.stdin.readline 

R, C = map(int, input().split())
graph = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

pipes = {'|' : [0, 2], '-' : [1, 3], '+' : [0, 1, 2, 3], '1' : [2, 3],
         '2' : [0, 3], '3' : [0, 1], '4' : [1, 2]}

for _ in range(R):
    graph.append(input().strip())
    
M = []
Z = []

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'M':
            M = [i, j]
        if graph[i][j] == 'Z':
            Z = [i, j]
            
visited = [[False for _ in range(C)] for _ in range(R)]

q = deque([M, Z])
visited[M[0]][M[1]] = True 
visited[Z[0]][Z[1]] = True

ans_shape = []
ans_loc = []

while q:
    x, y = q.popleft() 
    
    if graph[x][y] in ['M', 'Z']:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            
            if 0 <= xx < R and 0 <= yy < C:
                if graph[xx][yy] != '.' and not visited[xx][yy]:
                    q.append([xx, yy])
                    visited[xx][yy] = True
            
    else:
        for i in pipes[graph[x][y]]:
            xx = x + dx[i]
            yy = y + dy[i]
            
            if 0 <= xx < R and 0 <= yy < C:
                if graph[xx][yy] != '.':
                    if not visited[xx][yy]:
                        q.append([xx, yy])
                        visited[xx][yy] = True
                else:
                    if ans_loc == []:
                        ans_loc = [str(xx+1), str(yy+1)]
                    ans_shape.append((i+2) % 4)
            
ans_shape.sort() 

print(" ".join(ans_loc), end=" ")
print(ans_shape)
for key, val in pipes.items():
    if val == ans_shape:
        print(key)