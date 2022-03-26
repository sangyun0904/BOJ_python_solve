# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 18:24:31 2022

@author: USER
"""
import sys


while True:
    n_list =  list(map(int, sys.stdin.readline().split()))

    if n_list == [0,0,0]:
        break

    n_list.sort()

    if n_list[0] ** 2 + n_list[1] ** 2 == n_list[2] ** 2:
        print("right")
    else: 
        print("wrong")