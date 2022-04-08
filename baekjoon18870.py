#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:35:31 2022

@author: sangyoon
"""

import sys 

_ = sys.stdin.readline()

x_list = list(map(int, sys.stdin.readline().split()))

x_sort = sorted(list(set(x_list)))
x_dict = {}

for i in range(len(x_sort)):
    x_dict[x_sort[i]] = i

for i in x_list:
    print(x_dict[i], end=" ")