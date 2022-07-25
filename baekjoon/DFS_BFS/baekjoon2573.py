# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 10:15:45 2022

@author: USER
"""

import sys 
from collections import deque
input = sys.stdin.readline 

N , M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ice = 1 
year = 0

while ice == 1:
    year += 1
    melt = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                cnt = 0
                for n in range(4):
                    xx = dx[n] + j
                    yy = dy[n] + i
                    if 0 <= xx < M and 0 <= yy < N:
                        if board[yy][xx] == 0:
                            cnt += 1
                melt[i][j] = cnt 
                
    for i in range(N):
        for j in range(M):
            meltedIce = board[i][j] - melt[i][j]
            if meltedIce < 0:
                board[i][j] = 0
            else:
                board[i][j] = meltedIce
        
    ice = 0 
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and not visited[i][j]:
                ice += 1
                queue = deque([[j, i]])
                while queue:
                    x, y = queue.popleft() 
                    for n in range(4):
                        xx = dx[n] + x
                        yy = dy[n] + y
                        if 0 <= xx < M and 0 <= yy < N:
                            if board[yy][xx] != 0 and not visited[yy][xx]:
                                queue.append([xx, yy])
                                visited[yy][xx] = True 
                            
if ice == 0:
    print(0)    
else:
    print(year)                
                
                
                
                
                
                
                
                
                
                
                