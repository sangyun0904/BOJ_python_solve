#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:23:49 2022

@author: sangyoon
"""

from collections import deque
import sys 

input = sys.stdin.readline 

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    
indegree = [0 for _ in range(N+1)]
for i in graph:
    for j in i:
        indegree[j] += 1

q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        
while q:
    cur = q.popleft() 
    
    print(cur, end=" ")
    
    for i in graph[cur]:
        indegree[i] -= 1 
        
        if indegree[i] == 0:
            q.append(i)