#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 18:11:08 2022

@author: sangyoon
"""

num_list = [i for i in range(1, 10001)]
for i in range(1, 10001):
    if i in num_list:
        print(i)
    kaprekar = i 
    for j in str(i):
        kaprekar += int(j)
    if kaprekar in num_list:
        num_list.remove(kaprekar)