#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 14:38:10 2022

@author: sangyoon
"""
from collections import deque

computers = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    graph.append(list(map(int, input().split())))
    
    
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        start = queue.popleft()
        for edge in graph:
            if edge[0] == start and not visited[edge[1]]:
                queue.append(edge[1])
                visited[edge[1]] = True 
                
            if edge[1] == start and not visited[edge[0]]:
                queue.append(edge[0])
                visited[edge[0]] = True 
        
answer = 0
visited = [False] * (computers + 1)

bfs(graph, 1, visited)


for i in visited:
    if i:
        answer+=1
        
print(answer - 1)