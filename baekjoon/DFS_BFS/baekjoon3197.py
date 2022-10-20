#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 12:40:56 2022

@author: sangyoon
"""

import sys 
from collections import deque 

input = sys.stdin.readline 

def find_swan(q):
    next_q = deque()
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            
            if 0 <= xx < R and 0 <= yy < C:
                if not visited[xx][yy]: 
                    if graph[xx][yy] != 'X':
                        if graph[xx][yy] == 'L':
                            return True, q
                        q.append([xx, yy])
                    else:
                        next_q.append([xx, yy])
                    visited[xx][yy] = True
                    
                    
    return False, next_q


def melt(water):
    R = len(graph)
    C = len(graph[0])
    next_water = deque() 
    
    while water:
        cur = water.popleft() 
        x = cur[0]
        y = cur[1]
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            
            if 0 <= xx < R and 0 <= yy < C:
                if graph[xx][yy] == "X":
                    graph[xx][yy] = "."
                    next_water.append([xx, yy])
                    
    return next_water


def start():
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'L':
                visited[i][j] = True 
                return deque([[i, j]])
        

                    

R, C = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False for _ in range(C)] for _ in range(R)]

graph = []

for _ in range(R):
    graph.append(list(input().strip()))
    
q = start()

time = 0

water = deque()

for i in range(R):
    for j in range(C):
        if graph[i][j] == '.' or graph[i][j] == 'L':
            water.append([i,j])
    
while True:
    
    print(q)
    
    meet, q = find_swan(q)
    
    if meet:
        print(time)
        break 
    
                        
    water = melt(water)
    for i in graph:
        print(i)
    print()
                
    time += 1