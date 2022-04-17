#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:02:30 2022

@author: sangyoon
"""

import sys 

N, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    board.append(sys.stdin.readline())
    
ans = N * M 

for i in range(N+1-8):
    for j in range(M+1-8):
        ans_temp = 0
        for n in range(i, i+8):
            for m in range(j, j+8):
                if m % 2 == n % 2:
                    if board[n][m] != "B":
                        ans_temp += 1
                else:
                    if board[n][m] != "W":
                        ans_temp += 1
        if ans_temp < ans:
            ans = ans_temp
        ans_temp = 0
        for n in range(i, i+8):
            for m in range(j, j+8):
                if m % 2 == n % 2:
                    if board[n][m] != "W":
                        ans_temp += 1
                else:
                    if board[n][m] != "B":
                        ans_temp += 1
        if ans_temp < ans:
            ans = ans_temp
                
print(ans)   