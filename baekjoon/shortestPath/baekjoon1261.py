#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 12:54:45 2022

@author: sangyoon
"""

import sys 
import heapq 

input = sys.stdin.readline 

M, N = map(int, input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False for _ in range(M)] for _ in range(N)]

graph = []
for _ in range(N):
    graph.append(input().strip())
    
start = [0,0]

q = [[0, start]]

while q:
    bwall, cur = heapq.heappop(q)
    x, y = cur
    
    if cur == [N-1, M-1]:
        print(bwall)
        break
    
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        
        if 0 <= xx < N and 0 <= yy < M:
            if not visited[xx][yy]:
                visited[xx][yy] = True 
                if graph[xx][yy] == "0":
                    heapq.heappush(q, [bwall, [xx, yy]])
                else:
                    heapq.heappush(q, [bwall+1, [xx, yy]])
    