#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 14:33:50 2022

@author: sangyoon
"""
from collections import deque
import sys 
input = sys.stdin.readline

N, M = map(int, input().split())

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

graph = []

for _ in range(N):
    graph.append(input())
    
walls = []
    
for i in range(N):
    for j in range(M):
        if graph[i][j] == "1":
            walls.append([j, i])

def bfs(start):
    ans = []
    for w in walls:
        visited = [[False for _ in range(M)] for _ in range(N)]
        q = deque()
        q.append([start, 1])
        while q:
            now = q.popleft()
            visited[now[0][1]][now[0][0]] = True
            if now[0] == [M-1, N-1]:
                ans.append(now[1])
            for i in range(4):
                x = now[0][0] + dx[i]
                y = now[0][1] + dy[i]
                if 0 <= x < M and 0 <= y < N:
                    if (graph[y][x] == "0") or ([x, y] == w):
                        if not visited[y][x]:
                            q.append([[x, y], now[1]+1])
                        
    if ans == []:
        return -1
    else:
        return min(ans)
        
print(bfs([0,0]))