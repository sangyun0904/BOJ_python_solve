#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 14:57:09 2022

@author: sangyoon
"""

from collections import deque
import sys 
input = sys.stdin.readline 

wheels = [[]]

for _ in range(4):
    wheels.append(input().strip())

K = int(input())

for _ in range(K):
    q = deque([list(map(int, input().split()))])
    moved = [False for _ in range(5)]
    
    while q:
        n, move = q.popleft()
        moved[n] = True
        
        if n-1 >= 1 and not moved[n-1]:
            if wheels[n-1][2] != wheels[n][6]:
                q.append([n-1, -move])
        if n+1 < 5 and not moved[n+1]:
            if wheels[n+1][6] != wheels[n][2]:
                q.append([n+1, -move])
    
        if move == 1:
            wheels[n] = wheels[n][-1] + wheels[n][:-1]
        else:
            wheels[n] = wheels[n][1:] + wheels[n][0]
                
ans = 0 

for i in range(4):
    ans += int(wheels[i+1][0]) * 2 ** i

print(ans)