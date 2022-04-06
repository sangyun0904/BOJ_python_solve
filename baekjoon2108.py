#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:09:23 2022

@author: sangyoon
"""

import sys 

N = int(sys.stdin.readline())

n_list = []

for _ in range(N):
    num = int(sys.stdin.readline())
    n_list.append(num)
    
n_list.sort()

max_cnt = 0
max_cnt_nums = []

for i in set(n_list):
    cnt = n_list.count(i)
    if cnt > max_cnt:
        max_cnt_nums = [i]
        max_cnt = cnt
    elif cnt == max_cnt:
        max_cnt_nums.append(i)

max_cnt_nums.sort()

print(round(sum(n_list) / len(n_list)))
print(n_list[len(n_list) // 2])
if len(max_cnt_nums) > 1:
    print(max_cnt_nums[1])
else:
    print(max_cnt_nums[0])
print(n_list[-1] - n_list[0])
