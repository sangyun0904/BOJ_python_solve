#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 15:40:53 2022

@author: sangyoon
"""

N, M = map(int, input().split())

answer = []

def combi(depth, N, M):
    
    if depth == 1:
        start = 0
    else:
        start = answer[-1]
        
    for i in range(start+1, N+1):
        answer.append(i)
        if depth == M:
            print(' '.join(map(str, answer)))
        else:
            combi(depth+1, N, M)
        answer.pop()
            
    return

combi(1, N, M)