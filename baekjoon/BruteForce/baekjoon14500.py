#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 13:38:56 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

techs = [[(0,0), (0,1), (0,2), (0,3)], [(0,0), (1,0), (2,0), (3,0)],
         [(0,0), (0,1), (1,0), (1,1)], [(0,0), (0,1), (0,2), (1,2)],
         [(0,0), (0,1), (0,2), (-1,2)], [(0,0), (0,1), (1,0), (2,0)],
         [(0,0), (1,0), (2,0), (2,1)], [(0,0), (0,1), (1,1), (1,2)],
         [(0,0), (0,1), (-1,1), (-1,2)], [(0,0), (1,0), (1,1), (2,1)],
         [(0,0), (1,0), (1,-1), (2,-1)], [(0,0), (1,0), (1,1), (2,0)],
         [(0,0), (1,0), (1,-1), (1,1)], [(0,0), (1,0), (1,-1), (2,0)],
         [(0,0), (0,1), (1,1), (0,2)], [(0,0), (0,1), (1,1), (2,1)],
         [(0,0), (1,0), (2,0), (2,-1)], [(0,0), (1,0), (0,1), (0,2)], 
         [(0,0), (1,0), (1,1), (1, 2)]]

N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))
    
ans = 0
    
for i in range(N):
    for j in range(M):
        for t in techs:
            temp = 0
            for k in range(4):
                xx = j + t[k][0]
                yy = i + t[k][1]
                if 0 <= xx < M and 0 <= yy < N:
                    temp += board[yy][xx]
                else:
                    break 
            if temp > ans:
                ans = temp 
                
print(ans)