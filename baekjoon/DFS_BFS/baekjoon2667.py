#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 13:38:16 2022

@author: sangyoon
"""

import sys 
from collections import deque

N = int(sys.stdin.readline())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))
    

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    
    cnt = 1
    
    while queue:
        
        a, b = queue.popleft()
        
        if a > 0: 
            if graph[a-1][b] == 1:
                cnt += 1
                graph[a-1][b] = 0
                queue.append((a-1, b))
                
        if b > 0:
            if graph[a][b-1] == 1:
                cnt += 1
                graph[a][b-1] = 0
                queue.append((a, b-1))
                
        if a < N-1:
            if graph[a+1][b] == 1:
                cnt += 1
                graph[a+1][b] = 0
                queue.append((a+1, b))
                
        if b < N-1:
            if graph[a][b+1] == 1:
                cnt += 1
                graph[a][b+1] = 0
                queue.append((a, b+1))
                
    return cnt

count = 0
house_cnt = []
for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            house_cnt.append(BFS(x, y))
            count += 1

house_cnt.sort()
            
print(count)
for i in house_cnt:
    print(i)