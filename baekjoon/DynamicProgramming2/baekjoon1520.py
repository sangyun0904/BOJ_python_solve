#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 20:57:17 2022

@author: sangyoon
"""

import sys 
import heapq
input = sys.stdin.readline 

N, M = map(int, input().split())

graph = []
memo = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

for _ in range(N):
   graph.append(list(map(int, input().split())))
    
start = (0,0)

queue = []

queue.append([-graph[0][0], start])
memo[0][0] = 1
visited[0][0] = True

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while queue:
    level, cur = heapq.heappop(queue)
    level = -level 
    
    if cur[0] == M-1 and cur[1] == N-1:
        break
    
    for i in range(4):
        xx = cur[0] + dx[i]
        yy = cur[1] + dy[i]
        
        if 0 <= xx < M and 0 <= yy < N:
            if graph[yy][xx] < level:
                memo[yy][xx] += memo[cur[1]][cur[0]]
                if not visited[yy][xx]:
                    heapq.heappush(queue, [-graph[yy][xx], (xx, yy)])
                    visited[yy][xx] = True
                
print(memo[-1][-1])