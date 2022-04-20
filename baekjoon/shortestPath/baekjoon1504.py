#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:44:20 2022

@author: sangyoon
"""

import sys
import heapq 

INF = sys.maxsize

def dijkstra(start):
    dist[start] = 0 
    q = []
    
    heapq.heappush(q, (0, start))
    
    while q:
        cost, now = heapq.heappop(q)
        for i in graph[now]:
            temp = cost + i[1]
            if temp < dist[i[0]]:
                dist[i[0]] = temp 
                heapq.heappush(q, (temp, i[0]))

input = sys.stdin.readline 

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
v1, v2 = map(int, input().split())
dist = [INF] * (N+1)
dijkstra(v1)
v_dist = dist[v2]
    
dist = [INF] * (N+1)
dijkstra(1)
ans = [dist[v1], dist[v2]]
dist = [INF] * (N+1)
dijkstra(N)
ans[0] = ans[0] + dist[v2]
ans[1] = ans[1] + dist[v1]

if min(ans) + v_dist >= INF:
    print(-1)
else:
    print(min(ans) + v_dist)
