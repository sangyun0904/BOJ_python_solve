#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:14:07 2022

@author: sangyoon
"""

import sys 
from collections import deque 
input = sys.stdin.readline 

def makeTree(cur):
    for i in graph[cur]:
        if not visited[i]:
            visited[i] = True 
            TreeNodes[cur][-1].append(i)
            TreeNodes[i][0] = cur 
            makeTree(i)

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    
TreeNodes = [[0, []] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
visited[R] = True

makeTree(R)

visited = [False for _ in range(N+1)]
visited[0] = True
answer = [1 for _ in range(N+1)]

q = deque()
for i in range(1, N+1):
    if TreeNodes[i][-1] == []:
        q.append(i)
        visited[i] = True
        
while q:
    cur = q.popleft() 
    temp = 0 
    for i in TreeNodes[cur][-1]:
        temp += answer[i]
    parent = TreeNodes[cur][0]
    if not visited[parent]:
        q.append(parent)
        visited[parent] = True
    answer[cur] += temp 
    
for i in range(Q):
    print(answer[int(input())])