#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 10:30:25 2022

@author: sangyoon
"""

import sys 
from itertools import permutations
input = sys.stdin.readline 

N = int(input())
exp = input().strip()
exp_list = [i for i in exp]
ops_idx = [i for i in range(N) if i % 2 == 1]
ops_order = permutations(ops_idx, N//2)

