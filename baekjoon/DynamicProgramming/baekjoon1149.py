#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:12:04 2022

@author: sangyoon
"""
import sys 
input = sys.stdin.readline 
INF = sys.maxsize

N = int(input())
houses = [list(map(int, input().split())) for _ in range(N)]

ans = [0,0,0]

for i in houses:
    r, g, b = ans 
    ans[0] = i[0] + min(g, b)
    ans[1] = i[1] + min(r, b)
    ans[2] = i[2] + min(r, g)
    
print(min(ans))