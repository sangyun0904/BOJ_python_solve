#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:44:34 2022

@author: sangyoon
"""

import sys 

S = sys.stdin.readline().strip()
S = S.upper()

unique_char = list(set(S))

cnt_list = []

for i in unique_char:
    cnt_list.append(S.count(i))
    
max_num = max(cnt_list)

if cnt_list.count(max_num) >= 2:
    print("?")
else:
    max_idx = cnt_list.index(max_num)
    print(unique_char[max_idx])
        