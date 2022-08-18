#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 16:07:12 2022

@author: sangyoon
"""

import sys 
from collections import deque 
input = sys.stdin.readline 

T = int(input())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

for _ in range(T):
    I = int(input())
    
    board = [[0 for _ in range(I)] for _ in range(I)]
    
    start = list(map(int, input().split()))
    target = list(map(int, input().split()))
    
    visited = [[False for _ in range(I)] for _ in range(I)]
    visited[start[0]][start[1]] = True 
    
    q = deque([[start, 0]])
    
    while q:
        cur, d = q.popleft()
        
        if cur == target:
            print(d)
            break
        
        for i in range(8):
            xx = cur[1] + dx[i]
            yy = cur[0] + dy[i]
            
            if 0 <= xx < I and 0 <= yy < I:
                if not visited[yy][xx]:
                    visited[yy][xx] = True 
                    q.append([[yy, xx], d+1])