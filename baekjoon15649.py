#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:57:54 2022

@author: sangyoon
"""

N, M = map(int, input().split())

visited = [False] * (N + 1)
answer = []

def permu(depth, N, M):
    for i in range(1,N+1):
        if not visited[i]:
            answer.append(i)
            visited[i] = True
            if depth == M:
                print(' '.join(map(str, answer)))
            else:
                permu(depth+1, N, M)
            answer.pop()
            visited[i] = False
    return

permu(1, N, M)