#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 16:34:01 2022

@author: sangyoon
"""

N = input()
n_list = []
for i in N:
    n_list.append(int(i))

n_list.sort(reverse=True)

for i in n_list:
    print(i, end="")