#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 16:02:03 2022

@author: sangyoon
"""

from collections import deque
import sys 
input = sys.stdin.readline 

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
    visited = [[False for _ in range(w)] for _ in range(h)]
    visited[start[0]][start[1]] = True
    
    if graph[start[0]][start[1]] == '#':
        q = deque([[0, 1, start]])
    else:
        q = deque([[0, 0, start]])
    
    while q:
        cnt, door, cur = q.popleft()
        x, y = cur 
        
        if cnt == 2:
            return door
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            
            if 0 <= xx < h and 0 <= yy < w:
                if not visited[xx][yy] and graph[xx][yy] != '*':
                    visited[xx][yy] = True
                    
                    if graph[xx][yy] == '#':
                        q.append([cnt, door+1, [xx, yy]])
                    elif graph[xx][yy] == '.':
                        q.appendleft([cnt, door, [xx, yy]])
                    elif graph[xx][yy] == '$':
                        q.appendleft([cnt+1, door, [xx, yy]])
                    
    

for _ in range(T):

    h, w = map(int, input().split())
    
    graph = [] # '.' : plain, '*' : wall, '#' : door, '$' : prisoner
    
    ans = []
    
    for _ in range(h):
        graph.append(input().strip())
        
    for i in range(h):
        for j in range(w):
            if i == 0 or i == h-1 or j == 0 or j == w-1:
                if graph[i][j] != '*':
                    ans.append(bfs([i, j]))
                    
    print(min(ans))