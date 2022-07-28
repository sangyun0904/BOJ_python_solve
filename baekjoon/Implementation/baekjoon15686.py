#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 14:21:22 2022

@author: sangyoon
"""

import sys 
from itertools import combinations 
input = sys.stdin.readline 

N, M = map(int, input().split())
INF = sys.maxsize
dx = [-1,1,0,0]
dy = [0,0,-1,1]

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))
    
chickens = []    

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chickens.append([i,j])
           
combis = list(combinations(chickens, M))

ans = INF

for comb in combis:
    
    chickenDist = 0
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                dist = 999 
                for ch in comb:
                    d = abs(i-ch[0]) + abs(j-ch[1])
                    if d < dist:
                        dist = d 
                chickenDist += dist
                
    if chickenDist < ans:
        ans = chickenDist 
    
        
print(ans)

                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    