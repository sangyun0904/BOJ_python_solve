#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 16:23:13 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N, B = map(int, input().split())

array = []

for _ in range(N):
    array.append(list(map(int, input().split())))
    
def array_mult(array1, array2):
    ret = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            temp1 = array1[i]
            temp2 = list(map(list, zip(*array2)))[j]
            
            for k in range(N):
                ret[i][j] += temp1[k] * temp2[k]
            ret[i][j] = ret[i][j] % 1000
    return ret 

memo = [[] for _ in range(37)]
memo[0] = array

for i in range(1, 37):
    memo[i] = array_mult(memo[i-1], memo[i-1])
    
ans = array
B -= 1

while B != 0:
    cnt = 0 
    for i in range(0, 37):
        if 2 ** i <= B:
            cnt = i
        else:
            break
    ans = array_mult(ans, memo[cnt])
    B -= 2 ** cnt
    
for i in ans:
    for j in i:
        print(j % 1000, end=" ")
    print()