#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:14:07 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

class TreeNode():
    data = None
    parent = None 
    childs = []
    
    def __init__(self, data, parent = None):
        self.data = data
        self.parent = parent
        
def makeTree(cur):
    for i in graph[cur.data]:
        if not visited[i]:
            new_node = TreeNode(i, cur)
            cur.childs.append(new_node)
            visited[i] = True
            makeTree(new_node)
            
def postOrder(cur):
    global cnt 
    
    for child in cur.childs:
        postOrder(child)
        
    cnt += 1 
    answer[cur.data] = cnt

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(N+1)]
root_node = TreeNode(R)
visited[R] = True 

makeTree(root_node)

answer = [0 for _ in range(N+1)]

cnt = 0

print(root_node.data)
for i in root_node.childs:
    print(i.data)
    
print(graph)
#postOrder(root_node)

#for i in range(Q):
#    print(answer[int(input())])