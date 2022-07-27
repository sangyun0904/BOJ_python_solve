#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 10:07:46 2022

@author: sangyoon
"""

import sys 
from collections import deque
input = sys.stdin.readline 

T = int(input())

for _ in range(T):
    
    N, K = map(int, input().split())
    
    time = list(map(int, input().split()))
    
    memo = [0 for _ in range(N+1)]
    order = [[] for _ in range(N+1)]
    reverse = [[] for _ in range(N+1)]
    
    for _ in range(K):
        a, b = map(int, input().split())
        order[a].append(b)
        reverse[b].append(a)
        
    target = int(input())
    
    for i in range(1, N+1):
        if reverse[i] == []:
            queue = deque([[i, time[i-1]]])
            while queue:
                node, t = queue.popleft() 
                for n in order[node]:
                    if memo[node] + t > memo[n]:
                        memo[n] = memo[node] + t
                        queue.append([n, time[n-1]])
                        
    print(memo[target] + time[target-1])