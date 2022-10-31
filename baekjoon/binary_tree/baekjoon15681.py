#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:14:07 2022

@author: sangyoon
"""

import sys 
from collections import deque
input = sys.stdin.readline 

class TreeNode():
    data = None
    parent = None 
    childs = []
    
    def __init__(self, data, parent = None):
        self.data = data
        self.parent = parent

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(N+1)]
root_node = TreeNode(R)
visited[R] = True 

q = deque([R])

cur_node = root_node

while q:
    cur = q.popleft()
    
    new_node = TreeNode(cur, cur_node)
    
    for i in graph[cur]:
        if not visited[i]:
            visited[i] = True 
            q.append(i)