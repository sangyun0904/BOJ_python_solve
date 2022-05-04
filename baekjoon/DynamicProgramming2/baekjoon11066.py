#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 17:59:11 2022

@author: sangyoon
"""
import sys 
input = sys.stdin.readline 

INF = sys.maxsize

T = int(input())
for _ in range(T):
    N = int(input())
    sizes = list(map(int, input().split()))
    print(sizes)
    while len(sizes) > 2:
        min_sum = INF
        min_idx = 0
        for i in range(len(sizes)-1):
            if sum(sizes[i:i+2]) < min_sum:
                min_sum = sum(sizes[i:i+2])
                min_idx = i 
        print(sizes, min_idx, min_sum)
        sizes = sizes[:min_idx] + [min_sum] + sizes[min_idx+2:]
    print(sizes)
    