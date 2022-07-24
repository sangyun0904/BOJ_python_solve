#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 18:15:06 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 
from collections import deque

N = int(input())
K = int(input())

board = [[0 for _ in range(N+2)] for _ in range(N+2)]

for i in range(N+2):
    for j in range(N+2):
        if i == 0 or i == N+1 or j == 0 or j == N+1:
            board[i][j] = 1 
    
board[1][1] = 1
snake = deque([[1,1]])
direction = [0,1]

for _ in range(K):
    row, col = map(int, input().split())
    board[row][col] = 2 
    
L = int(input())
ans = 0
gameEnd = False

for _ in range(L):
    X, C = input().strip().split()
    X = int(X)
    while ans < X:
        ans += 1
        head = snake[-1]
        yy = head[0] + direction[0]
        xx = head[1] + direction[1]
        if board[yy][xx] == 0:
            snake.append([yy,xx])
            board[yy][xx] = 1 
            tail = snake.popleft()
            board[tail[0]][tail[1]] = 0 
        elif board[yy][xx] == 1:
            ans += 1 
            gameEnd = True
        else:
            snake.append([yy,xx])
            board[yy][xx] = 1
        if gameEnd:
            break 
        print(ans)
        for line in board:
            print(line)
        print()
        
    if gameEnd:
        break 
    else:
        if C == "D":
            if direction == [0,1]:
                direction = [1,0]
            elif direction == [1,0]:
                direction = [0,-1]
            elif direction == [0,-1]:
                direction = [-1,0]
            else:
                direction = [0,1]
        else:
            if direction == [1,0]:
                direction = [0,1]
            elif direction == [0,-1]:
                direction = [1,0]
            elif direction == [-1,0]:
                direction = [0,-1]
            else:
                direction = [-1,0]
    
print(ans)
                