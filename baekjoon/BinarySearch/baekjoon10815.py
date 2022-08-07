#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:39:41 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N = int(input())
nList = list(map(int, input().split()))

M = int(input())
mList = list(map(int, input().split()))

nList.sort() 

ans = []

for i in mList:
    start = 0 
    end = N - 1
    mid = 0
    
    while start <= end:
        mid = (start + end) // 2 
        
        if nList[mid] < i:
            start = mid + 1 
        else:
            end = mid - 1
    
    if start == N :
        ans.append(0)
    if nList[start] == i:
        ans.append(1)
    else:
        ans.append(0)
        
print(*ans)