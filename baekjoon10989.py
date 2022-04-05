#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 17:55:17 2022

@author: sangyoon
"""

import sys

MAX_NUM = 10000

N = int(sys.stdin.readline())
n_list = [0] * (MAX_NUM + 1)

for _ in range(N):
    n_list[int(sys.stdin.readline())] += 1

for i in range(len(n_list)):
    for j in range(n_list[i]):
        print(i)