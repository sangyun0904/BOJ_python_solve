#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 19:13:32 2022

@author: sangyoon
"""

from collections import deque
import sys 

input = sys.stdin.readline 

N, M = map(int, input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
    
air_cnt = [[0 for _ in range(M)] for _ in range(N)]

time = 0 

while True:
    cheese = 0
    is_outside = [[0 for _ in range(M)] for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                if is_outside[i][j] == 0:
                    visited = [[False for _ in range(M)] for _ in range(N)]
                    q = deque([[i, j]])
                    
                    isOut = False
                    
                    while q:
                        x, y = q.popleft()
                        
                        if x in [0, N-1] or y in [0, M-1]:
                            isOut = True 
                        
                        for k in range(4):
                            xx = x + dx[k]
                            yy = y + dy[k]
                            
                            if 0 <= xx < N and 0 <= yy < M:
                                if not visited[xx][yy] and board[xx][yy] == 0:
                                    q.append([xx,yy])
                                    visited[xx][yy] = True
                                    
                    for a in range(N):
                        for b in range(M):
                            if visited[a][b]:
                                if isOut:
                                    is_outside[a][b] = 1
                                else:
                                    is_outside[a][b] = -1
                    
                                    
                        
                
                air_cnt[i][j] = 0 
            else:
                cheese += 1
                cnt = 0
                
                for k in range(4):
                    xx = i + dx[k]
                    yy = j + dy[k]
                    
                    if 0 <= xx < N and 0 <= yy < M:
                        if is_outside[xx][yy] == 1:
                            cnt += 1 
                            
                air_cnt[i][j] = cnt 
                
    if cheese == 0:
        break
                
    for i in range(N):
        for j in range(M):
            if air_cnt[i][j] >= 2:
                board[i][j] = 0
                
    time += 1 
    
print(time)                        
                