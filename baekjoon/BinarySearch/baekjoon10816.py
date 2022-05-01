#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:37:10 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N = int(input())
n_list = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

n_list.sort()
m_list.sort()
s = 0

for i in m_list :
    start = s
    end = N 
    while start <= end:
        mid = (start + end) // 2
        if n_list[mid] < i:
            start = mid + 1 
        else:
            end = mid - 1 
    cnt = 0 
    s = start
    for j in range(start, N):
        if n_list[j] == i:
            cnt += 1 
        else:
            break 
    print(cnt, end=" ")