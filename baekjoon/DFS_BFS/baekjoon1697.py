#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 13:59:58 2022

@author: sangyoon
"""
from collections import deque

N, K = map(int, input().split())
times = [-1 for i in range(100001)]

def bfs(start):
    q = deque()
    q.append([start, 0])
    
    while q:
        now = q.popleft()
        times[now[0]] = now[1]
        if now[0] == K:
            print(now[1])
            break
        if now[0]-1 >= 0 :
            if times[now[0]-1] == -1:
                q.append([now[0]-1, now[1]+1])
        if now[0]+1 <= 100000:
            if times[now[0]+1] == -1:
                q.append([now[0]+1, now[1]+1])
        if now[0]*2 <= 100000:
            if times[now[0]*2] == -1:
                q.append([now[0]*2, now[1]+1])
        
bfs(N)