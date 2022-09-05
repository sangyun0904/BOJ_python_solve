#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 11:29:51 2022

@author: sangyoon
"""

import sys 
from collections import deque
input = sys.stdin.readline 

R, C = map(int, input().split())

graph = []
for _ in range(R):
    graph.append(input().strip())
    
N = int(input())

heights = list(map(int, input().split()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def throw(direction, height):
    height = -height
    for i in range(C):
        if direction == "left":
            if graph[height][i] == "x":
                graph[height] = graph[height][:i] + "." + graph[height][i+1:]
                break
        else:
            if graph[height][C-i-1] == "x":
                graph[height] = graph[height][:C-i-1] + "." + graph[height][C-i:]
                break


def bfs(start, visited, ground):
    q = deque([start])
    ret = [start]
    visited[start[0]][start[1]] = True
    isGround = False
    
    while q:
        x, y = q.popleft()
        
        if x == R-1:
            isGround = True
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            
            if 0 <= xx < R and 0 <= yy < C:
                if not visited[xx][yy] and graph[xx][yy] == "x":
                    q.append([xx, yy])
                    ret.append([xx, yy])
                    visited[xx][yy] = True 
                    
    if isGround:
        for x, y in ret:
            ground[x][y] = True
        return []
    else:            
        return ret

def find_cluster(ground):
    clusters = []
    visited = [[False for _ in range(C)] for _ in range(R)]
    
    for i in range(R):
        for j in range(C):
            if graph[i][j] == "x" and not visited[i][j]:
                cluster= bfs([i, j], visited, ground)
                clusters.append(cluster)
                
    return clusters


def fall():
    ground = [[False for _ in range(C)] for _ in range(R)]
    clusters = find_cluster(ground)
    
    for clus in clusters:
        
        if clus == []:
            continue
        
        isFall = True
        clus.sort(key=lambda x : -x[0])
        
        while isFall:
            checked = [False for _ in range(100)]
            next_clus = []
            
            for i in clus:
                x, y = i 
                graph[x] = graph[x][:y] + "." + graph[x][y+1:]
                graph[x+1] = graph[x+1][:y] + "x" + graph[x+1][y+1:]
                next_clus.append([x+1, y])
                if not checked[y]:
                    if x+2 == R:
                        isFall = False 
                    elif ground[x+2][y]:
                        isFall = False 
                    else:
                        checked[y] = True
            
            clus = next_clus

                    
            
            
for i in range(N):
    if i % 2 == 0:
        throw("left", heights[i])
    else:
        throw("right", heights[i])
        
    fall()
              
for i in graph:
    print(i)