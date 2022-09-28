#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:50:52 2022

@author: sangyoon
"""

from collections import deque
import sys 
input = sys.stdin.readline 

N, M = map(int, input().split())

board = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(N):
    board.append(list(map(int, input().split())))
    
def group_size(start):
    visited = [[False for _ in range(N)] for _ in range(N)]
    
    q = deque([start])
    l = board[start[0]][start[1]]
    
    visited[start[0]][start[1]] = True
    cnt = 1
    blocks = [start]
    rainbow = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            xx = dx[i] + x 
            yy = dy[i] + y
            if 0 <= xx < N and 0 <= yy < N and not visited[xx][yy]:
                if board[xx][yy] in [0,l]:
                    visited[xx][yy] = True 
                    cnt += 1 
                    q.append([xx, yy])
                    if board[xx][yy] == 0:
                        rainbow += 1 
                    else:
                        blocks.append([xx, yy])
                        
    blocks.sort()
                    
    return cnt, rainbow, blocks[0]

def erase_group(start):
    q = deque([start])
    l = board[start[0]][start[1]]
    
    while q:
        x, y = q.popleft() 
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            
            if 0 <= xx < N and 0 <= yy < N and board[xx][yy] in [0, l]:
                board[xx][yy] = None 
                q.append([xx, yy])
                

def gravity():
    for i in range(N-2, -1, -1):
        for j in range(N):
            if board[i][j] != None and board[i][j] != -1:
                ii = i
                jj = j 
                while ii != N-1 and board[ii+1][j] == None:
                    temp = board[ii][jj]
                    board[ii][jj] = board[ii+1][j]
                    board[ii+1][j] = temp 
                    ii += 1
                    

def turn_board():
    temp = list(map(list, zip(*board)))
    ret = []
    for i in range(N-1, -1, -1):
        ret.append(temp[i])
    return ret

ans = 0

while True:
    groups = []
    standard_block = [[False for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if board[i][j] not in [-1, 0, None]:
                size, rainbow, block  = group_size([i,j])
                if size >= 2 and not standard_block[block[0]][block[1]]:
                    groups.append([size, rainbow, block])
                    standard_block[block[0]][block[1]] = True
    
    
    if len(groups):
        groups.sort()
        ans += groups[-1][0] ** 2
        erase_group(groups[-1][2])
        gravity()
        board = turn_board()
        gravity()
    else:
        break
        
        
print(ans)
            