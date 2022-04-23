#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 20:16:52 2022

@author: sangyoon
"""

import sys 
from collections import deque 

input = sys.stdin.readline

def BFS(start):
    q = deque()
    q.append((start, 1))
    visited[0][0] = True
    
    while q:
        n, d = q.popleft()
        x, y = n
        if x == M-1 and y == N-1:
            return d
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < M and 0 <= yy < N:
                if graph[yy][xx] == "1" and not visited[yy][xx]:
                    q.append(((xx, yy), d+1))
                    visited[yy][xx] = True 
                    

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(input())

visited = [[False for _ in range(M)] for _ in range(N)]
   
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

print(BFS((0,0)))