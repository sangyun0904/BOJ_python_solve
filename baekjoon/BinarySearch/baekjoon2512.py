#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 13:28:41 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N = int(input())
requests = list(map(int, input().split()))
M = int(input())

start = 0 
end = M

ans = 0

while start <= end:
    mid = (start + end) // 2 
    
    temp = 0 
    for i in requests:
        if i < mid:
            temp += i 
        else:
            temp += mid 
            
    if temp > M:
        end = mid - 1 
    else:
        start = mid + 1
        
    ans = end
    
print(min(max(requests), ans))
