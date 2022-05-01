# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 18:47:01 2022

@author: USER
"""

import heapq

graph = []
visited = []
dist = []
isTrap = []

def trap(graph, n):
    N = len(graph)
    new = [[] for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in graph[i]:
            if i == n:
                new[j[0]].append([n, j[1]])
            else:
                if j[0] == n:
                    new[n].append([i, j[1]])
                else:
                    new[i].append(j[0], j[1])
                    
    return new

def dijkstra(graph, start):
    q = []
    heapq.heappush(q, (0, start))
    visited[start] = True
    while q:
        cost, cur = heapq.heappop(q)
        visited[cur] = True
        for n, c in graph[cur]:
            if isTrap[n]:
                graph = trap(graph, n)
            if not visited[n]:
                dist[n] = cost + c
                heapq.heappush(q, (dist[n], n))

def solution(n, start, end, roads, traps):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    dist = [0 for _ in range(n+1)]
    isTrap = [False for _ in range(n+1)]
    for i in traps:
        isTrap[i] = True
    for i in roads:
        graph[i[0]].append([i[1], i[2]])
    dijkstra(graph, start)
    answer = dist[end]
    
    return answer

n = 3
start = 1 
end = 3 
roads = [[1, 2, 2], [3, 2, 3]]
traps = [2]
print(solution(n, start, end, roads, traps))