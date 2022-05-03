#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 17:07:02 2022

@author: sangyoon
"""
import sys 
input = sys.stdin.readline
N = int(input())

n_list = list(map(int, input().split()))
memo = 0
temp = 0
for i in range(N): 
    if temp + n_list[i] > 0:
        temp += n_list[i]
    else:
        temp = 0
    if memo < temp:
        memo = temp

if memo == 0:
    print(max(n_list))
else:
    print(memo)