#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 12:54:37 2022

@author: sangyoon
"""

N, M, K = list(map(int, input().split()))

nums = list(map(int, input().split()))
nums.sort(reverse=True)

first = nums[0]
second = nums[1]

result = 0
cnt = 1

for _ in range(M):
    if cnt == K:
        result += second
        cnt = 1
    else:
        result += first
        cnt += 1
        
print(result)