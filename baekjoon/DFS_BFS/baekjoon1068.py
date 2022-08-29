#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 15:46:58 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N = int(input())

graph = [[] for _ in range(N)]

parents = list(map(int, input().split()))
R = int(input())
root = 0

for i in range(N):
    if parents[i] == -1:
        root = i
    else:
        graph[parents[i]].append(i)
    
q = [R]

while q:
    cur = q.pop()
    
    for i in graph[cur]:
        q.append(i)
    
    for i in graph:
        if cur in i:
            i.remove(cur)
        
    graph[cur] = [-1]
    
print(graph.count([]))