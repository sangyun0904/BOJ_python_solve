#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 09:43:23 2022

@author: sangyoon
"""

import sys 
from collections import deque
input = sys.stdin.readline 


def findPath(start, target):
    visited = [False for _ in range(10000)] 
    queue = deque([(start, "")])
    
    while queue:
        node, p = queue.popleft()
        if node == target:
            return p
        
        newNode = int(str(node)[1:] + str(node)[0])
        if not visited[newNode]:
            visited[newNode] = True
            newPath = p + "L"
            queue.append([newNode, newPath])
        
        newNode = int(str(node)[-1] + str(node)[:-1])
        if not visited[newNode]:
            visited[newNode] = True
            newPath = p + "R"
            queue.append([newNode, newPath])
        
        newNode = (node * 2) % 10000
        if not visited[newNode]:
            visited[newNode] = True
            newPath = p + "D"
            queue.append([newNode, newPath])

        if node != 0:
            newNode = node - 1
        else:
            newNode = 9999
        if not visited[newNode]:
            visited[newNode] = True
            newPath = p + "S"
            queue.append([newNode, newPath])
          

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(findPath(a, b))
    
    