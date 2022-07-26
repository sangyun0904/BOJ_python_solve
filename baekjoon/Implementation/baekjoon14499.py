#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:59:33 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N, M, y, x, K = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

dice = [0, [0,0,0,0], 0]
move = [[], [1,0], [-1,0], [0,-1], [0,1]]
current = (x, y)

commands = list(map(int, input().split()))

for c in commands:
    xx = current[0] + move[c][0]
    yy = current[1] + move[c][1]
    
    if xx < 0 or yy < 0 or xx >= M or yy >= N:
        continue
    
    current = (xx, yy)
    
    if c == 1:
        temp = dice[0] 
        dice[0] = dice[1][3]
        dice[1][3] = dice[2]
        dice[2] = dice[1][1]
        dice[1][1] = temp
    elif c == 2:
        temp = dice[1][1]
        dice[1][1] = dice[2]
        dice[2] = dice[1][3]
        dice[1][3] = dice[0]
        dice[0] = temp
    elif c == 3:
        dice[1] = dice[1][1:] + [dice[1][0]]
    else:
        dice[1] = [dice[1][-1]] + dice[1][:-1]
        
    if board[current[1]][current[0]] == 0:
        board[current[1]][current[0]] = dice[1][3]
    else:
        dice[1][3] = board[current[1]][current[0]]
        board[current[1]][current[0]] = 0      
          
    print(dice[1][1])
        
        