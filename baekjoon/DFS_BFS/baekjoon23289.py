#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 14:00:39 2022

@author: sangyoon
"""

from collections import deque
import sys 
input = sys.stdin.readline 

R, C, K = map(int, input().split())

room = []

for _ in range(R):
    room.append(list(map(int, input().split())))
    
warmer = [] # 1: right, 2: left, 3: up, 4: down
targets = []

for i in range(R):
    for j in range(C):
        if room[i][j] == 5:
            targets.append([i, j])
            room[i][j] = 0 
        elif room[i][j] != 0:
            warmer.append([room[i][j], i, j])
            room[i][j] = 0 
            
W = int(input())

walls = []

for _ in range(W):
    walls.append(list(map(int, input().split())))
    
walls_graph = [[[] for _ in range(C)] for _ in range(R)]

for w in walls:
    x, y, b = w 
    x -= 1
    y -= 1
    
    if b == 0:
        walls_graph[x][y].append([-1, 0])
        walls_graph[x-1][y].append([1, 0])
    else:
        walls_graph[x][y].append([0, 1])
        walls_graph[x][y+1].append([0, -1])
        
    
def warming(warmer, walls):
    dx = [[], [-1, 0, 1], [-1, 0, 1], [-1, -1, -1], [1, 1, 1]]
    dy = [[], [1, 1, 1], [-1, -1, -1], [-1, 0, 1], [-1, 0, 1]]
    
    for w in warmer:
        direct, start_x, start_y = w 
        
        visited = [[False for _ in range(C)] for _ in range(R)]
        
        if direct == 1:
            start_y += 1
        elif direct == 2:
            start_y -= 1 
        elif direct == 3:
            start_x -= 1
        else:
            start_x += 1
        
        q = deque([[5, start_x, start_y]])
        visited[start_x][start_y] = True
        
        while q:
            d, x, y = q.popleft()
            
            if d == 0:
                break
            
            room[x][y] += d 
            
            for i in range(3):
                dxi = dx[direct][i]
                dyi = dy[direct][i]
                xx = x + dxi
                yy = y + dyi
                
                if 0 <= xx < R and 0 <= yy < C:
                    if not visited[xx][yy]:
                        if dxi == 0 or dyi == 0:
                            if [dxi, dyi] not in walls_graph[x][y]:
                                q.append([d-1, xx, yy])
                                visited[xx][yy] = True
                        else:
                            if direct == 1 or direct == 2:
                                if [dxi, 0] not in walls_graph[x][y] and [0, dyi] not in walls_graph[xx][y]:
                                    q.append([d-1, xx, yy])
                                    visited[xx][yy] = True
                            else:
                                if [0, dyi] not in walls_graph[x][y] and [dxi, 0] not in walls_graph[x][yy]:
                                    q.append([d-1, xx, yy])
                                    visited[xx][yy] = True
                                    
def coordinate():
    temp_change = [[0 for _ in range(C)] for _ in range(R)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(R):
        for j in range(C):
            
            for k in range(4):
                dxk = dx[k]
                dyk = dy[k]
                
                xx = i + dx[k]
                yy = j + dy[k]
                
                if 0 <= xx < R and 0 <= yy < C:
                    if [dxk, dyk] not in walls_graph[i][j]:
                        if room[i][j] > room[xx][yy]:
                            temp = (room[i][j] - room[xx][yy]) // 4 
                            temp_change[i][j] -= temp 
                            temp_change[xx][yy] += temp
            
    for i in range(R):
        for j in range(C):
            room[i][j] += temp_change[i][j]
            

def cool():
    for i in range(R):
        for j in range(C):
            
            if i in [0, R-1] or j in [0, C-1]:
                if room[i][j] != 0:
                    room[i][j] -= 1
                    

def check_target():
    ret = True
    
    for t in targets:
        x, y = t 
        
        if room[x][y] < K:
            ret = False 
    
    return ret

choco = 0
            
while True:
    warming(warmer, walls)
    
    coordinate()
    
    cool()
    
    choco += 1
    
    if choco > 100:
        break
    
    if check_target():
        break
       
print(choco)            
            
        