# -*- coding: utf-8 -*-
"""
Created on Thu May 26 10:52:54 2022

@author: USER
"""
import heapq
import sys 
input = sys.stdin.readline 
INF = sys.maxsize

n = int(input()) 
m = int(input())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1].append([b,c])
    
for i in range(n):
    dist = [INF for _ in range(n)]
    visited = [False for _ in range(n)]
    q = [(0, i+1)]
    dist[i] = 0
    while q:
        cost, now = heapq.heappop(q)
        visited[now-1] = True
        for j in graph[now-1]:
            if not visited[j[0]-1] and dist[j[0]-1] > cost + j[1]:
                dist[j[0]-1] = cost + j[1]
                heapq.heappush(q, (dist[j[0]-1], j[0])) 
                
    for d in dist:
        if d >= INF:
            print(0, end=" ")
        else:
            print(d, end=" ")
    print()