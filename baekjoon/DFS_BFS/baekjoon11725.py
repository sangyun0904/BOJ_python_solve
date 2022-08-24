# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 15:37:24 2022

@author: USER
"""

import sys 
from collections import deque
input = sys.stdin.readline 

N = int(input())

graph = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b) 
    graph[b].append(a)
    
parent = [0 for _ in range(N+1)]

q = deque([1])
while q:
    node = q.popleft()
    for i in graph[node]:
        if i != 1 and parent[i] == 0:
            parent[i] = node 
            q.append(i)
            
for i in range(2, N+1):
    print(parent[i])