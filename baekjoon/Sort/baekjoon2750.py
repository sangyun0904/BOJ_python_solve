#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 17:17:46 2022

@author: sangyoon
"""

N = int(input())
n_list = []

for _ in range(N):
    n_list.append(int(input()))
    
n_list.sort()

for i in n_list:
    print(i)