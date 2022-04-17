#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 12:28:59 2022

@author: sangyoon
"""

import sys 
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in graph:
    i.sort()
    
visited = [False] * (N+1)

def DFS(current):
    
    visited[current] = True 
    print(current, end=" ")
    
    for i in graph[current]:
        if not visited[i]:
            DFS(i)
            
    return

def BFS(start):
    visited = [False] * (N+1)
    visited[start] = True
    
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        print(current, end=" ")
        for i in graph[current]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

DFS(V)
print()
BFS(V)