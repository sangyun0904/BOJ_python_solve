#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 19:00:08 2022

@author: sangyoon
"""

import sys 
from collections import deque 
input = sys.stdin.readline 

W, H = map(int, input().split())

board = []
visited = [[False for _ in range(W)] for _ in range(H)]
mirorCnt = [[0 for _ in range(W)] for _ in range(H)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(H):
    board.append(input().strip())
    
ans = sys.maxsize
    
for i in range(H):
    for j in range(W):
        if board[i][j] == 'C':
            queue = deque([[(i, j), 0, -1]])
            visited[i][j] = True 
            
            while queue:
                cur, miror, d = queue.popleft() 
                y, x = cur 
                for k in range(4):
                    xx = x + dx[k]
                    yy = y + dy[k]
                    
                    if 0 <= xx < W and 0 <= yy < H and board[yy][xx] != "*" and (xx, yy) != (j, i):
                        if not visited[yy][xx] or miror <= mirorCnt[yy][xx]:
                            if d == k or d == -1:
                                m = miror 
                            else:
                                m = miror + 1
                            if board[yy][xx] == 'C':
                                if m < ans:
                                    ans = m
                            else:                          
                                visited[yy][xx] = True 
                                mirorCnt[yy][xx] = miror
                                queue.append([(yy, xx), m, k])
            
print(ans)