#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 16:23:39 2022

@author: sangyoon
"""
from collections import deque
import sys 
input = sys.stdin.readline 

graph = []
for _ in range(8):
    graph.append(input().strip())

player = (0,7)
goal = (7,0)

dx = [-1,-1,-1,0,0,1,1,1,0]
dy = [-1,0,1,-1,1,-1,0,1,0]
visited = [[False for _ in range(8)] for _ in range(8)]

def solution(graph, player, goal):
    
    walls = [[False for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if graph[i][j] == "#":
                walls[i][j] = True
    
    q = deque()
    q.append(player)
    while q:
        now = q.popleft()
        if now == goal:
            return 1
        
        for i in range(9):
            xx = now[0] + dx[i]
            yy = now[1] + dy[i]
            if 0 <= xx < 8 and 0 <= yy <8:
                if (not walls[yy-1][xx]) and (not walls[yy][xx]):
                    if not visited[yy][xx]:
                        visited[yy][xx] = True
                        q.append((xx, yy))
        next_walls = [[False for _ in range(8)] for _ in range(8)] 
        for i in range(7):
            for j in range(8):
                if walls[i][j]:
                    next_walls[i+1][j] = True 
        walls = next_walls
        print(walls)
        
    return 0
        
print(solution(graph, player, goal))