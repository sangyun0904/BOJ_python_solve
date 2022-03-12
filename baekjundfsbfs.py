#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 17:05:33 2022

@author: sangyoon
"""

from collections import deque 

nodes, edges, start = map(int, input().split()) 

graph = []
for i in range(edges):
    graph.append(list(map(int, input().split())))

def dfs(graph, start, visited):
    visited[start] = True 
    print(start, end=" ")
    for edge in graph:
        if edge[0] == start and not visited[edge[1]]:
            dfs(graph, edge[1], visited)

def bfs(graph, queue, visited):
    while queue:
        start = queue.popleft()
        print(start, end=" ")
        for edge in graph:
            if edge[0] == start and not visited[edge[1]]:
                queue.append(edge[1])
                visited[edge[1]] = True
            if edge[1] == start and not visited[edge[0]]:
                queue.append(edge[0])
                visited[edge[0]] = True
                
visited = [False] * (nodes + 1)
print("DFS :", end=" ")
dfs(graph, start, visited)
print()
queue = deque([start])
visited = [False] * (nodes + 1)
print("BFS :", end=" ")
bfs(graph, queue, visited)