#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 16:10:51 2022

@author: sangyoon
"""

N = int(input())

queens = [-1] * N
cnt = 0
    
def n_queen(step, N):
    global cnt
    
    isAble = [True] * N
    for idx in range(step):
        attacks = [queens[idx]+(step - idx), queens[idx]-(step-idx), queens[idx]]
        for a in attacks:
            if a >= 0 and a<N:
                isAble[a] = False
    for i in range(N):
        if isAble[i]:
            if step == N-1:
                cnt += 1
            else:
                queens[step] = i
                n_queen(step+1, N)
                queens[step] = -1
    return

n_queen(0, N)
print(cnt)