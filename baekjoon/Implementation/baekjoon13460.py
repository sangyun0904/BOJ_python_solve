#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 12:23:36 2022

@author: sangyoon
"""

from collections import deque
import sys 
input = sys.stdin.readline 

N, M = map(int, input().split())

board = []

for i in range(N):
    board.append(input().strip())
    
red, blue = [], []

for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            red = [i, j]
        if board[i][j] == "B":
            blue = [i, j]
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([[0, red, blue]])

def bfs(q):
    while True:
        dim, rloc, bloc = q.popleft()
        rx, ry = rloc 
        bx, by = bloc
        
        if dim == 10: 
            return -1
        
        for i in range(4):
            rmove = 0
            bmove = 0
            rxx = rx + dx[i]
            ryy = ry + dy[i]
            while True:
                if board[rxx][ryy] == "#" or board[rxx][ryy] == "O":
                    break 
                rxx = rxx + dx[i]
                ryy = ryy + dy[i]
                rmove += 1
            
            bxx = bx + dx[i]
            byy = by + dy[i]
            while True:
                if board[bxx][byy] == "#" or board[bxx][byy] == "O":
                    break 
                bxx = bxx + dx[i]
                byy = byy + dy[i]
                bmove += 1 
                
            if board[bxx][byy] == "O":
                continue
                
            if board[rxx][ryy] == "O":
                return dim + 1
            
                
            if rxx == bxx and ryy == byy:
                if rmove > bmove:
                    rxx -= dx[i]
                    ryy -= dy[i]
                else:
                    bxx -= dx[i]
                    byy -= dy[i]

            rxx -= dx[i]
            ryy -= dy[i]
            bxx -= dx[i]
            byy -= dy[i]
            q.append([dim+1, [rxx, ryy], [bxx, byy]])
    return -1
                
                    
ans = bfs(q)
print(ans)            
            

















            
            
            
            