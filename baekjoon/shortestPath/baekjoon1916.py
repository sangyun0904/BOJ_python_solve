# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 15:17:54 2022

@author: USER
"""

import sys 
import heapq 

input = sys.stdin.readline 
INF = sys.maxsize

N = int(input())
M = int(input())

bus = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    bus[a].append((b, cost))
    
start, end = map(int, input().split())

q = [(0, start)]
dist = [INF for _ in range(N+1)]
dist[start] = 0

while q:
    newCost, cur = heapq.heappop(q)
    
    if newCost > dist[cur]:
        continue 
    
    else:
        for i in bus[cur]:
            
            d = newCost + i[1]
            
            if dist[i[0]] > d:
                dist[i[0]] = d 
                heapq.heappush(q, (d, i[0]))

print(dist[end])