#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 16:34:38 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N = int(input())

graph = [[] for _ in range(N+1)]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
answer = 0 

def DFS(node, dist, visited):
    global  answer
    
    if dist > answer:
        answer = dist
        
    for i in graph[node]:
        n, d = i
        if not visited[n]:
            visited[n] = True
            DFS(n, dist+d, visited)

for _ in range(N):
    data = list(map(int, input().split()))
    node = data[0]
    l = len(data) - 2 
    
    for i in range(l // 2):
        graph[node].append([data[i*2+1], data[i*2+2]])

for i in range(1, N):
    visited = [False for _ in range(N+1)]
    visited[i] = True
    DFS(i, 0, visited)
    
print(answer)