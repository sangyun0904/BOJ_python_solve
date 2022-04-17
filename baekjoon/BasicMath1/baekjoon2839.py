# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 22:07:37 2022

@author: USER
"""

import sys 

#N = int(sys.stdin.readline())
N = int(input())

current = N

memory = -1

if N % 5 == 0:
    print(N // 5)
else:
    while current > 0:
        if current % 3 == 0:
            memory = current // 3
        current -= 5 

    if memory != -1:
        print(memory + (N - memory * 3) // 5)
    else:
        print(memory)