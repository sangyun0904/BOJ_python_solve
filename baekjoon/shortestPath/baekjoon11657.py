#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:29:28 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 
INF = int(1e9)

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A-1].append([B, C])
    
distance = [INF for _ in range(N)]
    
def bellman_ford(graph, start):
    distance[start-1] = 0
    infinite = False
    
    for i in range(N):
        for j in range(N):
            for k in graph[j]:
                node, cost = k
                if distance[j] != INF and distance[node-1] > distance[j] + cost:
                    distance[node-1] = distance[j] + cost 
                    if i == N-1:
                        infinite = True
    return infinite

if bellman_ford(graph, 1):
    print(-1)
else:
    for dist in distance[1:]:
        if dist == INF:
            print(-1)
        else:
            print(dist)