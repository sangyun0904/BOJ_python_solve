#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 8 18:37:20 2022

@author: sangyoon
"""

import sys 
from collections import deque 

b, a = map(int, input().split())
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

while a != 0 and b != 0:
    graph = []

    for _ in range(a):
        graph.append(list(map(int, input().split())))

    visited = [[False for _ in range(b)] for _ in range(a)]
    ans = 0

    for i in range(a):
        for j in range(b):
            if graph[i][j] == 1 and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True

                while q:
                    y, x = q.popleft()

                    for k in range(8):
                        xx = x + dx[k]
                        yy = y + dy[k]

                        if 0 <= xx < b and 0 <= yy < a:
                            if graph[yy][xx] == 1 and not visited[yy][xx]:
                                q.append((yy, xx))
                                visited[yy][xx] = True 

                ans += 1 
    print(ans)

    b, a = map(int, input().split())

