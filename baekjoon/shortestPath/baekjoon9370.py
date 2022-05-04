#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:48:59 2022

@author: sangyoon
"""

import sys 
import heapq
input = sys.stdin.readline 

INF = sys.maxsize

def dijkstra(s):
    q = []
    routes = [-1 for _ in range(n)]
    heapq.heappush(q, (0, s))
    while q:
        dist, now = heapq.heappop(q)
        
        for node, cost in graph[now-1]:
            temp = dist + cost
            if distance[node-1] > temp:
                heapq.heappush(q, (temp, node))
                distance[node-1] = temp
                routes[node-1] = now
    return routes

T = int(input())
for _ in range(T):
   
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    g_h = 0
    
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a-1].append((b, d))
        graph[b-1].append((a, d))
    candidates = []
    for _ in range(t):
        candidates.append(int(input()))
    
    distance = [INF for _ in range(n)]
    routes = dijkstra(s)
    for candid in candidates:
        cur = candid 
        while cur != s and cur != -1:
            cur = routes[cur-1]
            if cur in [g, h] and routes[cur-1] in [g, h]:
                print(candid, end=" ")
    print()
    
        