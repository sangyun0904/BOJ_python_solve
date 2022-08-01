#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 16:33:39 2022

@author: sangyoon
"""

import sys 
from collections import deque
input = sys.stdin.readline 

INF = sys.maxsize

N, M = map(int, input().split())
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())

graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
    

for _ in range(N):
    graph.append(list(map(int, input().split())))
            
ans = INF
            
visited = [[[False, False] for _ in range(M)] for _ in range(N)]

queue = deque([[(Hx-1, Hy-1), 0, 0]])
visited[Hx-1][Hy-1][0] = True

while queue:
    cur, broke, d = queue.popleft() 
    y, x = cur
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        
        if 0 <= xx < M and 0 <= yy < N and not visited[yy][xx][broke]:
            if xx == Ey-1 and yy == Ex-1:
                if d+1 < ans:
                    ans = d+1
                
            elif graph[yy][xx] == 0:
                visited[yy][xx][broke] = True 
                queue.append([(yy, xx), broke, d+1])
            
            else:
                if broke == 0:
                    visited[yy][xx][1] = True 
                    queue.append([(yy,xx), 1, d+1])
                    
if ans == INF:
    print(-1)
else:
    print(ans)
                    