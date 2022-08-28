#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 18:09:10 2022

@author: sangyoon
"""

import sys 
from collections import deque
input = sys.stdin.readline 

N, M = map(int, input().split())

ladder = []
snake  = []

for _ in range(N):
    ladder.append(list(map(int, input().split())))

for _ in range(M):
    snake.append(list(map(int, input().split())))
    
visited = [False for _ in range(101)]
visited[1] = True
q = deque([[0, 1]])

while q:
    t, cur = q.popleft()
    
    for lad in ladder:
        if cur == lad[0]:
            cur = lad[1]
            
    for sna in snake:
        if cur == sna[0]:
            cur = sna[1]
            
    if cur == 100:
        print(t)
        break
    
    for i in range(1, 7):
        if cur + i <= 100 and not visited[cur + i]:
            q.append([t+1, cur + i])
            visited[cur + i] = True 
            