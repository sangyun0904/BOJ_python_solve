#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 21:24:36 2022

@author: sangyoon
"""

import sys
import heapq
input = sys.stdin.readline 

N = int(input())

leftheap = []
rightheap = []

for _ in range(N):
    
    num = int(input())
    
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, -num)
        
    else:
        heapq.heappush(rightheap, num)
    
    if len(rightheap) != 0:
        num1 = -heapq.heappop(leftheap)
        num2 = heapq.heappop(rightheap)
        
        if num1 > num2:
            heapq.heappush(rightheap, num1)
            heapq.heappush(leftheap, -num2)
        else:
            heapq.heappush(rightheap, num2)
            heapq.heappush(leftheap, -num1)
        
    print(-leftheap[0])