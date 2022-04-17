#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 15:59:29 2022

@author: sangyoon
"""

N, M = map(int, input().split())

answer = []

def combi(depth, N, M):
        
    for i in range(1, N+1):
        answer.append(i)
        if depth == M:
            print(' '.join(map(str, answer)))
        else:
            combi(depth+1, N, M)
        answer.pop()
            
    return

combi(1, N, M)