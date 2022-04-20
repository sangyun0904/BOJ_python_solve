#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 09:21:09 2022

@author: sangyoon
"""

import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
costs = [INF] * (V+1)

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

def dijkstra(start):
    costs[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        cost, node = heapq.heappop(q)
        for n, c in graph[node]:
            temp = cost + c
            if temp < costs[n]:
                costs[n] = temp
                heapq.heappush(q, (temp, n))

dijkstra(K)
for i in costs[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)
            
            