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
        a1 = queens[idx]+(step - idx)
        a2 = queens[idx]-(step-idx)
        a3 = queens[idx]
        if a1 >= 0 and a1 < N:
            isAble[a1] = False
        if a2 >= 0 and a2 < N:
            isAble[a2] = False
        if a3 >= 0 and a3 < N:
            isAble[a3] = False
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