#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 13:06:36 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

INF = sys.maxsize
N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
answer = INF
start = 0
    
def TSP(bm, dist, node, depth):
    global answer
    
    if bm == 2 ** N - 1 and node == start:
        if dist < answer:
            answer = dist
    
    for i in range(N):
        if graph[node][i] != 0 and not bm & (1<<i):
            TSP(bm + (1<<i), dist + graph[node][i], i, depth+1)

            
TSP(0, 0, start, 0)
            
print(answer)