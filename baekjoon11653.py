#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 19:35:55 2022

@author: sangyoon
"""

import sys 

#N = int(sys.stdin.readline())
N = int(input())

elements = []

if N != 1:
    isPrime = False
    while isPrime == False:
        isPrime = True
        for i in range(2, N):
            if i > N // i:
                break
            if N % i == 0:
                elements.append(i)
                N = N // i 
                isPrime = False 
                break
    for i in elements:
        print(i)
    print(N)