#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 15:46:20 2022

@author: sangyoon
"""

import sys
from collections import deque
input = sys.stdin.readline 

K = int(input())

for _ in range(K):
    V, E = map(int, input().split()) 
    
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
        
    visited = [False for _ in range(V+1)]
    colors = [-1 for _ in range(V+1)]
    
    isBipartite = True
    
    for n in range(1, V+1):
        if not visited[n]:
            
            queue = deque([[n, 1]])
            
            while queue:
                cur, depth = queue.popleft() 
                visited[cur] = True 
                
                if depth % 2 == 1:
                    colors[cur] = 1
                else:
                    colors[cur] = 0
            
                for i in graph[cur]:
                    if visited[i]:
                        if colors[i] == (depth % 2):
                            isBipartite = False
                    else:
                        queue.append([i, depth+1])
                        
                if not isBipartite:
                    break 
        
    if isBipartite:
        print("YES")
    else:
        print("NO")
                    
    
    