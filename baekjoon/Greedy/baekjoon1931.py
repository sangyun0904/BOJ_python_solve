#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 18:48:31 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N = int(input())

meetings = []

for _ in range(N):
    meetings.append(list(map(int, input().split())))
    
meetings.sort(key=lambda x: (x[1], x[0])) 

cnt = 0
end = 0
for i in meetings:
    if i[0] > end:
        cnt += 1 
        end = i[1]
        
print(cnt)