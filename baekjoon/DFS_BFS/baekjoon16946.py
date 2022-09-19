#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:39:20 2022

@author: sangyoon
"""

from collections import deque
import sys 
input = sys.stdin.readline 

N, M = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False for _ in range(M)] for _ in range(N)]
cnts = [0]

graph = []
for _ in range(N):
    graph.append(input().strip())
    
labels = [[0 for _ in range(M)] for _ in range(N)]

def BFS(start):
    q = deque([start])
    visited[start[0]][start[1]] = True
    cnt = 0
    
    while q:
        x, y = q.popleft()
        labels[x][y] = label
        cnt += 1 
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            
            if 0 <= xx < N and 0 <= yy < M:
                if not visited[xx][yy] and graph[xx][yy] == "0":
                    q.append([xx, yy]) 
                    visited[xx][yy] = True
                    
    cnts.append(cnt)
            

label = 1

for i in range(N):
    for j in range(M):
        if graph[i][j] == "0" and not visited[i][j]:
            BFS([i, j])
            label += 1
            

for i in range(N):
    for j in range(M):
        if labels[i][j] != 0:
            print(0, end="")
        else:
            ans = 1
            check = 0
            for k in range(4):
                xx = i + dx[k]
                yy = j + dy[k]
                if 0 <= xx < N and 0 <= yy < M and not check & (1 << labels[xx][yy]):
                    ans += cnts[labels[xx][yy]]
                    check += (1 << labels[xx][yy])
            print(ans, end="")
    print() 