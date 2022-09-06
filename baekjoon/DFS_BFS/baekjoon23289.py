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
dx = [[], [-1, 0, 1], [-1, 0, 1], [-1, -1, -1], [1, 1, 1]]
dy = [[], [1, 1, 1], [-1, -1, -1], [-1, 0, 1], [-1, 0, 1]]

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
    
def warming(warmer, walls):
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
            
            room[x][y] += d 
            
            for i in range(3):
                xx = x + dx[direct][i]
                yy = y + dy[direct][i]
                
                if 0 <= xx < R and 0 <= yy < C:
                    if not visited[xx][yy]:
                        visited[xx][yy] = True
                        q.append([d-1, xx, yy])
            

warming(warmer, walls)

print(warmer)

for i in room:
    print(i)           
            
            
        