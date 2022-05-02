# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 18:47:01 2022

@author: USER
"""

import heapq

INF = int(1e9)
    
def solution(n, start, end, roads, traps):
    answer = 0
    graph = [[] for _ in range(n+1)]
    reverse_graph = [[] for _ in range(n+1)]
    dist = [INF for _ in range(n+1)]
    isTrap = [False for _ in range(n+1)]
    for i in traps:
        isTrap[i] = True
    for i in roads:
        graph[i[0]].append((i[1], i[2]))
    for i in roads:
        reverse_graph[i[1]].append((i[0], i[2]))
        
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        cost, cur = heapq.heappop(q)
        print(dist)
        if dist[cur] < cost:
            continue
        if isTrap[cur]:
            for i in reverse_graph[cur]:
                if cost + i[1] < dist[i[0]]:
                    dist[i[0]] = cost + i[1]
                    heapq.heappush(q, (cost + i[1], i[0]))
        else:
            for i in graph[cur]:
                if cost + i[1] < dist[i[0]]:
                    dist[i[0]] = cost + i[1]
                    heapq.heappush(q, (cost + i[1], i[0]))
        
    answer = dist[end]
    
    return answer

n = 3
start = 1 
end = 3 
roads = [[1, 2, 2], [3, 2, 3]]
traps = [2]
print(solution(n, start, end, roads, traps))