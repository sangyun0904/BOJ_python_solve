#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 17:38:33 2022

@author: sangyoon
"""

import sys

MAX_NUM = 1000000

N = int(sys.stdin.readline())
n_list = [False] * (2 * MAX_NUM + 1)

for _ in range(N):
    n_list[int(sys.stdin.readline()) + MAX_NUM] = True

for i in range(len(n_list)):
    if n_list[i]:
        print(i - MAX_NUM)