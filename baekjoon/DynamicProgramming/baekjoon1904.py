#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 13:00:31 2022

@author: sangyoon
"""
#import sys
#input = sys.stdin.readline
N = int(input())

fibo_list = [0 for i in range(N+1)]
fibo_list[0] = 1
fibo_list[1] = 1

ans = 0

for i in range(2, N+1):
    n1 = fibo_list[i-2]
    n2 = fibo_list[i-1]
    fibo_list[i] = (n1 + n2) % 15746
    
print(fibo_list[N])