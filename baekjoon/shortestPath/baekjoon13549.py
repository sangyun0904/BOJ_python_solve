#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:22:47 2022

@author: sangyoon
"""
import heapq

N, K = map(int, input().split())
INF = int(1e9)
distance = [INF for _ in range(100000)]

def dijkstra(N, K):
    q = []
    heapq.heappush(q, (0, N))
    distance[N] = 0
    while q:
        c, n = heapq.heappop(q)
        
        if n == K:
            return c
        
        if n * 2 <= 100000:
            if distance[n * 2] > c:
                heapq.heappush(q, (c, n*2))
                distance[n*2] = c
        if n + 1 <= 100000:
            if distance[n + 1] > c + 1:
                heapq.heappush(q, (c+1, n+1))
                distance[n+1] = c+1
        if n - 1 >= 0:
            if distance[n - 1] > c + 1:
                heapq.heappush(q, (c+1, n-1))
                distance[n-1] = c+1
                
print(dijkstra(N, K))    