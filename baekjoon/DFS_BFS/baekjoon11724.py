#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 15:19:08 2022

@author: sangyoon
"""

import sys 
from collections import deque 
input = sys.stdin.readline 

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
ans = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, N+1):
    if not visited[i]:
        q = deque() 
        q.append(i)
        while q:
            cur = q.popleft() 
            for j in graph[cur]:
                if not visited[j]:
                    visited[j] = True 
                    q.append(j) 
        ans += 1 
        
print(ans)